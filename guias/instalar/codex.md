# Instalar no OpenAI Codex

**Português** · [English](#english)

**Para:** Codex CLI, extensão de IDE e app desktop do ChatGPT · **Tempo:** 2 minutos · **Situação:** compatível, não testado

O Codex lê skills no formato Agent Skills. Segundo a [documentação do Codex](https://developers.openai.com/codex/skills), as skills do usuário ficam em `~/.agents/skills/` e as de um projeto em `.agents/skills/` na raiz do repositório. Abra o Codex, copie o prompt e cole no chat:

```text
Instale para mim as skills da família "sync" do repositório público https://github.com/Pandora-Tech-LTDA/pandora-box (branch main, pasta skills/sync).

Cada subpasta de skills/sync que tem um arquivo SKILL.md é uma skill. Ignore a pasta "references".

Copie cada uma dessas subpastas, inteira, para ~/.agents/skills/<nome-da-subpasta>/. Se alguma já existir, me pergunte antes de substituir.

Apague os arquivos temporários do download. No final, me mostre uma tabela com as skills instaladas e o que cada uma faz, e me diga como começar a usar.
```

O Codex detecta skills novas sozinho. Se alguma não aparecer, reinicie.

**Atenção:** as skills foram escritas para o Claude. No Codex, o comportamento pode variar, principalmente quando uma skill chama outra (o `/sync-docs` e o `/sync-mva` usam o `sync-me`).

Se testar e encontrar diferenças, conte numa [issue](https://github.com/Pandora-Tech-LTDA/pandora-box/issues/new/choose).

[Voltar para todas as plataformas](../como-instalar-skills.md)

---

<a id="english"></a>

# Install on OpenAI Codex

**English** · [Português](#instalar-no-openai-codex)

**For:** Codex CLI, IDE extension and ChatGPT desktop app · **Time:** 2 minutes · **Status:** compatible, not tested

Codex reads skills in the Agent Skills format. According to the [Codex documentation](https://developers.openai.com/codex/skills), user skills live in `~/.agents/skills/` and project skills in `.agents/skills/` at the repository root. Open Codex, copy the prompt and paste it into the chat:

```text
Install the "sync" skill family from the public repository https://github.com/Pandora-Tech-LTDA/pandora-box (branch main, folder skills/sync).

Each subfolder of skills/sync that contains a SKILL.md file is a skill. Ignore the "references" folder.

Copy each of these subfolders, in full, to ~/.agents/skills/<subfolder-name>/. If any already exists, ask me before replacing it.

Delete the temporary download files. At the end, show me a table of the installed skills and what each one does, and tell me how to get started.
```

Codex picks up new skills automatically. If one doesn't show up, restart it.

**Note:** these skills were written for Claude. In Codex, behavior may differ, especially when one skill calls another (`/sync-docs` and `/sync-mva` use `sync-me`).

If you test it and find differences, tell us in an [issue](https://github.com/Pandora-Tech-LTDA/pandora-box/issues/new/choose).

[Back to all platforms](../como-instalar-skills.md#english)
