document.addEventListener('DOMContentLoaded', function() {
    const modal = document.getElementById('imageViewer');
    const modalImg = document.getElementById('modalImage');
    const closeBtn = document.querySelector('.image-viewer .close');

    document.querySelectorAll('img.clickable-image, .richtext-content img').forEach(function(img) {
        img.addEventListener('click', function() {
            modal.style.display = 'flex';
            modalImg.src = this.src;
            document.body.classList.add('no-scroll');
        });
    });

    closeBtn.addEventListener('click', function() {
        modal.style.display = 'none';
        document.body.classList.remove('no-scroll');
    });

    modal.addEventListener('click', function(e) {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
        document.body.classList.remove('no-scroll');
    });
});