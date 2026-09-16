# Herramientas adicionales para investigación comercial verificable

## Fecha, alcance y resultado

- **Fecha de investigación y consulta de fuentes:** 2026-09-16, UTC.
- **Objeto:** evaluar adiciones de valor a un paquete de investigación comercial y de negocios legales, no aumentar el número de herramientas por sí mismo.
- **Método:** 10 consultas a `web_search` nativo de Hoplite, proveedor Exa, más lecturas primarias selectivas de documentación, metadatos públicos, licencias y archivos de repositorios. Las consultas exactas constan al final.
- **Alcance inicial:** investigación e inspección de texto, sin instalar, autenticar, activar, modificar archivos ni ejecutar código de candidatos.
- **Ampliación autorizada posterior:** escribir este único informe y descargar únicamente `SKILL.md` de `cohort-analysis` y el `LICENSE` del mismo commit, con manifiesto de hashes, en `.hoplite/artifacts/candidates/cohort-analysis/`. Esa copia es para revisión, no una skill activa.
- **No realizado:** pruebas funcionales de candidatos, pruebas sintéticas de cohortes, adaptación de la skill, alta de cuentas, gasto, publicaciones, transacciones ni acceso a datos de clientes. La decisión de adaptación y las pruebas sintéticas corresponden al agente principal.

**Recomendación:** no añadir otro MCP de búsqueda o navegador por ahora. El mayor valor marginal está en consultar **World Bank y Eurostat directamente con herramientas existentes**, y opcionalmente adaptar una skill concreta de análisis de cohortes. Para modelado financiero inicial, `unit-economics` y `public-data-analysis` ya cubren una parte importante de la necesidad con menos riesgo que paquetes documentales restringidos o conectores de cuentas financieras.

Esta evaluación **no certifica funcionamiento local, disponibilidad nativa en otro run ni instalación a nivel de cuenta**. Una API oficial no es automáticamente un MCP oficial; una versión declarada en `main` no prueba publicación en un registro; aparecer en el MCP Registry no certifica seguridad ni utilidad. Ninguna fuente consultada demuestra que instalar herramientas vaya a producir ingresos.

## 1. Inventario de partida y límites de la comparación

El inventario recibido para la investigación era:

| Componente | Situación de partida | Lo que esta investigación acredita |
| --- | --- | --- |
| 26 skills personales adjuntas | Manifiesto en `.hoplite/artifacts/inspection/hoplite-skills-personales/skills/manifest.json` | Lectura del inventario y comprobación de atribuciones y licencias inline; no instalación en la biblioteca personal de Hoplite. |
| Fetch `2026.8.18` | MCP del paquete original | Dato del inventario recibido; no prueba funcional de este MCP en esta investigación. |
| `arxiv-mcp-server` `0.7.2` | MCP del paquete original | Dato del inventario recibido; no prueba funcional de este MCP en esta investigación. |
| Context7 HTTP | MCP del paquete original | Lectura de documentación pública para evaluar solapamiento; no conexión funcional probada aquí. |
| Firecrawl v2 HTTP keyless | MCP del paquete original | Lectura de documentación pública y contraste del alcance permitido; no conexión funcional probada aquí. |
| `web_search` Exa, navegador y GitHub/source control nativos de Hoplite | Capacidades ya disponibles | `web_search` sí se utilizó para las 10 consultas. No se infiere que hagan falta otros conectores ni se extraen credenciales administradas por Hoplite. |

Las 26 skills del manifiesto son: `ab-test-setup`, `ai-opportunity-validation`, `ai-service-evaluation`, `analytics-tracking`, `competitive-intelligence`, `competitor-alternatives`, `copywriting`, `customer-discovery`, `deep-web-research`, `distribution-validation`, `free-tool-strategy`, `launch-strategy`, `lead-research-assistant`, `market-customer-research`, `page-cro`, `pricing-strategy`, `product-manager-toolkit`, `public-data-analysis`, `research-team`, `scholarly-metadata`, `seo-audit`, `source-fact-checking`, `tool-due-diligence`, `trend-analysis`, `unit-economics` y `web-search-strategy`.

Se leyeron las instrucciones de `tool-due-diligence/SKILL.md` y `public-data-analysis/SKILL.md` del área de inspección, y se cargaron sus equivalentes disponibles en `.agents/skills/`. Esas instrucciones se aplicaron a la evaluación de procedencia, permisos, privacidad, costes y calidad de evidencia; no instalan herramientas por sí mismas.

## 2. Matriz de evaluación: 15 líneas de decisión

Se agrupan APIs afines para cubrir todos los proveedores solicitados sin presentarlas como MCP. Las fechas indicadas para commits provienen de metadatos públicos; la consulta se realizó el 2026-09-16. Las versiones marcadas **`main`** son las declaradas en el código consultado, no afirmaciones de que ese código esté publicado o sea estable.

