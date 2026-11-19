# Instalar no VS Code com GitHub Copilot

**Português** · [English](#english)

**Para:** VS Code com GitHub Copilot em modo agente · **Tempo:** 2 minutos · **Situação:** compatível, não testado

Segundo o [guia do padrão Agent Skills](https://agentskills.io/skill-creation/quickstart), o VS Code procura skills em `.agents/skills/` na raiz do projeto. Abra a pasta do projeto, abra o chat do Copilot em **modo agente**, copie o prompt e cole:

```text
Instale para mim as skills da família "sync" do repositório público https://github.com/Pandora-Tech-LTDA/pandora-box (branch main, pasta skills/sync).

Cada subpasta de skills/sync que tem um arquivo SKILL.md é uma skill. Ignore a pasta "references".

Copie cada uma dessas subpastas, inteira, para .agents/skills/ (na raiz deste projeto) <nome-da-subpasta>/. Se alguma já existir, me pergunte antes de substituir.

Apague os arquivos temporários do download. No final, me mostre uma tabela com as skills instaladas e o que cada uma faz, e me diga como começar a usar.
```

Depois, digite `/skills` no chat do modo agente para conferir se elas aparecem.

**Atenção:** as skills foram escritas para o Claude. No Copilot, o comportamento pode variar.

Se testar e encontrar diferenças, conte numa [issue](https://github.com/Pandora-Tech-LTDA/pandora-box/issues/new/choose).

[Voltar para todas as plataformas](../como-instalar-skills.md)

---

<a id="english"></a>

# Install on VS Code with GitHub Copilot

**English** · [Português](#instalar-no-vs-code-com-github-copilot)

**For:** VS Code with GitHub Copilot in agent mode · **Time:** 2 minutes · **Status:** compatible, not tested

According to the [Agent Skills quickstart](https://agentskills.io/skill-creation/quickstart), VS Code looks for skills in `.agents/skills/` at the project root. Open the project folder, open the Copilot chat in **agent mode**, copy the prompt and paste it:

```text
Install the "sync" skill family from the public repository https://github.com/Pandora-Tech-LTDA/pandora-box (branch main, folder skills/sync).

Each subfolder of skills/sync that contains a SKILL.md file is a skill. Ignore the "references" folder.

Copy each of these subfolders, in full, to .agents/skills/ (at the root of this project) <subfolder-name>/. If any already exists, ask me before replacing it.

Delete the temporary download files. At the end, show me a table of the installed skills and what each one does, and tell me how to get started.
```

Then type `/skills` in agent mode chat to check that they show up.

**Note:** these skills were written for Claude. In Copilot, behavior may differ.

If you test it and find differences, tell us in an [issue](https://github.com/Pandora-Tech-LTDA/pandora-box/issues/new/choose).

[Back to all platforms](../como-instalar-skills.md#english)
