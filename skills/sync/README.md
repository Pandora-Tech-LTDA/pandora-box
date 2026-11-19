<img src="../../assets/banner-sync.png" alt="Sync. A IA pergunta. Você decide. Uma família de skills que entrevista você sobre o seu projeto até haver entendimento compartilhado e, no fim, entrega o material para montar o seu MVA." width="100%">

# Sync

**Português** · [English](#english)

**Skills para o Claude que entrevistam você sobre o seu projeto antes de qualquer linha ser escrita.**

A maioria dos projetos com IA começa pela ferramenta e descobre o problema no meio do caminho. O Sync inverte a ordem: primeiro vêm as perguntas, depois a construção.

> **Situação.** As quatro skills estão publicadas na versão 0.1, em teste.

---

## Como funciona

**A IA começa pela sua visão.** A primeira pergunta é como você imagina o projeto funcionando. A IA devolve essa visão em um parágrafo e mostra quantas decisões faltam para ela ficar de pé.

**A IA pergunta em rodadas, e só o que importa.** O projeto é tratado como uma árvore de decisões. Em cada rodada, a IA faz todas as perguntas que já podem ser respondidas e espera as suas respostas antes de seguir. Cada resposta libera as perguntas seguintes. O que é reversível ou de baixo impacto a IA assume e lista como "assumi", para você corrigir se quiser.

**Cada sugestão mostra o que custa.** A IA recomenda um caminho e diz o que se perde com ele. Assim você tem um motivo concreto para concordar ou discordar. Se preferir pensar sem influência, peça para esconder as sugestões.

**As decisões são suas.** Nas decisões que sustentam a visão, um "sim" sem motivo não basta. Discordar é parte do método. Os riscos ficam anotados, e a IA oferece analisá-los quando fizer sentido.

**Os fatos são da IA.** O que dá para descobrir nos seus arquivos ou documentos, a IA pesquisa sozinha e mostra onde encontrou.

**Nada é construído sem confirmação.** Quando a visão está clara, a IA oferece fechar, mesmo com pontos em aberto, e termina com um resumo do entendimento compartilhado. Só depois do seu aceite a IA passa para a próxima etapa.

---

## As skills

| Skill | Para quê | Entrega | Situação |
|---|---|---|---|
| [`/sync-docs`](sync-docs/) | Entender e documentar um projeto. **Comece por aqui.** | `sync/glossario.md` e `sync/decisoes.md` no seu projeto, ou um registro no chat | v0.1, em teste |
| [`/sync-mva`](sync-mva/) | Montar um MVA a partir do registro do `/sync-docs` | Prompt do agente com testes automatizados, documentos de referência e manual de montagem no Cowork | v0.1, em teste |
| [`/syncdb`](syncdb/) | Criar dados de exemplo sem expor dados reais | Bases sintéticas em CSV ou Markdown, a partir de um arquivo de exemplo | v0.1, em teste |
| [`/sync-me`](sync-me/) | Amadurecer uma ideia ou projeto, sem gerar arquivos. É também o método de entrevista usado pelas outras skills. | Resumo com decisões, discordâncias e perguntas em aberto | v0.1, em teste |

### O fluxo recomendado

```
/sync-docs  →  /sync-mva  →  /syncdb
```

1. **`/sync-docs`** entrevista você sobre o processo que quer resolver e registra o vocabulário e as decisões.
2. **`/sync-mva`** parte desse registro, completa só o que falta e entrega o material para montar o MVA.
3. **`/syncdb`** gera os dados sintéticos de que o MVA precisa para ser testado com segurança.

**Exemplo.** Você quer um agente que analise a frequência dos funcionários. O `/sync-docs` esclarece qual é a dor, quem usa a análise e quais regras de ponto valem. O `/sync-mva` define que o agente precisa de uma planilha de frequência e da política de ponto, e escreve o prompt com casos de teste. O `/syncdb` cria uma planilha de frequência fictícia, com os mesmos campos da real.

---

## Instalação

Funciona no Claude.ai, no Claude Cowork e no Claude Code, e é compatível com o OpenAI Codex, o VS Code com GitHub Copilot e outros agentes que leem o formato Agent Skills.

Escolha a sua plataforma em [Como instalar as skills](../../guias/como-instalar-skills.md). No Claude.ai, no Cowork e no Claude Code, as quatro skills vêm juntas no plugin **pandora**, num arquivo só: [pandora.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/pandora.zip). Instaladas assim, elas aparecem como `/pandora:sync-docs` e assim por diante.

---

## Créditos e licenças

- `/sync-me` e `/sync-docs` são derivadas das skills [`grilling`](https://www.aihero.dev/skills-grilling), [`grill-me`](https://www.aihero.dev/skills-grill-me) e [`grill-with-docs`](https://www.aihero.dev/skills-grill-with-docs) de **Matt Pocock** ([mattpocock/skills](https://github.com/mattpocock/skills), licença MIT; cópia em [`references/mattpocock-skills/LICENSE`](references/mattpocock-skills/LICENSE)).
- `/sync-mva` e `/syncdb` seguem a metodologia MVA, ©2026 Pandora Tech LTDA ([`references/mva/FONTE.md`](references/mva/FONTE.md)).

## Para quem mantém o projeto

- [`DECISOES.md`](DECISOES.md): decisões de produto e de método.
- [`references/`](references/): material de origem.

---
---

<a id="english"></a>

<img src="../../assets/banner-sync-en.png" alt="Sync. The AI asks. You decide. A family of skills that interviews you about your project until you share the same understanding, then delivers what you need to build your MVA." width="100%">

# Sync

**English** · [Português](#sync)

**Skills that interview you about your project before a single line is written.**

Most AI projects start with the tool and discover the problem halfway through. Sync reverses the order: questions first, building second.

> **Status.** All four skills are published at version 0.1, in testing.

## How it works

**The AI starts from your vision.** The first question is how you picture the project working. The AI plays that vision back in one paragraph and shows how many decisions are left to make it stand.

**The AI asks in rounds, and only what matters.** The project is treated as a decision tree. In each round, the AI asks every question that can already be answered and waits for your answers before moving on. Each answer unlocks the next questions. Anything reversible or low-impact the AI assumes and lists as "assumed", for you to correct if you want.

**Every suggestion shows its cost.** The AI recommends a path and says what you give up with it, so you have a concrete reason to agree or disagree. If you prefer to think without influence, ask it to hide the suggestions.

**Decisions are yours.** On decisions that hold up the vision, a "yes" without a reason is not enough. Disagreeing is part of the method. Risks are noted, and the AI offers to go through them when it makes sense.

**Facts are the AI's job.** Whatever can be found in your files or documents, the AI looks up on its own and shows you where it found it.

**Nothing gets built without confirmation.** Once the vision is clear, the AI offers to wrap up, even with open points, and ends with a summary of the shared understanding. Only after you agree does the AI move to the next step.

## The skills

| Skill | Purpose | Output | Status |
|---|---|---|---|
| [`/sync-docs`](sync-docs/) | Understand and document a project. **Start here.** | `sync/glossario.md` and `sync/decisoes.md` in your project, or a record in the chat | v0.1, testing |
| [`/sync-mva`](sync-mva/) | Build an MVA (Minimum Viable Automation) from the `/sync-docs` record | Agent prompt with automated tests, reference documents and a Cowork setup manual | v0.1, testing |
| [`/syncdb`](syncdb/) | Create sample data without exposing real data | Synthetic datasets in CSV or Markdown, from a sample file | v0.1, testing |
| [`/sync-me`](sync-me/) | Develop an idea or project, without creating files. It is also the interview method the other skills use. | Summary of decisions, disagreements and open questions | v0.1, testing |

### Recommended flow

```
/sync-docs  →  /sync-mva  →  /syncdb
```

1. **`/sync-docs`** interviews you about the process you want to solve and records its vocabulary and decisions.
2. **`/sync-mva`** starts from that record, fills only the gaps and delivers what you need to build the MVA.
3. **`/syncdb`** generates the synthetic data the MVA needs to be tested safely.

**Example.** You want an agent that analyzes employee attendance. `/sync-docs` clarifies the pain point, who uses the analysis and which timekeeping rules apply. `/sync-mva` determines that the agent needs an attendance spreadsheet and the timekeeping policy, and writes the prompt with test cases. `/syncdb` creates a fictional attendance spreadsheet with the same fields as the real one.

## Installation

Works on Claude.ai, Claude Cowork and Claude Code, and is compatible with OpenAI Codex, VS Code with GitHub Copilot and other agents that read the Agent Skills format.

Pick your platform in [How to install the skills](../../guias/como-instalar-skills.md#english). On Claude.ai, Cowork and Claude Code, the four skills come together in the **pandora** plugin, in a single file: [pandora.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/pandora.zip). Installed this way, they show up as `/pandora:sync-docs` and so on.

## Credits and licenses

- `/sync-me` and `/sync-docs` are derived from the [`grilling`](https://www.aihero.dev/skills-grilling), [`grill-me`](https://www.aihero.dev/skills-grill-me) and [`grill-with-docs`](https://www.aihero.dev/skills-grill-with-docs) skills by **Matt Pocock** ([mattpocock/skills](https://github.com/mattpocock/skills), MIT license; copy in [`references/mattpocock-skills/LICENSE`](references/mattpocock-skills/LICENSE)).
- `/sync-mva` and `/syncdb` follow the MVA methodology, ©2026 Pandora Tech LTDA ([`references/mva/FONTE.md`](references/mva/FONTE.md)).

The skills themselves are written in Brazilian Portuguese and work in any language the conversation uses.

