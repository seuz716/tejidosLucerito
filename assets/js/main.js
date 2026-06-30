// =============================================
// DATA — reemplaza los src de imagen con tus links de nube
// =============================================
const ADMIN_PASSWORD = 'lucerito2025'; // Cambia esto

// CONFIG — Actualiza estos valores con tus datos reales
const CONFIG = {
  whatsapp: '573000000000', // Sin + ni espacios
  instagram: 'tejidoslucerito',
  facebook: 'tejidoslucerito',
  email: 'info@tejidoslucerito.com',
  direccion: 'Gualmatán, Nariño, Colombia'
};

function getWhatsAppLink(text = '') {
  return `https://wa.me/${CONFIG.whatsapp}${text ? '?text=' + encodeURIComponent(text) : ''}`;
}

function getRandomImg() {
  const imgs = document.querySelectorAll('img[data-random]');
  imgs.forEach(img => {
    const randomIndex = Math.floor(Math.random() * galeriaImgs.length);
    img.src = galeriaImgs[randomIndex].src;
    img.alt = galeriaImgs[randomIndex].alt;
  });
}

const defaultProductos = [
  {
    id: 1, cat: 'ruanas', catLabel: 'Ruanas y mantas',
    nombre: 'Ruana tradicional nariñense',
    precio: 95000, precioAntes: null,
    estado: 'disponible', nuevo: true,
    personalizable: true,
    img: 'images/-j2HIgfU.jpeg',
    desc: 'Tejida en telar de pie con lana de oveja 100% natural. Gruesa, cálida, impermeable. Disponible en colores tierra, negro, gris páramo y burdeos.',
    detalles: { Material: 'Lana de oveja 100%', Técnica: 'Telar de pie', Tiempo: '4-6 días', Tallas: 'S, M, L, XL', Cuidado: 'Lavado a mano agua fría' }
  },
  {
    id: 2, cat: 'mochilas', catLabel: 'Mochilas',
    nombre: 'Mochila crochet multicolor',
    precio: 75000, precioAntes: 90000,
    estado: 'disponible', nuevo: false,
    personalizable: true,
    img: 'images/2cIkc2C-.jpeg',
    desc: 'Crochet elaborado con hilo grueso de algodón. Colores basados en la paleta nariñense. Cierre de botón artesanal y correa ajustable.',
    detalles: { Material: 'Hilo algodón', Técnica: 'Crochet', Tiempo: '3-5 días', Capacidad: '8 litros aprox.', Cuidado: 'Lavado suave a mano' }
  },
  {
    id: 3, cat: 'accesorios', catLabel: 'Accesorios',
    nombre: 'Set bufanda + gorro páramo',
    precio: 55000, precioAntes: null,
    estado: 'disponible', nuevo: true,
    personalizable: true,
    img: 'images/2fVInDbL.jpeg',
    desc: 'Set combinado tejido en palillo con lana virgen. La bufanda mide 160cm y el gorro viene en talla única con dobladillo ajustable.',
    detalles: { Material: 'Lana virgen', Técnica: 'Palillo / agujas', Tiempo: '2-3 días', Colores: '8 combinaciones disponibles', Cuidado: 'Lavado a mano' }
  },
  {
    id: 4, cat: 'hogar', catLabel: 'Para el hogar',
    nombre: 'Tapete redondo de telar',
    precio: 85000, precioAntes: null,
    estado: 'disponible', nuevo: false,
    personalizable: false,
    img: 'images/4S6Q7ukd.jpeg',
    desc: 'Tejido en telar con hilo de yute y lana reciclada. Diámetro 80cm. Ideal para sala o comedor. Cada uno es diferente, no hay dos iguales.',
    detalles: { Material: 'Yute + lana reciclada', Técnica: 'Telar de pie', Dimensión: '80 cm diámetro', Tiempo: '5-7 días', Cuidado: 'Sacudir, no lavar' }
  },
  {
    id: 5, cat: 'infantil', catLabel: 'Infantil',
    nombre: 'Gorro baby alpaca',
    precio: 35000, precioAntes: null,
    estado: 'disponible', nuevo: false,
    personalizable: true,
    img: 'images/5d1kL5l1.jpeg',
    desc: 'Suave, hipoalergénico, perfecto para recién nacidos y bebés hasta 18 meses. Disponible en varios colores pastel y con borla opcional.',
    detalles: { Material: 'Hilo algodón baby', Técnica: 'Palillo', Tallas: '0-6m, 6-12m, 12-18m', Tiempo: '1-2 días', Cuidado: 'Lavado delicado 30°' }
  },
  {
    id: 6, cat: 'ruanas', catLabel: 'Ruanas y mantas',
    nombre: 'Manta andina de viaje',
    precio: 120000, precioAntes: 145000,
    estado: 'disponible', nuevo: false,
    personalizable: false,
    img: 'images/8CkPeEn0.jpeg',
    desc: 'Grande, versátil y abrigadora. Úsala como ruana, manta de sofá o colcha ligera. Tejida en telar con lana mezclada, diseño geométrico nariñense.',
    detalles: { Material: 'Lana mezclada', Técnica: 'Telar de pie', Dimensión: '180x140 cm', Tiempo: '7-10 días', Cuidado: 'Lavado a mano agua tibia' }
  },
  {
    id: 7, cat: 'mochilas', catLabel: 'Mochilas',
    nombre: 'Bolso crochet de mercado',
    precio: 48000, precioAntes: null,
    estado: 'disponible', nuevo: false,
    personalizable: true,
    img: 'images/ABO_xAJ3.jpeg',
    desc: 'Abierto, resistente, ideal para mercado o playa. Tejido en macramé y crochet con hilo de algodón grueso. Se dobla y cabe en el bolsillo.',
    detalles: { Material: 'Algodón grueso', Técnica: 'Crochet + macramé', Tiempo: '2-3 días', Colores: '6 opciones', Cuidado: 'Lavado a mano' }
  },
  {
    id: 8, cat: 'accesorios', catLabel: 'Accesorios',
    nombre: 'Medias de lana páramo',
    precio: 28000, precioAntes: null,
    estado: 'agotado', nuevo: false,
    personalizable: false,
    img: 'images/D0oMSe5d.jpeg',
    desc: 'Tejidas en palillo con lana virgen nariñense. Gruesas, sin costuras, perfectas para el frío. Disponibles en talla S-M y M-L.',
    detalles: { Material: 'Lana virgen', Técnica: 'Palillo circular', Tallas: 'S-M / M-L', Tiempo: '2-3 días', Cuidado: 'Lavado a mano frío' }
  }
];

