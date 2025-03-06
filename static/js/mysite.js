import MobileMenu from './modules/mobileMenu.js';
import WordCarousel from './modules/wordCarousel.js';
import StickyHeader from './modules/stickyHeader.js';

const MySite = {
    config: {
        carouselDelay: 3000,
        menuTransitionDelay: 300
    },

    init() {
        MobileMenu.init(this.config.menuTransitionDelay);
        WordCarousel.init(this.config.carouselDelay);
        StickyHeader.init();
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
window.toggleSubMenu = toggleSubMenu;

window.updateURLParameter = function(param, value) {
    const url = new URL(window.location.href);
    url.searchParams.set(param, value);
    window.location.href = url.toString();
};

window.toggleFilter = function(param, value) {
    const url = new URL(window.location.href);
    let values = url.searchParams.get(param) ? url.searchParams.get(param).split(',') : [];

    if (values.includes(value)) {
        values = values.filter(v => v !== value);
    } else {
        values.push(value);
    }

    if (values.length > 0) {
        url.searchParams.set(param, values.sort().join(','));
    } else {
        url.searchParams.delete(param);
    }

    window.location.href = url.toString();
};

// Utilisation pour les villes
window.toggleVille = function(ville) {
    toggleFilter('ville', ville);
};