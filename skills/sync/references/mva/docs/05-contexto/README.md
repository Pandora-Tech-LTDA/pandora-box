# 05 — Contexto e protocolo de dados para experimentos

**Objetivo:** preparar uma representação mínima suficiente do contexto para testar a hipótese sem depender, no primeiro ciclo, da infraestrutura produtiva.

## Princípio operacional

No MVA, o construtor deve conseguir focar na **lógica da automação e no resultado esperado**, e não nos conectores.

Quando a automação futura depender de dados corporativos, APIs, bancos ou integrações ainda indisponíveis, o experimento pode trabalhar com **contexto sintético** ou representações intermediárias.

Essa representação não precisa reproduzir exatamente o payload futuro. Ela precisa ser **plausível e suficiente para testar a hipótese**.

Exemplos:
- um CSV sintético de pessoas e cargos;
- um Excel existente usado como referência para uma futura API;
- um JSON com campos inferidos a partir do processo;
- documentos Markdown representando políticas ou procedimentos;
- amostras sintéticas inspiradas na estrutura conhecida dos dados reais.

A ausência de uma API ou conector **não impede o MVA**. Ela adia o teste de integração.

## Protocolo de baixo risco

Sempre que possível, os primeiros ciclos devem evitar dados pessoais, confidenciais ou produtivos. O contexto sintético permite testar comportamento, lógica e valor antes de introduzir dependências de compliance, LGPD e infraestrutura.

O contexto sintético não elimina a necessidade de validações posteriores com infraestrutura e dados reais. Ele desacopla o **aprendizado inicial** dessas dependências.

## Critério de passagem

Existe contexto suficiente quando o experimento consegue executar um caso representativo e produzir evidência sobre a hipótese, mesmo que formatos, conectores e schemas definitivos ainda não existam.