const defaultCombos = [
  {
    id: 'c1',
    nombre: 'Kit páramo completo',
    items: 'Ruana tradicional + bufanda + gorro a juego. Todo en la paleta que elijas.',
    precioActual: 155000,
    precioAntes: 185000,
    badge: '16% off',
    imgs: [
      'images/MSWJyv8j.jpeg',
      'images/otubdlel.jpeg',
      'images/qGUMwu7e.jpeg'
    ]
  },
  {
    id: 'c2',
    nombre: 'Combo hogar nariñense',
    items: 'Manta andina + tapete redondo. Ideal para renovar la sala con identidad propia.',
    precioActual: 185000,
    precioAntes: 220000,
    badge: '16% off',
    imgs: [
      'images/rmmYhQdW.jpeg',
      'images/vDOIHA_2.jpeg',
      'images/z-jM594v.jpeg'
    ]
  },
  {
    id: 'c3',
    nombre: 'Kit regalo bebé',
    items: 'Gorro baby + medias de algodón + mochilita mini. Empacado para regalo.',
    precioActual: 92000,
    precioAntes: 110000,
    badge: '16% off',
    imgs: [
      'images/z2xe92Kv.jpeg',
      'images/_ZKDwEYC.jpeg',
      'images/gxICe-hO.jpeg'
    ]
  }
];

function imgOnError(el, src) {
  el.onerror = null;
  el.src = 'data:image/svg+xml,' + encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><rect width="100%" height="100%" fill="%237A6B5E"/><text x="50%" y="50%" font-family="sans-serif" font-size="12" fill="%23F5E6C8" text-anchor="middle" dy="5">Imagen no disponible</text></svg>');
}

