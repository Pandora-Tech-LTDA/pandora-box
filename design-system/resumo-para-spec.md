# Resumo dos temas para a spec

O `/sync-spec` copia para a spec o bloco do tema escolhido, sem alterar. Assim a IA de código aplica o padrão visual mesmo sem abrir o link. Ao mudar de versão o design system, este arquivo muda junto.

## Pandora Claro

```markdown
### Padrão visual: Pandora DS v1, tema Pandora Claro

- **Folha de estilo:** `https://cdn.jsdelivr.net/gh/Pandora-Tech-LTDA/pandora-box@design-system-v1/design-system/pandora.css` com `<html data-theme="claro">`. Sem acesso ao link, use os valores abaixo.
- **Fontes:** Instrument Sans 600 nos títulos (tracking -0.02em); Inter 400/500 no texto; JetBrains Mono para código.
- **Tamanhos:** texto 14px; rótulos e metadados 11 a 12,5px; títulos 18, 24 e 32px; **campos de formulário 16px**.
- **Cores:** fundo `#FFFFFF` · superfície `#F6F4F8` · texto `#161018` · texto secundário `#4B4453` · apagado `#6B6473` · borda `#E3DFE8`.
- **Destaque:** `#7024AE` (texto sobre ele `#FFFFFF`), só em ação principal, foco, item ativo e link (`#6A1FA6`). Um único destaque por tela.
- **Situação:** sucesso `#14743A` · perigo `#B42328` (botão de perigo `#B42328`) · atenção `#8A5A00`. Sempre acompanhadas de texto.
- **Forma:** cantos de 4px (selos), 6px (botões e campos) e 8px (cartões); bordas de 1px; sem sombras nem degradês.
- **Espaço:** múltiplos de 4px (4, 8, 12, 16, 24, 32, 48, 64); largura máxima de 1120px.
- **Acessibilidade:** contraste mínimo WCAG AA (4,5:1 no texto); foco sempre visível; respeitar `prefers-reduced-motion`; tela de 390px sem rolagem lateral.
- **Estados de toda tela:** carregando, vazio, erro e sucesso.
```

## Pandora Escuro

```markdown
### Padrão visual: Pandora DS v1, tema Pandora Escuro

- **Folha de estilo:** `https://cdn.jsdelivr.net/gh/Pandora-Tech-LTDA/pandora-box@design-system-v1/design-system/pandora.css` com `<html data-theme="escuro">`. Sem acesso ao link, use os valores abaixo.
- **Fontes:** Instrument Sans 600 nos títulos (tracking -0.02em); Inter 400/500 no texto; JetBrains Mono para código.
- **Tamanhos:** texto 14px; rótulos e metadados 11 a 12,5px; títulos 18, 24 e 32px; **campos de formulário 16px**.
- **Cores:** fundo `#0A0A0B` · superfície `#141216` · texto `#EDEBEF` · texto secundário `#BDB7C3` · apagado `#8F8996` · borda `#2B2831`.
- **Destaque:** `#8B3FD1` (texto sobre ele `#FFFFFF`), só em ação principal, foco, item ativo e link (`#C9A6E8`). Um único destaque por tela.
- **Situação:** sucesso `#5BD48A` · perigo `#FF7A7A` (botão de perigo `#C9363C`) · atenção `#F2C14E`. Sempre acompanhadas de texto.
- **Forma:** cantos de 4px (selos), 6px (botões e campos) e 8px (cartões); bordas de 1px; sem sombras nem degradês.
- **Espaço:** múltiplos de 4px (4, 8, 12, 16, 24, 32, 48, 64); largura máxima de 1120px.
- **Acessibilidade:** contraste mínimo WCAG AA (4,5:1 no texto); foco sempre visível; respeitar `prefers-reduced-motion`; tela de 390px sem rolagem lateral.
- **Estados de toda tela:** carregando, vazio, erro e sucesso.
```

## Neutro

```markdown
### Padrão visual: Pandora DS v1, tema Neutro

- **Folha de estilo:** `https://cdn.jsdelivr.net/gh/Pandora-Tech-LTDA/pandora-box@design-system-v1/design-system/pandora.css` com `<html data-theme="neutro">`. Sem acesso ao link, use os valores abaixo.
- **Fontes:** Instrument Sans 600 nos títulos (tracking -0.02em); Inter 400/500 no texto; JetBrains Mono para código.
- **Tamanhos:** texto 14px; rótulos e metadados 11 a 12,5px; títulos 18, 24 e 32px; **campos de formulário 16px**.
- **Cores:** fundo `#FFFFFF` · superfície `#F5F5F4` · texto `#1C1917` · texto secundário `#44403C` · apagado `#6B6560` · borda `#E5E2DE`.
- **Destaque:** `#1F3A5F` (texto sobre ele `#FFFFFF`), só em ação principal, foco, item ativo e link (`#1F4E8C`). Um único destaque por tela.
- **Situação:** sucesso `#15703A` · perigo `#B42318` (botão de perigo `#B42318`) · atenção `#8A5A00`. Sempre acompanhadas de texto.
- **Forma:** cantos de 4px (selos), 6px (botões e campos) e 8px (cartões); bordas de 1px; sem sombras nem degradês.
- **Espaço:** múltiplos de 4px (4, 8, 12, 16, 24, 32, 48, 64); largura máxima de 1120px.
- **Acessibilidade:** contraste mínimo WCAG AA (4,5:1 no texto); foco sempre visível; respeitar `prefers-reduced-motion`; tela de 390px sem rolagem lateral.
- **Estados de toda tela:** carregando, vazio, erro e sucesso.
```

## Alto contraste

```markdown
### Padrão visual: Pandora DS v1, tema Alto contraste

- **Folha de estilo:** `https://cdn.jsdelivr.net/gh/Pandora-Tech-LTDA/pandora-box@design-system-v1/design-system/pandora.css` com `<html data-theme="alto-contraste">`. Sem acesso ao link, use os valores abaixo.
- **Fontes:** Instrument Sans 600 nos títulos (tracking -0.02em); Inter 400/500 no texto; JetBrains Mono para código.
- **Tamanhos:** texto 14px; rótulos e metadados 11 a 12,5px; títulos 18, 24 e 32px; **campos de formulário 16px**.
- **Cores:** fundo `#000000` · superfície `#000000` · texto `#FFFFFF` · texto secundário `#FFFFFF` · apagado `#E6E6E6` · borda `#FFFFFF`.
- **Destaque:** `#FFD400` (texto sobre ele `#000000`), só em ação principal, foco, item ativo e link (`#FFD400`). Um único destaque por tela.
- **Situação:** sucesso `#7CFFB2` · perigo `#FF8A8A` (botão de perigo `#FF8A8A`) · atenção `#FFD400`. Sempre acompanhadas de texto.
- **Forma:** cantos de 4px (selos), 6px (botões e campos) e 8px (cartões); bordas de 1px; sem sombras nem degradês.
- **Espaço:** múltiplos de 4px (4, 8, 12, 16, 24, 32, 48, 64); largura máxima de 1120px.
- **Acessibilidade:** contraste mínimo WCAG AA (4,5:1 no texto); foco sempre visível; respeitar `prefers-reduced-motion`; tela de 390px sem rolagem lateral.
- **Estados de toda tela:** carregando, vazio, erro e sucesso.
```
