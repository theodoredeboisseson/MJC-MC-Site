const WordCarousel = {
    init(carouselDelay) {
        this.carouselDelay = carouselDelay;
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
        }, this.carouselDelay || 3000);
    }
};

export default WordCarousel;