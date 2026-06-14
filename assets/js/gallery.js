
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
