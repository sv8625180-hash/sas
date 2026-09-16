import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const root = path.dirname(fileURLToPath(import.meta.url));
const project = path.resolve(root, '../..');
const skillRoot = path.join(project, '.agents', 'skills');
const destination = path.join(os.homedir(), '.agents', 'skills');
const hash = bytes => crypto.createHash('sha256').update(bytes).digest('hex');

function plainPath(filename) {
  let current = path.resolve(filename);
  for (;;) {
    try {
      if (fs.lstatSync(current).isSymbolicLink()) {
        throw new Error(`No se admiten enlaces simbólicos: ${current}`);
      }
    } catch (error) {
      if (error.code !== 'ENOENT') throw error;
    }
    const parent = path.dirname(current);
    if (parent === current) break;
    current = parent;
  }
}

function read(filename, limit = 131072) {
  plainPath(filename);
  const fd = fs.openSync(filename, fs.constants.O_RDONLY | (fs.constants.O_NOFOLLOW ?? 0));
  try {
    const stat = fs.fstatSync(fd);
    if (!stat.isFile() || stat.size > limit) throw new Error(`Archivo no válido o demasiado grande: ${filename}`);
    const buffer = Buffer.alloc(limit + 1);
    let length = 0;
    while (length < buffer.length) {
      const count = fs.readSync(fd, buffer, length, buffer.length - length, null);
      if (!count) break;
      length += count;
    }
    if (length > limit) throw new Error(`Archivo demasiado grande: ${filename}`);
    return buffer.subarray(0, length);
  } finally {
    fs.closeSync(fd);
  }
}

function inventory() {
  const manifest = JSON.parse(read(path.join(project, 'docs', 'provenance', 'skills-export-manifest.json'), 1048576));
  if (manifest.schema_version !== 1 || manifest.scope?.kind !== 'export-only' ||
      !Array.isArray(manifest.skills) || !manifest.skills.length || manifest.skills.length > 128) {
    throw new Error('El ZIP no contiene un manifiesto válido. Extrae TODO el paquete.');
  }
  const extraPath = path.join(project, 'docs', 'provenance', 'additional-skills.json');
  if (fs.existsSync(extraPath)) {
    const extra = JSON.parse(read(extraPath, 1048576));
    if (extra.schema_version !== 1 || !Array.isArray(extra.skills)) throw new Error('Manifiesto adicional no válido.');
    manifest.skills.push(...extra.skills);
    if (manifest.skills.length > 128) throw new Error('Demasiadas skills para una importación acotada.');
  }
  const seen = new Set();
  return manifest.skills.map(entry => {
    const name = entry.name;
    if (typeof name !== 'string' || name.length > 64 || !/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(name) || seen.has(name)) {
      throw new Error('El manifiesto contiene un nombre no válido o duplicado.');
    }
    seen.add(name);
    if (entry.path !== `${name}/SKILL.md` || !/^[a-f0-9]{64}$/.test(entry.export_root_sha256 ?? '')) {
      throw new Error(`Ruta o hash no válido: ${name}`);
    }
    const bytes = read(path.join(skillRoot, name, 'SKILL.md'));
    if (hash(bytes) !== entry.export_root_sha256) throw new Error(`Hash incorrecto: ${name}. Descarga otra vez el ZIP.`);
    return { name, bytes, sha256: entry.export_root_sha256, target: path.join(destination, name, 'SKILL.md') };
  });
}

function prepare(entries) {
  plainPath(destination);
  const pending = [];
  for (const entry of entries) {
    plainPath(entry.target);
    const folder = path.dirname(entry.target);
    if (fs.existsSync(folder)) {
      if (!fs.statSync(folder).isDirectory() || !fs.existsSync(entry.target)) {
        throw new Error(`Existe una carpeta o archivo incompatible: ${folder}. No se ha copiado nada.`);
      }
      if (hash(read(entry.target)) !== entry.sha256) {
        throw new Error(`Ya existe una skill DISTINTA: ${entry.name}. No se ha copiado nada. No la reemplaces sin revisarla.`);
      }
    } else {
      pending.push(entry);
    }
  }
  // Validate every collision before creating any skill; never overwrite a root.
  for (const entry of pending) {
    plainPath(entry.target);
    fs.mkdirSync(path.dirname(entry.target), { recursive: true, mode: 0o700 });
    fs.writeFileSync(entry.target, entry.bytes, { flag: 'wx', mode: 0o600 });
  }
  for (const entry of entries) {
    if (hash(read(entry.target)) !== entry.sha256) throw new Error(`Fallo en la comprobación final: ${entry.name}`);
  }
  console.log(`PREPARADO: ${entries.length}/${entries.length} skills locales verificadas.`);
  console.log(`Archivos nuevos: ${pending.length}. Destino: ${destination}`);
  console.log('Esto NO ha importado nada a tu cuenta de Hoplite ni ha instalado MCP.');
}

