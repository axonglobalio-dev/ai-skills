# REVISÃO V3.2 — CHECKLIST COMPLETO

## Arquivos

- [x] `index.html` atualizado com comentários de seção
- [x] `input.css` atualizado com containers corretos
- [x] `output.css` recompilado (23KB minificado)
- [x] `tailwind.config.js` preservado com paleta de cores
- [x] `package.json` criado com dependências
- [x] `postcss.config.js` configurado
- [x] `assets/README.md` atualizado com dimensões finais

## Stack Técnica

- [x] Sem React
- [x] Sem Vite
- [x] Sem Next.js
- [x] Sem TypeScript
- [x] Sem GSAP
- [x] Sem Framer Motion
- [x] Sem Tailwind CDN
- [x] HTML simples + Tailwind compilado
- [x] JavaScript mínimo apenas para FAQ e tracking

## Layout e Containers

- [x] `.content-container` = max-width 1120px
- [x] `.hero-container` = max-width 1440px
- [x] `.offer-container` = max-width 1280px
- [x] `.faq-container` = max-width 920px
- [x] `.reading-width` = max-width 720px
- [x] Seção 2 separa texto (720px) e cards (1120px) em wrappers diferentes
- [x] `section[id]` tem `scroll-margin-top: 96px`
- [x] Hero preparada para asset real (1600x1000px mínimo)

## Navegação e Âncoras

- [x] Programa → `#programa`
- [x] Método → `#metodo`
- [x] Oferta → `#oferta`
- [x] FAQ → `#faq`
- [x] Ver como funciona → `#como-funciona`
- [x] Sem `href="#"` em links de navegação
- [x] Links legais (Termos/Privacidade) com `aria-disabled="true"` e sem URL falsa
- [x] Nav com links desktop completos (Programa, Método, Oferta, FAQ)

## Tracking e Pixel

- [x] Pixel Facebook correto: `974940322122465`
- [x] Checkout Hotmart correto: `https://pay.hotmart.com/M105920942X`
- [x] Evento `PageView` implementado no head
- [x] Evento `ViewContent` ao scrollar para oferta
- [x] Evento `ClickCheckout` customizado no CTA
- [x] Função `handleCheckoutClick()` com delay de 300ms
- [x] Sem `InitiateCheckout` como substituto
- [x] Sem pixel antigo ou checkout antigo no código

## Copy e Estratégia

- [x] Sem promessa de "tela zero"
- [x] Sem acesso vitalício
- [x] Sem atualizações gratuitas
- [x] Sem desconto riscado ("de R$97 por R$27")
- [x] Sem bônus inventados
- [x] Sem depoimentos inventados
- [x] Sem autoridade inventada
- [x] Método EFM = Escolha, Faça, Marque
- [x] 8 entregáveis reais preservados
- [x] Acentuação revisada (mágica, Só, rápido, criança, missão, experiência, você, fácil, cartões, calendário, próxima ação, execução, segurança, possível, construção, observação, imaginação, família)
- [x] Tom humano, adulto, acolhedor, sem culpa

## Acessibilidade

- [x] FAQ com `aria-expanded` dinâmico
- [x] FAQ com `aria-controls` apontando para IDs únicos
- [x] Primeira pergunta do FAQ aberta por padrão
- [x] Foco visível com `:focus-visible`
- [x] Reduced motion via `@media (prefers-reduced-motion)`
- [x] Alt em imagens (placeholder e assets futuros)
- [x] Headings em ordem lógica (H1 → H2 → H3)
- [x] Contraste do botão: texto `#1D1D1F` no fundo `#EFA12A`
- [x] HTML semântico (nav, section, footer, article)

## Assets e Placeholders

- [x] `hero-object.webp` documentado como pendente (1600x1000px mínimo, 2200x1400px ideal)
- [x] `creator-photo.webp` documentado como pendente (600x600px)
- [x] `og-sos-telas.jpg` documentado como pendente (1200x630px)
- [x] Placeholder do hero não menciona "720x540"
- [x] Placeholder usa gradiente elegante e discreto
- [x] Código pronto para receber asset real com mínima alteração
- [x] Comentários claros indicando onde inserir cada asset

## Comentários no Código

- [x] Cada seção principal comentada no HTML com bloco delimitador
- [x] Comentários descrevem função de cada seção
- [x] Comentários não poluem excessivamente o arquivo
- [x] Assets futuros documentados com comentários inline

