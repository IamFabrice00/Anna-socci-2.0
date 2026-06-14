import os
import json
import shutil

OUTPUT_DIR = r"C:\Users\Logon Fabrice\Desktop\ANTIGRAVITY\Anna Socci"
DATA_DIR = os.path.join(OUTPUT_DIR, "data")
PORTFOLIO_JSON_PATH = os.path.join(DATA_DIR, "portfolio.json")

CATEGORIES = [
    "Wedding", "Campaigns", "Celebrities", "Beauty", "Jewelry", 
    "Bridal", "Nature", "Landscapes", "Travel", "Fine Art"
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ANNA SOCCI - {title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{depth}assets/css/style.css">
</head>
<body>
    <header class="navbar">
        <a href="{depth}index.html" class="logo">ANNA SOCCI</a>
        <div class="menu-icon" onclick="toggleMenu()">☰</div>
    </header>

    <div class="sidebar-menu" id="sidebar">
        <div class="close-btn" onclick="toggleMenu()">✕</div>
        <nav>
            <a href="{depth}index.html">HOME</a>
            {nav_links}
        </nav>
    </div>

    <main class="gallery-container">
        <h1 class="page-title">{title}</h1>
        <div class="masonry-grid" id="masonry">
            <!-- Grid generated via JS -->
        </div>
    </main>

    <footer>
        <div class="footer-content">
            <div class="contact-info">
                <h3>CONTACTS</h3>
                <a href="mailto:annasocci@gmail.com">annasocci@gmail.com</a>
                <a href="#">Privacy and cookie policy</a>
            </div>
            <div class="socials">
                <a href="https://www.instagram.com/socciografando" target="_blank">Instagram</a>
            </div>
        </div>
        <div class="copyright">© 2026 ANNA SOCCI.</div>
    </footer>

    <div class="cookie-banner" id="cookie-banner">
        <p>This website uses only essential cookies to ensure proper functioning and improve your browsing experience.</p>
        <div class="cookie-actions">
            <a href="#">Privacy policy</a>
            <button onclick="acceptCookies()">Ok</button>
        </div>
    </div>

    <script src="{depth}assets/js/gallery.js"></script>
    <script>
        const photos = {photos_json};
        initGallery(photos, '{depth}');
    </script>
</body>
</html>
"""

CSS_CONTENT = """
:root {
    --bg-color: #000000;
    --text-color: #FFFFFF;
    --accent-color: #888888;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    background-color: var(--bg-color);
    color: var(--text-color);
    font-family: 'Montserrat', sans-serif;
    line-height: 1.6;
    overflow-x: hidden;
    opacity: 0;
    animation: fadeIn 1s forwards;
}

@keyframes fadeIn { to { opacity: 1; } }

.navbar {
    position: fixed;
    top: 0; left: 0; right: 0;
    padding: 20px 40px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
    background: linear-gradient(rgba(0,0,0,0.8), transparent);
    transition: background 0.3s;
}

.navbar.scrolled { background: rgba(0,0,0,0.95); }

.logo {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    color: var(--text-color);
    text-decoration: none;
    letter-spacing: 4px;
    text-transform: uppercase;
}

.menu-icon {
    font-size: 28px;
    cursor: pointer;
    user-select: none;
}

.sidebar-menu {
    position: fixed;
    top: 0; right: -400px;
    width: 300px;
    height: 100vh;
    background: rgba(10,10,10,0.98);
    z-index: 1000;
    transition: right 0.4s ease;
    padding: 80px 40px;
    display: flex;
    flex-direction: column;
}

.sidebar-menu.open { right: 0; }

.sidebar-menu nav a {
    display: block;
    color: var(--text-color);
    text-decoration: none;
    font-size: 14px;
    margin-bottom: 20px;
    letter-spacing: 2px;
    text-transform: uppercase;
    transition: color 0.3s;
}

.sidebar-menu nav a:hover { color: var(--accent-color); }

.close-btn {
    position: absolute;
    top: 25px; right: 40px;
    font-size: 24px;
    cursor: pointer;
}

.page-title {
    font-family: 'Playfair Display', serif;
    text-align: center;
    margin: 120px 0 60px;
    font-size: 48px;
    letter-spacing: 6px;
    text-transform: uppercase;
    font-weight: 400;
}

.gallery-container {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 20px 100px;
}

.masonry-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}

@media (max-width: 1024px) { .masonry-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 768px) { .masonry-grid { grid-template-columns: 1fr; } }

.grid-item {
    position: relative;
    overflow: hidden;
    cursor: pointer;
    aspect-ratio: 3/4;
}

.grid-item img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.6s ease;
}

