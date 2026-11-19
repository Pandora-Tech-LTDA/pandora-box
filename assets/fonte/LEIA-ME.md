# Fonte dos banners

- `banner.html` gera `../banner.png` (página principal).
- `banner-sync.html` gera `../banner-sync.png` (produto /pandora:sync).
- `gerar_banners_skills.py` gera, em `skills/`, os banners de cada skill (PT e EN). Capture cada HTML em 1280×440, escala 2×, e salve em `../banners/<skill>-<idioma>.webp` (WebP, qualidade 88).
- `banner-en.html` e `banner-sync-en.html` geram as versões em inglês (`../banner-en.png` e `../banner-sync-en.png`), usadas na parte em inglês dos READMEs.
- Para um produto novo, copie `banner-sync.html`, troque selo, título, texto e o elemento gráfico (um só por peça: cubo, anel, arco, marca de + ou coluna de pontos).


`banner.html` gera `../banner.png` (1280×440, renderizado a 2×) seguindo o design system da Pandora:
fundo `#0A0A0B`, luz roxa de um canto, malha de pontos de 34px, Instrument Sans + Newsreader itálico,
cubo isométrico em fio e logo invertido oficial.

Para regenerar, abra o HTML num navegador (com internet, para as fontes do Google) e capture
a área de 1280×440 em escala 2×.

## Card social (Open Graph)

- `social-card.html` gera `../social-preview.png` (1280×640), a imagem que aparece quando o link do repositório é compartilhado.
- Margem segura de 80px em todos os lados, como recomenda o GitHub: nada importante fica fora dela. Abra o HTML com `#guias` no fim do endereço para ver a margem.
- Para usar: no GitHub, *Settings → General → Social preview → Edit → Upload an image* e envie `assets/social-preview.png`.
- Para outro produto, troque selo, título, texto e o elemento gráfico, e capture em 1280×640 (escala 1×).
