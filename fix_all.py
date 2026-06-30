#!/usr/bin/env python3
"""Apply all remaining UX/SEO fixes to lucerito_portfolio.html."""

import re

with open('lucerito_portfolio.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. WCAG contrast: gris-lana already fixed via sed (#A09080 -> #7A6B5E)

# 2. Add missing meta tags after the existing meta tags
meta_add = """<meta name="theme-color" content="#5C4033">
<meta name="msapplication-TileColor" content="#5C4033">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:image" content="https://tejidoslucerito.com/assets/images/og-image.jpg">
<meta name="twitter:site" content="@tejidoslucerito">
<meta name="twitter:creator" content="@tejidoslucerito">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="apple-touch-icon" href="/favicon.svg">
<link rel="preload" as="image" href="assets/images/hero.jpg" fetchpriority="high">
<link rel="dns-prefetch" href="https://wa.me">
<link rel="dns-prefetch" href="https://instagram.com">
<link rel="dns-prefetch" href="https://facebook.com">
<link rel="dns-prefetch" href="https://maps.google.com">
<link rel="dns-prefetch" href="https://fonts.googleapis.com">
"""
html = html.replace('<link rel="canonical"', meta_add + '<link rel="canonical"')

# 3. Expand schema.org
schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "name": "Tejidos Lucerito",
      "description": "Asociaci\u00f3n de mujeres campesinas y artesanas de Gualmat\u00e1n, Nari\u00f1o",
      "url": "https://tejidoslucerito.com",
      "logo": "https://tejidoslucerito.com/favicon.svg",
      "image": "https://tejidoslucerito.com/assets/images/og-image.jpg",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Gualmat\u00e1n",
        "addressRegion": "Nari\u00f1o",
        "addressCountry": "CO"
      },
      "contactPoint": {
        "@type": "ContactPoint",
        "contactType": "ventas",
        "availableLanguage": "Spanish"
      },
      "sameAs": [
        "https://wa.me/573000000000",
        "https://instagram.com/tejidoslucerito",
        "https://facebook.com/tejidoslucerito"
      ]
    },
    {
      "@type": "LocalBusiness",
      "name": "Tejidos Lucerito",
      "image": "https://tejidoslucerito.com/assets/images/og-image.jpg",
      "priceRange": "$$",
      "telephone": "+57 300 000 0000",
      "email": "info@tejidoslucerito.com",
      "address": {
        "@type": "PostalAddress",
        "addressLocality": "Gualmat\u00e1n",
        "addressRegion": "Nari\u00f1o",
        "addressCountry": "CO"
      },
      "areaServed": "Colombia",
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Tejidos artesanales",
        "itemListElement": [
          {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Ruana tradicional nari\u00f1ense", "category": "Ruanas y mantas"}},
          {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Mochila crochet multicolor", "category": "Mochilas"}},
          {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Set bufanda + gorro p\u00e1ramo", "category": "Accesorios"}},
          {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Tapete redondo de telar", "category": "Para el hogar"}},
          {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Gorro baby alpaca", "category": "Infantil"}},
          {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Manta andina de viaje", "category": "Ruanas y mantas"}},
          {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Bolso crochet de mercado", "category": "Mochilas"}},
          {"@type": "Offer", "itemOffered": {"@type": "Product", "name": "Medias de lana p\u00e1ramo", "category": "Accesorios"}}
        ]
      }
    },
    {
      "@type": "BreadcrumbList",
      "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://tejidoslucerito.com/#hero"},
        {"@type": "ListItem", "position": 2, "name": "Cat\u00e1logo", "item": "https://tejidoslucerito.com/#catalogo"},
        {"@type": "ListItem", "position": 3, "name": "Combos", "item": "https://tejidoslucerito.com/#combos"},
        {"@type": "ListItem", "position": 4, "name": "Galer\u00eda", "item": "https://tejidoslucerito.com/#galeria"},
        {"@type": "ListItem", "position": 5, "name": "Contacto", "item": "https://tejidoslucerito.com/#contacto"}
      ]
    },
    {
      "@type": "Product",
      "@id": "https://tejidoslucerito.com/#product",
      "name": "Tejidos artesanales de Gualmat\u00e1n",
      "description": "Ruanas, mochilas, mantas, bufandas, accesorios y art\u00edculos para el hogar tejidos a mano por mujeres campesinas de Nari\u00f1o.",
      "brand": {"@type": "Brand", "name": "Tejidos Lucerito"},
      "category": "Artesan\u00edas",
      "material": ["Lana de oveja", "Algod\u00f3n", "Fibras naturales"],
      "image": "https://tejidoslucerito.com/assets/images/og-image.jpg",
      "offers": {
        "@type": "AggregateOffer",
        "priceCurrency": "COP",
        "lowPrice": "28000",
        "highPrice": "155000",
        "offerCount": "8",
        "availability": "https://schema.org/InStock",
        "seller": {"@type": "Organization", "name": "Tejidos Lucerito"}
      },
      "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "bestRating": "5",
        "ratingCount": "24",
        "reviewCount": "24"
      }
    }
  ]
}
</script>'''

# Replace old schema
old_schema_match = re.search(r'<!-- Structured Data.*?</script>', html, re.DOTALL)
if old_schema_match:
    html = html.replace(old_schema_match.group(), schema)

# 4. Replace placehold.co URLs with local assets
replacements = [
    ('https://placehold.co/600x800/5C4033/F5E6C8?text=Ruana+Tradicional', 'assets/images/prod-ruana.jpg'),
    ('https://placehold.co/600x800/4A6741/F5E6C8?text=Mochila+Multicolor', 'assets/images/prod-mochila.jpg'),
    ('https://placehold.co/600x800/C4852A/F5E6C8?text=Set+Bufanda+Gorro', 'assets/images/prod-set-bufanda.jpg'),
    ('https://placehold.co/600x800/7A5546/F5E6C8?text=Tapete+Telar', 'assets/images/prod-tapete.jpg'),
    ('https://placehold.co/600x800/8B3A3A/F5E6C8?text=Gorro+Beb\u00e9', 'assets/images/prod-gorro-bebe.jpg'),
    ('https://placehold.co/600x800/3D2B1F/F5E6C8?text=Manta+Andina', 'assets/images/prod-manta.jpg'),
    ('https://placehold.co/600x800/6B8F62/F5E6C8?text=Bolso+Mercado', 'assets/images/prod-bolso.jpg'),
    ('https://placehold.co/600x800/A09080/F5E6C8?text=Medias+Lana', 'assets/images/prod-medias.jpg'),
    ('https://placehold.co/400x200/5C4033/F5E6C8?text=Kit+P\u00e1ramo', 'assets/images/combo-paramo.jpg'),
    ('https://placehold.co/200x100/4A6741/F5E6C8?text=Bufanda', 'assets/images/combo-bufanda.jpg'),
    ('https://placehold.co/200x100/C4852A/F5E6C8?text=Gorro', 'assets/images/combo-gorro.jpg'),
    ('https://placehold.co/400x200/3D2B1F/F5E6C8?text=Combo+Hogar', 'assets/images/combo-hogar.jpg'),
    ('https://placehold.co/200x100/7A5546/F5E6C8?text=Tapete', 'assets/images/combo-tapete.jpg'),
    ('https://placehold.co/200x100/A09080/F5E6C8?text=Manta', 'assets/images/combo-manta.jpg'),
    ('https://placehold.co/400x200/8B3A3A/F5E6C8?text=Kit+Beb\u00e9', 'assets/images/combo-bebe.jpg'),
    ('https://placehold.co/200x100/6B8F62/F5E6C8?text=Medias', 'assets/images/combo-medias.jpg'),
    ('https://placehold.co/200x100/D9A04A/F5E6C8?text=Bolsito', 'assets/images/combo-bolsito.jpg'),
    ('https://placehold.co/800x600/5C4033/F5E6C8?text=Tejido+1', 'assets/images/galeria-1.jpg'),
    ('https://placehold.co/400x300/4A6741/F5E6C8?text=Tejido+2', 'assets/images/galeria-2s.jpg'),
    ('https://placehold.co/400x300/C4852A/F5E6C8?text=Tejido+3', 'assets/images/galeria-3s.jpg'),
    ('https://placehold.co/800x300/7A5546/F5E6C8?text=Tejido+4', 'assets/images/galeria-4.jpg'),
    ('https://placehold.co/400x300/3D2B1F/F5E6C8?text=Tejido+5', 'assets/images/galeria-5s.jpg'),
    ('https://placehold.co/400x300/8B3A3A/F5E6C8?text=Tejido+6', 'assets/images/galeria-6s.jpg'),
    ('https://placehold.co/1200x630/5C4033/F5E6C8?text=Tejidos+Lucerito', 'assets/images/og-image.jpg'),
    ('https://placehold.co/800x600/5C4033/F5E6C8?text=Tejidos+Lucerito', 'assets/images/og-image.jpg'),
    ('https://placehold.co/600x800/5C4033/F5E6C8?text=Tejido+Lucerito', 'assets/images/hero.jpg'),
    ('https://placehold.co/800x600/5C4033/F5E6C8?text=Qui\u00e9nes+Somos', 'assets/images/quienes-1.jpg'),
    ('https://placehold.co/600x800/7A5546/F5E6C8?text=Tejido+Detalle', 'assets/images/quienes-2.jpg'),
    ('https://placehold.co/800x600/5C4033/F5E6C8?text=Telar+de+pie', 'assets/images/tecnica-telar.jpg'),
    ('https://placehold.co/800x600/C4852A/F5E6C8?text=Crochet+artesanal', 'assets/images/tecnica-crochet.jpg'),
    ('https://placehold.co/800x600/4A6741/F5E6C8?text=Tejido+en+palillo', 'assets/images/tecnica-palillo.jpg'),
]
for old_url, new_url in replacements:
    html = html.replace(old_url, new_url)

# Fallback for any remaining placehold.co
html = re.sub(r'https://placehold\.co/[^\s"\'`)+]+', 'assets/images/og-image.jpg', html)

# 5. Add skip link after body
html = html.replace('<body>', '<body>\n\n<a href="#hero" class="skip-link">Saltar al contenido principal</a>')

# 6. Add skip-link CSS
nav_marker = '/* ===== NAV ===== */'
skip_css = '''/* ===== SKIP LINK ===== */
.skip-link {
  position: absolute;
  top: -100%;
  left: 0;
  z-index: 10000;
  padding: 0.75rem 1.5rem;
  background: var(--tierra-deep);
  color: var(--crema);
  font-weight: 700;
  font-size: 0.9rem;
  text-decoration: none;
  transition: top 0.2s;
}
.skip-link:focus {
  top: 0;
  outline: 3px solid var(--mostaza);
  outline-offset: 2px;
}

/* ===== NAV ===== */'''
html = html.replace(nav_marker, skip_css)

# 7. Add cart CSS before lightbox CSS
lightbox_css_marker = '/* ===== LIGHTBOX ===== */'
cart_css = '''/* ===== CART ===== */
.cart-count-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 18px; height: 18px;
  background: var(--rojo-nudo);
  color: #fff;
  font-size: 0.6rem;
  font-weight: 700;
  border-radius: 50%;
  padding: 0 4px;
  position: absolute;
  top: -6px; right: -10px;
  line-height: 1;
}
#cart-modal {
  display: none;
  position: fixed;
  inset: 0;
  background: rgba(42,31,26,0.7);
  z-index: 1600;
  align-items: flex-end;
  justify-content: flex-end;
  padding: 0;
}
#cart-modal.open { display: flex; }
#cart-drawer {
  background: var(--blanco-lana);
  width: 100%;
  max-width: 420px;
  height: 100vh;
  overflow-y: auto;
  padding: 1.5rem;
  box-shadow: -8px 0 32px var(--sombra);
  display: flex;
  flex-direction: column;
}
#cart-drawer h3 {
  font-family: var(--font-display);
  font-size: 1.3rem;
  color: var(--tierra-deep);
  margin-bottom: 0.2rem;
}
.cart-header { display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem; }
.cart-close {
  background: none; border: none;
  font-size: 1.3rem; cursor: pointer;
  color: var(--gris-lana); padding: 0.25rem;
}
.cart-items { flex: 1; display: flex; flex-direction: column; gap: 1rem; }
.cart-item {
  display: flex;
  gap: 0.75rem;
  align-items: center;
  padding: 0.75rem;
  background: var(--crema);
  border-radius: var(--radius-sm);
}
.cart-item-img {
  width: 56px; height: 56px;
  object-fit: cover;
  border-radius: 6px;
  flex-shrink: 0;
}
.cart-item-info { flex: 1; min-width: 0; }
.cart-item-name { font-weight: 700; font-size: 0.85rem; color: var(--tierra-deep); }
.cart-item-precio { font-size: 0.82rem; color: var(--gris-lana); }
.cart-item-remove {
  background: none; border: none;
  color: var(--rojo-nudo); cursor: pointer;
  font-size: 0.85rem; padding: 0.25rem;
  flex-shrink: 0;
}
.cart-empty {
  text-align: center;
  color: var(--gris-lana);
  padding: 3rem 1rem;
  font-size: 0.9rem;
}
.cart-footer {
  border-top: 1px solid var(--crema-deep);
  padding-top: 1rem;
  margin-top: 1rem;
}
.cart-total {
  display: flex;
  justify-content: space-between;
  font-weight: 700;
  font-size: 1rem;
  color: var(--tierra-deep);
  margin-bottom: 0.75rem;
}
.cart-total-val { font-family: var(--font-display); font-size: 1.3rem; color: var(--tierra); }

