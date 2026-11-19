# sync: skills de entrevista para tirar projetos do papel

Família de skills para qualquer pessoa que queira entender, documentar e construir um projeto
com a ajuda da IA. O objetivo é que usuário e IA cheguem a um entendimento compartilhado do projeto,
com o usuário sempre questionando, e que o projeto chegue a um MVA pronto para usar no Claude.

> 🚧 Em construção: a `syncing` está pronta (v0.1, em teste); as demais ainda não foram escritas.
> Para instalar quando estiverem prontas, veja [Como instalar as skills](../../guias/como-instalar-skills.md).

## Skills

| Skill | Como usar | O que faz | Baseada em |
|---|---|---|---|
| [`syncing`](syncing/) | Interna (o modelo aciona) | Método de entrevista em rodadas, usado pelas outras skills | [`grilling`](https://www.aihero.dev/skills-grilling), de Matt Pocock |
| `/sync-me` | Você digita | Entrevista livre, sem gerar arquivos. Termina com um resumo. | [`grill-me`](https://www.aihero.dev/skills-grill-me), de Matt Pocock |
| `/sync-docs` | Você digita | Entrevista que registra glossário e decisões em `sync/` | [`grill-with-docs`](https://www.aihero.dev/skills-grill-with-docs), de Matt Pocock |
| `/sync-mva` | Você digita | Monta um MVA: prompt do agente com testes, documentos de referência e manual de montagem no Cowork | Metodologia MVA (Pandora Tech LTDA) |
| `/syncdb` | Você digita, ou o modelo aciona | Gera bases sintéticas em CSV ou Markdown a partir de um arquivo de exemplo | Metodologia MVA (Pandora Tech LTDA) |

Fluxo recomendado: `/sync-docs` → `/sync-mva` → `/syncdb`.

## Créditos e licenças

- `syncing`, `/sync-me` e `/sync-docs` são derivadas das skills de **Matt Pocock**:
  [mattpocock/skills](https://github.com/mattpocock/skills), licença MIT
  (cópia da licença em [`references/mattpocock-skills/LICENSE`](references/mattpocock-skills/LICENSE)).
- `/sync-mva` e `/syncdb` seguem a metodologia MVA, © 2026 Pandora Tech LTDA
  (ver [`references/mva/FONTE.md`](references/mva/FONTE.md)).

## Documentação do projeto

- [`DECISOES.md`](DECISOES.md): decisões tomadas sobre a família.
- [`references/`](references/): material de origem (skills do Matt Pocock, metodologia MVA e links externos).
