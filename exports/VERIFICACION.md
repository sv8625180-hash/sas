# Verificación de la transferencia — 2026-09-16 UTC

## Paquete entregado

- Archivo: `hoplite-kit-portable.zip`, **216.670 bytes**.
- SHA-256: `ff0742b7450e6c299d5cae3d6d9eaf410eeb1529e9b65f3a70b80cc271b7a412`.
- **72 entradas únicas** bajo `hoplite-kit-portable/`: 71 archivos inventariados y el propio manifiesto.
- **27 skills** con hashes y procedencia: las 26 originales más `cohort-analysis`.
- **4 MCP**: Fetch, arXiv, Context7 y Firecrawl.
- Configuración sin credenciales; el ZIP no contiene sesiones, historial de Git, entornos instalados, los ZIP originales ni resultados comerciales anteriores.

## Pruebas realizadas

| Comprobación | Resultado y alcance |
| --- | --- |
| Construcción y checksum externo | El ZIP coincide con las fuentes explícitas del exportador. |
| Extracción en carpeta nueva | Integridad verificada antes y después de las pruebas; sin `.git`, `.venv` ni `node_modules` copiados en el ZIP. |
| Suite en el repositorio | **70/70 pruebas aprobadas**, incluidas 16 de portabilidad. |
| Suite desde la extracción final | **70/70 aprobadas**, usando el intérprete y las dependencias de la instalación aislada anterior. |
| Dependencias desde cero | Setup ejecutado en una extracción con HOME nuevo: primer intento interrumpido por SIGTERM; segundo intento completo, exit 0. No se presenta ese par como dos setups consecutivos satisfactorios. |
| Correspondencia del runtime | Los **47 archivos runtime** de la extracción instalada son idénticos a los del ZIP final. Solo cambiaron guía, procedencia, exportador, prueba de portabilidad y manifiesto. |
| Instalador personal local | `preparar` y `comprobar`: **27/27** con HOME aislado. No se ejecutó `importar`, login ni acceso a otra cuenta. |

## Operaciones MCP desde la instalación aislada

Comprobación del **2026-09-16 a las 03:57 UTC**, con datos públicos y sin reintentar límites del proveedor:

| MCP | Inicialización y catálogo | Operación funcional |
| --- | --- | --- |
| Fetch | Correctos; guard de URL privada también verificado | **Interrumpida**: el proceso Node de Readability terminó por SIGTERM durante la lectura de example.com. No se marca como aprobada. |
| arXiv | Correctos | Búsqueda real devolvió *Attention Is All You Need*. |
| Context7 | Correctos | Resolución real de documentación del SDK MCP de Python. |
| Firecrawl | Correctos | Scrape devolvió el contenido de example.com; puede proceder de caché. |

El sandbox también registró interrupciones del memory guard en procesos pequeños con unos 13 GiB disponibles según sus propias métricas, y un bloqueo del gestor `sandbox_setup` por lifecycle lease/fence. Ambos problemas se comunicaron a Hoplite; la instalación aislada utilizó el mismo script versionado, sin quitar la prueba de extracción HTML ni modificar los controles de la plataforma. El fallo funcional de Fetch queda conservado y separado de la integridad del paquete.

## Lo que no acredita esta entrega

- No se accedió a la cuenta de destino ni se autorizó su biblioteca personal.
- La disponibilidad nativa debe comprobarse en un hilo nuevo desde la revisión instalada en ese proyecto.
- Los servicios HTTP y sus cuotas no se transfieren ni se garantizan indefinidamente.
- Actions/Dependabot requieren habilitación y verificación en el repositorio de destino.

La evidencia detallada de esta ejecución se conserva localmente en `.hoplite/artifacts/portable-clean-verification-99_5yt9t/` y `.hoplite/artifacts/portable-final-verification-o1qjitot/`; esos logs no se incluyen en el ZIP para otra cuenta. Los resultados anteriores no sustituyen las comprobaciones indicadas en `LEEME-PRIMERO.md` para la cuenta nueva.
