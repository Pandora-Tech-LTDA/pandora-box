# Instalar em outros agentes

**Situação:** compatível, não testado

[Agent Skills](https://agentskills.io) é um formato aberto, e outros agentes também o adotam. Pelo guia do padrão, os locais mais comuns são:

| Escopo | Pasta |
|---|---|
| Só para um projeto | `.agents/skills/` na raiz do projeto |
| Para todos os projetos | `~/.agents/skills/` |

Alguns agentes usam uma pasta própria (por exemplo, `.<nome-do-agente>/skills/`) ou também leem `.claude/skills/`. Confira a documentação do seu agente.

**Instalação manual:** baixe o .zip de cada skill em [Skills da Pandora Box](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/tag/skills), descompacte e coloque a pasta da skill (por exemplo, `syncing/`, com o `SKILL.md` dentro) no local indicado.

**Instalação por prompt:** se o seu agente consegue rodar comandos, use o prompt do [Codex](codex.md), trocando a pasta de destino pela do seu agente.

As skills foram escritas e testadas no Claude. Se testar em outro agente, conte o resultado numa [issue](../../../../issues/new/choose).

[Voltar para todas as plataformas](../como-instalar-skills.md)