const galeriaImgs = [
  { src: 'images/-j2HIgfU.jpeg', alt: 'Ruana tejida a mano en telar' },
  { src: 'images/2cIkc2C-.jpeg', alt: 'Mochila de crochet multicolor' },
  { src: 'images/2fVInDbL.jpeg', alt: 'Set bufanda y gorro artesanal' },
  { src: 'images/4S6Q7ukd.jpeg', alt: 'Tapete de telar nariñense' },
  { src: 'images/5d1kL5l1.jpeg', alt: 'Detalle de tejido en palillo' },
  { src: 'images/8CkPeEn0.jpeg', alt: 'Artesana trabajando en telar' },
  { src: 'images/ABO_xAJ3.jpeg', alt: 'Manta andina' },
  { src: 'images/D0oMSe5d.jpeg', alt: 'Producto artesanal' },
  { src: 'images/I-KeqwjX.jpeg', alt: 'Tejido tradicional' },
  { src: 'images/Qk5deWSx.jpeg', alt: 'Ruana de lana' },
  { src: 'images/RyXD7U_f.jpeg', alt: 'Mochila artesanal' },
  { src: 'images/Y5e04J4G.jpeg', alt: 'Accesorio de lana' },
  { src: 'images/_ZKDwEYC.jpeg', alt: 'Producto nariñense' },
  { src: 'images/cgcvFhRD.jpeg', alt: 'Tejido en telar' },
  { src: 'images/gxICe-hO.jpeg', alt: 'Artesania campesina' },
  { src: 'images/h0duS-PT.jpeg', alt: 'Producto único' },
  { src: 'images/jTRVo9Pf.jpeg', alt: 'Manta tejida' },
  { src: 'images/msWJyv8j.jpeg', alt: 'Bufanda páramo' },
  { src: 'images/otubdlel.jpeg', alt: 'Gorro de lana' },
  { src: 'images/qGUMwu7e.jpeg', alt: 'Bolso crochet' },
  { src: 'images/rmmYhQdW.jpeg', alt: 'Producto especial' },
  { src: 'images/vDOIHA_2.jpeg', alt: 'Tejido artesanal' },
  { src: 'images/z-jM594v.jpeg', alt: 'Producto nariño' },
  { src: 'images/z2xe92Kv.jpeg', alt: 'Manta y ruana' }
];

// =============================================
// STATE
// =============================================
let productos = JSON.parse(localStorage.getItem('luc_productos') || 'null') || defaultProductos;
let activeFilter = 'all';
let adminUnlocked = false;
let currentProductModal = null;
let currentLightboxIndex = 0;

// =============================================
// RENDER PRODUCTS
// =============================================
function fmtPrecio(n) {
  return '$' + n.toLocaleString('es-CO');
}

function renderProductos() {
  const grid = document.getElementById('productos-grid');
  const q = (document.getElementById('catalogo-search')?.value || '').toLowerCase().trim();
  let filtered = activeFilter === 'all' ? productos : productos.filter(p => p.cat === activeFilter);
  if (q) {
    filtered = filtered.filter(p =>
      p.nombre.toLowerCase().includes(q) ||
      p.catLabel.toLowerCase().includes(q) ||
      (p.desc || '').toLowerCase().includes(q)
    );
  }
  if (filtered.length === 0) {
    grid.innerHTML = '<p style="text-align:center;padding:3rem 1rem;color:var(--gris-lana);">No encontramos productos que coincidan con tu búsqueda.</p>';
  } else {
    grid.innerHTML = filtered.map(p => `
    <article class="producto-card ${p.estado === 'agotado' ? 'agotado' : ''} reveal"
      data-id="${p.id}" role="listitem"
      aria-label="${p.nombre} — ${fmtPrecio(p.precio)}${p.estado === 'agotado' ? ' (Agotado)' : ''}">
      <div class="producto-img-wrap">
        <img src="${p.img}" alt="${p.nombre}" loading="lazy" onerror="imgOnError(this)">
        <div class="producto-badge">
          ${p.estado === 'agotado' ? '<span class="badge-agotado">Agotado</span>' : ''}
          ${p.nuevo && p.estado !== 'agotado' ? '<span class="badge-nuevo">Nuevo</span>' : ''}
          ${p.precioAntes && p.estado !== 'agotado' ? '<span class="badge-promo">Oferta</span>' : ''}
        </div>
        ${p.estado !== 'agotado' ? `
        <div class="producto-actions">
          <button class="producto-action-btn wa" data-action="add-cart" data-id="${p.id}">🛒 Agregar</button>
          <button class="producto-action-btn info" data-action="ver-mas" data-id="${p.id}">Ver más</button>
        </div>` : ''}
      </div>
      <div class="producto-body">
        <div class="producto-cat">${p.catLabel}</div>
        <h3 class="producto-nombre">${p.nombre}</h3>
        <div class="producto-footer">
          <div class="producto-precio">
            ${p.precioAntes ? '<span class="producto-precio-old">' + fmtPrecio(p.precioAntes) + '</span>' : ''}
            ${fmtPrecio(p.precio)}
          </div>
          ${p.personalizable ? '<span class="producto-personalizable">✏️ Personalizable</span>' : ''}
        </div>
      </div>
    </article>
  `).join('');
  }
  observeReveal();
}

