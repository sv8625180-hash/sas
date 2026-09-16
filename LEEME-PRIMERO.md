# Llevar todas las skills y MCP a otra cuenta de Hoplite

Este paquete contiene **27 skills de proyecto: las 26 originales más `cohort-analysis`**, los **4 servidores MCP**, sus instaladores, versiones fijadas, pruebas, procedencia y mantenimiento revisable. No contiene credenciales, sesiones, historial de Git, los ZIP originales ni resultados de investigaciones anteriores. No incluye dependencias preinstaladas: el setup las descarga desde sus registros públicos.

## 1. La forma más sencilla: adjuntar este ZIP en la cuenta nueva

1. Entra en **la cuenta de Hoplite de destino**. Crea o selecciona un proyecto conectado a un repositorio en el que tengas permiso para guardar estos archivos; preferiblemente, uno vacío.
2. Abre un hilo en ese proyecto y adjunta **`hoplite-kit-portable.zip` completo**, sin eliminar las carpetas ocultas `.agents`, `.hoplite` o `.github`.
3. Copia en el chat el contenido de **`PROMPT-PARA-HOPLITE.txt`**, incluido junto a esta guía.
4. El agente debe revisar el paquete, verificar sus hashes, copiarlo al repositorio sin pisar trabajo existente, ejecutar setup y pruebas y publicar los archivos mediante la vía autorizada. No basta con dejar el ZIP en Adjuntos.
5. Cuando los archivos estén publicados en la rama que usará el proyecto, inicia **un hilo nuevo** desde esa revisión para comprobar el catálogo nativo de skills y MCP. La carga del catálogo del hilo que hizo la instalación no acredita la del siguiente.

No necesitas dar acceso de la cuenta nueva al repositorio de origen: descarga primero el ZIP con la cuenta que ya tiene acceso y después adjúntalo en la de destino. La cuenta nueva sí debe tener los permisos y capacidades de Hoplite necesarios para su propio proyecto. El paquete no crea cuentas, concede permisos ni transfiere suscripciones o cuotas.

## 2. Comprobación del paquete y del proyecto

Extrae el ZIP en una carpeta nueva y entra en `hoplite-kit-portable/`. Revisa los scripts antes de ejecutarlos. Para comprobar el contenido antes de instalar:

```sh
python3 scripts/exportar_kit.py verify --directory .
```

`MANIFIESTO-PAQUETE.json` enumera todos los archivos salvo el propio manifiesto, con tamaño y SHA-256, las 27 skills y los 4 MCP. El verificador reconstruye también el manifiesto para comprobarlo. El archivo externo `hoplite-kit-portable.zip.sha256` cubre el ZIP completo y permite comprobar la descarga antes de extraerla, por ejemplo con `sha256sum -c hoplite-kit-portable.zip.sha256` en Linux. Los hashes detectan cambios; no son una firma independiente del editor.

Requisitos del setup: **Bash, Python 3.11–3.13, uv, Node.js ≥22.20 y npm**, conexión a Internet y acceso a los registros públicos. El setup del proyecto está orientado a Linux/macOS, incluido el sandbox Linux de Hoplite; no se ha verificado una instalación Windows nativa. Los entornos Python y Node se reconstruyen, nunca se copian desde la cuenta anterior.

Desde la raíz del proyecto instalado:

```sh
bash .hoplite/setup.sh
python3 scripts/verify_toolkit.py
tools/hoplite-research/.venv/bin/python -m unittest discover -s tests -v
tools/hoplite-research/.venv/bin/python tools/hoplite-research/scripts/research_client.py check --live
```

El verificador debe informar **26 skills originales, 1 adicional y 4 MCP configurados**. La última orden hace una operación pública acotada con cada servidor; su resultado debe distinguir inicialización, catálogo y prueba funcional. Conserva los errores y límites del proveedor, sin cambiar identidades o endpoints para eludirlos. Los reportes de esta ejecución se generan en la cuenta destino; no se reutiliza como prueba una comprobación de la cuenta de origen.

El setup efectivo de Hoplite debe ser `bash .hoplite/setup.sh`. Revisa Settings si hay un override previo, pues tiene prioridad sobre `.hoplite/settings.json`. Si el repositorio ya contiene otros archivos, skills, MCP o instrucciones, detén las colisiones y prepara una integración revisada: este kit está verificado como proyecto independiente, no como un reemplazo indiscriminado de otra configuración.

## 3. Qué incluye exactamente

### Skills

| | | |
| --- | --- | --- |
| `ab-test-setup` | `ai-opportunity-validation` | `ai-service-evaluation` |
| `analytics-tracking` | `competitive-intelligence` | `competitor-alternatives` |
| `copywriting` | `customer-discovery` | `deep-web-research` |
| `distribution-validation` | `free-tool-strategy` | `launch-strategy` |
| `lead-research-assistant` | `market-customer-research` | `page-cro` |
| `pricing-strategy` | `product-manager-toolkit` | `public-data-analysis` |
| `research-team` | `scholarly-metadata` | `seo-audit` |
| `source-fact-checking` | `tool-due-diligence` | `trend-analysis` |
| `unit-economics` | `web-search-strategy` | `cohort-analysis` *(adicional)* |

