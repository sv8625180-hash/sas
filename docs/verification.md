# Verificación y alcance de la entrega

Fecha: **2026-09-16 UTC**. Se distinguen instrucciones presentes, preparación local, conexión MCP, contenido real y alcance de cuenta. Nada de lo siguiente garantiza disponibilidad futura de servicios externos ni resultados económicos.

## Confirmado

| Comprobación | Resultado |
| --- | --- |
| Integridad de las skills originales | **26/26** raíces coinciden con los hashes del ZIP; atribuciones conservadas. |
| Adición revisada | `cohort-analysis`, fuente y MIT a commit fijo; raíz adaptada registrada. |
| Catálogo de proyecto | **27** skills; `load_skill` utilizado con las metodologías pertinentes y la nueva raíz. |
| Preparación personal local | `preparar` y `comprobar`: **27/27** en el catálogo local. No equivale a importación de cuenta. |
| Tentativa de importación personal | CLI oficial 2.3.2, exactamente 27 nombres y una tentativa el 16-09-2026 a las 03:06 UTC. Se detuvo al requerir autenticación/autorización; no se completó login ni se confirmó importación. No se guardaron ni publicaron códigos o enlaces de sesión. |
| Regresiones offline | **54/54** aprobadas: integridad, conflictos/symlinks, restricciones MCP, falsos positivos de errores, historial, monitor, cohortes y economía. |
| Cálculos | Aritmética de los tres escenarios y sensibilidad comprobada. Retención sintética ponderada **60%**; períodos no observados como `null`. |
| Prueba MCP final | **4/4** funcionales, `2026-09-16T02:53:00Z`, sin reintentos. [JSON completo](../reports/mcp-health.json). |
| Monitor de fuentes | **26** fuentes únicas: 17 sin cambios, 2 modificadas y 7 rutas actuales retiradas; salida 0, `needs_review=true`. [JSON completo](../reports/upstream-status.json). No se activó ningún cambio remoto. |
| Configuración CI | YAML, SHA de Actions e inputs revisados; esto no acredita ejecución en GitHub. |

Los avisos de rutas retiradas se refieren al archivo en el upstream actual: no indican que falten las copias locales verificadas. Las skills sin upstream externo quedan identificadas como mantenimiento local.

## Los cuatro MCP

| Servidor | Prueba del cliente local | Observación separada en herramientas nativas del run |
| --- | --- | --- |
| Fetch | Extracción de `example.com` y rechazo explícito del guard para URL privada | Documentación y JSON oficiales de Banco Mundial y Eurostat. |
| arXiv | Búsqueda del artículo *Attention Is All You Need* | Búsqueda económica acotada y abstract de `2407.01212`. |
| Context7 | Resolución del MCP Python SDK | Resolución y consulta de documentación. |
| Firecrawl | Scrape público keyless de `example.com` | Search acotado y Scrape de Hoplite/INE. Parte del contenido procede de caché. |

El campo `native_discovery: not_checked` del JSON es correcto: **ese script** no puede certificar el catálogo nativo de Hoplite. La columna derecha recoge operaciones observadas por el agente mediante las herramientas nativas, no un resultado inventado del script. Un run nuevo y otro proyecto requieren su propia comprobación. No se ejecutaron todas las nueve operaciones de arXiv ni las capacidades prohibidas de Firecrawl.

## Entorno y fallo conservado

- Node.js **24.19.0**, Python **3.12.3**, uv **0.9.28**. Dependencias de aplicación fijadas en los lockfiles.
- El gestor `sandbox_setup` rechazó dos claims aunque mostraba workspace listo y ninguna operación activa. Se notificó a Hoplite y se ejecutó el **mismo script versionado**, no una instalación alternativa sin persistencia.
- El primer setup final terminó con salida 0. En la segunda ejecución, el guard de memoria envió **SIGTERM a npm**, con RSS registrado de aproximadamente 153 MiB y unos 13 GiB de memoria disponible. Se notificó a la plataforma y se conservó el fallo; no se desactivó el guard ni se modificaron las pruebas para ocultarlo.
- La comprobación funcional posterior sí aprobó los cuatro MCP. Eso no convierte por sí solo el segundo setup interrumpido en un éxito.
- Recuperación autorizada del 2026-09-16 a las 03:10 UTC: `bash .hoplite/setup.sh` terminó con **salida 0**; la repetibilidad del estado verificado respecto al primer setup exitoso quedó comprobada (7 hashes de archivos, 54 versiones Python, Readability y paquetes personales coincidentes), sin alterar el guard ni borrar el SIGTERM previo.

## Lo que no acredita esta verificación

1. Importación autenticada de las 27 raíces a la **biblioteca personal** y disponibilidad en otro proyecto sin copias locales. Los MCP siguen siendo de proyecto por diseño de Hoplite.
2. Programación y permisos efectivos en GitHub antes de la publicación y ejecución real. El repositorio estaba vacío y sin rama base al empezar; no se crea ni fuerza una base protegida para sortear esa limitación.
3. Compatibilidad de toda futura actualización. Las propuestas requieren revisión; los MCP remotos dependen de sus proveedores.
4. Calidad comercial de una oferta, ventas, clientes, rentabilidad o investigación exhaustiva de Internet. Los experimentos del informe no se ejecutaron.

## Reproducir

```sh
bash .hoplite/setup.sh
tools/hoplite-research/.venv/bin/python -m unittest discover -s tests -v
tools/hoplite-research/.venv/bin/python tools/hoplite-research/scripts/research_client.py check --live
python3 scripts/check_upstreams.py
python3 scripts/business_math.py
```

El cliente conserva cada comprobación fechada bajo `.research/checks/`, ignorado por Git; `--output` actualiza una vista sin borrar ese historial. El mantenimiento de GitHub también conserva los informes públicos por ejecución como artefacto independiente de la PR. Los logs locales, ZIP, runtime, cachés y credenciales no se publican.