.grid-item:hover img { transform: scale(1.05); }

.overlay {
    position: absolute;
    inset: 0;
    background: rgba(0,0,0,0.5);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    opacity: 0;
    transition: opacity 0.4s ease;
    padding: 20px;
    text-align: center;
}

.grid-item:hover .overlay { opacity: 1; }

.overlay h3 {
    font-family: 'Playfair Display', serif;
    font-size: 20px;
    letter-spacing: 2px;
    margin-bottom: 10px;
    text-transform: uppercase;
    font-weight: 400;
}

.overlay p {
    font-family: 'Inter', sans-serif;
    font-size: 12px;
    letter-spacing: 1px;
    color: #ccc;
}

footer {
    padding: 60px 40px;
    border-top: 1px solid rgba(255,255,255,0.1);
}

.footer-content {
    display: flex;
    justify-content: space-between;
    margin-bottom: 40px;
}

.contact-info h3 { font-family: 'Playfair Display', serif; margin-bottom: 15px; letter-spacing: 2px;}
.contact-info a, .socials a {
    display: block; color: var(--accent-color); text-decoration: none; font-size: 12px; margin-bottom: 8px; letter-spacing: 1px;
}
.contact-info a:hover, .socials a:hover { color: var(--text-color); }

.copyright { text-align: center; font-size: 10px; color: var(--accent-color); letter-spacing: 2px; }

.cookie-banner {
    position: fixed; bottom: 0; left: 0; right: 0;
    background: #111; padding: 20px 40px;
    display: flex; justify-content: space-between; align-items: center;
    z-index: 1000; font-size: 12px; transform: translateY(100%); transition: transform 0.5s;
}

.cookie-banner.show { transform: translateY(0); }
.cookie-actions { display: flex; align-items: center; gap: 20px; }
.cookie-actions a { color: var(--text-color); }
.cookie-actions button { background: var(--text-color); color: var(--bg-color); border: none; padding: 8px 24px; cursor: pointer; font-weight: bold; border-radius: 2px;}

/* Lightbox */
.lightbox {
    position: fixed; inset: 0; background: rgba(0,0,0,0.95); z-index: 2000;
    display: flex; justify-content: center; align-items: center;
    opacity: 0; pointer-events: none; transition: opacity 0.3s;
}
.lightbox.active { opacity: 1; pointer-events: auto; }
.lightbox img { max-width: 90%; max-height: 90vh; object-fit: contain; }
.lightbox-close { position: absolute; top: 30px; right: 40px; font-size: 30px; cursor: pointer; }
.lightbox-prev, .lightbox-next { position: absolute; top: 50%; font-size: 40px; cursor: pointer; transform: translateY(-50%); padding: 20px;}
.lightbox-prev { left: 20px; }
.lightbox-next { right: 20px; }
"""

JS_CONTENT = """
function toggleMenu() {
    document.getElementById('sidebar').classList.toggle('open');
}

window.addEventListener('scroll', () => {
    const nav = document.querySelector('.navbar');
    if (window.scrollY > 50) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
});

function acceptCookies() {
    localStorage.setItem('cookiesAccepted', 'true');
    document.getElementById('cookie-banner').classList.remove('show');
}

