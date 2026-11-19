# Como instalar as skills

**Nível:** iniciante · **Tempo:** 5 minutos

As skills da Pandora Box funcionam no **Claude.ai** (navegador, app desktop e celular), no **Claude Cowork** e no **Claude Code**. Você não precisa saber programar.

> **Situação.** Da família Sync, só a `syncing` está publicada (v0.1, em teste). As demais entram nos links abaixo assim que forem publicadas.

---

## O que é uma skill

Uma skill é um pacote de instruções que ensina o Claude a fazer uma tarefa de um jeito específico. Tecnicamente, é uma pasta com um arquivo `SKILL.md`. Depois de instalada, o Claude a usa quando o assunto pede, ou quando você a chama pelo nome, por exemplo `/sync-docs`.

## Escolha onde você usa o Claude

| Você usa | Siga |
|---|---|
| **Claude.ai** ou **Claude Cowork** | [Opção A: baixar e enviar o arquivo](#opção-a-claudeai-e-claude-cowork) |
| **Claude Code** | [Opção B: instalar com um prompt](#opção-b-claude-code) |

As skills enviadas no Claude.ai ficam na sua conta e valem também no Cowork.

---

## Opção A: Claude.ai e Claude Cowork

**1. Baixe as skills.**

| Skill | Download |
|---|---|
| `syncing` (obrigatória: as outras dependem dela) | [syncing.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/syncing.zip) |
| Família Sync completa (um .zip com o .zip de cada skill) | [sync-todas.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/sync-todas.zip) |

Todos os arquivos estão na página [Skills da Pandora Box](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/tag/skills) e são atualizados automaticamente a cada nova versão.

**2. Ative a execução de código.** Em *Configurações → Capacidades*, ative a execução de código e criação de arquivos. As skills dependem dela.

**3. Envie cada skill.** Ainda em *Configurações → Capacidades*, na área **Skills**, clique em enviar e escolha o `.zip` de cada skill. Se você baixou o `sync-todas.zip`, abra-o antes: o Claude espera **um .zip por skill**.

**4. Teste.** Abra uma nova conversa e escreva, por exemplo: *"Use a skill syncing para me ajudar a amadurecer a ideia de um agente que analisa a frequência dos funcionários."*

Os nomes dos menus podem mudar com o tempo. Se não encontrar, pergunte ao próprio Claude onde ficam as skills nas configurações.

---

## Opção B: Claude Code

Abra o Claude Code em qualquer pasta, copie o prompt abaixo e cole no chat:

```text
Instale para mim as skills da família "sync" do repositório público https://github.com/Pandora-Tech-LTDA/pandora-box (branch main, pasta skills/sync).

Cada subpasta de skills/sync que tem um arquivo SKILL.md é uma skill. Ignore a pasta "references".

Copie cada uma dessas subpastas, inteira, para ~/.claude/skills/<nome-da-subpasta>/. Se alguma já existir, me pergunte antes de substituir.

Apague os arquivos temporários do download. No final, me mostre uma tabela com as skills instaladas e o que cada uma faz, e me diga como começar a usar.
```

O Claude pode pedir permissão para rodar comandos. Leia e aprove. Depois, feche e abra o Claude Code e digite `/` no chat: as skills instaladas aparecem na lista.

---

## Qual skill usar primeiro

```
/sync-docs  →  /sync-mva  →  /syncdb
```

1. **`/sync-docs`** entrevista você sobre o projeto e registra vocabulário e decisões. Comece por aqui.
2. **`/sync-mva`** monta o MVA a partir desse registro: prompt do agente com testes, documentos e manual de montagem.
3. **`/syncdb`** gera dados de exemplo (sintéticos) em CSV ou Markdown.

Para conversar sobre uma ideia sem gerar arquivos, use **`/sync-me`**. Enquanto essas skills não forem publicadas, teste a `syncing` diretamente.

## Problemas comuns

| Problema | O que fazer |
|---|---|
| O Claude não usa a skill | Abra uma nova conversa. Confira se a skill aparece em *Configurações → Capacidades → Skills* (Claude.ai e Cowork) ou em `~/.claude/skills/` (Claude Code). |
| O envio do .zip falha | Envie um .zip por skill, não o `sync-todas.zip` inteiro. Confira se a execução de código está ativada. |
| A skill faz todas as perguntas de uma vez, sem sugestões | Ela não carregou a `syncing`. Instale a `syncing` e peça: "carregue a skill syncing". |
| Quero continuar o projeto em outra conversa | Salve o registro que o `/sync-docs` entregou, ou trabalhe numa pasta de projeto para que ele grave os arquivos em `sync/`. |

## Créditos

As skills `syncing`, `/sync-me` e `/sync-docs` são derivadas das skills [`grilling`](https://www.aihero.dev/skills-grilling), [`grill-me`](https://www.aihero.dev/skills-grill-me) e [`grill-with-docs`](https://www.aihero.dev/skills-grill-with-docs) de **Matt Pocock** ([mattpocock/skills](https://github.com/mattpocock/skills), licença MIT). O `/sync-mva` e o `/syncdb` seguem a metodologia MVA, ©2026 Pandora Tech LTDA.
