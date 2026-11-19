# /pandora:sync-mva

**Português** · [English](#english)

**Montar um MVA: a menor automação que testa se a ideia resolve o problema.**

## O que é

O `/pandora:sync-mva` parte do registro do `/pandora:sync-docs`, identifica o que falta para montar o experimento e pergunta só isso, seguindo as etapas de modelagem, hipótese e contexto da metodologia MVA (Minimum Viable Automation). No fim, entrega o pacote para montar o agente.

## Quando usar

- O projeto é uma automação ou um agente que trabalha sobre documentos e dados.
- Você quer testar o valor rápido, antes de investir em um sistema completo.

**Quando não usar:** Se é um produto com telas, use o `/pandora:sync-spec`.

## Como usar

Na mesma pasta do `/pandora:sync-docs`, digite `/pandora:sync-mva`.

```
/pandora:sync-mva
```

Instalação: veja [Como instalar as skills](../../../guias/como-instalar-skills.md).

### O que acontece na conversa

1. Mostra uma tabela do que já está identificado, parcial, ausente ou é hipótese.
2. Pergunta só as lacunas, até chegar a uma hipótese no formato "Se intervirmos em … esperamos …, observável por …".
3. Diz "Já entendi…" e só gera depois do seu aceite.
4. Usa o `/pandora:syncdb` para criar os dados sintéticos de que o agente precisa.

### Dicas

- Sem dados reais? O MVA funciona com dados sintéticos.
- Defina um critério de sucesso que dê para observar.

## Resultados esperados

- A pasta `mva/<nome>/` com `LEIA-ME.md` (problema, hipótese, o que testa e o que não testa).
- `prompt-do-agente.md`, com um autoteste que o agente roda antes de trabalhar.
- `documentos/`, com os dados e textos de referência em CSV ou Markdown.
- `manual-cowork.md`, com o passo a passo para montar o agente no Cowork.

## Próximo passo

Montar o agente seguindo o `manual-cowork.md` e avaliar pelo critério de sucesso. Se o valor se confirmar e virar produto, siga para o `/pandora:sync-spec`.

## Créditos

Segue a metodologia MVA, ©2026 Pandora Tech LTDA.

---

<a id="english"></a>

# /pandora:sync-mva

**English** · [Português](#pandorasync-mva)

**Build an MVA: the smallest automation that tests whether the idea solves the problem.**

## What it is

`/pandora:sync-mva` starts from the `/pandora:sync-docs` record, identifies what is missing to build the experiment and only asks that, following the modeling, hypothesis and context stages of the MVA (Minimum Viable Automation) methodology. At the end, it delivers the package to set up the agent.

## When to use

- The project is an automation or agent that works on documents and data.
- You want to test the value fast, before investing in a full system.

**When not to use:** If it is a product with screens, use `/pandora:sync-spec`.

## How to use

In the same folder as `/pandora:sync-docs`, type `/pandora:sync-mva`.

```
/pandora:sync-mva
```

Installation: see [How to install the skills](../../../guias/como-instalar-skills.md#english).

### What happens in the conversation

1. It shows a table of what is identified, partial, missing or a hypothesis.
2. It asks only the gaps, until it reaches a hypothesis in the form "If we intervene at … we expect …, observable by …".
3. It says "I understand…" and generates only after you agree.
4. It uses `/pandora:syncdb` to create the synthetic data the agent needs.

### Tips

- No real data? The MVA works with synthetic data.
- Define a success criterion you can observe.

## Expected results

- The folder `mva/<name>/` with `LEIA-ME.md` (problem, hypothesis, what it tests and what it doesn't).
- `prompt-do-agente.md`, with a self-test the agent runs before working.
- `documentos/`, with reference data and texts in CSV or Markdown.
- `manual-cowork.md`, with step-by-step setup in Cowork.

## Next step

Set up the agent following `manual-cowork.md` and evaluate it against the success criterion. If the value holds and it becomes a product, move on to `/pandora:sync-spec`.

## Credits

Follows the MVA methodology, ©2026 Pandora Tech LTDA.
