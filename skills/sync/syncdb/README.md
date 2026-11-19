# /syncdb

**Português** · [English](#english)

**Dados de teste realistas, sem expor dados reais.**

## O que é

O `/syncdb` cria bases de dados **sintéticas**: fictícias, mas com a mesma estrutura, os mesmos formatos e o mesmo comportamento dos dados reais. Lê um arquivo de exemplo (planilha Excel, CSV, JSON, tabela em PDF) ou uma descrição, e nunca copia valores reais.

## Quando usar

- Você precisa testar um agente, uma automação ou um sistema sem usar dados de pessoas ou da empresa.
- Quer dados com casos difíceis (faltas, duplicados, campos vazios) para ver se a solução aguenta.
- O `/sync-mva` precisa dos documentos de referência de um MVA (ele chama o `/syncdb` sozinho).

**Quando não usar:** Para análise de dados reais, não é esta skill.

## Como usar

Digite `/syncdb` (ou `/pandora:syncdb`) e anexe um arquivo de exemplo, ou descreva os dados.

```
/syncdb gere uma planilha de frequência de 40 funcionários para outubro, com uns 5% de atrasos (anexo a planilha real como exemplo)
```

Instalação: veja [Como instalar as skills](../../../guias/como-instalar-skills.md).

### O que acontece na conversa

1. Mostra a estrutura que entendeu (tabelas, colunas, tipos, formatos) e confirma com você.
2. Combina volume, período, casos difíceis e proporções, numa rodada só.
3. Gera os dados por código, com relações coerentes entre as tabelas.

### Dicas

- Se o arquivo de exemplo tiver dados pessoais, ele avisa e garante que nada deles vai para a saída.
- A semente usada fica registrada, para gerar de novo os mesmos dados.

## Resultados esperados

- Os dados em **CSV** (ou **Markdown**, para textos como políticas). Nunca Excel, Word ou PDF.
- Um dicionário de dados por base: colunas, tipos, formatos, relações e os casos difíceis incluídos.

## Próximo passo

Usar os dados para testar o seu MVA ou sistema. Antes de usar dados reais, verifique as regras de privacidade (LGPD) da organização.

## Créditos

Segue o protocolo de contexto sintético da metodologia MVA, ©2026 Pandora Tech LTDA.

---

<a id="english"></a>

# /syncdb

**English** · [Português](#syncdb)

**Realistic test data without exposing real data.**

## What it is

`/syncdb` creates **synthetic** datasets: fictional, but with the same structure, formats and behavior as real data. It reads a sample file (Excel sheet, CSV, JSON, a table in a PDF) or a description, and never copies real values.

## When to use

- You need to test an agent, automation or system without using personal or company data.
- You want data with hard cases (absences, duplicates, empty fields) to see if the solution holds.
- `/sync-mva` needs an MVA's reference documents (it calls `/syncdb` on its own).

**When not to use:** For analyzing real data, this is not the skill.

## How to use

Type `/syncdb` (or `/pandora:syncdb`) and attach a sample file, or describe the data.

```
/syncdb generate an attendance sheet for 40 employees in October, with about 5% late arrivals (I'm attaching the real sheet as a sample)
```

Installation: see [How to install the skills](../../../guias/como-instalar-skills.md#english).

### What happens in the conversation

1. It shows the structure it understood (tables, columns, types, formats) and confirms with you.
2. It agrees on volume, period, hard cases and proportions, in a single round.
3. It generates the data with code, with consistent relationships between tables.

### Tips

- If the sample file has personal data, it warns you and makes sure none of it reaches the output.
- The seed is recorded, so the same data can be generated again.

## Expected results

- The data in **CSV** (or **Markdown**, for texts like policies). Never Excel, Word or PDF.
- A data dictionary per dataset: columns, types, formats, relationships and the hard cases included.

## Next step

Use the data to test your MVA or system. Before using real data, check your organization's privacy rules.

## Credits

Follows the synthetic context protocol of the MVA methodology, ©2026 Pandora Tech LTDA.
