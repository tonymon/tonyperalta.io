// Project filtering functionality
document.addEventListener('DOMContentLoaded', function() {
    const filterBtns = document.querySelectorAll('.filter-btn');
    const projectTiles = document.querySelectorAll('.project-tile');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all buttons
            filterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');

            const filterValue = this.getAttribute('data-filter');

            projectTiles.forEach(tile => {
                if (filterValue === 'all' || tile.getAttribute('data-category') === filterValue) {
                    tile.classList.remove('hidden');
                } else {
                    tile.classList.add('hidden');
                }
            });
        });
    });

    // Media filtering functionality
    const mediaFilterBtns = document.querySelectorAll('.media-filter-btn');
    const mediaCards = document.querySelectorAll('.media-card');

    mediaFilterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Remove active class from all media filter buttons
            mediaFilterBtns.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');

            const filterValue = this.getAttribute('data-filter');

            mediaCards.forEach(card => {
                if (filterValue === 'all' || card.getAttribute('data-category') === filterValue) {
                    card.classList.remove('hidden');
                } else {
                    card.classList.add('hidden');
                }
            });
        });
    });

    // AWS video thumbnail click handler
    const videoThumbnail = document.querySelector('.video-thumbnail');
    if (videoThumbnail) {
        videoThumbnail.addEventListener('click', function() {
            const videoLink = document.querySelector('.video-link');
            if (videoLink) {
                window.open(videoLink.href, '_blank');
            }
        });
    }
});

// Project click handlers
function handleProjectClick(projectId) {
    console.log('Project clicked:', projectId);
    // Add your project click logic here
}

// Photo Gallery Lightbox functionality
const photoItems = document.querySelectorAll('.photo-item');
const lightbox = document.getElementById('lightbox');
const lightboxImage = document.getElementById('lightbox-image');
const lightboxClose = document.querySelector('.lightbox-close');
const lightboxPrev = document.getElementById('lightbox-prev');
const lightboxNext = document.getElementById('lightbox-next');
let currentPhotoIndex = 0;
let allPhotos = [];

// Collect all photo data
photoItems.forEach((item, index) => {
    const imageSrc = item.getAttribute('data-image');
    const imageAlt = item.querySelector('img').getAttribute('alt');
    allPhotos.push({ src: imageSrc, alt: imageAlt });
    
    // Add click handler
    item.addEventListener('click', () => {
        currentPhotoIndex = index;
        showLightbox();
    });
});

function showLightbox() {
    lightbox.style.display = 'flex';
    lightboxImage.src = allPhotos[currentPhotoIndex].src;
    lightboxImage.alt = allPhotos[currentPhotoIndex].alt;
    document.body.style.overflow = 'hidden';
}

function hideLightbox() {
    lightbox.style.display = 'none';
    document.body.style.overflow = 'auto';
}

function showNextPhoto() {
    currentPhotoIndex = (currentPhotoIndex + 1) % allPhotos.length;
    lightboxImage.src = allPhotos[currentPhotoIndex].src;
    lightboxImage.alt = allPhotos[currentPhotoIndex].alt;
}

function showPrevPhoto() {
    currentPhotoIndex = (currentPhotoIndex - 1 + allPhotos.length) % allPhotos.length;
    lightboxImage.src = allPhotos[currentPhotoIndex].src;
    lightboxImage.alt = allPhotos[currentPhotoIndex].alt;
}

// Event listeners
lightboxClose.addEventListener('click', hideLightbox);
lightboxNext.addEventListener('click', showNextPhoto);
lightboxPrev.addEventListener('click', showPrevPhoto);

// Close lightbox when clicking outside the image
lightbox.addEventListener('click', (e) => {
    if (e.target === lightbox) {
        hideLightbox();
    }
});

// Keyboard navigation
document.addEventListener('keydown', (e) => {
    if (lightbox.style.display === 'flex') {
        switch(e.key) {
            case 'Escape':
                hideLightbox();
                break;
            case 'ArrowRight':
                showNextPhoto();
                break;
            case 'ArrowLeft':
                showPrevPhoto();
                break;
        }
    }
});