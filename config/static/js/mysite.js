document.addEventListener('DOMContentLoaded', function () {
    const burgerButton = document.getElementById('burger-button');
    const closeButton = document.getElementById('close-button');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuPanel = mobileMenu.querySelector('.fixed.inset-y-0');
    const overlay = mobileMenu.querySelector('.fixed.inset-0');

    function openMobileMenu() {
        mobileMenu.classList.remove('hidden');
        // Allow time for the display change before starting animations
        requestAnimationFrame(() => {
            overlay.classList.add('opacity-100');
            mobileMenuPanel.classList.remove('translate-x-full');
        });
    }

    function closeMobileMenu() {
        overlay.classList.remove('opacity-100');
        mobileMenuPanel.classList.add('translate-x-full');
        // Wait for animations to finish before hiding
        setTimeout(() => {
            mobileMenu.classList.add('hidden');
        }, 300);
    }

    burgerButton.addEventListener('click', openMobileMenu);
    closeButton.addEventListener('click', closeMobileMenu);

    // Close menu when clicking overlay
    overlay.addEventListener('click', closeMobileMenu);
});