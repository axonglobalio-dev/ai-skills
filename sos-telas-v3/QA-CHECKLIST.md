# CHECKLIST FINAL DE QA — LANDING SOS TELAS KIDS v3

## ✅ QA DE COPY

- [x] Não promete "tela zero" — Apenas menciona na seção de tranquilidade explicando que NÃO é essa a promessa
- [x] Não culpa os pais — Tom acolhedor, compreensivo, sem julgamento
- [x] Não inventa autoridade — Criador apresentado como pai real, não como especialista/guru
- [x] Não usa depoimentos inexistentes — Nenhum depoimento na página
- [x] Não usa comunidade inexistente — Nenhuma menção a grupo/comunidade
- [x] Não usa "bônus" — Entregáveis apresentados como "peças do sistema", não bônus
- [x] Não exagera promessa — Promessa correta: "tenha uma alternativa pronta"
- [x] Cada seção tem função clara — 12 seções com propósito definido
- [x] CTA é consistente — Todos usam "Quero começar hoje" ou variações coerentes

## ✅ QA VISUAL

- [x] Hero parece vitrine de produto — Objeto-herói dominante, palco visual full-width
- [x] Objeto-herói sem erro textual — Placeholder documentado aguardando asset real
- [x] Laranja não domina a página — Usado apenas em CTAs e detalhes de decisão
- [x] Verde aparece só como confirmação — Checks, microprovas, confirmações
- [x] Cards têm respiro — Padding generoso, spacing adequado
- [x] Oferta parece premium — Card branco com radius 36px, grid 58/42
- [x] FAQ está limpo — Accordion funcional, max-width 920px
- [x] Footer é discreto — Sem excesso de elementos
- [x] Não parece template — Design customizado Apple-like
- [x] Não parece infoproduto barato — Sem urgência falsa, contadores, selos genéricos

## ✅ QA TÉCNICO

- [x] Pixel correto: `974940322122465` — Presente no head e no script
- [x] Checkout correto: `https://pay.hotmart.com/M105920942X` — Todos os CTAs usam este link
- [x] Evento `PageView` — Implementado no head
- [x] Evento `ViewContent` — Implementado via scroll tracking na oferta
- [x] Evento `ClickCheckout` — Implementado na função handleCheckoutClick
- [x] Sem checkout antigo — Nenhum `C105595623Q` encontrado
- [x] Sem pixel antigo — Nenhum `932149439860105` encontrado
- [x] Sem `<base target="_blank">` — Não presente no código
- [x] Sem `href="#"` em CTAs — Todos links de checkout válidos, nav usa span, footer usa span para links placeholder
- [x] Tailwind CSS compilado — output.css gerado com sucesso (19KB minificado)
- [x] Cores da paleta presentes — #EFA12A (laranja) e #137A6A (verde) no CSS
- [x] Componentes obrigatórios criados — .content-container, .hero-container, .btn-primary, etc.
- [x] FAQ funcional — JavaScript de accordion implementado
- [x] Nav funcional — Solidifica ao scroll
- [x] Reduced motion — Suporte a prefers-reduced-motion implementado
- [x] Acessibilidade — aria-expanded, aria-controls, headings em ordem lógica
- [x] Responsividade — Classes md:, lg: para breakpoints

## 📁 ESTRUTURA DE ARQUIVOS ENTREGUE

```
/sos-telas-v3/
├── index.html          (54KB — Landing page completa)
├── input.css           (2.7KB — Configuração Tailwind + componentes)
├── output.css          (19KB — CSS compilado e minificado)
├── tailwind.config.js  (756B — Configuração Tailwind v3)
├── package.json        (117B — Dependências npm)
├── package-lock.json   (40KB — Lock file)
└── assets/
    └── README.md       (Documentação dos placeholders)
```

## ⚠️ OBSERVAÇÕES / PENDÊNCIAS

### Assets de Imagem (Placeholders Ativos)
Os seguintes arquivos devem ser adicionados na pasta `/assets`:

1. **hero-object.webp** (720x540px, fundo transparente)
   - Objeto-herói principal da landing
   - Placeholder ativo no código com div estilizada

2. **creator-photo.webp** (600x600px)
   - Foto do criador Manoel Calaça Junior
   - Placeholder ativo no código com div estilizada

3. **og-sos-telas.jpg** (1200x630px)
   - Imagem para Open Graph / redes sociais
   - Referenciada no meta tag og:image

### Links Placeholder no Footer
- Termos de Uso e Política de Privacidade estão como `<span>` (não clicáveis)
- Devem ser substituídos por `<a>` com URLs reais quando disponíveis

### Validação de Breakpoints
Recomenda-se testar manualmente em:
- Mobile: 390px, 430px, 768px
- Desktop: 1280px, 1440px, 1728px

### Performance
- CSS minificado: ~19KB
- HTML: ~54KB
- Total inicial: ~73KB (sem assets)
- Recomenda-se otimizar imagens WebP quando adicionadas

---

## CRITÉRIO FINAL DE APROVAÇÃO

A landing foi construída para que o visitante sinta:

✅ Isso é simples.  
✅ Isso é bonito.  
✅ Isso foi pensado.  
✅ Isso cabe na minha rotina.  
✅ Isso não me culpa.  
✅ Isso pode ajudar hoje.  
✅ R$27 faz sentido.

**Status:** PRONTA PARA PRODUÇÃO (aguardando assets de imagem)
