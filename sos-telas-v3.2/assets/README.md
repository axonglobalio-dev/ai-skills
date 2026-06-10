# Assets do SOS Telas Kids

Esta pasta contém os assets de imagem utilizados na landing page.

## Pendências Oficiais

Os seguintes assets devem ser inseridos antes da publicação:

### 1. hero-object.webp
**Local:** `/assets/hero-object.webp`

**Dimensões:**
- Mínimo recomendado: **1600x1000px**
- Ideal: **2200x1400px**

**Formato:** WebP ou PNG com fundo transparente real

**Uso:** Objeto-herói principal da seção Hero Showcase. Deve parecer uma vitrine de produto premium, sem moldura ou card ao redor.

**Substituição no código:**
No `index.html`, procure o comentário:
```html
<!-- Asset final: /assets/hero-object.webp -->
```
E substitua o placeholder pela tag `<img>` comentada.

---

### 2. creator-photo.webp
**Local:** `/assets/creator-photo.webp`

**Dimensões:** 600x600px

**Formato:** WebP ou JPG

**Uso:** Foto do criador (Manoel Calaça Junior) na seção "Sobre o Criador". Deve ser uma foto natural, sem pose de guru.

**Substituição no código:**
No `index.html`, procure o comentário:
```html
<!-- Asset final: /assets/creator-photo.webp -->
```
E substitua o placeholder pela tag `<img>` comentada.

---

### 3. og-sos-telas.jpg
**Local:** `/assets/og-sos-telas.jpg`

**Dimensões:** 1200x630px (padrão Open Graph)

**Formato:** JPG

**Uso:** Imagem para compartilhamento em redes sociais (Open Graph).

---

## Como Substituir os Placeholders

1. Adicione os arquivos reais nesta pasta `/assets`
2. No `index.html`, remova ou comente as divs de placeholder
3. Descomente as tags `<img>` correspondentes
4. Teste em desktop e mobile para garantir que o layout não quebre

## Notas Técnicas

- O placeholder atual do hero-object usa um gradiente elegante e não quebra o layout
- As dimensões recomendadas garantem qualidade em telas Retina/HiDPI
- Use compressão adequada para manter o carregamento rápido (idealmente <500KB por asset)
- Fundo transparente real significa sem bordas brancas ou artifacts ao redor do objeto
