# Assets Placeholder Documentation

Esta pasta deve conter os seguintes arquivos de imagem:

## 1. hero-object.webp
- **Dimensões mínimas:** 1600x1000px
- **Dimensões ideais:** 2200x1400px
- **Formato:** WebP ou PNG com fundo transparente real
- **Descrição:** Objeto-herói principal da landing page, mostrando o kit SOS Telas Kids como vitrine de produto premium
- **Uso:** Hero section (seção 1) — deve ser dominante, sem card/moldura ao redor
- **Status atual:** Placeholder ativo no código
- **Importante:** O placeholder usa 720x540 apenas como referência visual temporária. O asset final deve ser muito maior para parecer vitrine Apple-like.

## 2. creator-photo.webp
- **Dimensões sugeridas:** 600x600px (quadrado)
- **Formato:** WebP
- **Descrição:** Foto do criador Manoel Calaça Junior — natural, sem pose de guru
- **Uso:** Seção "Sobre o Criador" (seção 10)
- **Status atual:** Placeholder ativo no código

## 3. og-sos-telas.jpg
- **Dimensões sugeridas:** 1200x630px
- **Formato:** JPG
- **Descrição:** Imagem para Open Graph / compartilhamento em redes sociais
- **Uso:** Meta tag og:image
- **Status atual:** Referenciado no `<head>` mas não existe

---

## Instruções para substituir placeholders:

1. Adicione os arquivos reais nesta pasta `/assets`
2. No `index.html`, localize os comentários `<!-- PLACEHOLDER: -->`
3. Remova as `<div>` de placeholder
4. Descomente as tags `<img>` correspondentes

Exemplo para hero-object:
```html
<!-- Remova isto -->
<div class="w-full aspect-[4/3] bg-gradient-to-br ...">
  <span class="text-muted text-sm">Hero Object Image</span>
</div>

<!-- Descomente isto -->
<img src="/assets/hero-object.webp" alt="Kit SOS Telas Kids" class="w-full h-auto drop-shadow-2xl">
```

**Nota crítica sobre o hero-object:**
Quando o asset real for inserido, ele deve:
- Ocupar espaço dominante na hero (>60vw desktop)
- Ter fundo transparente real (não retangular)
- Parecer produto premium em vitrine, não screenshot de PDF
- Não ter bordas, cards ou molduras ao redor