## Componentes e Estilo

- [x] Botão primário: laranja `#EFA12A` com texto escuro `#1D1D1F` (melhor contraste)
- [x] Botão secundário: branco com borda
- [x] Cards com respiro (padding 24-32px)
- [x] Oferta com visual premium (rounded-[2.5rem], shadow-xl)
- [x] FAQ accordion limpo e funcional
- [x] Nav solidifica ao scroll com `.nav-solid`
- [x] Mobile CTA sticky mais discreto (full-width, z-30)

## Responsividade

- [x] Validação mobile: 390px, 430px, 768px
- [x] Validação desktop: 1280px, 1440px, 1728px
- [x] Sem overflow horizontal
- [x] Hero com CTA visível antes da rolagem longa no mobile
- [x] Cards empilham corretamente no mobile
- [x] Oferta legível em todos os tamanhos
- [x] FAQ abre/fecha sem quebrar layout

## Estrutura das Seções (12 seções na ordem correta)

1. [x] Hero Showcase
2. [x] Consciência + Mágica Fora das Telas (`#programa`)
3. [x] O Sistema (`#como-funciona`)
4. [x] Três Portas
5. [x] Método EFM (`#metodo`)
6. [x] Exemplos Reais de Missões (`#missoes`)
7. [x] O Que Vem no Kit (`#kit`)
8. [x] Dobra de Decisão / Oferta (`#oferta`)
9. [x] Tranquilidade e Perguntas Silenciosas (`#tranquilidade`)
10. [x] Sobre o Criador (`#criador`)
11. [x] FAQ (`#faq`)
12. [x] CTA Final + Footer

---

## Resumo das Correções v3.2

| Item | Status | Observação |
|------|--------|------------|
| Containers corrigidos | ✅ | reading-width 720px, content-container 1120px |
| Seção 2 com wrappers separados | ✅ | Texto e cards em divs diferentes |
| Scroll margin top | ✅ | 96px em section[id] |
| IDs de navegação | ✅ | #programa, #metodo, #oferta, #faq |
| Nav desktop completa | ✅ | Links Programa, Método, Oferta, FAQ |
| Hero pronta para asset real | ✅ | Placeholder elegante, dimensões documentadas |
| CTA mobile sticky discreto | ✅ | Full-width, z-30, sem bloquear leitura |
| Contraste botão primário | ✅ | Texto #1D1D1F no fundo #EFA12A |
| CTAs com href + onclick | ✅ | Todos os botões de compra |
| ClickCheckout funcionando | ✅ | fbq('trackCustom', 'ClickCheckout', ...) |
| Links legais sem href falso | ✅ | aria-disabled="true" |
| Comentários de seção | ✅ | Todas as 12 seções comentadas |
| Acentuação revisada | ✅ | Português brasileiro correto |
| Assets documentados | ✅ | README atualizado com dimensões finais |

---

## Como Rodar Localmente

```bash
cd /workspace/sos-telas-v3.2

# Instalar dependências (se necessário)
npm install

# Recompilar CSS (se alterar input.css)
npx tailwindcss -i ./input.css -o ./output.css --minify

# Servir localmente
npx http-server -p 8080
```

Acesse: `http://localhost:8080`

---

## Pendências para Produção

1. **Inserir `/assets/hero-object.webp`** (1600x1000px mínimo, fundo transparente)
2. **Inserir `/assets/creator-photo.webp`** (600x600px, foto natural)
3. **Inserir `/assets/og-sos-telas.jpg`** (1200x630px, Open Graph)
4. **Criar páginas de Termos de Uso e Política de Privacidade** (ou remover links do footer)

---

## Critério de Aprovação

A v3.2 está aprovada se:

- [x] Mantiver disciplina técnica da v3.1
- [x] Estiver mais fácil de manter (comentários, estrutura clara)
- [x] Corrigir estrutura da Seção 2 (texto 720px + cards 1120px)
- [x] Deixar hero pronta para asset real
- [x] Melhorar acabamento visual sem inventar nada
- [x] Preservar todos os CTAs e tracking
- [x] Eliminar links falsos
- [x] Comentar cada seção
- [x] Continuar fiel ao Blueprint Master

**Status:** ✅ PRONTA PARA PRODUÇÃO (aguardando assets reais)
