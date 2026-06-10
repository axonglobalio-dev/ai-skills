# Assets SOS Telas Kids v3.3

Este diretório deve conter os seguintes arquivos de imagem:

## 1. hero-object.webp
- **Dimensões mínimas:** 1600x1000px
- **Dimensões ideais:** 2200x1400px
- **Formato:** WebP ou PNG
- **Requisito:** Fundo transparente real
- **Uso:** Substituir o placeholder na seção Hero (seção 1)
- **Descrição:** Kit digital SOS Telas Kids organizado em materiais de missão

## 2. creator-photo.webp
- **Dimensões:** 600x600px
- **Formato:** WebP ou JPG
- **Requisito:** Foto natural, sem pose de guru
- **Uso:** Seção "Sobre o Criador" (seção 10)
- **Descrição:** Retrato de Manoel Calaça Junior

## 3. og-sos-telas.jpg
- **Dimensões:** 1200x630px
- **Formato:** JPG
- **Uso:** Meta tag Open Graph para compartilhamento em redes sociais

## Como substituir os placeholders

No arquivo `index.html`, localize o comentário:
```html
<!-- HERO ASSET FINAL: Substituir o bloco placeholder abaixo por: -->
```

Substitua o bloco `<div class="hero-object-placeholder">...</div>` por:
```html
<img
  src="./assets/hero-object.webp"
  alt="Kit digital SOS Telas Kids organizado em materiais de missão"
  class="hero-object-image"
  width="2200"
  height="1400"
  style="position: absolute; top: 11vh; left: 50%; transform: translateX(-38%); width: clamp(720px, 62vw, 1120px);"
/>
```
