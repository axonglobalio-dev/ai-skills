# SOS Telas Kids — Documentação de Assets

## 📌 Pendências Oficiais

Os seguintes arquivos devem ser inseridos na pasta `/assets/` para produção final:

---

### 1. `hero-object.webp` (Objeto-Herói Principal)

**Dimensões:**
- Mínimo recomendado: **1600x1000px**
- Ideal: **2200x1400px**
- Proporção: ~16:10 ou 22:14

**Especificações Técnicas:**
- Formato: **WebP** ou **PNG** com fundo transparente real
- O fundo deve ser transparente para integração perfeita com o gradiente da hero
- Não usar bordas, sombras ou molduras na imagem (isso é feito via CSS)
- A imagem deve parecer uma vitrine de produto Apple-like

**Como Inserir:**
No arquivo `index.html`, localize o comentário `<!-- HERO ASSET FINAL: -->` e substitua o bloco `<div class="hero-placeholder">` por:

```html
<img
  src="./assets/hero-object.webp"
  alt="Kit digital SOS Telas Kids organizado em materiais de missão"
  class="hero-object-image w-full h-auto drop-shadow-2xl"
  width="2200"
  height="1400"
/>
```

---

### 2. `creator-photo.webp` (Foto do Criador)

**Dimensões:**
- Recomendado: **600x600px**
- Formato quadrado

**Especificações Técnicas:**
- Formato: **WebP** ou **JPG** de alta qualidade
- Foto natural, sem pose de guru ou aparência artificial
- Fundo neutro ou levemente desfocado
- Iluminação profissional mas acolhedora

**Como Inserir:**
No arquivo `index.html`, localize o comentário `<!-- CREATOR ASSET FINAL: -->` na seção "Sobre o Criador" e substitua o bloco placeholder por:

```html
<img
  src="./assets/creator-photo.webp"
  alt="Manoel Calaça Junior"
  class="w-full h-auto rounded-3xl shadow-lg"
  width="600"
  height="600"
/>
```

---

### 3. `og-sos-telas.jpg` (Open Graph Image)

**Dimensões:**
- Obrigatório: **1200x630px**
- Proporção: 1.91:1 (padrão Open Graph)

**Especificações Técnicas:**
- Formato: **JPG** ou **PNG**
- Deve incluir o título "SOS Telas Kids" e uma prévia visual do produto
- Usar para compartilhamento em redes sociais (Facebook, LinkedIn, WhatsApp)

**Onde é Usado:**
Este arquivo é referenciado no `<head>` do HTML:
```html
<meta property="og:image" content="./assets/og-sos-telas.jpg">
```

---

## 📁 Estrutura Final da Pasta `/assets/`

```
/assets/
├── hero-object.webp      (1600x1000px mínimo, ideal 2200x1400px)
├── creator-photo.webp    (600x600px)
└── og-sos-telas.jpg      (1200x630px)
```

---

## ⚠️ Importante

- Os placeholders atuais são elegantes e não quebram o layout
- A landing está **pronta para produção** mesmo sem os assets reais
- Quando os assets forem inseridos, a troca é mínima (apenas substituir um bloco HTML)
- Não use imagens externas, aleatórias ou geradas por IA para os assets finais

---

## ✅ Checklist de Validação Após Inserção

- [ ] `hero-object.webp` inserido e com fundo transparente
- [ ] `creator-photo.webp` inserido e com aparência natural
- [ ] `og-sos-telas.jpg` inserido com dimensões corretas
- [ ] Todas as imagens carregam sem erro no console
- [ ] Hero não quebra em mobile após inserção do asset real
- [ ] Foto do criador não distorce em diferentes telas
