<img src="../../assets/banner-sync.png" alt="Sync. A IA pergunta. Você decide. Uma família de skills que entrevista você sobre o seu projeto até haver entendimento compartilhado e, no fim, entrega o material para montar o seu MVA." width="100%">

# Sync

**Skills para o Claude que entrevistam você sobre o seu projeto antes de qualquer linha ser escrita.**

A maioria dos projetos com IA começa pela ferramenta e descobre o problema no meio do caminho. O Sync inverte a ordem: primeiro vêm as perguntas, depois a construção.

> **Situação.** A `syncing`, o método de entrevista, está na versão 0.1, em teste. As demais skills estão em construção.

---

## Como funciona

**A IA pergunta em rodadas.** O projeto é tratado como uma árvore de decisões. Em cada rodada, a IA faz todas as perguntas que já podem ser respondidas e espera as suas respostas antes de seguir. Cada resposta libera as perguntas seguintes.

**Cada sugestão mostra o que custa.** A IA recomenda um caminho e diz o que se perde com ele. Assim você tem um motivo concreto para concordar ou discordar. Se preferir pensar sem influência, peça para esconder as sugestões.

**As decisões são suas.** Um "sim" sem motivo não fecha uma decisão. Se você aceitar tudo em uma rodada, a próxima começa com um desafio. Discordar é parte do método.

**Os fatos são da IA.** O que dá para descobrir nos seus arquivos ou documentos, a IA pesquisa sozinha e mostra onde encontrou.

**Nada é construído sem confirmação.** A sessão termina com um resumo do entendimento compartilhado. Só depois do seu aceite a IA passa para a próxima etapa.

---

## As skills

| Skill | Para quê | Entrega | Situação |
|---|---|---|---|
| `/sync-docs` | Entender e documentar um projeto. **Comece por aqui.** | `sync/glossario.md` e `sync/decisoes.md` no seu projeto, ou um registro no chat | Em construção |
| `/sync-mva` | Montar um MVA a partir do registro do `/sync-docs` | Prompt do agente com testes automatizados, documentos de referência e manual de montagem no Cowork | Em construção |
| `/syncdb` | Criar dados de exemplo sem expor dados reais | Bases sintéticas em CSV ou Markdown, a partir de um arquivo de exemplo | Em construção |
| `/sync-me` | Amadurecer uma ideia solta, sem gerar arquivos | Resumo com decisões, discordâncias e perguntas em aberto | Em construção |
| [`syncing`](syncing/) | O método de entrevista usado pelas outras skills | Não é chamada diretamente | v0.1, em teste |

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

Escolha a sua plataforma em [Como instalar as skills](../../guias/como-instalar-skills.md). Para o Claude.ai e o Cowork, o download direto é [syncing.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/syncing.zip).

---

## Créditos e licenças

- `syncing`, `/sync-me` e `/sync-docs` são derivadas das skills [`grilling`](https://www.aihero.dev/skills-grilling), [`grill-me`](https://www.aihero.dev/skills-grill-me) e [`grill-with-docs`](https://www.aihero.dev/skills-grill-with-docs) de **Matt Pocock** ([mattpocock/skills](https://github.com/mattpocock/skills), licença MIT; cópia em [`references/mattpocock-skills/LICENSE`](references/mattpocock-skills/LICENSE)).
- `/sync-mva` e `/syncdb` seguem a metodologia MVA, ©2026 Pandora Tech LTDA ([`references/mva/FONTE.md`](references/mva/FONTE.md)).

## Para quem mantém o projeto

- [`DECISOES.md`](DECISOES.md): decisões de produto e de método.
- [`references/`](references/): material de origem.
