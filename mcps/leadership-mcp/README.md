# Leadership MCP

> Liderança humanista entregue ao seu assistente de IA, no momento em que você escreve o e-mail difícil, dá o feedback ou comunica a decisão.

**Situação:** em teste · **Linguagem:** JavaScript (Node.js 18+) · **Transporte:** stdio e HTTP

**Código-fonte e documentação completa:** [Pandora-Tech-LTDA/leadership-mcp](https://github.com/Pandora-Tech-LTDA/leadership-mcp). Esta página é uma vitrine: o código, a base de conhecimento e as instruções atualizadas vivem no repositório próprio do projeto.

## O que ela faz

Quando a tarefa envolve uma pessoa ou um grupo, como um conflito, um feedback, uma decisão que afeta alguém ou uma conversa pessoal difícil, o assistente oferece consultar o Leadership MCP. Se você aceitar, a resposta é moldada a partir de uma base de liderança humanista organizada em quatro camadas:

1. **Gatilho:** a natureza da situação (conflito, feedback, decisão com impacto, relacionamento interno, interação externa, relacionamento pessoal, divergência e silêncio, autoridade informal, limites e carga).
2. **Filtros:** os princípios que se aplicam, como escuta ativa, comunicação não violenta e segurança psicológica.
3. **Ação:** uma hipótese de comportamento concreta.
4. **Resultado:** o efeito esperado, como confiança e engajamento.

A orientação é sempre uma hipótese, nunca uma prescrição. Você decide como agir.

## Ferramentas disponíveis

| Ferramenta | Parâmetros | Retorno |
|---|---|---|
| `buscar_orientacao` | `situacao: string` | Orientação consolidada: gatilho, filtros, ação e resultado |
| `listar_gatilhos` | nenhum | As categorias de situação cobertas pela base |

## Instalação

### Claude Desktop (local, via npm)

Em *Settings → Developer → Edit Config*, acrescente:

```json
{
  "mcpServers": {
    "leadership": {
      "command": "npx",
      "args": ["-y", "leadership-mcp"]
    }
  }
}
```

### Claude Code

```bash
claude mcp add leadership -- npx -y leadership-mcp
```

### Claude.ai (navegador, desktop e celular)

Existe um conector hospedado, que exige chave de acesso individual. Veja como pedir a chave e configurar em [leadership-mcp.campello.me](https://leadership-mcp.campello.me/).

## Exemplos de uso

> "Preciso responder o e-mail de um colega que está me acusando de atrasar o projeto dele."

> "Vou dar um feedback difícil para alguém do time amanhã. Me ajuda a preparar a conversa?"

## Limitações conhecidas

- A base de conhecimento está em português.
- O servidor classifica a situação por palavras-chave, sem IA própria: é determinístico e funciona sem internet, mas pode não reconhecer situações descritas de forma muito indireta.

---

<a id="english"></a>

# Leadership MCP (English)

An MCP server that brings a humanist leadership knowledge base to your AI assistant at the moment you write the hard email, give feedback or communicate a decision. Guidance is always a hypothesis, never a prescription. The knowledge base is in Portuguese.

Source code, install instructions and full documentation: [Pandora-Tech-LTDA/leadership-mcp](https://github.com/Pandora-Tech-LTDA/leadership-mcp).