function renderCombos() {
  const grid = document.getElementById('combos-grid');
  grid.innerHTML = defaultCombos.map(c => `
    <article class="combo-card reveal">
      <div class="combo-imgs">
        <img src="${c.imgs[0]}" alt="${c.nombre}" loading="lazy" onerror="imgOnError(this)">
        <img src="${c.imgs[1]}" alt="Detalle ${c.nombre}" loading="lazy" onerror="imgOnError(this)">
        <img src="${c.imgs[2]}" alt="Detalle ${c.nombre}" loading="lazy" onerror="imgOnError(this)">
      </div>
      <div class="combo-body">
        <div class="combo-badge">${c.badge}</div>
        <h3 class="combo-name">${c.nombre}</h3>
        <p class="combo-items">${c.items}</p>
        <div class="combo-footer">
          <div class="combo-precio">
            <span class="combo-precio-actual">${fmtPrecio(c.precioActual)}</span>
            <span class="combo-precio-old">${fmtPrecio(c.precioAntes)}</span>
          </div>
                      <button class="btn-primary" data-action="pedir-combo" data-combo="${c.nombre}" style="padding:0.6rem 1rem; font-size:0.82rem;">
              🛒 Agregar
            </button>
        </div>
        <div class="combo-ahorro">Ahorras ${fmtPrecio(c.precioAntes - c.precioActual)}</div>
      </div>
    </article>
  `).join('');
  observeReveal();
}

function renderGaleria() {
  const grid = document.getElementById('galeria-grid');
  grid.innerHTML = galeriaImgs.map((img, i) => `
    <div class="galeria-item reveal" role="listitem" tabindex="0"
      data-action="lightbox-open" data-img="${img.src}" data-alt="${img.alt}">
      <img src="${img.src}" alt="${img.alt}" loading="lazy" onerror="imgOnError(this)">
      <div class="galeria-overlay" aria-hidden="true"><span>🔍</span></div>
    </div>
  `).join('');
  observeReveal();
}

// =============================================
// FILTERS
// =============================================
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => {
      b.classList.remove('active');
      b.setAttribute('aria-pressed', 'false');
    });
    btn.classList.add('active');
    btn.setAttribute('aria-pressed', 'true');
    activeFilter = btn.dataset.filter;
    renderProductos();
  });
});



// =============================================
// FOCUS TRAP — Accesibilidad mejorada
// =============================================
let lastFocusedElement = null;

function trapFocus(modalId) {
  const modal = document.getElementById(modalId);
  const focusableEls = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
  const firstFocusable = focusableEls[0];
  const lastFocusable = focusableEls[focusableEls.length - 1];
  lastFocusedElement = document.activeElement;
  setTimeout(() => {
    const closeBtn = modal.querySelector('[aria-label*="Cerrar"], button');
    (closeBtn || firstFocusable)?.focus();
  }, 50);
  modal.addEventListener('keydown', function(e) {
    if (e.key === 'Tab') {
      if (e.shiftKey && document.activeElement === firstFocusable) { e.preventDefault(); lastFocusable?.focus(); }
      else if (!e.shiftKey && document.activeElement === lastFocusable) { e.preventDefault(); firstFocusable?.focus(); }
    }
  });
}

