# Instalar no Claude Code

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
