# Instalar no VS Code com GitHub Copilot

**Para:** VS Code com GitHub Copilot em modo agente · **Tempo:** 2 minutos · **Situação:** compatível, não testado

Segundo o [guia do padrão Agent Skills](https://agentskills.io/skill-creation/quickstart), o VS Code procura skills em `.agents/skills/` na raiz do projeto. A instalação é por projeto.

Abra a pasta do projeto no VS Code, abra o chat do Copilot em **modo agente**, copie o prompt e cole:

```text
Instale neste projeto as skills da família "sync" do repositório público https://github.com/Pandora-Tech-LTDA/pandora-box (branch main, pasta skills/sync).

Cada subpasta de skills/sync que tem um arquivo SKILL.md é uma skill. Ignore a pasta "references".

Copie cada uma dessas subpastas, inteira, para .agents/skills/<nome-da-subpasta>/ na raiz deste projeto. Se alguma já existir, me pergunte antes de substituir.

Apague os arquivos temporários do download. No final, liste as skills instaladas.
```

Depois, digite `/skills` no chat do modo agente para conferir se elas aparecem.

**Atenção:** as skills foram escritas e testadas no Claude. No Copilot, o comportamento pode variar. Se encontrar diferenças, conte numa [issue](../../../../issues/new/choose).

[Voltar para todas as plataformas](../como-instalar-skills.md)