function releaseFocusTrap() {
  if (lastFocusedElement) lastFocusedElement.focus();
}

// =============================================
// MODALS
// =============================================
function openProductModal(id) {
  const p = productos.find(x => x.id === id);
  if (!p) return;
  currentProductModal = p;
  document.getElementById('modal-product-img').src = p.img;
  document.getElementById('modal-product-img').alt = p.nombre;
  document.getElementById('modal-product-cat').textContent = p.catLabel;
  document.getElementById('modal-product-name').textContent = p.nombre;
  document.getElementById('modal-product-desc').textContent = p.desc;
  document.getElementById('modal-product-precio').textContent = fmtPrecio(p.precio);
  document.getElementById('modal-product-details').innerHTML = Object.entries(p.detalles || {})
    .map(([k,v]) => `<div class="modal-detail-row"><span class="modal-detail-key">${k}</span><span class="modal-detail-val">${v}</span></div>`).join('');
  document.getElementById('modal-product-actions').innerHTML = `
    <a href="https://wa.me/573000000000?text=Hola!%20Me%20interesa%20${encodeURIComponent(p.nombre)}%20(${fmtPrecio(p.precio)})" 
      class="btn-primary" target="_blank" rel="noopener" style="justify-content:center;">
      📱 Pedir por WhatsApp
    </a>
    <button class="btn-outline" data-action="close-product-modal" style="justify-content:center;">Cerrar</button>
  `;
  document.getElementById('product-modal').classList.add('open');
  document.getElementById('product-modal').setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
}

function closeProductModal() {
  document.getElementById('product-modal').classList.remove('open');
  document.getElementById('product-modal').setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
  releaseFocusTrap();
}

function openLightbox(src, alt) {
  const idx = galeriaImgs.findIndex(i => i.src === src);
  currentLightboxIndex = idx >= 0 ? idx : 0;
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox-img').alt = alt;
  document.getElementById('lightbox').classList.add('open');
  document.getElementById('lightbox').setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
  trapFocus('lightbox');
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('open');
  document.getElementById('lightbox').setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
  releaseFocusTrap();
}

function navigateLightbox(direction) {
  currentLightboxIndex += direction;
  if (currentLightboxIndex < 0) currentLightboxIndex = galeriaImgs.length - 1;
  if (currentLightboxIndex >= galeriaImgs.length) currentLightboxIndex = 0;
  const img = galeriaImgs[currentLightboxIndex];
  document.getElementById('lightbox-img').src = img.src;
  document.getElementById('lightbox-img').alt = img.alt;
}

// Swipe support para móviles
let touchStartX = 0;
document.getElementById('lightbox')?.addEventListener('touchstart', e => {
  touchStartX = e.touches[0].clientX;
});
document.getElementById('lightbox')?.addEventListener('touchend', e => {
  const touchEndX = e.changedTouches[0].clientX;
  const diff = touchStartX - touchEndX;
  if (Math.abs(diff) > 50) {
    navigateLightbox(diff > 0 ? 1 : -1);
  }
});

// Keyboard navigation para lightbox
document.addEventListener('keydown', e => {
  if (document.getElementById('lightbox')?.classList.contains('open')) {
    if (e.key === 'ArrowLeft') navigateLightbox(-1);
    if (e.key === 'ArrowRight') navigateLightbox(1);
  }
});

document.getElementById('lightbox').addEventListener('click', function(e) {
  if (e.target === this) closeLightbox();
});
document.getElementById('product-modal').addEventListener('click', function(e) {
  if (e.target === this) closeProductModal();
});

// =============================================
// WA HELPER
// =============================================
function pedirPorWA(id) {
  const p = productos.find(x => x.id === id);
  if (!p) return;
  const msg = `Hola! Me interesa *${p.nombre}* (${fmtPrecio(p.precio)}). ¿Está disponible?`;
  window.open('https://wa.me/573000000000?text=' + encodeURIComponent(msg), '_blank');
}

