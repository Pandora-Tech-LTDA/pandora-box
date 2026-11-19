<div align="center">

<img src="assets/banner.svg" alt="Pandora Box: uma caixa aberta espalha luz e pontos de conhecimento pelo mundo; no fundo dela brilha uma estrela dourada, a esperança. Abra a caixa, espalhe o conhecimento." width="100%">

<br>

**A caixa de conhecimento aberto da Pandora Tech.**<br>
Skills, MCPs, guias e prompts para qualquer pessoa usar, do primeiro passo ao avançado.

<br>

[![Licença do código: MIT](https://img.shields.io/badge/c%C3%B3digo-MIT-F5C451?style=flat-square)](LICENSE)
[![Licença do conteúdo: CC BY 4.0](https://img.shields.io/badge/conte%C3%BAdo-CC%20BY%204.0-A78BFA?style=flat-square)](LICENSE-CONTEUDO.md)
[![Idioma: português do Brasil](https://img.shields.io/badge/idioma-pt--BR-67E8F9?style=flat-square)](#)
[![Contribuições bem-vindas](https://img.shields.io/badge/contribui%C3%A7%C3%B5es-bem--vindas-FFF4D6?style=flat-square)](CONTRIBUTING.md)

[**⚡ Instalar as skills**](#-instalação-rápida) · [**🧰 O que tem aqui**](#-ferramentas-e-skills-disponíveis) · [**🚀 Por onde começar**](#-por-onde-começar) · [**🤝 Contribuir**](#-contribuindo)

</div>

---

## 📦 Por que Pandora Box?

No mito grego, Pandora abre uma caixa e tudo o que estava lá dentro se espalha pelo mundo.
Só uma coisa fica guardada no fundo: **a esperança**.

Aqui a caixa é aberta de propósito. O que sai dela é **conhecimento**: tudo o que aprendemos
construindo com IA, organizado para que qualquer pessoa possa usar. E o que fica guardado no
fundo, dentro do repositório, é a nossa esperança: **que cada vez mais pessoas abram a caixa também.**

Tudo aqui é aberto: leia, copie, adapte e use nos seus projetos.

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
