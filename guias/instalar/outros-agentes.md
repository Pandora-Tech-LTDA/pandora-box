# Instalar em outros agentes

**Português** · [English](#english)

**Situação:** compatível, não testado

[Agent Skills](https://agentskills.io) é um formato aberto adotado por outros agentes. Os locais mais comuns são `.agents/skills/` na raiz do projeto (só aquele projeto) e `~/.agents/skills/` (todos os projetos). Alguns agentes usam uma pasta própria, como `.<nome-do-agente>/skills/`, ou também leem `.claude/skills/`. Confira a documentação do seu agente.

- **Manual:** baixe o .zip de cada skill em [Skills da Pandora Box](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/tag/skills), descompacte e coloque a pasta da skill (por exemplo, `syncing/`, com o `SKILL.md` dentro) no local indicado.
- **Por prompt:** se o seu agente roda comandos, use o prompt do Codex, trocando a pasta de destino pela do seu agente.

Se testar e encontrar diferenças, conte numa [issue](https://github.com/Pandora-Tech-LTDA/pandora-box/issues/new/choose).

[Voltar para todas as plataformas](../como-instalar-skills.md)

---

<a id="english"></a>

# Install on other agents

**English** · [Português](#instalar-em-outros-agentes)

**Status:** compatible, not tested

[Agent Skills](https://agentskills.io) is an open format adopted by other agents. The most common locations are `.agents/skills/` at the project root (that project only) and `~/.agents/skills/` (all projects). Some agents use their own folder, such as `.<agent-name>/skills/`, or also read `.claude/skills/`. Check your agent's documentation.

- **Manually:** download each skill's .zip from [Pandora Box Skills](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/tag/skills), unzip it and place the skill folder (for example, `syncing/`, with `SKILL.md` inside) in that location.
- **With a prompt:** if your agent can run commands, use the Codex prompt and change the destination folder to your agent's.

If you test it and find differences, tell us in an [issue](https://github.com/Pandora-Tech-LTDA/pandora-box/issues/new/choose).

[Back to all platforms](../como-instalar-skills.md#english)
