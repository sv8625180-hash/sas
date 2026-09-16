# Mantenimiento y actualizaciones

## Qué se actualiza y cómo

| Componente | Detección / propuesta | Activación |
| --- | --- | --- |
| Python: Fetch, arXiv y SDK MCP | Dependabot `uv`, semanal; manifiesto y `uv.lock` | PR revisada, setup y pruebas; no auto-merge. |
| CLI personal y gestor `skills` | Dependabot `npm`, semanal | Versiones exactas del manifiesto, lockfile y verificación del contrato del CLI. |
| Readability.js y dependencias | Dependabot `npm` en su directorio dedicado | Lockfile revisado; setup comprueba extracción HTML real sin red. |
| GitHub Actions | Dependabot `github-actions`, semanal | SHA completo y revisión de permisos e inputs. |
| Skills derivadas de fuentes externas | `scripts/check_upstreams.py` compara el archivo del commit revisado con el head público | Informe con hashes y URLs, nunca sustitución automática de adaptaciones. |
| Skills locales sin upstream externo | Inventario explícito en el informe | Cambios mantenidos y revisados en este repositorio. |
| Puentes e instalador adaptados del ZIP | Mantenimiento local: el paquete no declara un feed de actualizaciones propio | No se sustituye código desde un origen supuesto; cualquier cambio se revisa y prueba. |
| MCP HTTP | Pruebas semanales de catálogo y contenido | El proveedor controla su servicio; un cambio o error no autoriza herramientas nuevas. |
| Skills personales de la cuenta | No hay sincronización autenticada desatendida configurada | Importación y verificación separadas; no guardar una clave personal en Actions para simular alcance global. |
| Runtimes de Hoplite | Administrados por la plataforma | No se afirma actualizar la imagen base desde este repositorio. Las versiones explícitas de CI se revisan cuando cambie la compatibilidad. |

## Workflows

- `verify.yml`: setup fijado, pruebas offline y segundo setup para verificar idempotencia. Token de solo lectura; sin secretos de investigación ni login de cuenta.
- `maintenance.yml`: lunes a las **06:17 UTC**, además de ejecución manual; solo rama predeterminada. Máximo 20 minutos, sin bucles de reintentos. Consulta fuentes y prueba los cuatro MCP con datos públicos.
- La rama `automation/toolkit-maintenance` mantiene una PR de evidencia. Se limita la escritura a `reports/*.json`. Un fallo de consulta se conserva y hace fallar el workflow; `continue-on-error` únicamente permite guardar evidencia antes de ese fallo final.
- Un artefacto independiente por ejecución conserva los dos informes y el historial de esa ejecución durante 30 días, incluso si falla publicar la PR. Solo incluye esos JSON públicos, nunca el runtime, las credenciales o directorios completos del sandbox.
- Los PR de Dependabot proponen los cambios de paquetes por separado. Ningún workflow fusiona automáticamente.

## Condiciones de activación en GitHub

Los ficheros locales no demuestran una tarea programada funcionando. Deben estar publicados en la rama predeterminada, con Actions y Dependabot habilitados. La creación de PR necesita que la política del repositorio permita a GitHub Actions crear pull requests, además de `contents: write` y `pull-requests: write` en ese job. Una política de la organización puede impedirlo; no se elude con tokens personales.

Los PR creados con `GITHUB_TOKEN` pueden no disparar otros workflows. El mantenimiento ejecuta sus pruebas antes de proponer el informe, pero no presenta como ejecutada una CI de PR que no arrancó. Los fallos de la propia automatización deben revisarse en Actions. Las cuotas y eventual coste de minutos son los de la cuenta de GitHub; no se contrató ningún plan.

En una transferencia, estas condiciones deben comprobarse de nuevo en el repositorio de destino. El ZIP no transfiere permisos, suscripciones ni el estado de Actions de otro repositorio; no se da por fusionado un cambio solo por haber creado un commit.

## Revisión de una actualización

1. Comprobar procedencia, licencia, commit/versión, permisos, scripts de instalación y cambios de herramientas.
2. No asignar una skill renombrada a otra solo por parecido. Si la fuente desaparece, el monitor informa `source_path_missing_review_required`; conserva la adaptación vigente.
3. Adaptar el cambio legítimo, mantener las atribuciones y actualizar conscientemente su huella en el manifiesto correspondiente.
4. Ejecutar setup, tests, comprobación funcional y revisar el diff completo. Los fallos son evidencia, no motivos para debilitar las pruebas.
5. Fusionar después de revisión autorizada. Si se desea actualizar una copia personal, revisar también diferencias y realizar la importación autenticada específica; no usar `--replace` de forma indiscriminada.

## Ejecución manual

```sh
python3 scripts/check_upstreams.py --output reports/upstream-status.json
tools/hoplite-research/.venv/bin/python tools/hoplite-research/scripts/research_client.py check --live --output reports/mcp-health.json
```

El monitor consulta solo archivos y metadatos públicos de los repositorios del manifiesto, sin autenticación, proxies de entorno ni redirecciones automáticas. Acota tamaño, número de fuentes y tiempo por solicitud. Un 403/429 detiene nuevas consultas en esa ejecución. No descarga ni ejecuta código fuente como parte de la actualización de skills.

El setup aplica conjuntamente el manifiesto y lockfile de Readability, sin modificar los archivos compartidos de la caché de Python; la huella de preparación cubre ambos. GitHub documenta actualmente uv 0.11 en Dependabot, mientras este entorno/CI está verificado con uv 0.9.28. Las PR con un formato de lock nuevo deben pasar el setup fijado o incluir una actualización de runtime revisada: no se presume compatibilidad futura ni se fuerza su fusión.

Referencias consultadas el 2026-09-16: [ecosistemas de Dependabot](https://docs.github.com/en/code-security/reference/supply-chain-security/supported-ecosystems-and-repositories), [opciones](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference), [eventos de workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows), [create-pull-request](https://github.com/peter-evans/create-pull-request).
