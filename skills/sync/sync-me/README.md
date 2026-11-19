# /sync-me

**Português** · [English](#english)

**Amadurecer uma ideia antes de decidir o que construir.**

## O que é

O `/sync-me` entrevista você sobre uma ideia, um plano ou um projeto até vocês chegarem a um entendimento compartilhado. Começa pela sua visão, devolve essa visão em um parágrafo e pergunta só o que sustenta essa visão. O que é reversível ou de baixo impacto ele assume e avisa. Não grava arquivos. Também é o método de entrevista que as outras skills da família usam.

## Quando usar

- Você tem uma ideia ainda solta e quer pensar melhor antes de agir.
- Quer testar um plano ou uma decisão com alguém que pergunte e discorde.
- Não quer gerar documentos, só clareza.

**Quando não usar:** Se o projeto vai seguir adiante e você quer registrar as decisões, use o `/sync-docs`.

## Como usar

Digite `/sync-me` (ou `/pandora:sync-me`, se instalou pelo plugin) e descreva a ideia em poucas linhas.

```
/sync-me quero criar um agente que avise a gestora quando alguém da equipe acumula atrasos
```

Instalação: veja [Como instalar as skills](../../../guias/como-instalar-skills.md).

### O que acontece na conversa

1. A IA pede a sua visão e a devolve em um parágrafo.
2. Mostra os temas e quantas decisões faltam.
3. Pergunta em rodadas numeradas, cada pergunta com uma sugestão e o que ela custa. Você responde pelo número.
4. Lista o que assumiu ("Assumi: …") para você corrigir, e guarda os riscos para oferecer depois.
5. Quando a visão está clara, oferece fechar.

### Dicas

- Discorde quando não concordar. "Não sei" também é uma resposta válida.
- Prefere uma pergunta por vez? É só pedir.
- Quer pensar sem influência? Peça para esconder as sugestões.

## Resultados esperados

- Um resumo no chat com a visão, as decisões (com o motivo), o que foi assumido, onde você discordou, as perguntas em aberto, os riscos e o que só um protótipo responde.
- Nenhum arquivo gravado.

## Próximo passo

Se o projeto vai seguir, rode o `/sync-docs` para registrar o glossário e as decisões.

## Créditos

Derivada das skills `grilling` e `grill-me` de Matt Pocock ([mattpocock/skills](https://github.com/mattpocock/skills), MIT).

---

<a id="english"></a>

# /sync-me

**English** · [Português](#sync-me)

**Develop an idea before deciding what to build.**

## What it is

`/sync-me` interviews you about an idea, plan or project until you share the same understanding. It starts from your vision, plays it back in one paragraph and only asks what holds that vision up. Anything reversible or low-impact it assumes and tells you. It creates no files. It is also the interview method the other skills in the family use.

## When to use

- You have a loose idea and want to think it through before acting.
- You want to test a plan or decision with someone who asks and pushes back.
- You want clarity, not documents.

**When not to use:** If the project will move forward and you want to record decisions, use `/sync-docs`.

## How to use

Type `/sync-me` (or `/pandora:sync-me` if installed through the plugin) and describe the idea in a few lines.

```
/sync-me I want an agent that alerts the manager when someone on the team keeps arriving late
```

Installation: see [How to install the skills](../../../guias/como-instalar-skills.md#english).

### What happens in the conversation

1. The AI asks for your vision and plays it back in one paragraph.
2. It shows the topics and how many decisions are left.
3. It asks in numbered rounds, each question with a suggestion and its cost. You answer by number.
4. It lists what it assumed ("Assumed: …") for you to correct, and keeps risks to offer later.
5. When the vision is clear, it offers to wrap up.

### Tips

- Disagree when you don't agree. "I don't know" is a valid answer.
- Prefer one question at a time? Just ask.
- Want to think without influence? Ask it to hide suggestions.

## Expected results

- A summary in the chat with the vision, decisions (with reasons), assumptions, disagreements, open questions, risks and what only a prototype can answer.
- No files created.

## Next step

If the project moves forward, run `/sync-docs` to record the glossary and decisions.

## Credits

Derived from Matt Pocock's `grilling` and `grill-me` skills ([mattpocock/skills](https://github.com/mattpocock/skills), MIT).