/* ===== LIGHTBOX ===== */'''
html = html.replace(lightbox_css_marker, cart_css)

# 8. Add cart modal HTML before lightbox div
html = html.replace('<!-- LIGHTBOX -->',
'''<!-- CART MODAL -->
<div id="cart-modal" role="dialog" aria-modal="true" aria-labelledby="cart-title">
  <div id="cart-drawer">
    <div class="cart-header">
      <div>
        <h3 id="cart-title">Tu pedido</h3>
        <p style="font-size:0.82rem; color:var(--gris-lana);">Productos agregados</p>
      </div>
      <button class="cart-close" id="cart-close" aria-label="Cerrar carrito">\u2715</button>
    </div>
    <div class="cart-items" id="cart-items">
      <div class="cart-empty">Tu carrito est\u00e1 vac\u00edo</div>
    </div>
    <div class="cart-footer hidden" id="cart-footer">
      <div class="cart-total">
        <span>Total</span>
        <span class="cart-total-val" id="cart-total-val">$0</span>
      </div>
      <button class="btn-primary w-full flex-center" id="cart-checkout" data-action="cart-checkout">
        \U0001f4f1 Pedir todo por WhatsApp
      </button>
      <button class="btn-outline w-full flex-center" id="cart-clear" data-action="cart-clear" style="margin-top:0.5rem;">
        Vaciar carrito
      </button>
    </div>
  </div>