function scrollToSection(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' });
}

// =============================================
// ADMIN PANEL
// =============================================
function openAdmin() {
  document.getElementById('admin-modal').classList.add('open');
  document.getElementById('admin-modal').setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
  trapFocus('admin-modal');
}

function closeAdmin() {
  document.getElementById('admin-modal').classList.remove('open');
  document.getElementById('admin-modal').setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
  releaseFocusTrap();
}

function checkAdminPwd() {
  const pwd = document.getElementById('admin-pwd').value;
  const msgEl = document.getElementById('admin-login-msg');
  if (pwd === ADMIN_PASSWORD) {
    adminUnlocked = true;
    document.getElementById('admin-login').style.display = 'none';
    document.getElementById('admin-content').style.display = 'block';
    renderAdminList();
  } else {
    msgEl.className = 'admin-msg err';
    msgEl.style.display = 'block';
    msgEl.textContent = 'Contraseña incorrecta. Intenta de nuevo.';
  }
}

document.getElementById('admin-pwd').addEventListener('keydown', e => {
  if (e.key === 'Enter') checkAdminPwd();
});

function renderAdminList() {
  const list = document.getElementById('admin-list');
  list.innerHTML = productos.map(p => `
    <div class="admin-prod-item" id="admin-prod-${p.id}">
      <img src="${p.img}" alt="${p.nombre}" class="admin-prod-thumb" id="admin-thumb-${p.id}">
      <div class="admin-prod-info">
        <div class="admin-prod-name">${p.nombre}</div>
        <div class="admin-prod-cat">${p.catLabel}</div>
      </div>
      <div class="admin-prod-controls">
        <input type="text" placeholder="URL nueva imagen" id="adm-img-${p.id}" value="${p.img}" 
          oninput="document.getElementById('admin-thumb-${p.id}').src=this.value">
        <input type="text" placeholder="Precio" id="adm-price-${p.id}" value="${p.precio}">
        <select id="adm-estado-${p.id}">
          <option value="disponible" ${p.estado==='disponible'?'selected':''}>✅ Disponible</option>
          <option value="agotado" ${p.estado==='agotado'?'selected':''}>❌ Agotado</option>
          <option value="pronto" ${p.estado==='pronto'?'selected':''}>🕐 Próximamente</option>
        </select>
      </div>
    </div>
  `).join('');
}

function saveAdminChanges() {
  const msgEl = document.getElementById('admin-save-msg');
  productos = productos.map(p => {
    const img = document.getElementById(`adm-img-${p.id}`)?.value?.trim() || p.img;
    const price = parseInt(document.getElementById(`adm-price-${p.id}`)?.value) || p.precio;
    const estado = document.getElementById(`adm-estado-${p.id}`)?.value || p.estado;
    return { ...p, img, precio: price, estado };
  });
  localStorage.setItem('luc_productos', JSON.stringify(productos));
  renderProductos();
  msgEl.className = 'admin-msg ok';
  msgEl.style.display = 'block';
  msgEl.textContent = '✅ Cambios guardados correctamente en este navegador.';
  setTimeout(() => { msgEl.style.display = 'none'; }, 3500);
}

