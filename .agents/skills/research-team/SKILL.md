---
name: research-team
description: Coordinar agentes nativos de Hoplite para investigar demanda, competidores, viabilidad y riesgos en paralelo, con tareas acotadas y una síntesis verificable.
---

# Equipo de investigación

Este es un procedimiento para `agent_spawn`, no una instalación de nuevos modelos ni procesos permanentes. Para una pregunta pequeña trabaja sin delegación.

1. Carga `deep-web-research` y, si hay una decisión comercial, `ai-opportunity-validation`. Define pregunta, restricciones y entregable en un brief compartido sin secretos.
2. Divide únicamente tareas independientes. Usa de dos a cuatro agentes como máximo en la primera ronda, con un presupuesto explícito de fuentes y consultas. El coste de ejecución en Hoplite sigue aplicando.
3. Si `agent_spawn` está disponible, usa estos perfiles de prompt autocontenidos con un tipo admitido como `docs`, `explore`, `general` o `review`. Son guías de trabajo, no agentes registrados ni permisos adicionales:
   - **Demanda y comprador (`explore`):** investiga hasta ocho fuentes públicas sobre problemas repetidos, soluciones compradas, presupuestos y barreras; entrega URLs, fechas, sesgos y evidencia que refute la necesidad.
   - **Competencia y precios (`docs`):** compara de tres a cinco competidores y sustitutos, incluido trabajo manual; verifica ofertas, precios, condiciones, límites y segmento, sin inventar cifras no públicas.
   - **Viabilidad y costes (`general`):** revisa capacidades técnicas, límites de proveedores y costes completos mediante documentación actual y ejemplos públicos; separa medidas de supuestos y no llama APIs de pago ni instala servicios sin autorización.
   - **Revisión crítica (`review`):** busca selección favorable, ingresos sin gastos, falta de distribución, licencias y riesgos de privacidad; prioriza objeciones, hechos invalidantes y preguntas pendientes.
   No inventes valores de `agent`, herramientas o modelos, ni pases un modelo si no hace falta elegirlo explícitamente.
4. Exige URL, fecha, fragmento o dato pertinente, categoría de evidencia, contradicciones y limitaciones. No compartas datos privados con un servicio de investigación. Todos los agentes trabajan en solo lectura salvo autorización de implementación.
5. Tras iniciar agentes, continúa la investigación independiente. Usa `agent_wait` al necesitar sus resultados, no un bucle de sondeo. Evita que dos agentes editen el mismo archivo.
6. Revisa las fuentes que sostienen decisiones importantes. Dos agentes que citan el mismo comunicado no son corroboración independiente. Resuelve discrepancias y separa hechos de recomendaciones.
7. Cierra con una síntesis, hipótesis invalidantes y el siguiente experimento autorizado. No continúes creando agentes, hilos o servicios indefinidamente.

Conserva brief, ledger y hallazgos en una ubicación autorizada para el proyecto actual. Los perfiles y skills no otorgan permiso para contactos, campañas, cargos, cuentas nuevas ni publicaciones.

## Alcance de esta copia portátil

Esta raíz contiene instrucciones autónomas para la sesión actual. Usa únicamente las herramientas y permisos que ya estén disponibles, no instala servicios ni configura MCP, y no autoriza contactos, gastos, cuentas, publicaciones ni acceso a datos privados.
