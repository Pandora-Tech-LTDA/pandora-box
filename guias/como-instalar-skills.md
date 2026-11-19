# Como instalar as skills

**Português** · [English](#english)

As skills da Pandora Box seguem o formato aberto [Agent Skills](https://agentskills.io): cada skill é uma pasta com um arquivo `SKILL.md`. Por isso funcionam no Claude e em outros agentes compatíveis.

| Plataforma | Guia | Situação |
|---|---|---|
| **Claude.ai (navegador, desktop e celular)** | [Claude.ai](instalar/claude-ai.md) | Suportado |
| **Claude Cowork** | [Claude Cowork](instalar/claude-cowork.md) | Suportado |
| **Claude Code** | [Claude Code](instalar/claude-code.md) | Suportado |
| **OpenAI Codex (CLI, extensão de IDE e app do ChatGPT)** | [OpenAI Codex](instalar/codex.md) | Compatível, não testado |
| **VS Code com GitHub Copilot** | [VS Code com GitHub Copilot](instalar/vscode-copilot.md) | Compatível, não testado |
| **Outros agentes compatíveis com Agent Skills** | [Outros agentes](instalar/outros-agentes.md) | Compatível, não testado |

"Compatível, não testado" quer dizer que a plataforma lê o mesmo formato de skill, mas a Pandora ainda não validou o comportamento das skills nela. Se testar, conte o resultado numa [issue](https://github.com/Pandora-Tech-LTDA/pandora-box/issues/new/choose).

## Downloads

Todos os arquivos ficam em [Skills da Pandora Box](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/tag/skills) e são atualizados automaticamente a cada nova versão.

| Arquivo | Para quê |
|---|---|
| [pandora.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/pandora.zip) | **Plugin com todas as skills.** Um arquivo só, para Claude.ai, Cowork e Claude Code |
| [sync-me.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/sync-me.zip) · [sync-docs.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/sync-docs.zip) · [sync-mva.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/sync-mva.zip) · [syncdb.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/syncdb.zip) | Skills avulsas, para instalar só uma ou usar em outros agentes |

> **Situação.** As quatro skills da família Sync estão publicadas na versão 0.1, em teste.

## Depois de instalar

```
/sync-docs  →  /sync-mva  →  /syncdb
```

Comece pelo `/sync-docs`, que entrevista você sobre o projeto e registra vocabulário e decisões. Instaladas pelo plugin, as skills aparecem como `/pandora:sync-docs` e assim por diante. Veja a página do [Sync](../skills/sync/) para entender o fluxo completo.

## Problemas comuns

| Problema | O que fazer |
|---|---|
| A IA não usa a skill | Abra uma nova conversa ou reinicie o aplicativo. Confira se a skill aparece na lista de skills da plataforma. |
| O envio falha | O `pandora.zip` vai em *Personalizar → Plugins*; os .zip avulsos vão em *Personalizar → Skills*. Confira se a execução de código está ativada. |
| A skill faz todas as perguntas de uma vez, sem sugestões | Ela não carregou o `sync-me`. Instale o plugin completo e peça: "carregue a skill sync-me". |
| Quero continuar o projeto em outra conversa | Salve o registro que o `/sync-docs` entregou, ou trabalhe numa pasta de projeto para que ele grave os arquivos em `sync/`. |

---

<a id="english"></a>

# How to install the skills

**English** · [Português](#como-instalar-as-skills)

Pandora Box skills follow the open [Agent Skills](https://agentskills.io) format: each skill is a folder with a `SKILL.md` file. That is why they work in Claude and other compatible agents.

| Platform | Guide | Status |
|---|---|---|
| **Claude.ai (web, desktop and mobile)** | [Claude.ai](instalar/claude-ai.md#english) | Supported |
| **Claude Cowork** | [Claude Cowork](instalar/claude-cowork.md#english) | Supported |
| **Claude Code** | [Claude Code](instalar/claude-code.md#english) | Supported |
| **OpenAI Codex (CLI, IDE extension and ChatGPT app)** | [OpenAI Codex](instalar/codex.md#english) | Compatible, not tested |
| **VS Code with GitHub Copilot** | [VS Code com GitHub Copilot](instalar/vscode-copilot.md#english) | Compatible, not tested |
| **Other Agent Skills–compatible agents** | [Outros agentes](instalar/outros-agentes.md#english) | Compatible, not tested |

"Compatible, not tested" means the platform reads the same skill format, but Pandora has not validated the skills' behavior there yet. If you test it, tell us in an [issue](https://github.com/Pandora-Tech-LTDA/pandora-box/issues/new/choose).

## Downloads

All files are on [Pandora Box Skills](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/tag/skills) and are updated automatically with every new version.

| File | Purpose |
|---|---|
| [pandora.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/pandora.zip) | **Plugin with every skill.** A single file for Claude.ai, Cowork and Claude Code |
| [sync-me.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/sync-me.zip) · [sync-docs.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/sync-docs.zip) · [sync-mva.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/sync-mva.zip) · [syncdb.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/syncdb.zip) | Individual skills, to install just one or use with other agents |

> **Status.** All four Sync skills are published at version 0.1, in testing.

## After installing

```
/sync-docs  →  /sync-mva  →  /syncdb
```

Start with `/sync-docs`, which interviews you about the project and records its vocabulary and decisions. Installed through the plugin, the skills show up as `/pandora:sync-docs` and so on. See the [Sync](../skills/sync/README.md#english) page for the full flow.

## Troubleshooting

| Problem | What to do |
|---|---|
| The AI doesn't use the skill | Start a new conversation or restart the app. Check that the skill shows up in the platform's skill list. |
| The upload fails | `pandora.zip` goes in *Customize → Plugins*; individual .zip files go in *Customize → Skills*. Check that code execution is on. |
| The skill asks everything at once, without suggestions | It didn't load `sync-me`. Install the full plugin and say: "load the sync-me skill". |
| I want to continue the project in another conversation | Save the record `/sync-docs` gave you, or work in a project folder so it saves the files to `sync/`. |
