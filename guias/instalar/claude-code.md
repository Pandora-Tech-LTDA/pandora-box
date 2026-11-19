# Instalar no Claude Code

**Português** · [English](#english)

**Para:** Claude Code no terminal, no app desktop ou na extensão de IDE · **Tempo:** 2 minutos

Abra o Claude Code em qualquer pasta, copie o prompt e cole no chat:

```text
Instale para mim as skills da família "sync" do repositório público https://github.com/Pandora-Tech-LTDA/pandora-box (branch main, pasta skills/sync).

Cada subpasta de skills/sync que tem um arquivo SKILL.md é uma skill. Ignore a pasta "references".

Copie cada uma dessas subpastas, inteira, para ~/.claude/skills/<nome-da-subpasta>/. Se alguma já existir, me pergunte antes de substituir.

Apague os arquivos temporários do download. No final, me mostre uma tabela com as skills instaladas e o que cada uma faz, e me diga como começar a usar.
```

O Claude pode pedir permissão para rodar comandos. Leia e aprove. Depois, reinicie o Claude Code e digite `/`: as skills instaladas aparecem na lista.

**Só para um projeto:** troque `~/.claude/skills/` por `.claude/skills/` no prompt, com o Claude Code aberto na pasta do projeto.

[Voltar para todas as plataformas](../como-instalar-skills.md)

---

<a id="english"></a>

# Install on Claude Code

**English** · [Português](#instalar-no-claude-code)

**For:** Claude Code in the terminal, desktop app or IDE extension · **Time:** 2 minutes

Open Claude Code in any folder, copy the prompt and paste it into the chat:

```text
Install the "sync" skill family from the public repository https://github.com/Pandora-Tech-LTDA/pandora-box (branch main, folder skills/sync).

Each subfolder of skills/sync that contains a SKILL.md file is a skill. Ignore the "references" folder.

Copy each of these subfolders, in full, to ~/.claude/skills/<subfolder-name>/. If any already exists, ask me before replacing it.

Delete the temporary download files. At the end, show me a table of the installed skills and what each one does, and tell me how to get started.
```

Claude may ask for permission to run commands. Read and approve them. Then restart Claude Code and type `/`: installed skills show up in the list.

**For a single project:** replace `~/.claude/skills/` with `.claude/skills/` in the prompt, with Claude Code open in the project folder.

[Back to all platforms](../como-instalar-skills.md#english)
