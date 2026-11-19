# O que é MCP (e por que você deveria se importar)

**Nível:** Iniciante · **Tempo de leitura:** 5 min

## Em uma frase

O **MCP (Model Context Protocol)** é um padrão aberto que permite conectar
assistentes de IA — como o Claude — a ferramentas, sistemas e dados externos.

## A analogia

Pense no MCP como uma **porta USB para a IA**. Antes, cada integração era um cabo
diferente. Com o MCP, qualquer ferramenta que "fala MCP" pode ser plugada em
qualquer assistente que também fala.

## Como funciona

```
[ Você ] ⇄ [ Assistente de IA (cliente MCP) ] ⇄ [ Servidor MCP ] ⇄ [ API / banco / sistema ]
```

- **Cliente MCP:** o app onde você conversa (Claude Code, Claude Desktop, Cursor...).
- **Servidor MCP:** um pequeno programa que expõe **ferramentas** (ações), **recursos**
  (dados para leitura) e **prompts** (modelos prontos).
- O assistente decide quando chamar cada ferramenta com base no seu pedido.

## Exemplos práticos

- Perguntar "quais boletos vencem essa semana?" e a IA consultar seu sistema financeiro.
- Pedir "cria uma tarefa para revisar o contrato" e a IA criar o card no seu gerenciador.
- Consultar a base de conhecimento da sua empresa sem sair do chat.

## Próximos passos

- Veja as MCPs disponíveis em [`../mcps/`](../mcps/).
- Documentação oficial: <https://modelcontextprotocol.io>
