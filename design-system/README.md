# Pandora DS

**Português** · [English](#english)

O design system de referência da Pandora Box: simples, moderno e pensado para experimentos. Ele garante telas legíveis, com bom contraste e coerentes entre si quando o projeto ainda não tem um design system próprio. É o padrão visual que o `/sync-spec` aplica nas specs.

> **Versão:** v1 · **Licença:** MIT · ©2026 Pandora Tech LTDA

## Temas

| Tema | Para quê |
|---|---|
| **Pandora Claro** (`claro`) | Padrão. Fundo branco, texto em tinta, roxo só como destaque. |
| **Pandora Escuro** (`escuro`) | Mesma linguagem em fundo escuro. |
| **Neutro** (`neutro`) | Grafite com destaque azul discreto, para quem não quer roxo. |
| **Alto contraste** (`alto-contraste`) | Preto, branco e amarelo, para acessibilidade máxima. |

Todas as combinações de texto passam no contraste mínimo WCAG AA (4,5:1).

## Como usar

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Pandora-Tech-LTDA/pandora-box@design-system-v1/design-system/pandora.css">
<html data-theme="claro">
```

Os componentes usam classes com o prefixo `ds-`, por exemplo `ds-btn ds-btn--primary`, `ds-input`, `ds-card`, `ds-table`. Veja todos funcionando nos exemplos.

## Arquivos

| Arquivo | Conteúdo |
|---|---|
| [`pandora.css`](pandora.css) | Tokens, os quatro temas e os componentes |
| [`tokens.json`](tokens.json) | Os mesmos tokens em JSON, para outras ferramentas |
| [`resumo-para-spec.md`](resumo-para-spec.md) | O resumo de cada tema que o `/sync-spec` coloca na spec |
| [`exemplo.html`](exemplo.html) | Cores e componentes básicos |
| [`exemplos/perfil.html`](exemplos/perfil.html) | Uma página de perfil completa |
| [`exemplos/componentes.html`](exemplos/componentes.html) | Componentes menos comuns: indicadores, etapas, arraste de arquivo, linha do tempo, acordeão e outros |

## Componentes

Botões, campos, seleção, área de texto, caixa de seleção, interruptor, cartão, selo, aviso, tabela, barra superior, navegação, abas, modal, avatar, lista, estado vazio e carregamento. Menos comuns: trilha de navegação, controle segmentado, etapas, barra de progresso, dica, notificação, acordeão, paginação, área de arraste de arquivo, linha do tempo, indicador numérico, filtro removível, tecla de atalho, grupo de avatares, divisor com texto, bloco de código e controle deslizante.

## Trocar pelo seu design system

O Pandora DS é só o ponto de partida. Para usar o seu, troque a folha de estilo e os valores do resumo na spec pelos do seu design system. O `/sync-spec` faz essa troca quando você pede.

---

<a id="english"></a>

# Pandora DS

**English** · [Português](#pandora-ds)

Pandora Box's reference design system: simple, modern and made for experiments. It keeps screens readable, with good contrast and consistent with each other, when a project has no design system of its own. It is the visual default `/sync-spec` applies to specs.

> **Version:** v1 · **License:** MIT · ©2026 Pandora Tech LTDA

Themes: **Pandora Claro** (light, default), **Pandora Escuro** (dark), **Neutro** (graphite with a muted blue accent) and **Alto contraste** (high contrast). Every text pairing meets WCAG AA (4.5:1).

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/Pandora-Tech-LTDA/pandora-box@design-system-v1/design-system/pandora.css">
<html data-theme="claro">
```

Components use `ds-` classes. See [`exemplo.html`](exemplo.html), [`exemplos/perfil.html`](exemplos/perfil.html) and [`exemplos/componentes.html`](exemplos/componentes.html). To use your own design system, replace the stylesheet and the summary values in the spec; `/sync-spec` does this when you ask.