function resetToDefaults() {
  if (!confirm('¿Restaurar todos los productos a sus valores originales? Se perderán los cambios guardados.')) return;
  localStorage.removeItem('luc_productos');
  productos = [...defaultProductos];
  renderAdminList();
  renderProductos();
  const msgEl = document.getElementById('admin-save-msg');
  msgEl.className = 'admin-msg ok';
  msgEl.style.display = 'block';
  msgEl.textContent = 'Productos restaurados a valores originales.';
}


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
    container.innerHTML = '<div class="cart-empty">Tu carrito está vacío<br><span style="font-size:0.8rem;">Agrega productos desde el catálogo</span></div>';
    footer.classList.add('hidden');
    return;
  }
  footer.classList.remove('hidden');
  container.innerHTML = cart.map((c, i) => `
    <div class="cart-item">
      <img src="${c.img}" alt="${c.nombre}" class="cart-item-img" loading="lazy">
      <div class="cart-item-info">
        <div class="cart-item-name">${c.nombre}</div>
        <div class="cart-item-precio">${fmtPrecio(c.precio)} ${c.qty > 1 ? '× ' + c.qty : ''}</div>
      </div>
      <button class="cart-item-remove" data-action="cart-remove" data-index="${i}" aria-label="Eliminar ${c.nombre}">✕</button>
    </div>
  `).join('');
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
  const label = document.getElementById('cart-count-label');
  if (!label) return;
  const orig = label.textContent;
  label.textContent = '✅ Agregado';
  setTimeout(() => { label.textContent = orig; updateCartBadge(); }, 1500);
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
  const items = cart.map(c => '• ' + c.nombre + ' × ' + (c.qty || 1) + ' = ' + fmtPrecio(c.precio * (c.qty || 1))).join('\n');
  const total = fmtPrecio(getCartTotal());
  const msg = 'Hola! Quiero hacer el siguiente pedido:\n\n' + items + '\n\nTotal: ' + total;
  window.open('https://wa.me/573000000000?text=' + encodeURIComponent(msg), '_blank');
}

// =============================================
// CENTRAL EVENT DELEGATION
// =============================================
(function() {
  document.addEventListener('click', function(e) {
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
        const combo = defaultCombos.find(function(c) { return c.nombre === comboName; });
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
      case 'lightbox-open': {
        const img = el.dataset.img;
        if (img) openLightbox(img);
        break;
      }
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
      case 'enviar-form':
        enviarFormulario();
        break;
      case 'close-cart':
        closeCart();
        break;
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
  document.addEventListener('input', function(e) {
    const el = e.target;
    if (el.dataset.thumbFor) {
      const thumb = document.getElementById('admin-thumb-' + el.dataset.thumbFor);
      if (thumb) thumb.src = el.value;
    }
  });
})();

// =============================================
// SEARCH INPUT
// =============================================
(function() {
  const si = document.getElementById('catalogo-search');
  if (si) {
    si.addEventListener('input', function() { renderProductos(); });
  }
})();

// =============================================
// DARK MODE TOGGLE
// =============================================
(function() {
  const dt = document.getElementById('dark-mode-toggle');
  if (dt) {
    const currentTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', currentTheme);
    dt.addEventListener('click', function() {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      const newTheme = isDark ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      dt.textContent = isDark ? '🌙' : '☀️';
    });
  }
})();

// =============================================
// CART OVERLAY CLICK
// =============================================
(function() {
  const cm = document.getElementById('cart-modal');
  if (cm) {
    cm.addEventListener('click', function(e) {
      if (e.target === this) closeCart();
    });
  }
})();

// Init cart
renderCart();
updateCartBadge();

document.getElementById('admin-modal').addEventListener('click', function(e) {
  if (e.target === this) closeAdmin();
});

// =============================================
// CONTACTO FORM
// =============================================
function validateContactForm() {
  const nombre = document.getElementById('contact-nombre').value.trim();
  const contacto = document.getElementById('contact-email').value.trim();
  const msgEl = document.getElementById('form-msg');
  const errorNombre = document.getElementById('error-nombre');
  const errorEmail = document.getElementById('error-email');

  errorNombre.style.display = 'none';
  errorEmail.style.display = 'none';
  msgEl.style.display = 'none';

  if (!nombre) {
    errorNombre.style.display = 'block';
    errorNombre.textContent = 'El nombre es obligatorio.';
    document.getElementById('contact-nombre').focus();
    return false;
  }

  if (!contacto) {
    errorEmail.style.display = 'block';
    errorEmail.textContent = 'El correo o WhatsApp es obligatorio.';
    document.getElementById('contact-email').focus();
    return false;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const waRegex = /^\+?\d{10,15}$/;
  if (!emailRegex.test(contacto) && !waRegex.test(contacto.replace(/\s/g, ''))) {
    errorEmail.style.display = 'block';
    errorEmail.textContent = 'Ingresa un correo válido o un numero de WhatsApp.';
    document.getElementById('contact-email').focus();
    return false;
  }

  return true;
}

function enviarFormulario() {
  if (!validateContactForm()) return;

  const nombre = document.getElementById('contact-nombre').value.trim();
  const contacto = document.getElementById('contact-email').value.trim();
  const interes = document.getElementById('contact-interes').value;
  const mensaje = document.getElementById('contact-mensaje').value.trim();
  const msgEl = document.getElementById('form-msg');

  const waText = `Hola! Soy ${nombre}. Me interesa: ${interes || 'consulta general'}. ${mensaje ? 'Mensaje: ' + mensaje : ''}. Contacto: ${contacto}`;
  window.open('https://wa.me/573000000000?text=' + encodeURIComponent(waText), '_blank');

  msgEl.className = 'admin-msg ok';
  msgEl.style.display = 'block';
  msgEl.textContent = '✅ Te redirigimos a WhatsApp. Si prefieres correo, escríbenos a info@tejidoslucerito.com';
  document.getElementById('contact-nombre').value = '';
  document.getElementById('contact-email').value = '';
  document.getElementById('contact-interes').value = '';
  document.getElementById('contact-mensaje').value = '';
}

// =============================================
// NAV SCROLL + MOBILE
// =============================================
const nav = document.getElementById('nav');
let lastScroll = 0;
window.addEventListener('scroll', () => {
  const s = window.scrollY;
  nav.classList.toggle('scrolled', s > 60);
  lastScroll = s;
}, { passive: true });

const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobile-menu');
hamburger.addEventListener('click', () => {
  const open = mobileMenu.classList.toggle('open');
  hamburger.classList.toggle('open', open);
  hamburger.setAttribute('aria-expanded', open);
  mobileMenu.setAttribute('aria-hidden', !open);
  document.body.style.overflow = open ? 'hidden' : '';
});
document.querySelectorAll('.mobile-link').forEach(link => {
  link.addEventListener('click', () => {
    mobileMenu.classList.remove('open');
    hamburger.classList.remove('open');
    hamburger.setAttribute('aria-expanded', 'false');
    mobileMenu.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  });
});

// =============================================
// SCROLL REVEAL
// =============================================
function observeReveal() {
  const els = document.querySelectorAll('.reveal:not(.visible)');
  if ('IntersectionObserver' in window) {
    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); obs.unobserve(e.target); } });
    }, { threshold: 0.12 });
    els.forEach(el => obs.observe(el));
  } else {
    els.forEach(el => el.classList.add('visible'));
  }
}

