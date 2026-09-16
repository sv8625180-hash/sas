---
name: cohort-analysis
description: Analiza cohortes y retención con denominadores explícitos, períodos comparables y datos públicos o sintéticos; distingue falta de observación, abandono y evidencia insuficiente.
---

# Análisis verificable de cohortes

Usa esta skill al evaluar retención, repetición de compra o adopción de una función. No demuestra por sí sola causalidad, rentabilidad ni demanda para un negocio nuevo.

## Procedimiento

1. Define la cohorte, el evento de entrada, la actividad que cuenta como retención, la zona horaria y la edad de cada período. No mezcles edad de cohorte con mes de calendario.
2. Revisa duplicados, identificadores, elegibilidad, tamaños y valores ausentes. Usa datos públicos o sintéticos; los datos de clientes necesitan autorización específica y no se envían a servicios externos.
3. Calcula `retenidos / elegibles` para cada cohorte y edad. Un denominador cero no produce una tasa cero: el resultado no está definido. Un período todavía no observado no es abandono.
4. Al agregar cohortes de la misma edad, divide la suma de retenidos por la suma de elegibles observados. No promedies porcentajes sin ponderación ni incluyas cohortes que aún no alcanzan esa edad.
5. Conserva numeradores, denominadores, exclusiones y períodos censurados junto a tablas o gráficos. Diferencia retención de usuarios, retención de ingresos y adopción; no deduzcas LTV sin margen, cohortes y supuestos de supervivencia.
6. Reporta patrones solo si los datos los sostienen. Una muestra pequeña o pocas cohortes no garantiza resultados significativos. No impongas una cuota de hallazgos ni atribuyas causalidad a una correlación temporal.
7. Propón el dato o experimento que discriminaría entre explicaciones. Entrevistas, campañas, sesiones de usuarios y contacto comercial requieren autorización; esta skill no la concede.

## Prueba sintética de aceptación

- Cohorte A: 8 retenidos de 10 → 80%.
- Cohorte B: 1 retenido de 5 → 20%.
- Agregado comparable: 9 de 15 → **60%, no 50%**.
- Período futuro: `null`, excluido del agregado, no 0%.
- Denominador cero: tasa no definida. Duplicados o retenidos superiores a elegibles: error.

En este proyecto, `python3 scripts/business_math.py` reproduce estos casos y escenarios económicos sin dependencias externas. En una importación personal esta raíz sigue siendo autónoma: la presencia de ese script no se presupone en otros proyectos.

## Entregable

Definiciones; tabla de cohortes con conteos y tasas; controles de calidad; incertidumbre; posibles explicaciones alternativas; siguiente prueba autorizada. Separa toda simulación de resultados comerciales observados.

## Procedencia y licencia

Adaptación revisada de **Cohort Analysis & Retention Explorer**, Pawel Huryn / PM Skills.
Fuente inmutable: https://github.com/phuryn/pm-skills/blob/8607e3b077817f89bf4a9b623246219734ac3be0/pm-data-analytics/skills/cohort-analysis/SKILL.md.
Licencia contrastada en el mismo commit: https://github.com/phuryn/pm-skills/blob/8607e3b077817f89bf4a9b623246219734ac3be0/LICENSE.
Revisión: 2026-09-16. Se conserva el objetivo analítico y se eliminan la exigencia de hallar patrones significativos y las suposiciones de acceso a datos privados.

MIT License

Copyright (c) 2026 Pawel Huryn

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
