---
name: pricing-strategy
description: "Investiga y propone precios, métricas de valor y empaquetado para una oferta digital o con IA, distinguiendo evidencia de supuestos y sin prometer ingresos."
---

# Estrategia de precios

## Objetivo

Convertir una hipótesis de precio en opciones comprobables, no adivinar el precio “correcto”. Aclara primero comprador, caso de uso, alternativa actual, región, moneda, canal de venta y objetivo (aprendizaje, adopción, margen o recuperación de costes).

## Flujo de trabajo

1. **Separa hechos y supuestos.** Registra precio actual, volumen, costes variables —incluidos modelos, revisión humana, soporte, pagos e impuestos cuando correspondan— y datos que aún faltan.
2. **Verifica alternativas.** Usa `web_search` para descubrir precios y el navegador para confirmar página, unidad, condiciones, fecha de consulta y costes adicionales. Una página de precios no prueba ventas ni disposición a pagar.
3. **Diseña la métrica.** Relaciona asiento, uso, proyecto, transacción u otro límite con el valor que recibe el comprador. Descarta métricas que penalicen el uso valioso, sean difíciles de entender o incentiven abuso.
4. **Propón empaquetados comparables.** Presenta dos o tres opciones de oferta, límite, soporte, coste de entrega y segmento; no presupongas que tres niveles, freemium o un descuento anual sirven siempre.
5. **Planifica investigación de disposición a pagar.** Formula preguntas neutrales sobre comportamiento pasado y alternativas. Van Westendorp, Gabor-Granger o conjoint pueden orientar si la muestra, el reclutamiento y el análisis son adecuados; no conviertas una muestra pequeña o sesgada en una cifra concluyente. Usa Python para dejar cálculos y escenarios reproducibles si hay datos.
6. **Define una validación ética.** Especifica cohorte, precio/oferta, métrica principal, guardarraíles y horizonte. Evita precios diferentes no comunicados a clientes comparables; una prueba de precio requiere revisión legal, comercial y autorización antes de ejecutarse.

## Evidencia requerida

- URLs y fecha de verificación para cada precio, unidad y condición competitiva.
- Fuente o rango explícito para costes, uso y valor; marca las estimaciones.
- Método, población y limitaciones de cualquier encuesta, entrevista o dato histórico.
- Escenarios bajo/base/alto con las ecuaciones y supuestos visibles, no una previsión única de ingresos.

## Entregable

Produce una tarjeta de precios con: comprador y trabajo resuelto; alternativa actual; métrica candidata; tabla de paquetes; costes y margen por escenario; incertidumbres; experimento mínimo; criterio de parada; y hechos que podrían refutar la recomendación.

## Límites

No afirmes que un aumento, descuento o métrica elevará conversión, MRR o beneficio sin resultados medidos. No contactes personas, lances encuestas, cambies precios, cobres, crees cuentas ni publiques una oferta sin autorización explícita.

## Skills relacionadas

- `ai-opportunity-validation`
- `competitor-alternatives`
- `analytics-tracking`
- `ab-test-setup`
- `page-cro`

## Alcance de esta copia portátil

Esta raíz contiene instrucciones autónomas para la sesión actual. Usa únicamente las herramientas y permisos que ya estén disponibles, no instala servicios ni configura MCP, y no autoriza contactos, gastos, cuentas, publicaciones ni acceso a datos privados.

## Atribución y licencia

Esta copia conserva solo la adaptación activa. No incluye material de referencia ni recursos de origen.

### Claude Code Templates / AI Templates — Daniel (San) Ávila

Origen registrado: https://raw.githubusercontent.com/davila7/claude-code-templates/ec126b9ded118ba66c2125fa39eb5b0e87d701bd/cli-tool/components/skills/business-marketing/pricing-strategy/SKILL.md.

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

Origen registrado: https://raw.githubusercontent.com/coreyhaines31/marketingskills/3617bdc883230c2eec6cd77721987f71650902e5/skills/pricing-strategy/SKILL.md.

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