// =============================================
// COUNTDOWN (próximos 30 días)
// =============================================
function getCountdownTarget() {
  const stored = localStorage.getItem('promo_target');
  if (stored) {
    const t = new Date(stored);
    if (t > new Date()) return t;
  }
  const now = new Date();
  const endOfMonth = new Date(now.getFullYear(), now.getMonth() + 1, 0, 23, 59, 59);
  const target = new Date(endOfMonth.getTime() + 15 * 24 * 60 * 60 * 1000);
  localStorage.setItem('promo_target', target.toISOString());
  return target;
}
function updateCountdown() {
  const target = getCountdownTarget();
  const now = new Date();
  const diff = target - now;
  if (diff <= 0) {
    document.getElementById('countdown-dias').textContent = '0';
    return;
  }
  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const el = document.getElementById('countdown-dias');
  if (el) el.textContent = days;
}
updateCountdown();
setInterval(updateCountdown, 60000);

// =============================================
// KEYBOARD ESC
// =============================================
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    closeLightbox();
    closeProductModal();
    closeAdmin();
  }
});

// =============================================
// INIT
// =============================================
renderProductos();
renderCombos();
renderGaleria();
renderCart();
updateCartBadge();
observeReveal();
document.getElementById('footer-year').textContent = new Date().getFullYear();





// Active nav link on scroll
const sections = document.querySelectorAll('section[id]');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => {
    if (window.scrollY >= s.offsetTop - 120) current = s.id;
  });
  document.querySelectorAll('.nav-links a').forEach(a => {
    a.classList.toggle('active', a.getAttribute('href') === '#' + current);
  });
}, { passive: true });
