document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('photoModal');
    const modalImg = document.getElementById('modalImage');
    const closeBtn = document.querySelector('.photo-modal .close');

    document.querySelectorAll('img.clickable-image, .richtext-content img').forEach(function(img) {
        img.addEventListener('click', function() {
            modal.style.display = 'flex';
            modalImg.src = this.src;
        });
    });

    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
});