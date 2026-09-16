# Uso real de las herramientas instaladas

Consultas realizadas el **2026-09-16 UTC**. Solo información pública o simulaciones. Los resultados de una operación no prueban todas las capacidades del servidor ni disponibilidad futura.

| Herramienta | Operación ejecutada | Resultado inspeccionado y límite |
| --- | --- | --- |
| Fetch, MCP nativo | Leer documentación del Banco Mundial y dos APIs públicas | Texto real de documentación y JSON con países, períodos, unidades y flags. No se necesitó otro MCP. |
| arXiv, MCP nativo | Buscar `ti:"Large Language Models" AND (ti:"Economics" OR ti:"Productivity")`, máximo 3 resultados; leer abstract `2407.01212` | Búsqueda paginada real y abstract de EconNLI. No se considera el preprint evidencia de demanda ni validación de modelos actuales. |
| Context7, MCP nativo | Resolver Python MCP SDK y consultar documentación de clientes y errores | IDs de biblioteca y ejemplos reales. La documentación actual puede diferir de SDK 1.30.0; el código instalado y las pruebas locales controlan compatibilidad. |
| Firecrawl, MCP nativo | Search del registro oficial, límite 3; Scrape de documentación de Hoplite y nota del INE | Search devolvió resultados; la nota del INE incluyó las cifras y tablas. No se usó Parse, uploads, acciones, headers ni cambios de proxy. |
| Firecrawl sobre el registry | Scrape de `https://registry.modelcontextprotocol.io` | Respondió con el contenedor «Loading servers…», **no el catálogo completo**. Un HTTP 200 no probó esa extracción; la revisión del catálogo utilizó documentación/metadatos públicos acotados. |

Los dos MCP stdio fallaron al inicializar antes de instalar dependencias. Después del setup funcionaron sus catálogos y operaciones públicas en este mismo run. Los fallos previos no se presentan como éxito; su causa se resolvió mediante preparación reproducible del proyecto.

## Banco Mundial

Fuente oficial: <https://api.worldbank.org/v2/country/ES/indicator/SP.POP.TOTL?date=2022:2023&format=json&per_page=10>.

- Indicador `SP.POP.TOTL`, población total; país `ES` / `ESP`, España.
- 2023: **48.352.528**; 2022: **47.786.102** habitantes.
- Metadatos: una página, dos observaciones, fuente 2; `lastupdated=2026-07-13`.
- Valores no nulos, sin flag de observación en esa respuesta. El año del dato no es la fecha de consulta.
- No se extrapola población a mercado accesible ni número de compradores. España es una prueba de API, **no una ubicación atribuida al usuario**.
- [Documentación](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392-about-the-indicators-api-documentation) confirma que esta API no necesita claves. Revisar [licencia del conjunto y excepciones](https://datacatalog.worldbank.org/public-licenses) al reutilizar datos.

## Eurostat

Fuente oficial: <https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_gdp?lang=EN&freq=A&geo=ES&na_item=B1GQ&unit=CP_MEUR&time=2023>.

- Dataset `NAMA_10_GDP`, JSON-stat 2.0, fuente `ESTAT`.
- Dimensiones `freq=A`, `unit=CP_MEUR`, `na_item=B1GQ`, `geo=ES`, `time=2023`; tamaño `[1,1,1,1,1]`.
- `value[0]=1497761.0`: **1.497.761 millones de euros**, PIB a precios de mercado, **precios corrientes**, no crecimiento real ni ingreso disponible.
- `status[0]=p`: **provisional**. Actualización de datos: `2026-09-08T11:00:00+0200`.
- La unidad, índice y flag se conservaron; no se infiere oportunidad de negocio de ese único indicador. [Condiciones de reutilización](https://ec.europa.eu/eurostat/en/help/copyright-notice).

## INE: revisión de una afirmación comercial

<https://www.ine.es/dyngs/Prensa/ETICCE20241T2025.htm>, publicación **22-10-2025**. El extracto de Fetch solo mostró un fragmento de un gráfico; no bastaba para verificar toda la nota. Firecrawl devolvió el cuerpo y las tablas, incluyendo **21,1% de uso de IA y 44,3% de cloud de pago** en empresas de ≥10 empleados en el primer trimestre de 2025. La respuesta fue de caché, fechada por el proveedor el 15-09-2026; no se afirma scraping sin caché.

## arXiv: límite de razonamiento económico

Guo y Yang, [EconNLI](https://arxiv.org/abs/2407.01212), publicado **01-07-2024**. El abstract declara que su evaluación encontró respuestas erróneas o alucinadas en razonamiento económico. Se leyó **el abstract**, no se replicó el estudio ni se evaluaron modelos de 2026. Sirve como advertencia metodológica contextual, no como una tasa actual de fiabilidad ni prueba comercial.

## Skills aplicadas

Se cargaron las raíces de `tool-due-diligence`, `deep-web-research`, `research-team`, `ai-opportunity-validation`, `source-fact-checking`, `web-search-strategy` y `unit-economics`. Las líneas delegadas aplicaron además investigación de clientes, distribución y análisis público. La skill nueva `cohort-analysis` se verifica con casos sintéticos reproducibles.

No se simularon contactos, pilotos o ingresos. Ninguna instrucción de una página se trató como autorización para ejecutar código, acceder a una cuenta, gastar dinero o publicar campañas.
