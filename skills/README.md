# 🧠 Skills

**Skills** são pacotes de instruções (um `SKILL.md` + arquivos de apoio) que ensinam
um agente de IA a executar uma tarefa recorrente do jeito certo.

## Catálogo

| Skill | O que faz |
|---|---|
| _em breve_ | |

## Como instalar uma skill

**Claude Code:** copie a pasta da skill para `~/.claude/skills/<nome-da-skill>/`
(para todos os projetos) ou `.claude/skills/<nome-da-skill>/` (só para um projeto).

**Claude.ai:** compacte a pasta da skill em `.zip` e envie em
*Configurações → Capacidades → Skills*.

## Como adicionar uma nova skill

1. Copie [`_modelo/`](_modelo/) para `skills/<nome-da-skill>/`.
2. Edite o `SKILL.md` — a `description` é o que faz a skill ser acionada, capriche nela.
3. Adicione a linha no catálogo acima.
