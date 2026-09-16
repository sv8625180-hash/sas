---
name: analytics-tracking
description: "Diseña o revisa un plan de analítica orientado a decisiones, con eventos verificables, minimización de datos y pruebas de calidad."
---

# Plan de analítica y medición

## Objetivo

Medir acciones que cambian una decisión de producto o comercial, no coleccionar eventos por defecto. Identifica la decisión, el embudo, los propietarios del dato, la herramienta ya autorizada y los requisitos de privacidad antes de proponer instrumentación.

## Flujo de trabajo

1. **Parte de preguntas accionables.** Define una métrica de resultado y, solo cuando ayuden a interpretarla, métricas de diagnóstico y guardarraíles. Especifica población, denominador, ventana y exclusiones.
2. **Modela eventos mínimos.** Para cada evento, fija nombre estable, definición, disparador, propiedades permitidas, valores esperados, identificador pseudónimo si procede, dueño y decisión asociada. Mantén contexto en propiedades, no en nombres infinitos de evento.
3. **Minimiza datos.** Excluye nombres, correos, teléfonos, texto libre, identificadores sensibles y datos innecesarios. Documenta consentimiento, retención, borrado y transferencias que el responsable legal debe validar.
4. **Diseña la implementación, no la ejecutes.** Adapta el plan al stack y plataforma que el usuario ya tiene autorizados. Usa el navegador y un entorno de prueba para verificar disparos, duplicados y propiedades; Python puede comprobar muestras exportadas si se proporcionan de forma autorizada.
5. **Cierra el circuito de calidad.** Comprueba esquema, hora, consistencia entre clientes, deduplicación y conversión aguas abajo. Versiona el plan y registra cambios que rompan comparabilidad histórica.

## Evidencia requerida

- Pregunta de decisión, definición de métrica y fuente de verdad por evento.
- Esquema de propiedades con tipo, ejemplo permitido y justificación.
- Resultado de pruebas en entorno permitido, incluidos eventos ausentes o duplicados.
- Limitaciones de consentimiento, cobertura y calidad del dato.

## Entregable

Entrega una matriz de tracking, diccionario de métricas, mapa de embudo, requisitos de privacidad, lista de implementación y protocolo de QA. Distingue hechos medidos, datos que faltan y métricas que no deberían usarse para inferir causalidad.

## Límites

No crees cuentas, publiques etiquetas o píxeles, importes audiencias, eludas consentimiento ni envíes datos personales a terceros sin autorización. Una instrumentación propuesta no prueba que una campaña o producto funcione.

## Skills relacionadas

- `ab-test-setup`
- `seo-audit`
- `page-cro`
- `ai-opportunity-validation`

## Alcance de esta copia portátil

Esta raíz contiene instrucciones autónomas para la sesión actual. Usa únicamente las herramientas y permisos que ya estén disponibles, no instala servicios ni configura MCP, y no autoriza contactos, gastos, cuentas, publicaciones ni acceso a datos privados.

## Atribución y licencia

Esta copia conserva solo la adaptación activa. No incluye material de referencia ni recursos de origen.

### Claude Code Templates / AI Templates — Daniel (San) Ávila

Origen registrado: https://raw.githubusercontent.com/davila7/claude-code-templates/ec126b9ded118ba66c2125fa39eb5b0e87d701bd/cli-tool/components/skills/business-marketing/analytics-tracking/SKILL.md.

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

Origen registrado: https://raw.githubusercontent.com/coreyhaines31/marketingskills/3617bdc883230c2eec6cd77721987f71650902e5/skills/analytics-tracking/SKILL.md.

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