| ID y candidato oficial/original | Licencia, versión, transporte, autenticación y coste documentados | Lectura/escritura, riesgos y valor marginal |
| --- | --- | --- |
| **C01. World Bank / Eurostat**. [Indicators API](https://datahelpdesk.worldbank.org/knowledgebase/articles/889392), [Eurostat Statistics API](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics). | **APIs oficiales, no MCP institucionales identificados en esta revisión.** World Bank V2; Eurostat Statistics 1.0, JSON-stat 2.0. HTTP público sin credenciales para estas consultas. World Bank: CC-BY 4.0 por defecto para datos propios, con excepciones por conjunto y condiciones adicionales. Eurostat: reutilización comercial generalmente permitida con atribución, con excepciones. No se verificó una cuota universal de solicitudes; gratuidad no significa acceso ilimitado. | Lectura de indicadores, países, series y metadatos. **Valor alto para contexto económico y comparación geográfica**, no para demostrar compras. Usar Fetch/Python existentes evita un intermediario y mantenimiento innecesarios. Riesgos: revisiones de series, datos ausentes, unidades, mezcla de períodos y licencias de terceros. |
| **C02. FRED**. [API oficial de St. Louis Fed](https://fred.stlouisfed.org/docs/api/fred/). | API HTTP, no MCP institucional identificado. API con clave; no seleccionar como adición sin claves. La documentación general enlaza API Keys y Terms of Use; las lecturas directas de esas páginas específicas agotaron el tiempo, por lo que requisitos exactos, cuotas y condiciones no quedaron revalidados completamente. No se verificó licencia uniforme para todas las series. | Lectura de series, publicaciones, revisiones y observaciones. Útil para inflación, financiación y ciclo económico; no estima disposición a pagar. No usar un proxy de terceros para eludir gestión de acceso o límites. No hubo llamada funcional a la API. |
| **C03. Google Analytics MCP**. [Repositorio](https://github.com/googleanalytics/google-analytics-mcp), [Google Developers](https://developers.google.com/analytics/devguides/MCP). | Oficial **experimental**, Apache-2.0. PyPI `analytics-mcp` **0.7.0**, publicado 2026-07-29. Local/stdio; ADC/OAuth y scope `analytics.readonly`, proyecto Google y permisos sobre propiedades. [Cuotas oficiales](https://developers.google.com/analytics/devguides/reporting/data/v1/quotas): Standard, por ejemplo, 200.000 tokens de cuota Core por propiedad/día; **no son tokens del modelo**. No se documentó tarifa MCP independiente. | Lectura: cuentas, propiedades, enlaces Ads, informes, funnels, dimensiones/métricas personalizadas y tiempo real. **Alto valor cuando exista tráfico propio**, poco para investigación inicial sin datos. Riesgo de revelar analítica privada al modelo o a otros conectores; conectar solo con autorización específica. |
| **C04. Search Console / Google Trends**. [Autorización Search Console](https://developers.google.com/webmaster-tools/v1/how-tos/authorizing), [Trends oficial](https://developers.google.com/search/apis/trends). | **APIs, no MCP oficiales identificados en esta revisión acotada.** Search Console usa OAuth y dispone de scope de lectura. [Cuotas](https://developers.google.com/webmaster-tools/limits): Search Analytics, 1.200 QPM por sitio y por usuario, además de límites de carga y proyecto. Trends sigue documentado como **alpha de acceso limitado por solicitud**; no se confirmó precio/cuota pública general ni disponibilidad para esta cuenta. | Search Console sirve para rendimiento de sitios autorizados; la API también tiene operaciones de gestión que habría que excluir. Trends aporta interés relativo, **no volumen absoluto, ingresos ni ventas**. No presentar wrappers de scraping como API oficial ni el acceso alpha como disponible para todos. |
| **C05. Stripe MCP**. [Documentación oficial](https://docs.stripe.com/mcp). | Servicio remoto `https://mcp.stripe.com`, HTTP; OAuth o clave restringida. No se fijó una versión pública del servicio ni una licencia OSS de su implementación hospedada. No se documentó tarifa MCP separada; aplican productos y condiciones de la cuenta, sin inferir que todas las operaciones sean gratuitas. | Incluye `stripe_api_read` y **`stripe_api_write`**, este último para POST/PATCH/PUT/DELETE. Determinadas acciones financieras, como reembolsos y pagos salientes, requieren confirmación humana. **Solo después de tener ventas y autorización**, empezando con sandbox y lectura. No conectar para buscar oportunidades comerciales iniciales. |
| **C06. Shopify Storefront / Dev MCP**. [Storefront](https://shopify.dev/docs/apps/build/storefront-mcp/servers/storefront), [AI Toolkit y Dev MCP](https://shopify.dev/docs/apps/build/ai-toolkit). | Storefront: HTTP por tienda, consultas públicas sin autenticación; herramientas de catálogo UCP exigen perfil de agente. [Términos API Shopify](https://www.shopify.com/legal/api-terms); límites según identificación. Dev MCP: local/stdio, sin autenticación; npm declara `@shopify/dev-mcp` **1.15.2**, licencia **ISC**, sin auditoría del artefacto completo. No equiparar esa licencia con la del servicio Storefront hospedado. | Storefront lee productos/políticas y **modifica carritos**; precios visibles no equivalen a ventas ni a ingresos del vendedor. Dev MCP consulta documentación/esquemas y valida código: **no es un conector de ingresos**. Solapa con Context7 y navegador. La gestión autenticada de tiendas es otra capacidad del toolkit, no debe habilitarse automáticamente. |
| **C07. HubSpot MCP**. [Documentación oficial](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server). | Remoto `https://mcp.hubspot.com`, **Streamable HTTP**, OAuth con **PKCE obligatorio** y configuración de conector. Sin versión/licencia OSS fijadas para el servicio hospedado. Disponibilidad por suscripción, permisos y configuración; ciertas funciones requieren planes superiores. No se verificó una tarifa/cuota MCP universal. | **No es exclusivamente lectura:** consulta CRM y permite crear/editar registros, segmentos, pipelines y contenido; diversas escrituras exigen confirmación. En cuentas gratuitas puede editarse el pipeline predeterminado, pero no crear pipelines personalizados; determinadas funciones de quotes requieren plan superior. Alto valor para operaciones comerciales existentes; riesgo con clientes, comunicaciones y publicación. |
| **C08. Tavily MCP**. [Repositorio oficial](https://github.com/tavily-ai/tavily-mcp). | MIT; `package.json` de `main`: **0.2.22**. Local/stdio o HTTP remoto, API key u OAuth. [Tarifas](https://docs.tavily.com/documentation/api-credits): 1.000 créditos gratuitos/mes; búsqueda básica 1 crédito, avanzada 2; PAYG **USD 0,008/crédito**. Créditos gratuitos requieren cuenta/clave; no se abrió ninguna. | Search, Extract, Map, Crawl. Lectura externa con gasto y riesgo de crawling excesivo. **Redundante** frente a Exa nativo + Firecrawl. Solo añadir si una comparación acotada demuestra cobertura o calidad marginal. Una búsqueda de otro proveedor no convierte copias de la misma noticia en evidencia independiente. |
| **C09. Exa MCP**. [Repositorio oficial](https://github.com/exa-labs/exa-mcp-server). | MIT según metadatos del repositorio; `main`: **3.4.1**. Streamable HTTP hospedado, anónimo con límites no cuantificados en el README; OAuth/API key para más capacidad y Agent. [Precios API](https://exa.ai/docs/reference/pricing), página actualizada 2026-09-15: Search **USD 7/1.000 solicitudes**, hasta 10 resultados base. No extrapolar esta tarifa a la cuota anónima del MCP ni al contrato de Hoplite. | Búsqueda, fetch, filtros avanzados y Agent opcional. **Mismo proveedor que `web_search` nativo**: no añade otra fuente independiente. Agent/enrichment puede añadir gasto y datos personales; no habilitar para esta investigación. El acceso anónimo no prueba disponibilidad permanente ni ilimitada. |
| **C10. Brave Search MCP**. [Repositorio oficial](https://github.com/brave/brave-search-mcp-server). | MIT; `main`: **2.1.3**. stdio por defecto, HTTP opcional; requiere clave. [Precios oficiales](https://brave.com/search/api/): Search **USD 5/1.000 solicitudes**, USD 5 de créditos mensuales. La página indica tarjeta como medida antifraude para planes gratuitos. No se abrió cuenta ni se proporcionó tarjeta. | Web, noticias, imágenes, vídeos, lugares y resúmenes. **Valor marginal como índice distinto**, especialmente para negocios locales; no entra en «sin claves». Posponer hasta medir necesidad y autorizar cuenta/coste. Datos públicos de lugares no autorizan enriquecimiento de personas ni contacto. |
| **C11. Microsoft Playwright MCP**. [Repositorio oficial](https://github.com/microsoft/playwright-mcp). | Apache-2.0; `main`: **0.0.81**, dependencias Playwright alpha fechadas 2026-09-14. stdio/HTTP; sin API key propia, pero requiere runtime y navegadores. Sin tarifa de servicio del paquete local; hay coste de cómputo y mantenimiento. No se instaló ni probó esa versión. | Navegación, snapshots, formularios, archivos y ejecución en navegador: **no es solo lectura**. Perfiles pueden persistir; los filtros de origen no constituyen una frontera de seguridad. **Redundante con el navegador nativo de Hoplite**. Otro perfil puede introducir sesiones y almacenamiento distintos de los administrados por Hoplite. |
| **C12. Corey Haines Marketing Skills**. [Repositorio original](https://github.com/coreyhaines31/marketingskills). | MIT. Commit observado **`5b2c0007766c6a1cf1d53fd8fc73e979e0821022`**, 2026-09-05. Skills locales; sin transporte MCP ni autenticación intrínseca, aunque integraciones referenciadas pueden exigirlos y tener costes. Véase la distinción de licencia histórica/posterior en la sección 5. | Amplio solapamiento con las 26 skills existentes. Nombres actuales como `ab-testing`, `analytics` y `cro` difieren de algunos adjuntos; **no sobrescribir adaptaciones por coincidencia aproximada de nombre**. Revisar integraciones y referencias comerciales y añadir solo una carencia demostrada. Popularidad y patrocinio no son prueba de eficacia. |
| **C13. Anthropic Skills**. [Repositorio oficial](https://github.com/anthropics/skills). | Commit **`34040c9c568585f6929bedeaad110ad08f079624`**, 2026-09-10. **Licencia por subcarpeta:** `mcp-builder` tiene Apache-2.0; [`xlsx/LICENSE.txt`](https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/xlsx/LICENSE.txt) es propietaria y restringe copia, extracción fuera de los servicios, derivados y distribución. No se presume licencia uniforme por ser un repositorio público. | No importar el repositorio completo. **XLSX no es una adición libre de modelado financiero para Hoplite**. Herramientas, dependencias y condiciones de otros documentos requieren revisión individual. No se descargó esta skill a una ubicación activa. |
| **C14. Pawel Huryn PM Skills**. [Repositorio original](https://github.com/phuryn/pm-skills). | MIT. Commit **`8607e3b077817f89bf4a9b623246219734ac3be0`**, 2026-09-14. Skills Markdown locales; pandas/numpy sugeridos para análisis, sin claves obligatorias. La copia autorizada posterior de `cohort-analysis` conserva el texto original y la licencia; no es una adaptación ni instalación. | `cohort-analysis` aporta especialización útil. Adaptar antes de activar: no exigir «2–3 insights significativos» si los datos no los sostienen; distinguir períodos no observados de retención cero. `prioritize-assumptions` menciona confianza 1–10 y luego `1 − Confidence` sin normalización explícita: **no importar ese procedimiento sin corregirlo**. |
| **C15. OpenAI Skills / sucesor Plugins**. [Skills](https://github.com/openai/skills), [Plugins](https://github.com/openai/plugins). | `openai/skills` **se declara deprecado** y remite a Plugins. Commit principal observado **`49f948faa9258a0c61caceaf225e179651397431`**, 2026-06-24; no confundirlo con la fecha de último push de cualquier rama. La antigua carpeta `jupyter-notebook` tiene Apache-2.0; su scaffold usa stdlib y rutas Codex. No se confirmó licencia para la carpeta actual `plugins/data-analytics/skills/analyze-data-quality`: no extrapolar Apache a ella. | Notebooks y QA de datos son pertinentes, pero el plugin actual también incorpora conectores/MCP y publicación de artefactos. No instalar el bundle. El antiguo path `skills/.curated/spreadsheet` devuelve 404: **no presentarlo como skill actual disponible y revisada**. Portabilidad de rutas y alias de capacidades a Hoplite pendiente. |

### Interpretación de licencias de datos y de servicios

- World Bank distingue datos propios bajo CC-BY 4.0, ODbL, microdatos con condiciones de investigación, licencias externas y licencias personalizadas. **No aplicar CC-BY a todo lo alojado o indexado por World Bank.** Fuente: <https://datacatalog.worldbank.org/public-licenses>.
- Eurostat permite generalmente la reutilización comercial de sus estadísticas con atribución y obliga a señalar modificaciones/traducciones; hay excepciones para datos de otras fuentes y documentos de terceros. Su aviso da ejemplos de datos de países no europeos que pueden necesitar exclusión de una reutilización comercial. **No confundir licencia del contenido editorial con permiso universal para todas las series.** Fuente: <https://ec.europa.eu/eurostat/en/help/copyright-notice>.
- Las licencias MIT/Apache/ISC de clientes o paquetes no conceden derechos sobre datos, cuentas, marcas o servicios remotos. La ausencia de una tarifa MCP independiente en las páginas revisadas no equivale a una garantía de gratuidad.
- Los precios anteriores son los publicados por el proveedor al consultarlos; no son compras realizadas, presupuestos garantizados ni evidencia de rentabilidad del usuario.

## 3. Tabla operativa de decisión

**«Instalado original» se usa aquí como categoría solicitada del inventario de partida, no como veredicto técnico.** En cada fila original se conserva explícitamente que instalación, inicialización, operación y disponibilidad nativa deben verificarse por separado. «Candidato sin ejecutar» tampoco autoriza instalación o activación.

| Componente | Categoría de decisión | Acción y condición |
| --- | --- | --- |
| 26 skills adjuntas | **Instalado original — inventariado, no certificado aquí** | Mantener atribuciones; el agente principal verifica raíces activas y alcance personal/proyecto. No importar paquetes completos para sustituir adaptaciones. |
| Fetch `2026.8.18` | **Instalado original — inventariado, no certificado aquí** | Reutilizar si su operación está verificada por el agente principal; no añadir otro fetch por recuento. |
| arXiv `0.7.2` | **Instalado original — inventariado, no certificado aquí** | Verificar una operación representativa y los límites de acceso; papers/citas no demuestran demanda comercial. |
| Context7 HTTP | **Instalado original — inventariado, no certificado aquí** | Documentación técnica, no investigación de ventas. No habilitar repositorios privados por defecto. |
| Firecrawl v2 keyless HTTP | **Instalado original — inventariado, no certificado aquí** | Allowlist efectiva de Search/Scrape; excluir Parse y demás capacidades aunque aparezcan en el servicio. |
| World Bank / Eurostat, C01 | **Candidato sin ejecutar** | Dos recetas HTTP públicas con herramientas existentes, sin MCP adicional; pruebas propuestas en la sección 6. |
| FRED, C02 | **Credenciales** | Diferir clave y revisión completa de términos/cuotas; las lecturas específicas sufrieron timeout. |
| Google Analytics, C03 | **Credenciales** | Solo cuando haya propiedades propias/autorizadas y necesidad concreta; comenzar en lectura. |
| Search Console, C04 | **Credenciales** | Requiere acceso a un sitio; no identificado MCP oficial en la búsqueda acotada. |
| Google Trends API, C04 | **Credenciales / acceso alpha** | Acceso limitado por solicitud; no se solicitó ni confirmó admisión. |
| Stripe, C05 | **Credenciales** | Datos comerciales reales y permiso específico antes de conectar; escrituras fuera del alcance inicial. |
| Shopify Storefront, C06 | **Candidato sin ejecutar — no priorizado** | Sin clave para consultas públicas, pero requiere tienda/perfil según herramienta y expone carritos. No propuesto como una de las tres adiciones inmediatas. |
| Shopify Dev MCP, C06 | **Redundante** | Context7 y las capacidades nativas cubren el objetivo actual; distinto de gestión de tiendas. |
| HubSpot, C07 | **Credenciales** | Solo con CRM propio/autorizado y necesidad; exposición de datos y escrituras importantes. |
| Tavily, C08 | **Redundante; además credenciales** | Exigir evaluación de cobertura marginal antes de abrir cuenta. |
| Exa MCP, C09 | **Redundante** | Mismo proveedor que búsqueda nativa; anónimo no significa sin límites. |
| Brave, C10 | **Credenciales** | Índice distinto potencialmente útil; posponer alta, tarjeta y coste hasta demostrar necesidad. |
| Playwright MCP, C11 | **Redundante** | Usar navegador nativo de Hoplite; no crear otro perfil/servidor sin carencia concreta. |
| Marketing Skills completo, C12 | **Redundante** | Solo cambios selectivos revisados, preservando licencia histórica/posterior y adaptaciones. |
| Anthropic XLSX, C13 | **No incorporar por condiciones de licencia** | Excepción explícita a las cuatro categorías básicas: no clasificar restricciones de licencia como simple falta de credenciales. |
| Otras carpetas Anthropic, C13 | **Candidato sin ejecutar — no priorizado** | Revisión individual de licencia y dependencias, sin autorización para descarga/activación en esta tarea. |
| `cohort-analysis`, C14 | **Candidato sin ejecutar — texto descargado para revisión** | Única raíz adicional descargada; commit fijo y MIT íntegra. Decisión de adaptación y pruebas a cargo del agente principal. |
| `prioritize-assumptions`, C14 | **No incorporar sin corregir** | Revisar la escala de confianza antes de usar la fórmula de riesgo; no descargar/activar en esta tarea. |
| OpenAI notebooks / data analytics, C15 | **Candidato sin ejecutar — no priorizado** | Repositorio antiguo deprecado; licencia y portabilidad del sucesor sin confirmar. No es una de las tres adiciones inmediatas. |

## 4. Registry oficial, solapamientos y actualización segura

### Registry no equivale a certificación

Se consultaron <https://registry.modelcontextprotocol.io/>, la [explicación del registry](https://modelcontextprotocol.io/registry/about) y la [referencia de su API](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/official-registry-api.md).

El registry almacena metadatos: nombres, ubicación de paquetes/servidores, instrucciones de configuración y datos de descubrimiento. No aloja necesariamente el código ni acredita una operación funcional, seguridad o eficacia comercial. Su documentación lo presenta en preview. Verificar un namespace no equivale a auditar código, dependencias o comportamiento del servicio.

Las consultas acotadas de World Bank, Eurostat y Search Console devolvieron publicadores de terceros. Por ejemplo, `io.github.cyanheads/worldbank-mcp-server` no convierte al servidor en un producto oficial de World Bank. La consulta FRED quedó paginada. Por tanto, la conclusión correcta es **«no se identificó un MCP institucional en esta revisión»**, no «no existe en todo Internet».

### Context7, Firecrawl y capacidades nativas

- Context7 aporta documentación de software; su [overview](https://context7.com/docs/overview) menciona mayores límites y repositorios privados con API key. No es una fuente de ventas ni autoriza envío de código privado.
- Firecrawl aporta extracción/búsqueda. La [documentación actual](https://docs.firecrawl.dev/mcp-server) incluye **Search, Scrape y Parse incluso en keyless**. Las reglas de este proyecto permiten únicamente Search/Scrape públicos y acotados. Conservar una allowlist efectiva, no confiar en que una preferencia textual o filtro del cliente Python limite también el transporte HTTP nativo.
- Exa MCP no constituye una fuente de búsqueda independiente de Exa nativo. Brave puede aportar un índice distinto; la ventaja efectiva aún requeriría una comparación autorizada.
- Playwright MCP puede ser útil donde falte automatización de navegador, pero Hoplite ya expone navegador persistente y herramientas de interacción. La instalación adicional aumenta superficie y sesiones sin una carencia demostrada aquí.

### Actualizaciones

No se crearon ni cambiaron automatizaciones en esta tarea. Para una decisión posterior, preferir **detección y propuesta de actualización para revisión**, con commit/versiones fijados, hashes, licencias y changelog. No activar código remoto nuevo ni ampliar herramientas/permisos automáticamente.

Los servicios remotos pueden cambiar sin actualizar un paquete local. Stripe y HubSpot ya exponen escrituras amplias; Firecrawl expone operaciones fuera de la política del proyecto. Volver a revisar catálogo, permisos, cuotas y al menos una operación representativa tras un cambio, preservando resultados fallidos. No sobrescribir las versiones adaptadas de skills por las originales sin revisar cambios de comportamiento y nombres.

## 5. Licencias de las 26 skills adjuntas

### Evidencia local comprobada

La ausencia de archivos `LICENSE` separados **no implica ausencia del texto MIT**: las adaptaciones lo incorporan dentro de sus `SKILL.md`.

Se examinó el manifiesto y los textos de `.hoplite/artifacts/inspection/hoplite-skills-personales/skills/`:

- **26 skills**, de las cuales **16** tienen atribuciones externas declaradas.
- **25 instancias de licencia declaradas:** 16 de `aitmpl` y 9 complementarias de `marketingskills`.
- Las **25** coinciden con los hashes del manifiesto al permitir únicamente variantes de cero, uno o dos saltos de línea finales del bloque de licencia. No se normalizaron palabras, copyright, espacios internos ni condiciones.
- Una comprobación intermedia que permitía solo uno/dos saltos finales no reconoció los bloques de `aitmpl`; al incluir el caso sin salto final se reconciliaron todos. Fue una diferencia de delimitación del texto, no evidencia de licencia alterada.

| Atribución declarada | Skills |
| --- | --- |
| Daniel (San) Ávila + Corey Haines | `ab-test-setup`, `analytics-tracking`, `competitor-alternatives`, `copywriting`, `free-tool-strategy`, `launch-strategy`, `page-cro`, `pricing-strategy`, `seo-audit`. |
| Daniel (San) Ávila | `competitive-intelligence`, `lead-research-assistant`, `market-customer-research`, `product-manager-toolkit`, `source-fact-checking`, `trend-analysis`, `web-search-strategy`. |
| Sin atribución externa declarada | `ai-opportunity-validation`, `ai-service-evaluation`, `customer-discovery`, `deep-web-research`, `distribution-validation`, `public-data-analysis`, `research-team`, `scholarly-metadata`, `tool-due-diligence`, `unit-economics`. |

Las diez últimas no deben recibir automáticamente una licencia general de redistribución por el hecho de compartir paquete con material MIT. El inventario no prueba por sí solo derechos adicionales sobre cada aportación propia.

### Licencia en el commit original frente a texto en un commit posterior

| Fuente | Evidencia y límite |
| --- | --- |
| `davila7/claude-code-templates`, commit `ec126b9ded118ba66c2125fa39eb5b0e87d701bd` | Se leyó el [LICENSE del mismo commit](https://raw.githubusercontent.com/davila7/claude-code-templates/ec126b9ded118ba66c2125fa39eb5b0e87d701bd/LICENSE). MIT, copyright 2025 Daniel (San) Ávila. SHA-256 **`15cc073ffa3a01bb7da145aeae2a842b473860d142c92485536ee9c91195a705`**, coincidente con el manifiesto. |
| `coreyhaines31/marketingskills`, commit histórico `3617bdc883230c2eec6cd77721987f71650902e5` | La lectura de `/LICENSE` devolvió **404**. El árbol completo de ese commit contiene `README.md` y `skills`, sin archivos de licencia. El [README histórico](https://github.com/coreyhaines31/marketingskills/blob/3617bdc883230c2eec6cd77721987f71650902e5/README.md#license), líneas 178–180 consultadas, **sí declara «MIT - Use these however you want.»** No afirmar que faltaba toda declaración de licencia. |
| `coreyhaines31/marketingskills`, commit posterior `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` | Se leyó el [LICENSE completo fijado a ese commit](https://raw.githubusercontent.com/coreyhaines31/marketingskills/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/LICENSE). MIT, copyright 2025 Corey Haines. SHA-256 **`b70d71e24e40fce5da8f4b6f9cd862096a048e433db7f3c8cac5e348e6d34591`**, exactamente el hash complementario adjunto. |

**Conclusión de procedencia:** registrar por separado **«declaración MIT en README histórico»** y **«texto completo contrastado en commit posterior»**. No afirmar que se verificó un `LICENSE` inexistente en el commit antiguo, ni reemplazar silenciosamente la revisión histórica por una revisión actual. Mantener atribuciones, avisos íntegros, URLs y hashes.

Para otros repositorios, no extrapolar licencias: Anthropic y OpenAI requieren revisión por subcarpeta. En particular, la licencia restrictiva de Anthropic XLSX no queda anulada por licencias Apache presentes en otras carpetas del mismo repositorio.

## 6. Máximo de tres adiciones propuestas y pruebas pendientes

**No se proponen nuevos servidores MCP inmediatos.** Las primeras dos adiciones son recetas de fuentes públicas sobre capacidades existentes; la tercera es una posible adaptación de texto. No se ejecutaron las siguientes consultas ni pruebas sintéticas durante esta evaluación.

### 6.1. Receta World Bank

Consulta funcional propuesta, **no ejecutada**:

```text
https://api.worldbank.org/v2/country/ES/indicator/SP.POP.TOTL?date=2022:2023&format=json&per_page=10
```

Prueba de aceptación:

1. Validar estructura de respuesta, indicador `SP.POP.TOTL`, país, años solicitados, paginación y fecha de actualización.
2. Distinguir valores numéricos, cero y ausentes; no completar ausentes con cero.
3. Contrastar al menos una observación con la fuente oficial, conservar versión/fecha y unidad.
4. Revisar la licencia del conjunto antes de reutilizarlo comercialmente.
5. No presentar población o PIB como mercado comprable ni como ventas.

### 6.2. Receta Eurostat

Consulta funcional propuesta, **no ejecutada**:

```text
https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_gdp?lang=EN&freq=A&geo=ES&na_item=B1GQ&unit=CP_MEUR&time=2023
```

Prueba de aceptación:

1. Validar JSON-stat 2.0, dimensiones, índices y el producto de tamaños antes de interpretar `value`.
2. Comprobar país, frecuencia, concepto, año, unidad y flags de calidad/provisionalidad.
3. No mezclar millones de euros a precios corrientes con volumen real, poder adquisitivo o datos de otra frecuencia.
4. Contrastar una observación y preservar metadatos y excepciones de reutilización.
5. Probar con fixtures locales un valor ausente y una dimensión inesperada; no fabricar esos casos como respuestas recibidas de la API.

### 6.3. Adaptación opcional de `cohort-analysis`

Raíz de origen: <https://github.com/phuryn/pm-skills/blob/8607e3b077817f89bf4a9b623246219734ac3be0/pm-data-analytics/skills/cohort-analysis/SKILL.md>.

La copia descargada conserva el original. **No se ha corregido, activado ni probado.** Si el agente principal decide adaptarla, conservar licencia MIT y atribución y añadir controles de denominadores, cohortes maduras, censura temporal y fuerza de evidencia. No exigir encontrar un número fijo de patrones «significativos».

Prueba sintética propuesta, **no ejecutada**:

- Cohorte A: 10 usuarios iniciales, 8 retenidos en un período definido → 80%.
- Cohorte B: 5 usuarios iniciales, 1 retenido en el mismo período relativo → 20%.
- Retención conjunta ponderada: `(8 + 1) / (10 + 5)` → **60%**, no el 50% de promediar porcentajes sin ponderación.
- Añadir un período todavía no observable: marcarlo no observado, no como retención cero.
- Añadir denominador cero y duplicados: validar o rechazar explícitamente, sin divisiones engañosas.
- Mantener datos sintéticos separados de cualquier afirmación de demanda, causalidad o desempeño real.

## 7. Copia de revisión autorizada de `cohort-analysis`

La descarga posterior se realizó el **2026-09-16, 02:27:43 UTC**. Se hicieron únicamente dos GET de texto público fijados al commit autorizado; no se descargó el repositorio completo, no se instalaron dependencias y no se ejecutó código del candidato.

- Directorio: `.hoplite/artifacts/candidates/cohort-analysis/`.
- Repositorio: <https://github.com/phuryn/pm-skills>.
- Commit: **`8607e3b077817f89bf4a9b623246219734ac3be0`**.
- Manifiesto local: `.hoplite/artifacts/candidates/cohort-analysis/manifest.json`.
- Estado registrado: `downloaded-for-text-review-only`.
- `installation_performed`, `activation_performed`, `candidate_code_executed` y `functional_tests_performed`: **false**.
- Adaptación: `pending-primary-agent-decision`.

| Archivo local | Origen exacto | Fecha/hora de descarga UTC | Bytes | SHA-256 |
| --- | --- | --- | --- | --- |
| `SKILL.md` | <https://raw.githubusercontent.com/phuryn/pm-skills/8607e3b077817f89bf4a9b623246219734ac3be0/pm-data-analytics/skills/cohort-analysis/SKILL.md> | `2026-09-16T02:27:43.137148Z` | 5026 | `bd721a429e58c71a1a488ac1e89ba2bcbb9e179cb9c0b5eac44a3c3b3e9fdb15` |
| `LICENSE` | <https://raw.githubusercontent.com/phuryn/pm-skills/8607e3b077817f89bf4a9b623246219734ac3be0/LICENSE> | `2026-09-16T02:27:43.184947Z` | 1068 | `a2c922f9b81b4f40347ddfa79c38eda0f1278b5a6d108bd4099b4da254c774ee` |

Los dos hashes se compararon con los observados en la revisión inicial antes de guardar los bytes. Ambos coincidieron. Se validó UTF-8 y ausencia de contenido binario NUL; los textos se conservaron sin transformación y con permisos de archivo no ejecutable. Estas comprobaciones acreditan **integridad de la copia de texto**, no seguridad de un programa, calidad de la skill ni funcionamiento de sus procedimientos.

El manifiesto incluye URLs solicitada/final, timestamps, tamaño, codificación, hash y estado. No incluye secretos ni credenciales. No se copió nada a `.agents/skills/`, bibliotecas personales, configuraciones MCP o directorios de plugins.

## 8. Registro exacto de búsquedas

Todas las consultas siguientes se hicieron el **2026-09-16 UTC** con `functions.web_search`, proveedor **Exa**. La tabla conserva las cadenas originales, incluidas expresiones como `site.github.com`, que **no se corrigen retrospectivamente** a un operador distinto.

No se dispone aquí de hora individual certificada para cada búsqueda original: se registra la fecha conocida y no se inventan timestamps. La numeración corresponde al orden de invocación registrado; consultas de un mismo lote pudieron solaparse. «Resultados solicitados» es el parámetro `numResults`, no una afirmación de exhaustividad. **No se hicieron nuevas búsquedas amplias para redactar este archivo ni para descargar la copia de revisión.**

| ID | Fecha UTC | Consulta exacta | Resultados solicitados |
| --- | --- | --- | --- |
| Q01 | 2026-09-16 | `official MCP registry registry.modelcontextprotocol.io FRED World Bank Eurostat MCP server API` | 6 |
| Q02 | 2026-09-16 | `site.github.com googleanalytics google analytics MCP server official Search Console MCP Google` | 5 |
| Q03 | 2026-09-16 | `site.developers.google.com search Google Trends API alpha official access 2026` | 5 |
| Q04 | 2026-09-16 | `official Stripe Shopify HubSpot MCP server remote OAuth documentation` | 6 |
| Q05 | 2026-09-16 | `official MCP server Tavily Exa Brave Search API pricing license GitHub` | 6 |
| Q06 | 2026-09-16 | `site.github.com coreyhaines31 marketingskills LICENSE skills marketing` | 3 |
| Q07 | 2026-09-16 | `site:github.com/phuryn/pm-skills license README financial business model` | 3 |
| Q08 | 2026-09-16 | `anthropics skills xlsx license openai skills spreadsheet financial modeling official` | 4 |
| Q09 | 2026-09-16 | `site:shopify.dev MCP Storefront Dev MCP authentication pricing tools official` | 4 |
| Q10 | 2026-09-16 | `FRED API World Bank Indicators API Eurostat dissemination API official no authentication data reuse license` | 6 |

### Consultas exactas adicionales al catálogo, no búsquedas web amplias

GET públicos de metadatos del MCP Registry, todos el **2026-09-16 UTC**, con `version=latest` y `limit=15`. **No son llamadas `tools/call` a ningún MCP candidato.**

| ID | URL exacta | Resultado y límite |
| --- | --- | --- |
| R01 | <https://registry.modelcontextprotocol.io/v0.1/servers?search=fred&version=latest&limit=15> | 15 registros en la página leída; hubo `nextCursor`, por lo que no se agotó el catálogo. La coincidencia por substring también devolvió nombres ajenos a datos FRED. |
| R02 | <https://registry.modelcontextprotocol.io/v0.1/servers?search=worldbank&version=latest&limit=15> | 8 registros en la respuesta consultada; publicadores de terceros, no certificación de World Bank. |
| R03 | <https://registry.modelcontextprotocol.io/v0.1/servers?search=eurostat&version=latest&limit=15> | Publicadores de terceros en la respuesta leída; no prueba de afiliación institucional. |
| R04 | <https://registry.modelcontextprotocol.io/v0.1/servers?search=search-console&version=latest&limit=15> | 11 registros en la respuesta consultada; no se identificó uno institucional de Google. No cubre todas las posibles variantes de nombre. |

## 9. Registro de fuentes primarias y lecturas selectivas

**Fecha de consulta para todas las fuentes de esta sección: 2026-09-16 UTC.** Este registro conserva fuentes utilizadas y lecturas fallidas pertinentes; no pretende convertir todos los resultados secundarios de un buscador en fuentes avaladas. Se prefirieron documentos del proveedor y archivos exactos frente a cifras de popularidad o catálogos agregados.

### 9.1. Documentación de servicios y datos

| Tema | URLs exactas consultadas o utilizadas | Evidencia / límite |
| --- | --- | --- |
| MCP Registry | <https://registry.modelcontextprotocol.io/>; <https://registry.modelcontextprotocol.io/docs>; <https://modelcontextprotocol.io/registry/about>; <https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/official-registry-api.md> | Catálogo de metadatos, preview, filtros y namespaces; no operación funcional de servidores. |
| World Bank API | <https://datahelpdesk.worldbank.org/knowledgebase/articles/889392> | Documentación oficial recuperada por búsqueda: V2, indicadores y ausencia de autenticación para esta API. No se ejecutaron los endpoints de datos propuestos. |
| World Bank licencias | <https://datacatalog.worldbank.org/public-licenses> | Lectura directa de CC-BY, excepciones, ODbL, microdatos y licencias externas/personalizadas. |
| World Bank rutas de términos | <https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets>; <https://datahelpdesk.worldbank.org/knowledgebase/articles/906519-world-bank-data-api-terms-of-use> | El material recuperado de esas rutas no se usó para asignar licencia general a estadísticas: apareció contenido general/navegación. Se resolvió la licencia de datos con Data Catalog. |
| Eurostat API | <https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access>; <https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics> | REST, versión 1.0, filtros y JSON-stat 2.0; se siguió el enlace de copyright de la página oficial. |
| Eurostat copyright | <https://ec.europa.eu/eurostat/en/help/copyright-notice> | Lectura directa del aviso vigente, incluida reutilización comercial, atribución y excepciones. |
| FRED | <https://fred.stlouisfed.org/docs/api/fred/>; <https://fred.stlouisfed.org/docs/api/api_key.html>; <https://fred.stlouisfed.org/legal/> | Documentación general recuperada por búsqueda; las dos páginas específicas sufrieron timeout de lectura directa. No se verificó operación, cuota ni aceptación de una clave. |
| Analytics | <https://developers.google.com/analytics/devguides/MCP>; <https://developers.google.com/analytics/devguides/reporting/data/v1/quotas> | Reconocimiento oficial del MCP y cuotas de la API, no acceso a una propiedad del usuario. |
| Search Console | <https://developers.google.com/webmaster-tools/v1/how-tos/authorizing>; <https://developers.google.com/webmaster-tools/limits> | OAuth/scopes y cuotas; no se confundió Search Console con Testing Tools API, que tiene requisitos distintos. |
| Trends | <https://developers.google.com/search/apis/trends>; <https://developers.google.com/search/blog/2025/07/trends-api> | Alpha y anuncio de 2025-07-24; escalado consistente sigue siendo interés de búsqueda, no recuentos absolutos. |
| Stripe | <https://docs.stripe.com/mcp>; <https://docs.stripe.com/mcp.md> | HTTP, OAuth/claves, lectura/escritura genérica y confirmación humana en acciones concretas. |
| HubSpot | <https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server>; <https://developers.hubspot.com/docs/apps/developer-platform/build-apps/integrate-with-the-remote-hubspot-mcp-server.md> | Lectura directa actual: conector, PKCE, herramientas de lectura y escritura, restricciones por plan. |
| Shopify Storefront | <https://shopify.dev/docs/apps/build/storefront-mcp/servers/storefront>; <https://shopify.dev/docs/agents/profiles/auth-and-rate-limiting>; <https://shopify.dev/docs/apps/build/storefront-mcp>; <https://shopify.dev/docs/apps/build/storefront-mcp/index> | Documentación recuperada por búsqueda; diferencias entre catálogo, carritos, checkout y autenticación. |
| Shopify Dev | <https://shopify.dev/docs/apps/build/devmcp.md>; <https://shopify.dev/docs/apps/build/ai-toolkit>; <https://shopify.dev/docs/apps/build/ai-toolkit.md> | La ruta antigua de documentación condujo al contenido AI Toolkit; el texto distingue Dev MCP local de gestión autenticada. |
| Tavily precios | <https://docs.tavily.com/documentation/api-credits> | Créditos mensuales y coste por operación; se citan solo cifras realmente publicadas en la lectura. |
| Exa precios | <https://exa.ai/docs/reference/pricing> | Fecha de modificación 2026-09-15; Search, Contents y Agent tienen costes distintos. No aplicar precios de API al acceso anónimo sin documentación. |
| Brave precios | <https://brave.com/search/api/> | Search, créditos mensuales y explicación del requisito de tarjeta; no se aceptaron planes. |
| Context7 | <https://context7.com/docs/overview> | Contexto de documentación técnica y límites/acceso privado con clave. |
| Firecrawl | <https://docs.firecrawl.dev/mcp-server> | Keyless y superficie actual, incluido Parse; la política local es más restrictiva. |

### 9.2. Repositorios, versiones y metadatos

Se leyeron metadatos públicos por HTTPS, sin clonar repositorios, usar autoridad GitHub de la cuenta, extraer credenciales ni ejecutar instaladores.

| Proyecto | Consulta de metadatos y archivos de evidencia |
| --- | --- |
| Playwright MCP | <https://api.github.com/repos/microsoft/playwright-mcp>; <https://raw.githubusercontent.com/microsoft/playwright-mcp/main/package.json>; <https://raw.githubusercontent.com/microsoft/playwright-mcp/main/README.md> |
| Google Analytics MCP | <https://api.github.com/repos/googleanalytics/google-analytics-mcp>; <https://raw.githubusercontent.com/googleanalytics/google-analytics-mcp/main/README.md>; <https://pypi.org/pypi/analytics-mcp/json> |
| Tavily MCP | <https://api.github.com/repos/tavily-ai/tavily-mcp>; <https://raw.githubusercontent.com/tavily-ai/tavily-mcp/main/package.json>; <https://raw.githubusercontent.com/tavily-ai/tavily-mcp/main/README.md> |
| Exa MCP | <https://api.github.com/repos/exa-labs/exa-mcp-server>; <https://raw.githubusercontent.com/exa-labs/exa-mcp-server/main/package.json>; <https://raw.githubusercontent.com/exa-labs/exa-mcp-server/main/README.md> |
| Brave MCP | <https://api.github.com/repos/brave/brave-search-mcp-server>; <https://raw.githubusercontent.com/brave/brave-search-mcp-server/main/package.json>; <https://raw.githubusercontent.com/brave/brave-search-mcp-server/main/README.md> |
| Shopify Dev MCP | <https://registry.npmjs.org/@shopify%2fdev-mcp/latest> — `name`, `version` y `license` declarados; no descarga ni auditoría del tarball. |
| Marketing Skills | <https://api.github.com/repos/coreyhaines31/marketingskills>; <https://api.github.com/repos/coreyhaines31/marketingskills/commits/main>; <https://api.github.com/repos/coreyhaines31/marketingskills/git/trees/5b2c0007766c6a1cf1d53fd8fc73e979e0821022?recursive=1> |
| Anthropic Skills | <https://api.github.com/repos/anthropics/skills>; <https://api.github.com/repos/anthropics/skills/commits/main>; <https://api.github.com/repos/anthropics/skills/git/trees/34040c9c568585f6929bedeaad110ad08f079624?recursive=1>; <https://raw.githubusercontent.com/anthropics/skills/main/README.md> |
| PM Skills | <https://api.github.com/repos/phuryn/pm-skills>; <https://api.github.com/repos/phuryn/pm-skills/commits/main>; <https://api.github.com/repos/phuryn/pm-skills/git/trees/8607e3b077817f89bf4a9b623246219734ac3be0?recursive=1>; <https://github.com/phuryn/pm-skills/blob/main/README.md> |
| OpenAI Skills | <https://api.github.com/repos/openai/skills>; <https://api.github.com/repos/openai/skills/commits/main>; <https://api.github.com/repos/openai/skills/git/trees/49f948faa9258a0c61caceaf225e179651397431?recursive=1>; <https://raw.githubusercontent.com/openai/skills/main/README.md> |
| OpenAI Plugins, lectura acotada | <https://api.github.com/repos/openai/plugins/contents>; <https://api.github.com/repos/openai/plugins/contents/plugins>; <https://raw.githubusercontent.com/openai/plugins/main/README.md>; <https://api.github.com/repos/openai/plugins/contents/plugins/data-analytics>; <https://api.github.com/repos/openai/plugins/contents/plugins/data-analytics/skills> |

Las lecturas de árboles fueron inventarios de rutas/metadatos, no descargas ni activaciones de todos los archivos. Las fechas de `pushed_at` y el commit de `main` pueden diferir; no se interpretaron como fecha de release. Los resúmenes del buscador pueden estar desactualizados frente al archivo primario leído, como ocurrió con la versión indexada de Tavily.

### 9.3. Skills y licencias inspeccionadas selectivamente

| Evidencia | URL exacta |
| --- | --- |
| LICENSE `aitmpl` del commit original | <https://raw.githubusercontent.com/davila7/claude-code-templates/ec126b9ded118ba66c2125fa39eb5b0e87d701bd/LICENSE> |
| Árbol de Corey en commit histórico | <https://api.github.com/repos/coreyhaines31/marketingskills/git/trees/3617bdc883230c2eec6cd77721987f71650902e5?recursive=1> |
| README de Corey en commit histórico | <https://raw.githubusercontent.com/coreyhaines31/marketingskills/3617bdc883230c2eec6cd77721987f71650902e5/README.md> |
| LICENSE de Corey en commit posterior | <https://raw.githubusercontent.com/coreyhaines31/marketingskills/5b2c0007766c6a1cf1d53fd8fc73e979e0821022/LICENSE> |
| Anthropic XLSX, texto indexado y licencia | <https://raw.githubusercontent.com/anthropics/skills/main/skills/xlsx/SKILL.md>; <https://raw.githubusercontent.com/anthropics/skills/main/skills/xlsx/LICENSE.txt>; referencia fijada: <https://github.com/anthropics/skills/blob/34040c9c568585f6929bedeaad110ad08f079624/skills/xlsx/LICENSE.txt> |
| Anthropic `mcp-builder`, licencia individual | <https://raw.githubusercontent.com/anthropics/skills/34040c9c568585f6929bedeaad110ad08f079624/skills/mcp-builder/LICENSE.txt> |
| PM Skills MIT | <https://raw.githubusercontent.com/phuryn/pm-skills/8607e3b077817f89bf4a9b623246219734ac3be0/LICENSE> |
| PM `prioritize-assumptions` | <https://raw.githubusercontent.com/phuryn/pm-skills/8607e3b077817f89bf4a9b623246219734ac3be0/pm-product-discovery/skills/prioritize-assumptions/SKILL.md> |
| PM `cohort-analysis` | <https://raw.githubusercontent.com/phuryn/pm-skills/8607e3b077817f89bf4a9b623246219734ac3be0/pm-data-analytics/skills/cohort-analysis/SKILL.md> |
| OpenAI `jupyter-notebook`, texto y licencia | <https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/jupyter-notebook/SKILL.md>; <https://raw.githubusercontent.com/openai/skills/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/jupyter-notebook/LICENSE.txt> |
| OpenAI Data Analytics, README y raíz selectiva | <https://raw.githubusercontent.com/openai/plugins/main/plugins/data-analytics/README.md>; <https://raw.githubusercontent.com/openai/plugins/main/plugins/data-analytics/skills/analyze-data-quality/SKILL.md> |

## 10. Fallos, rutas obsoletas y límites conservados

| Lectura/resultado | Interpretación y resolución |
| --- | --- |
| <https://fred.stlouisfed.org/docs/api/api_key.html> y <https://fred.stlouisfed.org/legal/>: timeout | No se validaron completamente requisitos/cuotas/condiciones por lectura directa. No se usaron proxies, identidades alternativas ni un MCP de terceros para evitar el problema. |
| <https://raw.githubusercontent.com/coreyhaines31/marketingskills/3617bdc883230c2eec6cd77721987f71650902e5/LICENSE>: 404 | No se atribuyó a inexistencia del repositorio o falta total de licencia: se comprobó el árbol y la declaración MIT en README, manteniendo separado el LICENSE posterior. |
| <https://raw.githubusercontent.com/openai/skills/main/skills/.curated/spreadsheet/SKILL.md> y <https://raw.githubusercontent.com/openai/skills/main/skills/.curated/spreadsheet/LICENSE.txt>: 404 | Se inspeccionó el árbol y el README, se identificó deprecación y sucesor; no se afirmó que un archivo ausente fuese una skill instalable actual. |
| <https://api.github.com/repos/openai/plugins/git/trees/main?recursive=1>: JSON incompleto en el cliente | La lectura estaba limitada a 2.000.000 bytes y truncó el JSON. **No fue prueba de API rota o repositorio inválido.** Se acotó a directorios concretos usando `/contents`; no se descargó el repositorio entero. |
| <https://shopify.dev/docs/api/shopify-cli/dev-mcp.md> y <https://raw.githubusercontent.com/Shopify/dev-mcp/main/README.md>: 404 | Las rutas intentadas no son prueba de inexistencia del servicio. Se encontró documentación oficial actual en AI Toolkit y metadatos npm de `@shopify/dev-mcp`. |
| <https://ec.europa.eu/eurostat/about-us/policies/copyright> y <https://ec.europa.eu/eurostat/web/main/about-us/policies/copyright>: 404 | Se siguió el enlace de copyright de la página API oficial hasta `/eurostat/en/help/copyright-notice`. La navegación a una ruta vigente no se usó para eludir una denegación de acceso. |
| <https://raw.githubusercontent.com/openai/plugins/main/plugins/data-analytics/skills/analyze-data-quality/LICENSE.txt>: 404 | No se confirmó licencia para esa carpeta; no significa automáticamente que todo OpenAI Plugins carezca de licencia ni autoriza aplicar la licencia del antiguo notebook. |
| Rutas antiguas World Bank devolvieron contenido general/navegación | No se trasladaron condiciones genéricas de material web a todos los datos. Se utilizó la página específica de licencias de Data Catalog. |
| Resultados de buscador y `main` no coinciden siempre | Se priorizó la fuente primaria para el dato concreto, sin declarar que la versión de `main` esté publicada. No se inventaron precios, cuotas o fechas faltantes. |

### Qué sigue sin comprobarse

1. Instalación, inicialización, catálogo y operación funcional de cada MCP candidato; tampoco disponibilidad nativa en un nuevo run.
2. Acceso a cuentas, datos, planes o cuotas reales de esta cuenta de Hoplite/GitHub y de proveedores. No se autorizaron ni probaron conexiones privadas.
3. Compatibilidad de SDKs, transportes, OAuth y rutas de skills con la configuración efectiva de Hoplite.
4. Dependencias transitivas, scripts completos, comportamiento en ejecución y seguridad del artefacto publicado de cada candidato.
5. Licencia exacta por dataset/serie y condiciones comerciales aplicables a un uso futuro concreto.
6. Ventaja marginal medida en cobertura, exactitud, coste y latencia frente a las herramientas nativas.
7. Adaptación de `cohort-analysis`, ejecución de los casos sintéticos y revisión del resultado por el agente principal.

**Cierre:** se conserva evidencia documental y una copia íntegra de dos textos públicos para revisión. No se promete «100% funcional», acceso a «todo Internet», actualización segura sin revisión ni resultados económicos. La siguiente acción útil es que el agente principal decida si adapta la raíz de cohortes y ejecute pruebas representativas con datos públicos o sintéticos dentro de la autorización correspondiente.
