# Investigación: herramientas útiles y negocios que merece la pena validar

**Corte: 16 de septiembre de 2026.** Esta investigación reduce incertidumbre; no demuestra ingresos propios, rentabilidad futura ni que se haya revisado todo Internet.

## Decisión provisional

La mejor primera apuesta **a investigar**, no a financiar todavía, es un servicio especializado para un comprador accesible con un problema recurrente y medible. Vender un resultado pequeño, supervisado y comprobable antes de construir una plataforma. Más MCP no resuelven por sí solos la falta de clientes, especialización o distribución.

| Si cuentas con… | Hipótesis a priorizar | Condición indispensable |
| --- | --- | --- |
| Capacidad técnica y acceso a un sector | Automatización B2B de un flujo concreto | Ahorro/valor comprobable mayor que costes y cuota; excepciones bajo control. |
| Relaciones locales y capacidad de atención | Operaciones de agenda y seguimiento de consultas solicitadas | Demanda entrante real y capacidad del negocio para atender trabajos rentables. |
| Competencia en datos y acceso a tiendas con ventas | Analítica/CRO orientada a margen | Datos fiables, volumen suficiente y permiso del titular; conversión no equivale a beneficio. |
| Ventaja de compra, reparación o ejecución presencial | Servicio local o reventa especializada | Margen después de tiempo, transporte, devoluciones, inventario e impuestos. |

MicroSaaS puede tener escalabilidad, pero primero necesita un problema repetido y un canal viable. Contenido/afiliación y leads no son ingresos pasivos: dependen de adquisición, plataformas, reputación y consentimiento. No se recomienda especulación financiera, spam ni promesas de resultados.

## Evidencia y contraevidencia

- El [INE](https://www.ine.es/dyngs/Prensa/ETICCE20241T2025.htm), publicado el 22-10-2025, informa para empresas españolas de ≥10 empleados de **44,3% con cloud de pago y 21,1% con IA** en el primer trimestre de 2025. Es adopción/gasto tecnológico, no prueba de que comprarán una nueva oferta de automatización.
- La actividad de marketplaces, comercio electrónico y servicios verticales muestra mercados existentes, pero también competencia y presión comercial. El [informe de oportunidades](oportunidades.md) conserva datos favorables y desfavorables, sus geografías y los casos en que solo se pudo leer evidencia indexada.
- El contexto macro de Banco Mundial/Eurostat ayuda a estudiar un mercado, **no identifica automáticamente clientes ni disposición a pagar**.
- No hubo entrevistas, ventas, pilotos pagados ni campañas del usuario durante esta tarea. La evidencia decisiva de un microsegmento sigue pendiente.

## Economía comprobable, no ingresos prometidos

En la simulación base, **5 clientes × USD 750 = USD 3.750 facturados**, pero el resultado operativo modelado es **USD 1.062,50 antes de impuestos**, después de valorar 80 horas de trabajo a USD 25/h y los demás supuestos. El escenario adverso pierde USD 1.281. Son entradas hipotéticas, no precios validados ni una previsión.

`python3 scripts/business_math.py` reproduce los escenarios y la sensibilidad del [informe completo](oportunidades.md). La nueva skill de cohortes añade una comprobación relevante para negocios recurrentes: 8/10 y 1/5 retenidos producen **60% ponderado**, no 50%; un período sin observar no es churn.

## Herramientas: qué cambia

Se integran los 4 MCP del paquete original y las 26 skills originales; se añade una única skill de cohortes tras revisar licencia y metodología. **No se instala otro MCP redundante.** Las APIs públicas de Banco Mundial y Eurostat ya funcionan mediante Fetch. Analytics, Search Console, Stripe o HubSpot solo aportarían valor con cuentas/datos propios y permisos explícitos; algunos permiten escrituras o transacciones.

La [matriz de 15 líneas](herramientas-evaluadas.md) distingue MCP oficial, API oficial, wrapper comunitario, acceso experimental, costes, licencias por carpeta y versiones declaradas frente a publicadas. No se importaron bundles propietarios ni conectores de clientes/pagos.

## Siguiente experimento, 7–14 días

Antes de elegir vertical, registrar país, habilidad demostrable, horas semanales, capital máximo arriesgable y acceso autorizado a compradores. Después seleccionar **un solo segmento y un solo proceso**, definir el resultado y un límite de entrega, estimar costes y diseñar un piloto manual.

Preparar preguntas y criterios de éxito/abandono no exige gastar ni contactar. La ejecución de entrevistas, contacto comercial, cobros, anuncios o cuentas nuevas requiere autorización específica; no se realizó aquí. El [plan completo](oportunidades.md) incluye umbrales falsables y condiciones para parar, no una promesa de conseguir clientes.

## Cobertura

Dos líneas independientes: 12 búsquedas temáticas sobre demanda/negocios y 10 sobre herramientas, con lecturas primarias seleccionadas. El agente principal añadió revisión de documentación de Hoplite/GitHub y uso real de los cuatro MCP y APIs públicas. Los informes registran consultas, URLs, fecha, extractos, sesgos y fallos de acceso. Esto es una revisión amplia y acotada, no exhaustiva.
