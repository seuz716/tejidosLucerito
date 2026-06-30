"""Apply remaining SEO fixes to lucerito_portfolio.html."""

with open("lucerito_portfolio.html", "r") as f:
    html = f.read()

# 1. Replace remaining placehold.co URLs in JS data with local assets
import re

ASSETS = "assets/images/"

# Product images mapping
prod_repl = {
    "https://placehold.co/600x800/5C4033/F5E6C8?text=Ruana+Tradicional": ASSETS + "prod-ruana.jpg",
    "https://placehold.co/600x800/4A6741/F5E6C8?text=Mochila+Multicolor": ASSETS + "prod-mochila.jpg",
    "https://placehold.co/600x800/C4852A/F5E6C8?text=Set+Bufanda+Gorro": ASSETS + "prod-set-bufanda.jpg",
    "https://placehold.co/600x800/7A5546/F5E6C8?text=Tapete+Telar": ASSETS + "prod-tapete.jpg",
    "https://placehold.co/600x800/8B3A3A/F5E6C8?text=Gorro+Bebé": ASSETS + "prod-gorro-bebe.jpg",
    "https://placehold.co/600x800/3D2B1F/F5E6C8?text=Manta+Andina": ASSETS + "prod-manta.jpg",
    "https://placehold.co/600x800/6B8F62/F5E6C8?text=Bolso+Mercado": ASSETS + "prod-bolso.jpg",
    "https://placehold.co/600x800/A09080/F5E6C8?text=Medias+Lana": ASSETS + "prod-medias.jpg",
    # Combos
    "https://placehold.co/400x200/5C4033/F5E6C8?text=Kit+Páramo": ASSETS + "combo-paramo.jpg",
    "https://placehold.co/200x100/4A6741/F5E6C8?text=Bufanda": ASSETS + "combo-bufanda.jpg",
    "https://placehold.co/200x100/C4852A/F5E6C8?text=Gorro": ASSETS + "combo-gorro.jpg",
    "https://placehold.co/400x200/3D2B1F/F5E6C8?text=Combo+Hogar": ASSETS + "combo-hogar.jpg",
    "https://placehold.co/200x100/7A5546/F5E6C8?text=Tapete": ASSETS + "combo-tapete.jpg",
    "https://placehold.co/200x100/A09080/F5E6C8?text=Manta": ASSETS + "combo-manta.jpg",
    "https://placehold.co/400x200/8B3A3A/F5E6C8?text=Kit+Bebé": ASSETS + "combo-bebe.jpg",
    "https://placehold.co/200x100/6B8F62/F5E6C8?text=Medias": ASSETS + "combo-medias.jpg",
    "https://placehold.co/200x100/D9A04A/F5E6C8?text=Bolsito": ASSETS + "combo-bolsito.jpg",
    # Galeria
    "https://placehold.co/800x600/5C4033/F5E6C8?text=Tejido+1": ASSETS + "galeria-1.jpg",
    "https://placehold.co/400x300/4A6741/F5E6C8?text=Tejido+2": ASSETS + "galeria-2s.jpg",
    "https://placehold.co/400x300/C4852A/F5E6C8?text=Tejido+3": ASSETS + "galeria-3s.jpg",
    "https://placehold.co/800x300/7A5546/F5E6C8?text=Tejido+4": ASSETS + "galeria-4.jpg",
    "https://placehold.co/400x300/3D2B1F/F5E6C8?text=Tejido+5": ASSETS + "galeria-5s.jpg",
    "https://placehold.co/400x300/8B3A3A/F5E6C8?text=Tejido+6": ASSETS + "galeria-6s.jpg",
}

for old, new in prod_repl.items():
    html = html.replace(old, new)

# 2. Add ASSETS constant before defaultProductos if not present
if "const ASSETS" not in html:
    html = html.replace(
        "const defaultProductos = [",
        "const ASSETS = 'assets/images/';\n\nconst defaultProductos = [",
        1
    )

# 3. Remove any stray CONFIG template literals
html = html.replace("${CONFIG.whatsapp}", "573000000000")

# 4. Fix the inline style on the sección-desc paragraph in "quienes somos"
html = html.replace(
    '<p class="section-desc" style="margin-top:0.75rem;">',
    '<p class="section-desc mt-sm">'
)

# 5. Fix the hero stats paragraph (process section)
html = html.replace(
    '<p class="section-desc" style="margin: 1rem auto 0; text-align:center; max-width:520px;">',
    '<p class="section-desc mx-auto text-center mt-md max-w-520">'
)

# 6. Fix ubicacion section label
html = html.replace(
    '<div class="section-label text-center mb-md" style="margin-bottom:1.5rem;">',
    '<div class="section-label text-center" style="margin-bottom:1.5rem;">'
)

# 7. Fix form-msg inline style
html = html.replace(
    '<div id="form-msg" class="admin-msg" style="display:none;"></div>',
    '<div id="form-msg" class="admin-msg hidden"></div>'
)

# 8. Replace the old JS section's function approach to use event delegation
# Check if admin login uses old style.display or class-based hidden
html = html.replace(
    "document.getElementById('admin-login').style.display = 'none';",
    "document.getElementById('admin-login').classList.add('hidden');"
)
html = html.replace(
    "document.getElementById('admin-content').style.display = 'block';",
    "document.getElementById('admin-content').classList.remove('hidden');"
)

# 9. Fix the párrafo con comentarios inline in ¿Qué hacemos? and combos
html = html.replace(
    '<p class="section-desc" style="margin: 1rem auto 0; text-align:center;">',
    '<p class="section-desc mx-auto text-center mt-md">'
)

with open("lucerito_portfolio.html", "w") as f:
    f.write(html)

print("✅ All SEO fixes applied!")
print(f"   Remaining placehold.co references: {html.count('placehold.co')}")
