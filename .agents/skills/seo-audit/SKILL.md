---
name: seo-audit
description: "Audita SEO técnico, contenido e intención de búsqueda con evidencia por URL y un plan priorizado, sin prometer rankings ni usar herramientas no disponibles."
---

# Auditoría SEO

## Alcance

Acuerda dominio, páginas prioritarias, países/idiomas, objetivo de negocio y acceso disponible. Sin autorización a Search Console, analítica o logs, limita las conclusiones a señales públicas y una muestra explícita de URLs.

## Flujo de trabajo

1. **Recoge el inventario mínimo.** Revisa navegación, `robots.txt`, sitemap, respuestas HTTP, redirecciones, etiquetas canónicas, metadatos y enlaces internos de páginas representativas. Usa navegación y MCP públicos solo si están expuestos; no supongas un crawler, Search Console ni una herramienta de pago.
2. **Evalúa indexabilidad antes que redacción.** Relaciona bloqueos, `noindex`, canonicals, duplicados, errores y arquitectura con evidencia concreta. Una consulta `site:` es una pista, no una medida fiable del índice.
3. **Comprueba intención y contenido.** Para cada URL prioritaria, identifica consulta/intención objetivo, título, encabezados, contenido útil, enlaces y posible canibalización. Evita reglas universales de longitud, densidad de palabra clave o número de H1.
4. **Revisa experiencia y datos estructurados con límites.** Señala problemas visibles de móvil, recursos, estabilidad o marcado solo cuando se puedan observar. Para rendimiento o Core Web Vitals, cita la herramienta y fecha de medición; no lo infieras de una captura.
5. **Prioriza por mecanismo.** Describe el impacto plausible, confianza, esfuerzo, dependencia y prueba de cierre para cada hallazgo. Si `agent_spawn` está disponible, separa carriles técnico, contenido y competencia sin tratar su coincidencia como validación independiente.

## Evidencia requerida

- URL, fecha, método de inspección y extracto/captura para cada hallazgo.
- Alcance de la muestra y qué páginas o datos no se pudieron revisar.
- Fuente primaria para reglas de buscadores o datos de rendimiento relevantes.

## Entregable

Produce una tabla priorizada con hallazgo, URL afectada, evidencia, hipótesis de impacto, confianza, esfuerzo, responsable sugerido y verificación posterior. Separa bloqueos técnicos, mejoras de contenido y experimentos; indica que mejores prácticas no garantizan indexación, tráfico ni ranking.

## Límites

No uses credenciales ajenas, fuerces rastreos intensivos, modifiques etiquetas, envíes sitemaps ni publiques contenido sin autorización. No afirmes una posición, volumen o ganancia de tráfico sin una fuente fechada y apropiada.

## Skills relacionadas

- `deep-web-research`
- `web-search-strategy`
- `analytics-tracking`
- `page-cro`
- `competitor-alternatives`

## Alcance de esta copia portátil

Esta raíz contiene instrucciones autónomas para la sesión actual. Usa únicamente las herramientas y permisos que ya estén disponibles, no instala servicios ni configura MCP, y no autoriza contactos, gastos, cuentas, publicaciones ni acceso a datos privados.

## Atribución y licencia

Esta copia conserva solo la adaptación activa. No incluye material de referencia ni recursos de origen.

### Claude Code Templates / AI Templates — Daniel (San) Ávila

Origen registrado: https://raw.githubusercontent.com/davila7/claude-code-templates/ec126b9ded118ba66c2125fa39eb5b0e87d701bd/cli-tool/components/skills/business-marketing/seo-audit/SKILL.md.

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

Origen registrado: https://raw.githubusercontent.com/coreyhaines31/marketingskills/3617bdc883230c2eec6cd77721987f71650902e5/skills/seo-audit/SKILL.md.

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
