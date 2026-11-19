# 📚 Wiki — Base de Conhecimento Público

Conhecimentos, dicas, skills, MCPs e materiais que eu uso no dia a dia e quero que
**qualquer pessoa** possa acessar — especialmente meus alunos e clientes.

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

**Nunca instalou uma skill?** Siga o guia [Como instalar as skills](guias/como-instalar-skills.md). Ele já traz o prompt pronto para copiar e colar.

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
