const StickyHeader = {
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
};

export default StickyHeader;