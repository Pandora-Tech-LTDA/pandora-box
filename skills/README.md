<img src="https://raw.githubusercontent.com/Pandora-Tech-LTDA/pandora-box/main/assets/banner-sync.png" alt="Sync. A IA pergunta. Você decide." width="100%">

# Pandora Box

**Português** · [English](#english)

Skills abertas da Pandora para trabalhar com IA com critério. Este plugin reúne todas as skills da [Pandora Box](https://github.com/Pandora-Tech-LTDA/pandora-box) num só pacote e é atualizado a cada nova versão.

## Família Sync

Skills que entrevistam você sobre o seu projeto antes de qualquer linha ser escrita. A IA pergunta em rodadas, sugere e mostra o que cada sugestão custa. As decisões ficam com você, e nas que importam um "sim" sem motivo não basta.

| Skill | Para quê |
|---|---|
| `/pandora:sync-docs` | Entender e documentar um projeto, registrando glossário e decisões. **Comece por aqui.** |
| `/pandora:sync-mva` | Montar um MVA a partir do registro do `/sync-docs`: prompt do agente com autoteste, documentos de referência e manual de montagem no Cowork. |
| `/pandora:syncdb` | Criar dados sintéticos em CSV ou Markdown a partir de um arquivo de exemplo, sem expor dados reais. |
| `/pandora:sync-me` | Amadurecer uma ideia, sem gerar arquivos. É também o método de entrevista das outras skills. |

**Fluxo recomendado:** `/sync-docs` → `/sync-mva` → `/syncdb`.

**Exemplo:** você quer um agente que analise a frequência dos funcionários. O `/sync-docs` esclarece a dor, quem usa a análise e quais regras de ponto valem. O `/sync-mva` define que o agente precisa de uma planilha de frequência e da política de ponto e escreve o prompt com casos de teste. O `/syncdb` cria uma planilha fictícia com os mesmos campos da real.

**Situação:** versão 0.1, em teste.

## Instalação

- **Claude.ai e Cowork:** baixe [pandora.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/pandora.zip) e envie em *Personalizar → Plugins → Adicionar → Enviar plugin*.
- **Claude Code:** `/plugin install pandora --marketplace Pandora-Tech-LTDA/pandora-box`.
- **Outras plataformas:** veja [Como instalar as skills](https://github.com/Pandora-Tech-LTDA/pandora-box/blob/main/guias/como-instalar-skills.md).

## Créditos e licença

`sync-me` e `sync-docs` são derivadas das skills `grilling`, `grill-me` e `grill-with-docs` de Matt Pocock ([mattpocock/skills](https://github.com/mattpocock/skills), licença MIT). `sync-mva` e `syncdb` seguem a metodologia MVA, ©2026 Pandora Tech LTDA. Código sob licença MIT.

---

<a id="english"></a>

# Pandora Box

**English** · [Português](#pandora-box)

Pandora's open skills for working with AI with sound judgment. This plugin bundles every [Pandora Box](https://github.com/Pandora-Tech-LTDA/pandora-box) skill in one package and is updated with each new version.

## Sync family

Skills that interview you about your project before a single line is written. The AI asks in rounds, makes suggestions and shows what each suggestion costs. You make the decisions, and on the ones that matter a "yes" without a reason is not enough.

| Skill | Purpose |
|---|---|
| `/pandora:sync-docs` | Understand and document a project, recording a glossary and decisions. **Start here.** |
| `/pandora:sync-mva` | Build an MVA (Minimum Viable Automation) from the `/sync-docs` record: agent prompt with self-test, reference documents and a Cowork setup manual. |
| `/pandora:syncdb` | Create synthetic data in CSV or Markdown from a sample file, without exposing real data. |
| `/pandora:sync-me` | Develop an idea, without creating files. It is also the interview method for the other skills. |

**Recommended flow:** `/sync-docs` → `/sync-mva` → `/syncdb`. The skills are written in Brazilian Portuguese and work in any language.

**Status:** version 0.1, in testing.

## Installation

- **Claude.ai and Cowork:** download [pandora.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/pandora.zip) and upload it in *Customize → Plugins → Add → Upload plugin*.
- **Claude Code:** `/plugin install pandora --marketplace Pandora-Tech-LTDA/pandora-box`.
- **Other platforms:** see [How to install the skills](https://github.com/Pandora-Tech-LTDA/pandora-box/blob/main/guias/como-instalar-skills.md#english).

## Credits and license

`sync-me` and `sync-docs` are derived from Matt Pocock's `grilling`, `grill-me` and `grill-with-docs` skills ([mattpocock/skills](https://github.com/mattpocock/skills), MIT license). `sync-mva` and `syncdb` follow the MVA methodology, ©2026 Pandora Tech LTDA. Code under the MIT license.

<sub>©2026 Pandora Tech LTDA</sub>
