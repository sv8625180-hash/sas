---
name: web-search-strategy
description: Design diverse current web queries, search operators, source targets and iterative gap-filling for internet investigations. Use when initial results are narrow, repetitive or insufficient.
---

# Web search strategy

1. Classify the question: fact, product comparison, technical capability, customer demand, historical trend or sentiment.
2. Write 3–5 genuinely different query angles, then narrow by buyer, workflow, geography and date. Use exact phrases or `site:` where supported.
3. Prefer official documentation for product behavior/prices and independent demand-side evidence for commercial claims. Include failure, cancellation, complaint and alternative queries.
4. Use native `web_search`. Its current schema, not the source agent's Claude-specific arguments, determines which filters are available. Do not invent `allowed_domains` or `blocked_domains` parameters.
5. Lee las páginas importantes con el navegador o un lector público disponible en la sesión. Registra el texto real de las afirmaciones numéricas; un resumen de búsqueda no es verificación.
6. After each round, list unresolved questions, repeated sources and missing viewpoints. Spend the next round on gaps rather than more of the same.
7. Stop at the research contract's limit or sufficient decision-relevant coverage. Report query coverage and unverified claims honestly.

Use `deep-web-research` for the full orchestration and evidence ledger. Search failure does not prove absence. Source-specific examples involving older years, other models or tools are illustrations, not instructions for the current session.

## Alcance de esta copia portátil

Esta raíz contiene instrucciones autónomas para la sesión actual. Usa únicamente las herramientas y permisos que ya estén disponibles, no instala servicios ni configura MCP, y no autoriza contactos, gastos, cuentas, publicaciones ni acceso a datos privados.

## Atribución y licencia

Esta copia conserva solo la adaptación activa. No incluye material de referencia ni recursos de origen.

### Claude Code Templates / AI Templates — Daniel (San) Ávila

Origen registrado: https://github.com/davila7/claude-code-templates/blob/028931d584e7c1c8aa9700ba24e9ca885e8eabe0/cli-tool/components/agents/ai-specialists/search-specialist.md.

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
