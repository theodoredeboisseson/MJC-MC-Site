const MobileMenu = {
    init(menuTransitionDelay) {
        this.menuTransitionDelay = menuTransitionDelay;
        [this.burgerButton, this.closeButton, this.menu] = ['burger-button', 'close-button', 'mobile-menu'].map(id => document.getElementById(id));
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
        setTimeout(() => this.menu.classList.add('hidden'), this.menuTransitionDelay);
    }
};

export default MobileMenu;