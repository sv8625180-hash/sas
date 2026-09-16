---
name: ab-test-setup
description: "Diseña experimentos A/B con hipótesis, métricas, tamaño muestral y análisis preespecificados, evitando conclusiones estadísticas exageradas."
---

# Diseño de pruebas A/B

## Objetivo

Convertir una decisión de producto, precio, copy o página en una prueba interpretable. Si no hay tráfico, baseline o capacidad de asignación consistente, recomienda investigación cualitativa, un piloto controlado o no experimentar todavía.

## Flujo de trabajo

1. **Formula una hipótesis falsable.** Relaciona observación fechada, cambio concreto, población, mecanismo esperado y métrica primaria; deja clara la variante de control.
2. **Fija medición y protección.** Define unidad de aleatorización, exposición, evento de conversión, denominador, ventanas de atribución, una métrica primaria, pocas secundarias y guardarraíles. Asegura que una persona vea una variante coherente al volver.
3. **Preespecifica el análisis.** Calcula tamaño por variante con baseline, MDE que justificaría el coste, nivel de error, potencia y asignación. Usa Python para conservar fórmula, versión de datos y resultado; no copies tablas de tamaño universal ni declares una duración mínima sin el patrón real de tráfico.
4. **Elige regla de parada.** Para análisis fijo, no detengas por mirar resultados repetidamente. Si necesitas mirar secuencialmente, define el método, umbrales y calendario antes de iniciar. Equilibra días de la semana y ciclos de negocio cuando afecten al comportamiento.
5. **Interpreta con prudencia.** Informa efecto absoluto y relativo, intervalo de incertidumbre, tamaño logrado, calidad de asignación, guardarraíles y significancia práctica. Un valor p no es la probabilidad de que la hipótesis sea cierta ni demuestra permanencia; trata segmentos no preespecificados como exploratorios.

## Evidencia requerida

- Observación que motivó la prueba y captura/descripción de cada variante.
- Definiciones de eventos y confirmación de QA antes de exponer usuarios.
- Supuestos, cálculo reproducible, regla de parada y factores externos registrados.
- Resultados brutos o agregados suficientes para revisar asignación y métricas.

## Entregable

Entrega un plan de experimento con hipótesis, variantes, población, aleatorización, métricas, tamaño/duración calculados, análisis, guardarraíles, riesgos y criterios de decisión. Tras la prueba, clasifica el resultado como apoyar, no apoyar o inconcluso; no como “ganador” sin evidencia suficiente.

## Límites

No actives variantes, modifiques precios, despliegues flags, compres tráfico ni expongas usuarios a una prueba sin autorización y revisión de riesgos. No selecciones segmentos o métricas después para fabricar una conclusión.

## Skills relacionadas

- `analytics-tracking`
- `page-cro`
- `copywriting`

## Alcance de esta copia portátil

Esta raíz contiene instrucciones autónomas para la sesión actual. Usa únicamente las herramientas y permisos que ya estén disponibles, no instala servicios ni configura MCP, y no autoriza contactos, gastos, cuentas, publicaciones ni acceso a datos privados.

## Atribución y licencia

Esta copia conserva solo la adaptación activa. No incluye material de referencia ni recursos de origen.

### Claude Code Templates / AI Templates — Daniel (San) Ávila

Origen registrado: https://raw.githubusercontent.com/davila7/claude-code-templates/ec126b9ded118ba66c2125fa39eb5b0e87d701bd/cli-tool/components/skills/business-marketing/ab-test-setup/SKILL.md.

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

### marketingskills — Corey Haines (atribución complementaria)

Origen registrado: https://raw.githubusercontent.com/coreyhaines31/marketingskills/3617bdc883230c2eec6cd77721987f71650902e5/skills/ab-test-setup/SKILL.md.

Se incluye íntegramente la licencia aplicable a esta adaptación para que la raíz sea autosuficiente.

#### MIT License

MIT License

Copyright (c) 2025 Corey Haines

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
