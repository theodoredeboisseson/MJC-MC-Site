const MySite = {
    config: {
        carouselDelay: 3000,
        menuTransitionDelay: 300
    },

    mobileMenu: {
        init() {
            const elements = ['burger-button', 'close-button', 'mobile-menu'].map(id => document.getElementById(id));
            [this.burgerButton, this.closeButton, this.menu] = elements;
            if (!this.menu) return;

            this.panel = this.menu.querySelector('.fixed.inset-y-0');
            this.overlay = this.menu.querySelector('.fixed.inset-0');
            this.bindEvents();
        },

        bindEvents() {
            const handlers = [
                [this.burgerButton, () => this.open()],
                [this.closeButton, () => this.close()],
                [this.overlay, () => this.close()]
            ];
            handlers.forEach(([element, handler]) => element?.addEventListener('click', handler));
        },

        open() {
            this.menu.classList.remove('hidden');
            requestAnimationFrame(() => {
                this.overlay.classList.add('opacity-100');
                this.panel.classList.remove('translate-x-full');
            });
        },

        close() {
            this.overlay.classList.remove('opacity-100');
            this.panel.classList.add('translate-x-full');
            setTimeout(() => this.menu.classList.add('hidden'), MySite.config.menuTransitionDelay);
        }
    },

    wordCarousel: {
        init() {
            this.words = document.querySelectorAll('.rotating-text');
            if (this.words.length === 0) return;
            this.currentIndex = 0;
            this.startRotation();
        },

        startRotation() {
            setInterval(() => {
                const current = this.words[this.currentIndex];
                const next = this.words[(this.currentIndex + 1) % this.words.length];
                
                current.classList.remove('active');
                current.classList.add('hidden');
                next.classList.remove('hidden');
                next.classList.add('active');
                
                this.currentIndex = (this.currentIndex + 1) % this.words.length;
            }, MySite.config.carouselDelay);
        }
    },

    stickyHeader: {
        init() {
            const header = document.querySelector('[data-sticky-header]');
            if (!header) return;

            let lastScroll = 0;
            window.addEventListener('scroll', () => {
                const currentScroll = window.scrollY;
                header.classList.toggle('shadow-lg', currentScroll > 0);
                lastScroll = currentScroll;
            });
        }
    },
    
    init() {
        this.mobileMenu.init();
        this.wordCarousel.init();
        this.stickyHeader.init();
    }
};

document.addEventListener('DOMContentLoaded', () => MySite.init());

function toggleSubMenu(button) {
    const submenu = button.parentElement.nextElementSibling;
    const svg = button.querySelector('svg');

    // Close any other open submenu
    document.querySelectorAll('.submenu.open').forEach(openSubmenu => {
        if (openSubmenu !== submenu) {
            openSubmenu.style.maxHeight = 0;
            openSubmenu.classList.remove('open');
            const parentDiv = openSubmenu.previousElementSibling;
            if (parentDiv) {
                const btn = parentDiv.querySelector('button');
                if (btn) {
                    const otherSvg = btn.querySelector('svg');
                    otherSvg.classList.remove('rotate-180');
                }
            }
        }
    });

    if (submenu.classList.contains('open')) {
        submenu.style.maxHeight = 0;
        submenu.classList.remove('open');
        svg.classList.remove('rotate-180');
    } else {
        submenu.style.maxHeight = submenu.scrollHeight + "px";
        submenu.classList.add('open');
        svg.classList.add('rotate-180');
    }
}