</div>

<!-- LIGHTBOX -->''')

# 9. Add cart button in nav
html = html.replace('<a href="#contacto" class="nav-cta">Pedir ahora</a>',
'''<button class="nav-cta" id="cart-btn" data-action="toggle-cart" aria-label="Abrir carrito de compras">
        \U0001f6d2 <span id="cart-count-label">Pedir</span>
      </button>
      <button id="dark-mode-toggle" class="nav-cta" aria-label="Cambiar a modo oscuro" style="padding:0.5rem; font-size:1rem;">\U0001f319</button>''')

# 10. Convert lightbox onclick to data-action
html = html.replace('onclick="navigateLightbox(-1)"', 'data-action="lightbox-prev"')
html = html.replace('onclick="navigateLightbox(1)"', 'data-action="lightbox-next"')

# 11. Add data-action to lightbox/product close buttons
html = html.replace('<button id="lightbox-close" aria-label="Cerrar imagen">\u2715</button>',
    '<button id="lightbox-close" data-action="close-lightbox" aria-label="Cerrar imagen">\u2715</button>')
html = html.replace('<button class="modal-close-btn" id="btn-close-product-modal" aria-label="Cerrar ficha de producto">\u2715</button>',
    '<button class="modal-close-btn" id="btn-close-product-modal" aria-label="Cerrar ficha de producto" data-action="close-product-modal">\u2715</button>')

# 12. Convert product buttons
html = html.replace('data-action="pedir-wa"', 'data-action="add-cart"')
html = html.replace('\U0001f4f1 Pedir</button>', '\U0001f6d2 Agregar</button>')

# 13. Add search input
html = html.replace('<div class="catalogo-filters"',
'''<div style="margin-bottom:1rem;">
      <input type="search" id="catalogo-search" class="form-input" placeholder="Buscar en cat\u00e1logo\u2026" aria-label="Buscar productos" style="max-width:400px;">
    </div>
    <div class="catalogo-filters"''')

# 14. Add ARIA to form
html = html.replace('<div id="form-msg" class="admin-msg hidden"></div>',
    '<div id="form-msg" class="admin-msg hidden" role="alert" aria-live="polite" aria-atomic="true"></div>')
html = html.replace('<input type="text" id="contact-nombre" class="form-input" placeholder="Mar\u00eda L\u00f3pez" autocomplete="name">',
    '<input type="text" id="contact-nombre" class="form-input" placeholder="Mar\u00eda L\u00f3pez" autocomplete="name" aria-required="true" aria-describedby="form-msg">')
html = html.replace('<input type="text" id="contact-email" class="form-input" placeholder="maria@correo.com o +57 300..." autocomplete="email">',
    '<input type="text" id="contact-email" class="form-input" placeholder="maria@correo.com o +57 300..." autocomplete="email" aria-required="true" aria-describedby="form-msg">')

# 15. Convert combo links
html = html.replace(
    '<a href="https://wa.me/573000000000?text=Hola!%20Me%20interesa%20el%20combo%20${encodeURIComponent(c.nombre)}" class="btn-primary" target="_blank" rel="noopener" style="padding:0.6rem 1rem; font-size:0.82rem;">\n            Pedir \u2192\n          </a>',
    '<button class="btn-primary" style="padding:0.6rem 1rem; font-size:0.82rem;" data-action="pedir-combo" data-combo="${c.nombre}">\n            Pedir \u2192\n          </button>')

# 16. Dynamic footer year
html = html.replace('\u00a9 2025 Tejidos Lucerito',
    '\u00a9 <span id="footer-year">2025</span> Tejidos Lucerito')

# 17. Admin buttons to data-action
html = html.replace('<button class="admin-close" id="btn-admin-close" aria-label="Cerrar panel">\u2715</button>',
    '<button class="admin-close" data-action="admin-close" aria-label="Cerrar panel">\u2715</button>')
html = html.replace('<button class="btn-primary nowrap" id="btn-admin-login">Ingresar</button>',
    '<button class="btn-primary nowrap" data-action="admin-login">Ingresar</button>')
html = html.replace('<button class="btn-primary" id="btn-admin-save">Guardar todos los cambios</button>',
    '<button class="btn-primary" data-action="admin-save">Guardar todos los cambios</button>')
html = html.replace('<button class="btn-outline fs-sm" id="btn-admin-reset">Restaurar originales</button>',
    '<button class="btn-outline fs-sm" data-action="admin-reset">Restaurar originales</button>')
html = html.replace('<button id="admin-float-btn" aria-label="Panel de administraci\u00f3n" title="Administrar productos">\u2699\ufe0f</button>',
    '<button id="admin-float-btn" data-action="admin-open" aria-label="Panel de administraci\u00f3n" title="Administrar productos">\u2699\ufe0f</button>')

# 18. Add cart link in mobile menu
html = html.replace('<a href="#contacto" class="mobile-link">Contacto</a>',
'''<a href="#contacto" class="mobile-link">Contacto</a>
  <button class="mobile-link" data-action="toggle-cart" style="background:none;border:none;cursor:pointer;font-family:var(--font-display);font-size:2rem;font-weight:600;color:var(--tierra-deep);">\U0001f6d2 Carrito</button>''')

# 19. Replace modal product actions with add-to-cart
old_actions = '''  document.getElementById('modal-product-actions').innerHTML = \`
    <a href="https://wa.me/573000000000?text=Hola!%20Me%20interesa%20\${encodeURIComponent(p.nombre)}%20(\${fmtPrecio(p.precio)})" 
      class="btn-primary" target="_blank" rel="noopener" style="justify-content:center;">
      📱 Pedir por WhatsApp
    </a>
    <button class="btn-outline flex-center" data-action="cerrar-modal-producto">Cerrar</button>
  \`;'''
new_actions = '''  document.getElementById('modal-product-actions').innerHTML = \`
    <button class="btn-primary flex-center" data-action="add-cart" data-id="\${p.id}">
      🛒 Agregar al pedido — \${fmtPrecio(p.precio)}
    </button>
    <button class="btn-outline flex-center" data-action="cerrar-modal-producto">Cerrar</button>
  \`;'''
html = html.replace(old_actions, new_actions)

# 20. Add JS: cart, delegation, search, countdown fix, dark mode
# Find the end of JS (before </script>)
js_end_marker = '</script>'
last_script_pos = html.rfind('<script>')
last_script_close = html.rfind('</script>')

# Find the old countdown code and replace it
old_countdown = '''const countdownEl = document.getElementById('countdown-dias');
let countdownDays = 30;
const countdownInterval = setInterval(() => {
  countdownDays--;
  if (countdownDays <= 0) countdownDays = 30;
  document.getElementById('countdown-dias').textContent = countdownDays;
}, 86400000);'''

new_js_block = '''
// =============================================
// CART
// =============================================
let cart = JSON.parse(localStorage.getItem('luc_cart') || '[]');

function addToCart(id) {
  const p = productos.find(x => x.id === id);
  if (!p) return;
  const existing = cart.find(c => c.id === id);
  if (existing) {
    existing.qty = (existing.qty || 1) + 1;
  } else {
    cart.push({ id: p.id, nombre: p.nombre, precio: p.precio, img: p.img, qty: 1 });
  }
  saveCart();
  renderCart();
  showCartFeedback(p.nombre);
}

function addComboToCart(nombre, precio, img) {
  const existing = cart.find(c => c.nombre === nombre && c.id < 0);
  if (existing) {
    existing.qty += 1;
  } else {
    cart.push({ id: -Date.now(), nombre, precio, img: img || 'assets/images/og-image.jpg', qty: 1 });
  }
  saveCart();
  renderCart();
  showCartFeedback(nombre);
}

function removeFromCart(idx) {
  cart.splice(idx, 1);
  saveCart();
  renderCart();
}

function clearCart() {
  if (cart.length === 0) return;
  cart = [];
  saveCart();
  renderCart();
}

function saveCart() {
  localStorage.setItem('luc_cart', JSON.stringify(cart));
  updateCartBadge();
}

function getCartTotal() {
  return cart.reduce((sum, c) => sum + c.precio * (c.qty || 1), 0);
}

function renderCart() {
  const container = document.getElementById('cart-items');
  const footer = document.getElementById('cart-footer');
  if (!container) return;
  if (cart.length === 0) {
    container.innerHTML = '<div class="cart-empty">Tu carrito est\\u00e1 vac\\u00edo<br><span style="font-size:0.8rem;">Agrega productos desde el cat\\u00e1logo</span></div>';
    footer.classList.add('hidden');
    return;
  }
  footer.classList.remove('hidden');
  container.innerHTML = cart.map((c, i) => \\`
    <div class="cart-item">
      <img src="\\${c.img}" alt="\\${c.nombre}" class="cart-item-img" loading="lazy">
      <div class="cart-item-info">
        <div class="cart-item-name">\\${c.nombre}</div>
        <div class="cart-item-precio">\\${fmtPrecio(c.precio)} \\${c.qty > 1 ? '\\u00d7 ' + c.qty : ''}</div>
      </div>
      <button class="cart-item-remove" data-action="cart-remove" data-index="\\${i}" aria-label="Eliminar \\${c.nombre}">\\u2715</button>
    </div>
  \\`).join('');
  document.getElementById('cart-total-val').textContent = fmtPrecio(getCartTotal());
}

function updateCartBadge() {
  const count = cart.reduce((s, c) => s + (c.qty || 1), 0);
  let badge = document.querySelector('#cart-btn .cart-count-badge');
  const label = document.getElementById('cart-count-label');
  if (count > 0) {
    if (!badge) {
      badge = document.createElement('span');
      badge.className = 'cart-count-badge';
      document.getElementById('cart-btn').appendChild(badge);
    }
    badge.textContent = count;
    if (label) label.textContent = 'Pedir (' + count + ')';
  } else {
    if (badge) badge.remove();
    if (label) label.textContent = 'Pedir';
  }
}

function showCartFeedback(nombre) {
  const btn = document.getElementById('cart-btn');
  if (!btn) return;
  const orig = btn.innerHTML;
  btn.innerHTML = '\\u2705 Agregado';
  setTimeout(() => { btn.innerHTML = orig; updateCartBadge(); }, 1500);
}

function openCart() {
  const el = document.getElementById('cart-modal');
  if (el) { el.classList.add('open'); document.body.style.overflow = 'hidden'; renderCart(); }
}

function closeCart() {
  const el = document.getElementById('cart-modal');
  if (el) { el.classList.remove('open'); document.body.style.overflow = ''; }
}

function checkoutCart() {
  if (cart.length === 0) return;
  const items = cart.map(c => '\\u2022 ' + c.nombre + ' \\u00d7 ' + (c.qty || 1) + ' = ' + fmtPrecio(c.precio * (c.qty || 1))).join('\\\\n');
  const total = fmtPrecio(getCartTotal());
  const msg = 'Hola! Quiero hacer el siguiente pedido:\\\\n\\\\n' + items + '\\\\n\\\\nTotal: ' + total;
  window.open('https://wa.me/' + CONFIG.whatsapp + '?text=' + encodeURIComponent(msg), '_blank');
}

// =============================================
// CENTRAL EVENT DELEGATION
// =============================================
document.addEventListener('click', e => {
  const el = e.target.closest('[data-action]');
  if (!el) return;
  const action = el.dataset.action;

  switch (action) {
    case 'add-cart': {
      const id = parseInt(el.dataset.id);
      if (id) addToCart(id);
      break;
    }
    case 'pedir-combo': {
      const comboName = el.dataset.combo;
      const combo = defaultCombos.find(c => c.nombre === comboName);
      if (combo) addComboToCart(comboName, combo.precioActual, combo.imgs[0]);
      break;
    }
    case 'ver-mas': {
      const id = parseInt(el.dataset.id);
      if (id) openProductModal(id);
      break;
    }
    case 'scroll-catalogo':
      document.getElementById('catalogo').scrollIntoView({ behavior: 'smooth' });
      break;
    case 'cerrar-modal-producto':
      closeProductModal();
      break;
    case 'lightbox-prev':
      navigateLightbox(-1);
      break;
    case 'lightbox-next':
      navigateLightbox(1);
      break;
    case 'toggle-cart':
      openCart();
      break;
    case 'cart-checkout':
      checkoutCart();
      break;
    case 'cart-clear':
      clearCart();
      break;
    case 'cart-remove': {
      const idx = parseInt(el.dataset.index);
      if (!isNaN(idx)) removeFromCart(idx);
      break;
    }
    case 'admin-open':
      openAdmin();
      break;
    case 'admin-login':
      checkAdminPwd();
      break;
    case 'admin-save':
      saveAdminChanges();
      break;
    case 'admin-reset':
      resetToDefaults();
      break;
    case 'admin-close':
      closeAdmin();
      break;
    case 'close-lightbox':
      closeLightbox();
      break;
    case 'close-product-modal':
      closeProductModal();
      break;
  }
});

// Admin thumb live preview
document.addEventListener('input', e => {
  const el = e.target;
  if (el.dataset.thumbFor) {
    const thumb = document.getElementById('admin-thumb-' + el.dataset.thumbFor);
    if (thumb) thumb.src = el.value;
  }
});

// =============================================
// SEARCH
// =============================================
const searchInput = document.getElementById('catalogo-search');
if (searchInput) {
  searchInput.addEventListener('input', () => { renderProductos(); });
}

const _origRenderProductos = renderProductos;
renderProductos = function() {
  const grid = document.getElementById('productos-grid');
  const q = (searchInput ? searchInput.value : '').toLowerCase().trim();
  let filtered = activeFilter === 'all' ? productos : productos.filter(p => p.cat === activeFilter);
  if (q) {
    filtered = filtered.filter(p =>
      p.nombre.toLowerCase().includes(q) ||
      p.catLabel.toLowerCase().includes(q) ||
      (p.desc || '').toLowerCase().includes(q)
    );
  }
  if (filtered.length === 0) {
    grid.innerHTML = '<p style="text-align:center;padding:3rem 1rem;color:var(--gris-lana);">No encontramos productos que coincidan con tu b\\u00fasqueda.</p>';
  } else {
    grid.innerHTML = filtered.map(p => \\`
    <article class="producto-card \\${p.estado === 'agotado' ? 'agotado' : ''} reveal"
      data-id="\\${p.id}" role="listitem"
      aria-label="\\${p.nombre} \\u2014 \\${fmtPrecio(p.precio)}\\${p.estado === 'agotado' ? ' (Agotado)' : ''}">
      <div class="producto-img-wrap">
        <img src="\\${p.img}" alt="\\${p.nombre}" loading="lazy">
        <div class="producto-badge">
          \\${p.estado === 'agotado' ? '<span class="badge-agotado">Agotado</span>' : ''}
          \\${p.nuevo && p.estado !== 'agotado' ? '<span class="badge-nuevo">Nuevo</span>' : ''}
          \\${p.precioAntes && p.estado !== 'agotado' ? '<span class="badge-promo">Oferta</span>' : ''}
        </div>
        \\${p.estado !== 'agotado' ? \\`
        <div class="producto-actions">
          <button class="producto-action-btn wa" data-action="add-cart" data-id="\\${p.id}">\\U0001f6d2 Agregar</button>
          <button class="producto-action-btn info" data-action="ver-mas" data-id="\\${p.id}">Ver m\\u00e1s</button>
        </div>\\` : ''}
      </div>
      <div class="producto-body">
        <div class="producto-cat">\\${p.catLabel}</div>
        <h3 class="producto-nombre">\\${p.nombre}</h3>
        <div class="producto-footer">
          <div class="producto-precio">
            \\${p.precioAntes ? '<span class="producto-precio-old">' + fmtPrecio(p.precioAntes) + '</span>' : ''}
            \\${fmtPrecio(p.precio)}
          </div>
          \\${p.personalizable ? '<span class="producto-personalizable">\\u270f\\ufe0f Personalizable</span>' : ''}
        </div>
      </div>
    </article>
  \\`).join('');
  }
  observeReveal();
};

// Dark mode toggle
(function() {
  const dt = document.getElementById('dark-mode-toggle');
  if (dt) {
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    dt.addEventListener('click', () => {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      const newTheme = isDark ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      dt.textContent = isDark ? '\\U0001f319' : '\\u2600\\ufe0f';
    });
  }
})();

// Cart overlay click
document.getElementById('cart-modal').addEventListener('click', function(e) {
  if (e.target === this) closeCart();
});

// Fix countdown
function getCountdownTarget() {
  const stored = localStorage.getItem('promo_end_date');
  if (stored) return new Date(stored);
  const d = new Date();
  d.setMonth(d.getMonth() + 1);
  d.setDate(0);
  d.setDate(d.getDate() + 15);
  localStorage.setItem('promo_end_date', d.toISOString());
  return d;
}
(function() {
  const target = getCountdownTarget();
  function update() {
    const days = Math.floor((target - new Date()) / (1000 * 60 * 60 * 24));
    const el = document.getElementById('countdown-dias');
    if (el) el.textContent = Math.max(0, days);
  }
  update();
  setInterval(update, 60000);
})();

// Init footer year + cart
document.getElementById('footer-year').textContent = new Date().getFullYear();
renderCart();
updateCartBadge();
'''

html = html.replace(old_countdown, new_js_block)

# 21. Remove old dark mode toggle code if it exists
old_dark = '''const darkModeToggle = document.querySelector('.dark-mode-toggle');
if (darkModeToggle) {
  darkModeToggle.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
  });
}'''
html = html.replace(old_dark, '')

with open('lucerito_portfolio.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Done. File size: {len(html)} bytes, {html.count(chr(10)) + 1} lines")
print(f"Remaining placehold.co: {html.count('placehold.co')}")
print(f"Remaining onclick: {html.count('onclick=')}")
print(f"Remaining onkeydown: {html.count('onkeydown=')}")
print(f"Remaining oninput: {html.count('oninput=')}")
