"""Generate beautiful, themed SVG placeholder images for Tejidos Lucerito."""
import os

OUT = "assets/images"
os.makedirs(OUT, exist_ok=True)

COLORS = {
    "tierra": "#5C4033", "tierra-light": "#7A5546", "tierra-deep": "#3D2B1F",
    "crema": "#F5E6C8", "crema-warm": "#EDD9A3", "crema-deep": "#D4B483",
    "verde": "#4A6741", "verde-light": "#6B8F62", "mostaza": "#C4852A",
    "rojo": "#8B3A3A", "blanco": "#FDFAF4", "gris": "#A09080",
}

def svg(w, h, bg, text="", fg="#F5E6C8", pattern="none"):
    lines = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">']
    lines.append(f'<defs><pattern id="p" patternUnits="userSpaceOnUse" width="40" height="40">')
    if pattern == "weave":
        lines.append(f'<path d="M0 20h40M20 0v40" stroke="{fg}" stroke-width="0.5" opacity="0.15"/>')
    elif pattern == "dots":
        lines.append(f'<circle cx="20" cy="20" r="1.5" fill="{fg}" opacity="0.12"/>')
    elif pattern == "lines":
        lines.append(f'<line x1="0" y1="0" x2="40" y2="40" stroke="{fg}" stroke-width="0.5" opacity="0.1"/>')
    elif pattern == "zigzag":
        lines.append(f'<polyline points="0,20 10,10 20,20 30,10 40,20" fill="none" stroke="{fg}" stroke-width="1" opacity="0.12"/>')
    elif pattern == "cross":
        lines.append(f'<line x1="10" y1="10" x2="30" y2="30" stroke="{fg}" stroke-width="0.8" opacity="0.1"/>')
        lines.append(f'<line x1="30" y1="10" x2="10" y2="30" stroke="{fg}" stroke-width="0.8" opacity="0.1"/>')
    lines.append('</pattern></defs>')
    lines.append(f'<rect width="{w}" height="{h}" fill="{bg}"/>')
    lines.append(f'<rect width="{w}" height="{h}" fill="url(#p)"/>')
    lines.append(f'<rect width="{w}" height="{h}" fill="url(#g)" opacity="0.3"/>' if False else '')
    if text:
        lines.append(f'<text x="{w/2}" y="{h/2}" font-family="serif" font-size="{min(w,h)*0.07}" fill="{fg}" text-anchor="middle" dominant-baseline="middle" opacity="0.6">{text}</text>')
    lines.append('</svg>')
    return ''.join(lines)

def write(name, w, h, bg, text="", fg="#F5E6C8", pattern="none"):
    with open(f"{OUT}/{name}", "w") as f:
        f.write(svg(w, h, bg, text, fg, pattern))

# Hero
write("hero.jpg", 900, 1100, COLORS["tierra"], "Tejidos Lucerito", pattern="weave")

# Quienes somos
write("quienes-1.jpg", 480, 480, COLORS["tierra-light"], "Artesanas\nGualmatán", pattern="weave")
write("quienes-2.jpg", 360, 320, COLORS["verde"], "Tejido\nTradicional", pattern="zigzag")

# Técnicas
write("tecnica-telar.jpg", 500, 375, COLORS["tierra-deep"], "Telar de pie", pattern="weave")
write("tecnica-crochet.jpg", 500, 375, COLORS["verde"], "Crochet", pattern="dots")
write("tecnica-palillo.jpg", 500, 375, COLORS["tierra"], "Palillo", pattern="lines")

# Productos (8)
prods = [
    ("prod-ruana.jpg", COLORS["tierra"], "Ruana\nTradicional"),
    ("prod-mochila.jpg", COLORS["verde"], "Mochila\nMulticolor"),
    ("prod-set-bufanda.jpg", COLORS["mostaza"], "Set\nBufanda+Gorro"),
    ("prod-tapete.jpg", COLORS["tierra-light"], "Tapete\nde Telar"),
    ("prod-gorro-bebe.jpg", COLORS["rojo"], "Gorro\nBaby Alpaca"),
    ("prod-manta.jpg", COLORS["tierra-deep"], "Manta\nAndina"),
    ("prod-bolso.jpg", COLORS["verde-light"], "Bolso\nde Mercado"),
    ("prod-medias.jpg", COLORS["gris"], "Medias\nde Lana"),
]
for name, bg, text in prods:
    write(name, 600, 800, bg, text, pattern="weave")

# Combos
combos = [
    ("combo-paramo.jpg", COLORS["tierra"], "Kit Páramo"),
    ("combo-hogar.jpg", COLORS["tierra-deep"], "Combo Hogar"),
    ("combo-bebe.jpg", COLORS["rojo"], "Kit Bebé"),
    ("combo-bufanda.jpg", COLORS["verde"], "Bufanda"),
    ("combo-gorro.jpg", COLORS["mostaza"], "Gorro"),
    ("combo-tapete.jpg", COLORS["tierra-light"], "Tapete"),
    ("combo-manta.jpg", COLORS["gris"], "Manta"),
    ("combo-medias.jpg", COLORS["verde-light"], "Medias"),
    ("combo-bolsito.jpg", COLORS["mostaza"], "Bolsito"),
]
for name, bg, text in combos:
    w, h = (400, 200) if "paramo" in name or "hogar" in name or "bebe" in name else (200, 100)
    write(name, w, h, bg, text, pattern="dots")

# Galería
galeria = [
    ("galeria-1.jpg", COLORS["tierra"], "Ruana en telar", "weave"),
    ("galeria-2.jpg", COLORS["verde"], "Mochila crochet", "dots"),
    ("galeria-3.jpg", COLORS["mostaza"], "Set bufanda", "lines"),
    ("galeria-4.jpg", COLORS["tierra-light"], "Tapete nariñense", "zigzag"),
    ("galeria-5.jpg", COLORS["tierra-deep"], "Detalle palillo", "cross"),
    ("galeria-6.jpg", COLORS["rojo"], "Artesana en telar", "weave"),
]
for name, bg, text, pat in galeria:
    write(name, 800, 600, bg, text, pattern=pat)

# Additional gallery sizes
write("galeria-2s.jpg", 400, 300, COLORS["verde"], "Mochila", pattern="dots")
write("galeria-3s.jpg", 400, 300, COLORS["mostaza"], "Bufanda", pattern="lines")
write("galeria-5s.jpg", 400, 300, COLORS["tierra-deep"], "Detalle", pattern="cross")
write("galeria-6s.jpg", 400, 300, COLORS["rojo"], "Artesana", pattern="weave")

# OG Image
write("og-image.jpg", 1200, 630, COLORS["tierra-deep"], "Tejidos Lucerito\nGualmatán, Nariño", pattern="weave")

print("✅ All SVGs generated!")
