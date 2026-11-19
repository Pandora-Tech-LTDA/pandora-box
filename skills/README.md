# 🧠 Skills

**Skills** são pacotes de instruções (um `SKILL.md` + arquivos de apoio) que ensinam
um agente de IA a executar uma tarefa recorrente do jeito certo.

## Catálogo

| Skill | O que faz | Status |
|---|---|---|
| [Família `sync`](sync/) | Entrevistas guiadas para entender, documentar e montar um projeto, até um MVA | 🚧 Em construção |

## Como instalar uma skill

Siga o guia [Como instalar as skills](../guias/como-instalar-skills.md). Ele tem o passo a passo para iniciantes e o prompt pronto para colar no Claude.

## Como adicionar uma nova skill

1. Copie [`_modelo/`](_modelo/) para `skills/<nome-da-skill>/`.
2. Edite o `SKILL.md` — a `description` é o que faz a skill ser acionada, capriche nela.
3. Adicione a linha no catálogo acima.
