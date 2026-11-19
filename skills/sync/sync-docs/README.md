# /sync-docs

**Português** · [English](#english)

**Entender e documentar um projeto. Comece por aqui.**

## O que é

O `/sync-docs` faz a mesma entrevista do `/sync-me`, mas começa pelo processo e pelo problema e **registra durante a conversa** o vocabulário do projeto (glossário) e as decisões, com o motivo de cada uma. Esse registro permite continuar em outra conversa e é a base do `/sync-spec` e do `/sync-mva`. No fim, recomenda qual dos dois seguir.

## Quando usar

- Você vai construir algo e quer partir de um problema bem entendido.
- Quer que as decisões fiquem registradas, com o motivo.
- Vai continuar o projeto em outra conversa ou passar para outra pessoa.

**Quando não usar:** Só quer pensar uma ideia, sem registro: use o `/sync-me`.

## Como usar

Abra o Claude numa pasta de projeto (Cowork ou Claude Code), digite `/sync-docs` (ou `/pandora:sync-docs`) e descreva o projeto. Sem pasta de projeto, o registro fica no chat.

```
/sync-docs quero automatizar a análise de frequência dos funcionários da unidade
```

Instalação: veja [Como instalar as skills](../../../guias/como-instalar-skills.md).

### O que acontece na conversa

1. Avisa onde o registro vai ficar.
2. Pergunta sobre o problema, o processo de hoje, o estado desejado, os documentos e o critério de sucesso.
3. Grava cada termo e cada decisão assim que se resolvem.
4. Fecha com um resumo e recomenda o próximo passo.

### Dicas

- Descreva o processo como ele é de fato, não como deveria ser.
- Se já existir uma pasta `sync/`, ele continua de onde parou.

## Resultados esperados

- `sync/glossario.md`: os termos do projeto e o que significam.
- `sync/decisoes.md`: cada decisão com data, motivo, alternativas descartadas e discordâncias.
- A recomendação do próximo passo: `/sync-spec` ou `/sync-mva`.

## Próximo passo

`/sync-spec` para um produto com telas; `/sync-mva` para uma automação ou um agente.

## Créditos

Derivada da skill `grill-with-docs` de Matt Pocock ([mattpocock/skills](https://github.com/mattpocock/skills), MIT).

---

<a id="english"></a>

# /sync-docs

**English** · [Português](#sync-docs)

**Understand and document a project. Start here.**

## What it is

`/sync-docs` runs the same interview as `/sync-me`, but starts from the process and the problem and **records during the conversation** the project's vocabulary (glossary) and decisions, each with its reason. That record lets you continue in another conversation and is the base for `/sync-spec` and `/sync-mva`. At the end, it recommends which one to follow.

## When to use

- You are going to build something and want to start from a well-understood problem.
- You want decisions recorded, with reasons.
- You will continue in another conversation or hand the project to someone.

**When not to use:** You only want to think an idea through, without a record: use `/sync-me`.

## How to use

Open Claude in a project folder (Cowork or Claude Code), type `/sync-docs` (or `/pandora:sync-docs`) and describe the project. Without a project folder, the record stays in the chat.

```
/sync-docs I want to automate the employee attendance analysis for our unit
```

Installation: see [How to install the skills](../../../guias/como-instalar-skills.md#english).

### What happens in the conversation

1. It tells you where the record will live.
2. It asks about the problem, today's process, the desired state, the documents and the success criteria.
3. It saves each term and decision as soon as they are settled.
4. It closes with a summary and recommends the next step.

### Tips

- Describe the process as it actually is, not as it should be.
- If a `sync/` folder already exists, it picks up where you left off.

## Expected results

- `sync/glossario.md`: the project's terms and what they mean.
- `sync/decisoes.md`: each decision with date, reason, discarded alternatives and disagreements.
- A recommended next step: `/sync-spec` or `/sync-mva`.

## Next step

`/sync-spec` for a product with screens; `/sync-mva` for an automation or agent.

## Credits

Derived from Matt Pocock's `grill-with-docs` skill ([mattpocock/skills](https://github.com/mattpocock/skills), MIT).
