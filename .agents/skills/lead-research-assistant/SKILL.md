---
name: lead-research-assistant
description: "Investiga cuentas empresariales públicas que encajan con una hipótesis comercial, usando señales verificables y sin recopilar datos personales ni realizar contacto."
---

# Investigación de cuentas objetivo

## Objetivo

Construir una lista pequeña y defendible de organizaciones para validar una hipótesis comercial. Esta skill investiga empresas y roles funcionales, no personas, correos, teléfonos, perfiles personales ni enriquecimiento de contactos.

## Flujo de trabajo

1. **Define el ICP y la hipótesis.** Especifica comprador organizacional, industria, tamaño, geografía, trabajo a resolver, alternativa actual, exclusiones y señales públicas de necesidad. Distingue un requisito indispensable de una preferencia.
2. **Busca organizaciones mediante fuentes públicas.** Usa `web_search` para descubrir empresas, anuncios, casos, documentación, vacantes o noticias; usa el navegador para verificar la fuente original y su fecha. Respeta límites de acceso y no automatices scraping.
3. **Registra señales, no suposiciones.** Para cada cuenta, asocia una o más fuentes con señal de ajuste, posible desencadenante, contradicción y calidad de evidencia. Una vacante o una noticia no prueba presupuesto, urgencia ni intención de compra.
4. **Prioriza con una rúbrica visible.** Puntúa ajuste al problema, señal de necesidad, accesibilidad pública y riesgo de equivocación. Muestra pesos, datos ausentes y por qué una cuenta queda fuera; la puntuación guía revisión, no predice cierre.
5. **Prepara la siguiente investigación autorizable.** Recomienda qué verificar después y el rol funcional pertinente, por ejemplo responsable de operaciones o seguridad, sin identificar ni recopilar datos personales. Si `agent_spawn` está disponible, reparte sectores o regiones independientes y reconcilia duplicados y evidencia.

## Evidencia requerida

- URL, organización, fecha y extracto de cada señal pública.
- Definición del ICP, rúbrica, pesos, exclusiones y limitaciones de cobertura.
- Hechos separados de inferencias sobre necesidad, presupuesto o momento de compra.

## Entregable

Entrega una tabla de cuentas con sitio web, industria/tamaño solo si son públicos, señales verificadas, por qué encaja o no, contradicciones, rol funcional sugerido, prioridad explicada y siguiente dato a verificar. Incluye una síntesis de sesgos de búsqueda y cuentas que desconfirman la hipótesis.

## Límites

No recopiles ni infieras información personal, raspees plataformas, crees listas de contacto, envíes outreach, conectes perfiles, importes a un CRM ni publiques datos sin autorización específica. No presentes la lista como demanda comprobada ni como probabilidad de venta.

## Skills relacionadas

- `market-customer-research`
- `competitive-intelligence`
- `web-search-strategy`
- `ai-opportunity-validation`

## Alcance de esta copia portátil

Esta raíz contiene instrucciones autónomas para la sesión actual. Usa únicamente las herramientas y permisos que ya estén disponibles, no instala servicios ni configura MCP, y no autoriza contactos, gastos, cuentas, publicaciones ni acceso a datos privados.

## Atribución y licencia

Esta copia conserva solo la adaptación activa. No incluye material de referencia ni recursos de origen.

### Claude Code Templates / AI Templates — Daniel (San) Ávila

Origen registrado: https://raw.githubusercontent.com/davila7/claude-code-templates/ec126b9ded118ba66c2125fa39eb5b0e87d701bd/cli-tool/components/skills/business-marketing/lead-research-assistant/SKILL.md.

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