document.addEventListener('DOMContentLoaded', () => {
    if (!localStorage.getItem('cookiesAccepted')) {
        setTimeout(() => document.getElementById('cookie-banner').classList.add('show'), 1000);
    }
    
    // Create Lightbox DOM
    const lb = document.createElement('div');
    lb.className = 'lightbox';
    lb.innerHTML = `
        <div class="lightbox-close" onclick="closeLightbox()">✕</div>
        <div class="lightbox-prev" onclick="changeSlide(-1)">❮</div>
        <img id="lightbox-img" src="" alt="">
        <div class="lightbox-next" onclick="changeSlide(1)">❯</div>
    `;
    document.body.appendChild(lb);
});

let currentPhotos = [];
let currentIndex = 0;
let basePath = '';

function initGallery(photos, pathDepth) {
    currentPhotos = photos;
    basePath = pathDepth;
    const grid = document.getElementById('masonry');
    
    if (photos.length === 0) {
        grid.innerHTML = "<p style='text-align:center; grid-column: 1/-1;'>Nessuna foto trovada in questa categoria.</p>";
        return;
    }
    
    let html = '';
    photos.forEach((p, index) => {
        html += `
        <div class="grid-item" onclick="openLightbox(${index})">
            <img src="${basePath}photos/thumbs/${p.filename}" loading="lazy" alt="${p.tags.join(', ')}">
            <div class="overlay">
                <h3>${p.category}</h3>
                <p>${p.tags.join(' • ')}</p>
            </div>
        </div>
        `;
    });
    grid.innerHTML = html;
}

function openLightbox(index) {
    currentIndex = index;
    const lb = document.querySelector('.lightbox');
    const img = document.getElementById('lightbox-img');
    img.src = basePath + 'photos/originals/' + currentPhotos[currentIndex].filename;
    lb.classList.add('active');
}

function closeLightbox() {
    document.querySelector('.lightbox').classList.remove('active');
}

function changeSlide(dir) {
    currentIndex += dir;
    if (currentIndex < 0) currentIndex = currentPhotos.length - 1;
    if (currentIndex >= currentPhotos.length) currentIndex = 0;
    document.getElementById('lightbox-img').src = basePath + 'photos/originals/' + currentPhotos[currentIndex].filename;
}
"""

def generate_site():
    print("Avvio STEP 5: Generazione Sito...")
    
    # Crea cartelle base
    os.makedirs(os.path.join(OUTPUT_DIR, "assets", "css"), exist_ok=True)
    os.makedirs(os.path.join(OUTPUT_DIR, "assets", "js"), exist_ok=True)
    
    # Crea CSS e JS
    with open(os.path.join(OUTPUT_DIR, "assets", "css", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS_CONTENT)
    with open(os.path.join(OUTPUT_DIR, "assets", "js", "gallery.js"), "w", encoding="utf-8") as f:
        f.write(JS_CONTENT)
        
    # Carica JSON
    with open(PORTFOLIO_JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    photos = data.get("photos", [])
    
    # Genera link di navigazione
    nav_links = ""
    for cat in CATEGORIES:
        nav_links += f'<a href="{{depth}}{cat.lower().replace(" ", "-")}/index.html">{cat.upper()}</a>\n'

    # Funzione helper per creare pagine
    def create_page(path, title, depth, filtered_photos):
        content = HTML_TEMPLATE.format(
            title=title, 
            depth=depth, 
            nav_links=nav_links.format(depth=depth),
            photos_json=json.dumps(filtered_photos)
        )
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
            
    # Crea Home
    create_page(os.path.join(OUTPUT_DIR, "index.html"), "PORTFOLIO", "", photos)
    
    # Crea Pagine Categoria
    for cat in CATEGORIES:
        cat_folder_name = cat.lower().replace(" ", "-")
        cat_dir = os.path.join(OUTPUT_DIR, cat_folder_name)
        os.makedirs(cat_dir, exist_ok=True)
        cat_photos = [p for p in photos if p.get("category") == cat]
        create_page(os.path.join(cat_dir, "index.html"), cat.upper(), "../", cat_photos)
        
    print("STEP 5 - SITO GENERATO CON SUCCESSO.")
    print("Per eseguire il deploy locale, usa un server http nella cartella 'Anna Socci'.")

if __name__ == "__main__":
    generate_site()
