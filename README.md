# 📦 Pandora Box — Base de Conhecimento Público

Conhecimentos, dicas, skills, MCPs e materiais que eu uso no dia a dia e quero que
**qualquer pessoa** possa acessar.

Tudo aqui é aberto: leia, copie, adapte e use nos seus projetos.

---

## 🗺️ Como navegar

| Seção | O que você encontra |
|---|---|
| [`mcps/`](mcps/) | Servidores MCP (Model Context Protocol) que desenvolvi, com instruções de instalação e uso |
| [`skills/`](skills/) | Skills para Claude e outros agentes — instruções empacotadas para tarefas recorrentes |
| [`guias/`](guias/) | Tutoriais passo a passo, do básico ao avançado |
| [`dicas/`](dicas/) | Dicas rápidas, atalhos e boas práticas — leitura de 2 minutos |
| [`prompts/`](prompts/) | Prompts prontos e testados para copiar e adaptar |
| [`recursos/`](recursos/) | Links, ferramentas, cursos e referências que recomendo |

## 🧰 Ferramentas e skills disponíveis

| Nome | Tipo | Para que serve | Status |
|---|---|---|---|
| [Família `sync`](skills/sync/) | Skills | Entrevistas guiadas para você entender, documentar e montar o próprio projeto, até um MVA pronto para usar no Claude | 🚧 Em construção |
| ↳ `/sync-me` | Skill | Conversa livre que questiona a sua ideia até ela ficar clara. Não grava arquivos. | 🚧 |
| ↳ `/sync-docs` | Skill | Mesma conversa, registrando glossário e decisões do projeto. **Comece por aqui.** | 🚧 |
| ↳ `/sync-mva` | Skill | Monta um MVA a partir do `/sync-docs`: prompt do agente com testes, documentos e manual de montagem no Cowork | 🚧 |
| ↳ `/syncdb` | Skill | Gera bases de dados sintéticas (CSV ou Markdown) a partir de um arquivo de exemplo | 🚧 |
| ↳ [`syncing`](skills/sync/syncing/) | Skill (interna) | O método de entrevista usado pelas outras. Você não precisa chamá-la. | 🧪 v0.1 |

### ⚡ Instalação rápida

Copie o prompt abaixo e cole no **Claude Code** ou no **Claude Cowork**. O próprio Claude baixa e instala as skills para você.

```text
Instale para mim as skills da família "sync" do repositório público https://github.com/Pandora-Tech-LTDA/pandora-box (branch main, pasta skills/sync).

Cada subpasta de skills/sync que tem um arquivo SKILL.md é uma skill. Ignore a pasta "references".

- Se você for o Claude Code: copie cada uma dessas subpastas, inteira, para ~/.claude/skills/<nome-da-subpasta>/. Se alguma já existir, me pergunte antes de substituir.
- Se você for o Claude Cowork (ou não conseguir gravar em ~/.claude/skills): crie nesta pasta um arquivo <nome-da-subpasta>.zip para cada skill, com a subpasta inteira dentro, e me explique passo a passo como enviar cada .zip nas configurações do Claude, na área de Skills.

Apague os arquivos temporários do download. No final, me mostre uma tabela com as skills instaladas e o que cada uma faz, e me diga como começar a usar.
```

Depois de instalar, **feche e abra o Claude de novo** (ou abra uma nova conversa). Passo a passo detalhado e solução de problemas: [Como instalar as skills](guias/como-instalar-skills.md).

## 🚀 Por onde começar

- **Nunca usou MCP?** Comece por [`guias/o-que-e-mcp.md`](guias/o-que-e-mcp.md).
- **Quer instalar uma MCP específica?** Veja a lista em [`mcps/`](mcps/).
- **Quer usar uma skill?** Veja o guia [Como instalar as skills](guias/como-instalar-skills.md) e o catálogo em [`skills/`](skills/).

## 🤝 Contribuindo

Encontrou um erro, tem uma dúvida ou uma sugestão? Abra uma
[issue](../../issues/new/choose). Quer contribuir com conteúdo? Leia o
[CONTRIBUTING.md](CONTRIBUTING.md).

## ⚖️ Licença

- **Código** (MCPs, scripts, exemplos): [MIT](LICENSE)
- **Conteúdo** (textos, guias, dicas): [CC BY 4.0](LICENSE-CONTEUDO.md) — use à vontade, citando a fonte.
