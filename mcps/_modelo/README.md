# Nome da MCP

> Uma frase dizendo o que essa MCP faz e para quem ela é útil.

**Status:** 🧪 Beta · **Linguagem:** TypeScript/Python · **Transporte:** stdio / HTTP

## O que ela faz

- Ferramenta 1 — o que faz
- Ferramenta 2 — o que faz

## Pré-requisitos

- Node.js 20+ ou Python 3.11+
- Conta/chave de API em _serviço X_ (se aplicável)

## Instalação

```bash
git clone https://github.com/Pandora-Tech-LTDA/wiki.git
cd wiki/mcps/nome-da-mcp
npm install
```

## Configuração

Copie o arquivo de exemplo e preencha suas credenciais:

```bash
cp .env.example .env
```

### Claude Code

```bash
claude mcp add nome-da-mcp -- node /caminho/para/wiki/mcps/nome-da-mcp/dist/index.js
```

### Claude Desktop (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "nome-da-mcp": {
      "command": "node",
      "args": ["/caminho/para/wiki/mcps/nome-da-mcp/dist/index.js"],
      "env": { "API_KEY": "sua-chave-aqui" }
    }
  }
}
```

## Ferramentas disponíveis

| Ferramenta | Parâmetros | Retorno |
|---|---|---|
| `nome_da_ferramenta` | `param: string` | O que retorna |

## Exemplos de uso

> "Pergunte ao Claude: ..."

## Limitações conhecidas

-

## Changelog

- **v0.1.0** — Primeira versão.
