# /sync-spec

**Português** · [English](#english)

**A spec para uma IA de código construir o seu sistema com segurança.**

## O que é

O `/sync-spec` transforma o registro do `/sync-docs` na **spec** de um produto ou sistema com telas: propósito, estado de pronto, usuários e acesso, segurança e dados, telas e fluxos, arquitetura, padrão visual e um plano de etapas. Foi pensado para quem não é desenvolvedor experiente e vai entregar a spec a um modelo: conduz a conversa em blocos, explica por que cada tema importa e, se você cansar, aplica um padrão seguro.

## Quando usar

- O projeto é um produto ou sistema com telas e pessoas usando.
- Você vai pedir a uma IA de código (Claude Code, Codex ou outra) para construir.
- Quer começar com login, permissões, dados e organização do código bem resolvidos.

**Quando não usar:** Se é uma automação ou um agente sem telas, use o `/sync-mva`. Se o problema ainda não está claro, rode o `/sync-docs` antes.

## Como usar

Na mesma pasta do `/sync-docs`, digite `/sync-spec` (ou `/pandora:sync-spec`). Ele lê `sync/glossario.md` e `sync/decisoes.md` e pergunta só o que falta.

```
/sync-spec
```

Instalação: veja [Como instalar as skills](../../../guias/como-instalar-skills.md).

### O que acontece na conversa

1. Bloco 1, propósito, visão e estado de pronto: vem do registro; você confirma o que significa "pronto" e o que fica fora.
2. Bloco 2, produto, usuários e acesso: papéis, login, 2FA e dados sensíveis.
3. Bloco 3, telas e fluxos: o caminho do usuário, com wireframes em texto das telas principais.
4. Bloco 4, arquitetura e repositório: a IA sugere a tecnologia, os módulos e a organização das pastas.
5. Bloco 5, plano de etapas: a ordem de construção, cada etapa verificável.
6. Antes de gerar, confere conflitos; gera só com o seu aceite.

### Dicas

- Em qualquer bloco, diga "usa o padrão" para aplicar o padrão seguro e seguir.
- Tem design system próprio? Diga a qualquer momento, até depois da spec pronta, e ele troca o Pandora DS pelo seu.
- A spec não decide onde publicar; isso fica para depois.

## Resultados esperados

- `sync/spec.md`, pronta para uma IA de código: como usar a spec, propósito, estado de pronto, fora do escopo, usuários e permissões, segurança e dados, módulos e requisitos com critério de aceite, fluxos e telas, padrão visual, arquitetura, plano de etapas, glossário, decisões e pendências.
- Opcional: `sync/tela-referencia.html`, uma tela de referência visual.
- Para usar: abra o projeto numa IA de código e peça "Leia sync/spec.md e siga o plano de etapas, começando pela etapa 1".

## Próximo passo

Entregar a spec a uma IA de código e construir etapa por etapa.

## Créditos

Ideias de `to-spec` (Matt Pocock, MIT), `wireframes` (ba-toolkit, MIT) e `aidlc-requirements` (AWS, MIT-0); detalhes em [`FONTES.md`](FONTES.md). Padrão visual: [Pandora DS](../../../design-system/).

---

<a id="english"></a>

# /sync-spec

**English** · [Português](#sync-spec)

**The spec a coding AI needs to build your system safely.**

## What it is

`/sync-spec` turns the `/sync-docs` record into the **spec** for a product or system with screens: purpose, done state, users and access, security and data, screens and flows, architecture, visual standard and a step-by-step plan. It is made for people who are not experienced developers and will hand the spec to a model: it walks through topics, explains why each one matters and, if you get tired, applies a safe default.

## When to use

- The project is a product or system with screens and people using it.
- You will ask a coding AI (Claude Code, Codex or another) to build it.
- You want login, permissions, data and code organization sorted out from the start.

**When not to use:** If it is an automation or agent without screens, use `/sync-mva`. If the problem is not clear yet, run `/sync-docs` first.

## How to use

In the same folder as `/sync-docs`, type `/sync-spec` (or `/pandora:sync-spec`). It reads `sync/glossario.md` and `sync/decisoes.md` and only asks what is missing.

```
/sync-spec
```

Installation: see [How to install the skills](../../../guias/como-instalar-skills.md#english).

### What happens in the conversation

1. Topic 1, purpose, vision and done state: taken from the record; you confirm what "done" means and what is out of scope.
2. Topic 2, product, users and access: roles, login, 2FA and sensitive data.
3. Topic 3, screens and flows: the user's path, with text wireframes of the main screens.
4. Topic 4, architecture and repository: the AI suggests the technology, modules and folder layout.
5. Topic 5, step plan: the build order, each step verifiable.
6. Before generating, it checks for conflicts; it generates only after you agree.

### Tips

- In any topic, say "use the default" to apply the safe default and move on.
- Have your own design system? Say so at any point, even after the spec is done, and it replaces Pandora DS with yours.
- The spec doesn't decide where to deploy; that comes later.

## Expected results

- `sync/spec.md`, ready for a coding AI: how to use the spec, purpose, done state, out of scope, users and permissions, security and data, modules and requirements with acceptance criteria, flows and screens, visual standard, architecture, step plan, glossary, decisions and open items.
- Optional: `sync/tela-referencia.html`, one visual reference screen.
- To use it: open the project in a coding AI and ask "Read sync/spec.md and follow the step plan, starting with step 1".

## Next step

Hand the spec to a coding AI and build step by step.

## Credits

Ideas from `to-spec` (Matt Pocock, MIT), `wireframes` (ba-toolkit, MIT) and `aidlc-requirements` (AWS, MIT-0); details in [`FONTES.md`](FONTES.md). Visual standard: [Pandora DS](../../../design-system/).
