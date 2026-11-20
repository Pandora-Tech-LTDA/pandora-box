# MCPs

Servidores **MCP (Model Context Protocol)** que desenvolvi. Uma MCP conecta um
assistente de IA (Claude, Cursor, etc.) a ferramentas e dados externos.

> Não sabe o que é MCP? Leia antes [`../guias/o-que-e-mcp.md`](../guias/o-que-e-mcp.md).

## Catálogo

| MCP | O que faz | Status |
|---|---|---|
| [leadership-mcp](leadership-mcp/) | Liderança humanista no momento da conversa difícil: o assistente oferece consultar a base antes de responder | Em teste |

<!-- Ao adicionar uma MCP, inclua uma linha acima:
| [nome-da-mcp](nome-da-mcp/) | Descrição curta | Estável / Beta / Em construção |
-->

## Como adicionar uma nova MCP

1. Copie a pasta [`_modelo/`](_modelo/) para `mcps/<nome-da-mcp>/`.
2. Preencha o `README.md` (o que faz, instalação, configuração, ferramentas, exemplos).
3. Coloque o código-fonte na pasta, **sem nenhuma chave ou segredo** — use `.env.example`.
4. Adicione a linha no catálogo acima.
