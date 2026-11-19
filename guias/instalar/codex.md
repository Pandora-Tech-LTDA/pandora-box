# Instalar no OpenAI Codex

**Para:** Codex CLI, extensão de IDE e app desktop do ChatGPT · **Tempo:** 2 minutos · **Situação:** compatível, não testado

O Codex lê skills no formato aberto Agent Skills. Segundo a [documentação do Codex](https://developers.openai.com/codex/skills), as skills do usuário ficam em `~/.agents/skills/` e as de um projeto em `.agents/skills/` na raiz do repositório.

Abra o Codex, copie o prompt e cole no chat:

```text
Instale para mim as skills da família "sync" do repositório público https://github.com/Pandora-Tech-LTDA/pandora-box (branch main, pasta skills/sync).

Cada subpasta de skills/sync que tem um arquivo SKILL.md é uma skill. Ignore a pasta "references".

Copie cada uma dessas subpastas, inteira, para ~/.agents/skills/<nome-da-subpasta>/. Se alguma já existir, me pergunte antes de substituir.

Apague os arquivos temporários do download. No final, liste as skills instaladas e o que cada uma faz.
```

O Codex detecta skills novas sozinho. Se alguma não aparecer, reinicie.

**Atenção:** as skills foram escritas e testadas no Claude. No Codex, o comportamento pode variar, principalmente quando uma skill chama outra (as portas do Sync chamam a `syncing`). Se encontrar diferenças, conte numa [issue](../../../../issues/new/choose).

[Voltar para todas as plataformas](../como-instalar-skills.md)
