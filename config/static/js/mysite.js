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

    dropdownMenu: {
        init() {
            this.dropdowns = document.querySelectorAll('.group .absolute');
            if (this.dropdowns.length === 0) return;
            this.adjustPositions();
            this.bindEvents();
        },

        adjustPositions() {
            if (window.innerWidth < 1024) return;
            
            const viewportWidth = window.innerWidth;
            this.dropdowns.forEach(menu => {
                const isOverflowing = menu.getBoundingClientRect().right > viewportWidth;
                menu.style.left = isOverflowing ? 'auto' : '0';
                menu.style.right = isOverflowing ? '0' : 'auto';
            });
        },

        bindEvents() {
            const debounce = (fn, delay) => {
                let timeout;
                return () => {
                    clearTimeout(timeout);
                    timeout = setTimeout(() => fn(), delay);
                };
            };

            window.addEventListener('resize', debounce(() => this.adjustPositions(), 100));

            const observer = new MutationObserver(() => {
                setTimeout(() => this.adjustPositions(), 10);
            });

            this.dropdowns.forEach(dropdown => {
                observer.observe(dropdown, {
                    attributes: true,
                    attributeFilter: ['class']
                });
            });
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
        ['dropdownMenu', 'mobileMenu', 'wordCarousel','stickyHeader'].forEach(module => this[module].init());
    }
};

document.addEventListener('DOMContentLoaded', () => MySite.init());