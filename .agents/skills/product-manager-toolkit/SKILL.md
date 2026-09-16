---
name: product-manager-toolkit
description: "Estructura descubrimiento, priorización, PRDs y métricas de producto con supuestos explícitos, evidencia de clientes y decisiones revisables."
---

# Toolkit de producto

## Objetivo

Convertir una oportunidad en una decisión de producto trazable: qué problema se abordará, para quién, qué no se hará, cómo se comprobará y qué información podría cambiar la prioridad.

## Flujo de trabajo

1. **Formula el problema.** Identifica segmento, trabajo, desencadenante, comportamiento actual, daño del statu quo y resultado deseado. Separa solicitudes de solución de evidencia de problema.
2. **Sintetiza evidencia.** Agrupa investigación existente, datos de uso autorizados, soporte y fuentes públicas; conserva cita, fecha, muestra y contradicción. No describas entrevistas, pilotos o ventas como realizados si solo están propuestos.
3. **Genera opciones y límites.** Plantea alternativas de solución, no solo una función. Define alcance, fuera de alcance, dependencias, riesgos y la versión mínima que puede enseñar algo útil.
4. **Prioriza de forma auditable.** RICE puede ordenar hipótesis mediante `alcance × impacto × confianza / esfuerzo`, pero sus entradas no son hechos objetivos. Documenta rangos, fuente, incertidumbre y sensibilidad; usa Python para mostrar cálculos, no scripts inexistentes ni una puntuación que suplante juicio.
5. **Escribe y mide.** Produce un brief o PRD con decisión, usuarios, criterios de aceptación, fallos previsibles, métrica de resultado, guardarraíles y plan de aprendizaje. Vuelve a priorizar cuando cambie la evidencia.

## Evidencia requerida

- Problema, segmento y fuente de cada señal relevante.
- Supuestos cuantificados y método de priorización reproducible.
- Restricciones técnicas, operativas, legales y de soporte conocidas.
- Definición de éxito, línea base si existe y cuándo se revisará la decisión.

## Entregable

Entrega un memo de decisión o PRD breve: contexto, evidencia, oportunidades, opciones, recomendación condicionada, RICE/matriz con entradas trazables, alcance, criterios de aceptación, métricas, riesgos, preguntas abiertas y siguiente experimento autorizado.

## Límites

No inventes hallazgos de clientes, comprometas roadmap, abras tickets, contactes participantes ni despliegues una función sin autorización. No confundas una métrica de vanidad o una correlación con impacto causal.

## Skills relacionadas

- `ai-opportunity-validation`
- `market-customer-research`
- `analytics-tracking`
- `ab-test-setup`

## Alcance de esta copia portátil

Esta raíz contiene instrucciones autónomas para la sesión actual. Usa únicamente las herramientas y permisos que ya estén disponibles, no instala servicios ni configura MCP, y no autoriza contactos, gastos, cuentas, publicaciones ni acceso a datos privados.

## Atribución y licencia

Esta copia conserva solo la adaptación activa. No incluye material de referencia ni recursos de origen.

### Claude Code Templates / AI Templates — Daniel (San) Ávila

Origen registrado: https://raw.githubusercontent.com/davila7/claude-code-templates/ec126b9ded118ba66c2125fa39eb5b0e87d701bd/cli-tool/components/skills/business-marketing/product-manager-toolkit/SKILL.md.

Se incluye íntegramente la licencia aplicable a esta adaptación para que la raíz sea autosuficiente.

#### MIT License

MIT License

Copyright (c) 2025 Daniel (San) Ávila

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
