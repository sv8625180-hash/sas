# Investigación comercial con skills y MCP

Toolkit reproducible para **este proyecto de Hoplite**. Integra las **26 skills de los ZIP originales**, una adaptación adicional revisada de **`cohort-analysis`**, y **4 servidores MCP**. No promete ingresos, investigación exhaustiva de Internet ni disponibilidad permanente de servicios externos.

## Transferir a otra cuenta desde cero

Descarga [el ZIP portable completo](exports/hoplite-kit-portable.zip) y [su SHA-256](exports/hoplite-kit-portable.zip.sha256). En la cuenta destino, adjunta el ZIP en un hilo de un proyecto nuevo y pega [este prompt](PROMPT-PARA-HOPLITE.txt). La [guía paso a paso](LEEME-PRIMERO.md), incluida también en el ZIP, distingue instalación de proyecto, importación personal autorizada y comprobación nativa en un hilo nuevo.

El ZIP contiene las 27 skills, los 4 MCP, locks, setup, pruebas y mantenimiento; excluye credenciales, dependencias instaladas e historial. Se reconstruye con `python3 scripts/exportar_kit.py build` y se contrasta con los archivos actuales mediante `python3 scripts/exportar_kit.py check`. Consulta la [verificación de esta entrega](exports/VERIFICACION.md), incluidos los fallos de entorno y lo pendiente en la cuenta destino.

## Resultado y alcance

| Capa | Resultado | Límite |
| --- | --- | --- |
| Skills de proyecto | 27 raíces en `.agents/skills/`, con hashes y procedencia | Se aplican al trabajar desde esta revisión del repositorio. |
| Fetch y arXiv | Instalación local, versiones fijadas y entorno sin credenciales heredadas | Las operaciones de red siguen sujetas a robots, disponibilidad y cuotas. |
| Context7 y Firecrawl | Configuración HTTP y operaciones públicas probadas | Servicios gestionados por sus proveedores; no se puede fijar su implementación remota. |
| Biblioteca personal de Hoplite | Instalador selectivo preparado | La importación autenticada y la disponibilidad en otros proyectos se verifican aparte; copiar archivos al sandbox no acredita ninguna de las dos. |
| GitHub | Dependabot, CI y mantenimiento semanal definidos | Solo este repositorio. Requieren publicación en la rama predeterminada y permisos de GitHub; no actualizan toda la cuenta ni fusionan PR automáticamente. |

La evidencia fechada y los límites de cada capa están en [verificación](docs/verification.md). Los reportes son pruebas concretas, no una certificación de todas las operaciones posibles.

## Investigación realizada

- [Síntesis y decisiones](docs/research/2026-09-16/RESUMEN.md).
- [Siete modelos de negocio, fuentes, contraevidencia y plan de validación](docs/research/2026-09-16/oportunidades.md).
- [Quince líneas de evaluación de herramientas, licencias, costes y permisos](docs/research/2026-09-16/herramientas-evaluadas.md).
- [Uso real de los MCP y APIs públicas, sin nuevos conectores](docs/research/2026-09-16/uso-real.md).

**Conclusión comercial provisional:** priorizar un servicio especializado que resuelva un proceso recurrente y medible de compradores accesibles; estudiar un producto después de validar repetición y pago. País, habilidades, capital, horas y acceso a clientes pueden cambiar la recomendación. Ninguna compra agregada, precio de competidor o simulación demuestra ventas propias.

## Instalación y comprobación

Requisitos: Bash, Python 3.11–3.13, `uv`, Node.js ≥22.20 y npm. Hoplite ejecuta el mismo setup en un nuevo sandbox cuando esta configuración esté en su rama de origen.

```sh
bash .hoplite/setup.sh
tools/hoplite-research/.venv/bin/python -m unittest discover -s tests -v
tools/hoplite-research/.venv/bin/python tools/hoplite-research/scripts/research_client.py check --live
python3 scripts/business_math.py
```

No se importa la biblioteca personal durante el setup. Las pruebas unitarias no consultan proveedores; `check --live` sí realiza consultas públicas acotadas. Conserva un 429 como limitación y no reintentes cambiando identidad o endpoint.

Los ejemplos económicos son **sintéticos, mensuales y en USD**, con trabajo humano valorado. No son beneficios netos, cotizaciones de proveedores ni previsiones de ingresos. Los períodos de retención no observados quedan como `null`, no como abandono.

## Biblioteca personal y otros proyectos

```sh
node tools/personal-skills/instalar.mjs preparar
node tools/personal-skills/instalar.mjs comprobar
node tools/personal-skills/instalar.mjs importar
```

Los dos primeros comandos solo preparan y verifican el catálogo **local**. El tercero usa el CLI oficial con los nombres concretos del manifiesto, requiere autenticación y confirmación, y no ejecuta `onboard`, `--all` ni `--replace`. No pegues claves, tokens o códigos de login en el chat ni en GitHub. Una colisión distinta se detiene sin sobrescribir tu trabajo.

La [biblioteca personal](https://hoplite.sh/docs/agent/skills) aplica a proyectos iniciados por su propietario, no a automations. Una skill del repositorio con el mismo nombre tiene prioridad. Comprueba la importación en un run de otro proyecto, sin las copias de este repositorio; éxito local no es esa comprobación.

Los [MCP se configuran por proyecto](https://hoplite.sh/docs/agent/mcp). Para otro proyecto integra el setup y las entradas de `.hoplite/settings.json`, preservando lo existente y evitando duplicarlas con las de Settings → Project → MCP. No existe en este toolkit una instalación MCP universal para toda la cuenta.

## Actualizaciones seguras

Consulta [mantenimiento](docs/maintenance.md). Dependabot propone actualizaciones de Python, npm y Actions. El monitor de skills compara fuentes inmutables con sus versiones actuales y prepara un informe; **no reemplaza adaptaciones ni ejecuta instrucciones recién descargadas**. Las nuevas versiones se revisan y prueban antes de activarse. Las skills de autoría local requieren mantenimiento local y la biblioteca personal es una copia separada, no una sincronización automática.

## Privacidad y licencias

Solo datos públicos o sintéticos. No hay claves ni dependencias vendorizadas; archivos de runtime, historial, adjuntos y entornos están ignorados por Git. Firecrawl se limita a Search/Scrape: no Parse, uploads, headers, acciones ni proxies personalizados. Sus herramientas HTTP nativas no heredan los filtros del cliente Python.

Se conservan las atribuciones y licencias incluidas en las raíces de skills. [Manifiesto original](docs/provenance/skills-export-manifest.json) y [adición revisada](docs/provenance/additional-skills.json). No se atribuye una licencia general a material que no la declara, ni se importa en bloque contenido propietario de otros catálogos.