function environment() {
  const env = { ...process.env, DISABLE_TELEMETRY: '1' };
  const key = Object.keys(env).find(name => name.toUpperCase() === 'PATH');
  const previous = key ? env[key] : '';
  for (const name of Object.keys(env)) if (name.toUpperCase() === 'PATH') delete env[name];
  env.PATH = [path.join(root, 'node_modules', '.bin'), path.dirname(process.execPath), previous].filter(Boolean).join(path.delimiter);
  return env;
}

function tool(relative, args, capture = false) {
  const filename = path.join(root, 'node_modules', relative);
  plainPath(filename);
  const result = spawnSync(process.execPath, [filename, ...args], {
    cwd: root,
    env: environment(),
    stdio: capture ? ['ignore', 'pipe', 'pipe'] : 'inherit',
    encoding: 'utf8',
    ...(capture ? { timeout: 60000, maxBuffer: 2097152 } : {}),
  });
  if (result.error) throw result.error;
  if (result.status !== 0) {
    if (capture && result.stderr) console.error(result.stderr.slice(0, 2000));
    throw new Error(`La herramienta terminó con error (${result.status ?? result.signal}). No continúes; revisa el mensaje anterior.`);
  }
  return result.stdout;
}

function verify(entries) {
  const versions = JSON.parse(read(path.join(root, 'package.json'))).dependencies;
  for (const [name, version] of Object.entries(versions)) {
    if (!/^\d+\.\d+\.\d+(?:-[\w.-]+)?$/.test(version)) throw new Error(`Fija una versión exacta de ${name}.`);
    const metadata = JSON.parse(read(path.join(root, 'node_modules', name, 'package.json')));
    if (metadata.version !== version) throw new Error(`Se necesita ${name}@${version}. Ejecuta el setup del proyecto.`);
  }
  const listing = JSON.parse(tool('skills/bin/cli.mjs', ['list', '--global', '--json'], true));
  if (!Array.isArray(listing)) throw new Error('El catálogo local no tiene el formato esperado. No se importó nada.');
  for (const entry of entries) {
    const matches = listing.filter(item => item.name === entry.name);
    if (matches.length !== 1 || typeof matches[0].path !== 'string') {
      throw new Error(`El catálogo no identifica una única copia de ${entry.name}. No se importó nada.`);
    }
    const listed = matches[0].path;
    const filename = path.basename(listed) === 'SKILL.md' ? listed : path.join(listed, 'SKILL.md');
    if (hash(read(filename)) !== entry.sha256) throw new Error(`El catálogo ha elegido una copia DISTINTA de ${entry.name}. No se importó nada.`);
  }
  console.log(`VERIFICADO: ${entries.length}/${entries.length} skills presentes en el catálogo LOCAL y con hashes correctos.`);
  console.log('La biblioteca personal de Hoplite todavía requiere una importación y su comprobación posterior.');
}

try {
  const action = process.argv[2];
  if (!['preparar', 'comprobar', 'importar'].includes(action)) {
    throw new Error('Uso: node instalar.mjs preparar | comprobar | importar');
  }
  const entries = inventory();
  if (action === 'preparar') {
    prepare(entries);
  } else {
    verify(entries);
    if (action === 'importar') {
      console.log('Se seleccionan SOLO los nombres del paquete. Revisa la confirmación de Hoplite.');
      console.log('No se ejecuta onboard. Si se inicia sesión, hazlo en el navegador oficial; no pegues claves en el chat.');
      tool('@usehoplite/cli/bin/hoplite-cli.js', ['skills', 'import-global', ...entries.flatMap(entry => ['--name', entry.name])]);
      console.log('Revisa el resultado anterior: cancelar o encontrar skills existentes no significa importar todas.');
      console.log('La comprobación final se hace en un hilo nuevo de otro proyecto, como indica la guía.');
    }
  }
} catch (error) {
  console.error(`\nERROR: ${error.message}`);
  console.error('Detente en este paso. No uses --all ni --replace y no compartas claves o códigos de inicio de sesión.');
  process.exitCode = 1;
}
