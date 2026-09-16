---
name: scholarly-metadata
description: Contrasta metadatos académicos públicos de Crossref y OpenAlex, deduplica por DOI y distingue citas, revisiones y retractaciones de evidencia comercial.
---

# Metadatos académicos contrastados

Procedimiento propio y autónomo, no un MCP nuevo ni una suscripción. Descubre los lectores o clientes HTTP realmente disponibles antes de usarlos. No presupongas que un conector de otro proyecto esté instalado aquí.

1. Define pregunta, fechas, área y criterios de inclusión. Busca también revisiones críticas, correcciones y resultados negativos. Un preprint, una revista o muchas citas no garantizan que una conclusión sea válida.
2. Consulta documentación vigente del proveedor antes de automatizar. Empieza con una consulta pública por proveedor y hasta cinco resultados; amplía solo si hace falta. Crossref y OpenAlex documentan acceso básico sin cuenta a fecha de 13-09-2026, sujeto a límites que pueden cambiar.
3. Con lectores públicos existentes, las rutas documentadas incluyen `https://api.crossref.org/works` y `https://api.openalex.org/works`. Codifica los parámetros de búsqueda y utiliza `rows` o `per_page` para acotar. No pongas claves en URLs ni crees cuentas para desbloquear consultas. Detente ante 401, 403 o 429; no rotes identidades, proxies o rutas para sortear restricciones.
4. Registra título, DOI normalizado, año, tipo de documento, editorial o revista, URL, fuente y fecha de consulta. Deduplica por DOI y revisa manualmente coincidencias por título; preprints y versiones publicadas pueden tener identificadores distintos.
5. Contrasta la ficha con la editorial y, cuando sea legalmente accesible, el texto relevante. Revisa correcciones, retractaciones y versión. La ausencia de una bandera de retractación no demuestra ausencia de problemas. Dos índices pueden reproducir el mismo registro: no cuentan como dos estudios independientes.
6. Distingue resumen, metadatos y texto completo. Un DOI no otorga derechos de descarga o republicación. Crossref advierte que algunos abstracts pueden tener copyright; cita y resume lo necesario en vez de copiar un corpus. No acumules correos ni perfiles personales.
7. Para conclusiones sobre negocios con IA, examina población, tarea, comparación, magnitud del efecto, costes y fallos antes de extrapolar. La factibilidad técnica o productividad en un experimento no demuestra demanda, rentabilidad o ingresos del usuario.

Entrega referencias deduplicadas, qué material se leyó realmente, discrepancias, nivel de evidencia y límites de acceso. Conserva fallos de los proveedores separados de los éxitos de otras fuentes.

Fuentes de mantenimiento consultadas el 13-09-2026:
- https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- https://developers.openalex.org/api-reference/authentication

## Alcance de esta copia portátil

Esta raíz contiene instrucciones autónomas para la sesión actual. Usa únicamente las herramientas y permisos que ya estén disponibles, no instala servicios ni configura MCP, y no autoriza contactos, gastos, cuentas, publicaciones ni acceso a datos privados.