Se conserva el `SKILL.md` íntegro de cada raíz, incluidas sus atribuciones y licencias. Los ZIP originales solo aportaban raíces autónomas, no bibliotecas completas de scripts o referencias de terceros. No se atribuye una licencia general a todo el paquete. Las skills nativas que proporciona Hoplite no son parte de esta exportación ni se copian desde una cuenta.

### MCP

| Nombre de configuración | Transporte | Qué se transfiere |
| --- | --- | --- |
| `research-fetch` | stdio | Lanzador local, dependencias fijadas y controles de URLs públicas. |
| `research-arxiv` | stdio | Lanzador local, dependencias fijadas y almacenamiento local aislado. |
| `research-context7` | HTTP | Configuración para `https://mcp.context7.com/mcp`. |
| `research-firecrawl` | HTTP | Configuración para `https://mcp.firecrawl.dev/v2/mcp`. |

La configuración actual no incluye claves. Los endpoints remotos, cuotas y condiciones dependen de sus proveedores y pueden cambiar. Si un proveedor exige credenciales, autorízalas en la configuración segura de **la cuenta destino**, no en archivos del kit ni en el chat. No existe en este paquete una instalación MCP universal para todos los proyectos de una cuenta.

Firecrawl se limita a **Search/Scrape de información pública**: sin Parse, uploads, headers personalizados, acciones ni proxies. Las restricciones de uso también están en `AGENTS.md`; el transporte HTTP nativo no hereda los filtros del cliente Python.

## 4. Opcional: biblioteca personal de la cuenta nueva

Las 27 skills del proyecto ya estarán disponibles en ese proyecto. Para utilizarlas como **skills personales** en otros proyectos iniciados por el mismo usuario, hace falta una importación autenticada independiente.

Haz este paso en **tu terminal privada**, con el paquete extraído y las dependencias de `tools/personal-skills` instaladas. Comprueba que la autenticación corresponde a la cuenta de destino antes de autorizar cualquier importación. Si ya existe una sesión de otra cuenta, no continúes con ella.

```sh
npm ci --prefix tools/personal-skills --ignore-scripts --no-audit --no-fund --engine-strict --registry=https://registry.npmjs.org
node tools/personal-skills/instalar.mjs preparar
node tools/personal-skills/instalar.mjs comprobar
node tools/personal-skills/instalar.mjs importar
```

`preparar` copia las 27 raíces a `~/.agents/skills` sin reemplazar versiones distintas. `comprobar` verifica el catálogo **local**, no el remoto. `importar` invoca el CLI oficial fijado en el lockfile y selecciona solo esos 27 nombres. El CLI necesita la autenticación y confirmación de la cuenta de destino; sigue su flujo oficial en tu equipo. No pegues claves, tokens, códigos de login ni capturas que los contengan en Hoplite, GitHub o este paquete.

No ejecutes `onboard` para esta tarea: puede importar historial ajeno al kit. No uses `--all` ni `--replace` para resolver colisiones sin revisión. Cancelar la confirmación o encontrar nombres ya existentes no significa haber importado 27 skills nuevas.

La aceptación final se hace abriendo, como ese usuario, un hilo en **otro proyecto que no contenga copias en `.agents/skills`** y comprobando las 27 skills. Las skills personales no se aplican a automations; una raíz del repositorio con el mismo nombre tiene prioridad. Sin esa prueba, el estado correcto es «importación personal pendiente de verificar», no «instalado en toda la cuenta».

## 5. Actualizaciones en la cuenta nueva

El paquete incluye `.github/workflows` y `.github/dependabot.yml`. Para que funcionen, publica sus archivos en la rama predeterminada del repositorio de destino y habilita allí Actions/Dependabot y, si la política lo permite, la creación de PR por Actions. El mantenimiento semanal propone informes y las actualizaciones de dependencias se revisan en PR: **no se fusionan automáticamente**.

Los MCP HTTP siguen siendo servicios remotos. Las skills personales son una copia separada, no una sincronización automática con este proyecto. Consulta [docs/maintenance.md](docs/maintenance.md) antes de activar cambios descargados.

## Criterios de entrega en la cuenta destino

- [ ] El ZIP y todos los archivos inventariados pasan la verificación de integridad.
- [ ] Las 27 raíces y los 4 MCP están guardados en el repositorio de destino.
- [ ] Setup y pruebas offline pasan en una instalación limpia.
- [ ] Cada MCP inicializa, anuncia su catálogo esperado y supera una operación pública real; cualquier fallo queda registrado.
- [ ] Un hilo nuevo desde la revisión publicada descubre las 27 skills y los 4 MCP nativamente.
- [ ] Si se pidió biblioteca personal, la importación autorizada se comprueba en otro proyecto sin copias locales.
- [ ] Si se pidió mantenimiento, su activación se comprueba en Actions del repositorio nuevo.

Referencias oficiales consultadas el 2026-09-16: [skills e importación personal](https://hoplite.sh/docs/agent/skills), [MCP por proyecto](https://hoplite.sh/docs/agent/mcp), [CLI y autenticación](https://hoplite.sh/docs/cli). Preparar el paquete no realiza ninguna de las autorizaciones de la cuenta destino.
