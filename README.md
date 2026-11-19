<div align="center">

<img src="assets/banner.png" alt="Pandora Box. Abra a caixa. O conhecimento se espalha. Skills, MCPs, guias e prompts para qualquer pessoa usar. Ao lado, um cubo isométrico aberto, com pontos de luz subindo da caixa; no fundo dela, um ponto branco: a esperança." width="100%">

<br>

**A caixa de conhecimento aberto da Pandora.**<br>
Skills, MCPs, guias e prompts para trabalhar com IA com critério, do primeiro passo ao uso avançado.

<br>

[![Licença do código: MIT](https://img.shields.io/badge/c%C3%B3digo-MIT-7024AE?style=flat-square)](LICENSE)
[![Licença do conteúdo: CC BY 4.0](https://img.shields.io/badge/conte%C3%BAdo-CC%20BY%204.0-7024AE?style=flat-square)](LICENSE-CONTEUDO.md)
[![Idioma: português do Brasil](https://img.shields.io/badge/idioma-pt--BR-161018?style=flat-square)](#)
[![Contribuições abertas](https://img.shields.io/badge/contribui%C3%A7%C3%B5es-abertas-161018?style=flat-square)](CONTRIBUTING.md)

[Produtos](#produtos) · [Instalação rápida](#instalação-rápida) · [Organização](#como-o-repositório-está-organizado) · [Contribuir](#contribuir)

</div>

---

## Por que Pandora Box

No mito, Pandora abre a caixa e tudo o que havia dentro se espalha pelo mundo. Só a esperança fica guardada no fundo.

Aqui a caixa é aberta de propósito. O que sai dela é conhecimento: o que a Pandora aprende construindo com IA, organizado para que qualquer pessoa possa aplicar no próprio trabalho. O que fica guardado, dentro deste repositório, é a esperança de que mais pessoas abram a caixa também.

Todo o material é aberto. Leia, copie, adapte e use, citando a fonte.

---

## Produtos

<a href="skills/sync/"><img src="assets/banner-sync.png" alt="Sync. A IA pergunta. Você decide. Uma família de skills que entrevista você sobre o seu projeto até haver entendimento compartilhado e, no fim, entrega o material para montar o seu MVA." width="100%"></a>

### Sync

**Skills para o Claude que entrevistam você sobre o seu projeto antes de qualquer linha ser escrita.**

A maioria dos projetos com IA começa pela ferramenta. O Sync começa pelas perguntas: o que você quer resolver, para quem, com quais dados e com qual critério de sucesso. A IA pergunta em rodadas, sugere e mostra o custo de cada sugestão. As decisões ficam com você, e um "sim" sem motivo não fecha nenhuma delas.

No fim, você sai com o projeto documentado e, se quiser, com o material para montar um MVA no Claude: o prompt do agente com testes, os documentos de referência e o manual de montagem.

| Skill | O que faz | Situação |
|---|---|---|
| `/sync-docs` | Entrevista sobre o projeto e registra glossário e decisões. **Ponto de partida.** | Em construção |
| `/sync-mva` | Monta o MVA a partir do que o `/sync-docs` registrou | Em construção |
| `/syncdb` | Gera bases de dados sintéticas em CSV ou Markdown a partir de um arquivo de exemplo | Em construção |
| `/sync-me` | Entrevista livre sobre uma ideia, sem gerar arquivos | Em construção |
| [`syncing`](skills/sync/syncing/) | O método de entrevista usado pelas outras skills | v0.1, em teste |

[Conhecer o Sync ↗](skills/sync/) · [Instalar](#instalação-rápida)

---

## Instalação rápida

As skills seguem o formato aberto [Agent Skills](https://agentskills.io) e funcionam no Claude e em outros agentes compatíveis. Escolha a sua plataforma:

| Plataforma | Como instala | Guia |
|---|---|---|
| **Claude.ai** (navegador, desktop e celular) | Baixe [syncing.zip](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/download/skills/syncing.zip) e envie nas configurações | [Instruções](guias/instalar/claude-ai.md) |
| **Claude Cowork** | Mesmo .zip do Claude.ai | [Instruções](guias/instalar/claude-cowork.md) |
| **Claude Code** | Prompt pronto | [Instruções](guias/instalar/claude-code.md) |
| **OpenAI Codex** | Prompt pronto | [Instruções](guias/instalar/codex.md) |
| **VS Code com GitHub Copilot** | Prompt pronto, por projeto | [Instruções](guias/instalar/vscode-copilot.md) |
| **Outros agentes** | Pasta `.agents/skills` | [Instruções](guias/instalar/outros-agentes.md) |

As skills são escritas para o Claude. Nas demais plataformas, o formato é compatível, mas o comportamento ainda não foi validado. Todos os downloads ficam em [Skills da Pandora Box](https://github.com/Pandora-Tech-LTDA/pandora-box/releases/tag/skills).

---

## Como o repositório está organizado

| Pasta | Conteúdo |
|---|---|
| [`skills/`](skills/) | Skills para o Claude: instruções empacotadas para tarefas recorrentes |
| [`mcps/`](mcps/) | Servidores MCP (Model Context Protocol), com instalação e uso |
| [`guias/`](guias/) | Tutoriais passo a passo, do básico ao avançado |
| [`dicas/`](dicas/) | Dicas curtas e boas práticas |
| [`prompts/`](prompts/) | Prompts testados, prontos para adaptar |
| [`recursos/`](recursos/) | Ferramentas, leituras e referências recomendadas |

**Por onde começar.** Se você nunca usou uma skill, siga [Como instalar as skills](guias/como-instalar-skills.md). Se nunca ouviu falar de MCP, leia [O que é MCP](guias/o-que-e-mcp.md).

---

## Contribuir

Encontrou um erro, tem uma dúvida ou quer sugerir um conteúdo? Abra uma [issue](../../issues/new/choose). Para contribuir com material, leia o [guia de contribuição](CONTRIBUTING.md).

## Licença

- **Código** (MCPs, scripts e exemplos): [MIT](LICENSE).
- **Conteúdo** (textos, guias e dicas): [CC BY 4.0](LICENSE-CONTEUDO.md). Use à vontade, citando a fonte.

<sub>©2026 Pandora Tech LTDA</sub>
