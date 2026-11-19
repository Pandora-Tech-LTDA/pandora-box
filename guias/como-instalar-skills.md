# Como instalar as skills

As skills da Pandora Box seguem o formato aberto [Agent Skills](https://agentskills.io): cada skill é uma pasta com um arquivo `SKILL.md`. Por isso funcionam no Claude e em outros agentes compatíveis.

Escolha onde você usa a IA e siga o guia da plataforma.

| Plataforma | Como instala | Guia | Situação |
|---|---|---|---|
| **Claude.ai** (navegador, desktop e celular) | Envio de um .zip por skill | [Claude.ai](instalar/claude-ai.md) | Testado |
| **Claude Cowork** | Envio de um .zip por skill | [Claude Cowork](instalar/claude-cowork.md) | Testado |
| **Claude Code** | Prompt pronto | [Claude Code](instalar/claude-code.md) | Testado |
| **OpenAI Codex** (CLI, extensão de IDE e app do ChatGPT) | Prompt pronto | [Codex](instalar/codex.md) | Compatível, não testado |
| **VS Code com GitHub Copilot** | Prompt pronto, por projeto | [VS Code e Copilot](instalar/vscode-copilot.md) | Compatível, não testado |
| **Outros agentes** compatíveis com Agent Skills | Pasta `.agents/skills` | [Outros agentes](instalar/outros-agentes.md) | Compatível, não testado |

"Compatível, não testado" quer dizer que a plataforma lê o mesmo formato de skill, mas a Pandora ainda não validou o comportamento das skills nela. Se testar, conte o resultado numa [issue](../../../issues/new/choose).

## Downloads

Todos os arquivos .zip ficam em [Skills da Pandora Box](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/tag/skills) e são atualizados automaticamente a cada nova versão.

| Skill | Download |
|---|---|
| `syncing` (obrigatória: as outras skills Sync dependem dela) | [syncing.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/syncing.zip) |
| Família Sync completa (um .zip com o .zip de cada skill) | [sync-todas.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/sync-todas.zip) |

> **Situação.** Da família Sync, só a `syncing` está publicada (v0.1, em teste). As demais entram nos downloads assim que forem publicadas.

## Depois de instalar

```
/sync-docs  →  /sync-mva  →  /syncdb
```

Comece pelo `/sync-docs`, que entrevista você sobre o projeto e registra vocabulário e decisões. Veja a página do [Sync](../skills/sync/) para entender o fluxo completo.

## Problemas comuns

| Problema | O que fazer |
|---|---|
| A IA não usa a skill | Abra uma nova conversa ou reinicie o aplicativo. Confira se a skill aparece na lista de skills da plataforma. |
| O envio do .zip falha | Envie um .zip por skill, não o `sync-todas.zip` inteiro. No Claude.ai e no Cowork, confira se a execução de código está ativada. |
| A skill faz todas as perguntas de uma vez, sem sugestões | Ela não carregou a `syncing`. Instale a `syncing` e peça: "carregue a skill syncing". |
| Quero continuar o projeto em outra conversa | Salve o registro que o `/sync-docs` entregou, ou trabalhe numa pasta de projeto para que ele grave os arquivos em `sync/`. |
