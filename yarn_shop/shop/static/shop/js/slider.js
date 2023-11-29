function Slider (array) {
    this.sliderURLs = array;
    this.currentIndex = 0;
    this.nextButton = document.querySelector('.slider_next');
    this.previousButton = document.querySelector('.slider_previous');
    this.sliderImage = document.querySelector('.product_image');

    this.initialization = () => {
        this.nextButton.addEventListener('click', () => {
            this.nextButtonClick();
        });

        this.previousButton.addEventListener('click',() => {
            this.previousButtonClick();
        });

        this.sliderImage.src =  this.sliderURLs[this.currentIndex];
        this.previousButton.disabled = true;
    };

    this.nextButtonClick = () => {
        this.currentIndex++;
        this.sliderImage.src = this.sliderURLs[this.currentIndex];
        this.previousButton.disabled = false;
        this.previousButton.classList.remove('disabled');

        if (this.currentIndex === (this.sliderURLs.length - 1)) {
            this.nextButton.disabled = true;
            this.nextButton.classList.add('disabled');
        };
    };
    
    this.previousButtonClick = () => {
        this.currentIndex--;
        this.sliderImage.src = this.sliderURLs[this.currentIndex];
        this.nextButton.disabled = false;
        this.nextButton.classList.remove('disabled');

        if (this.currentIndex === 0) {
            this.previousButton.disabled = true;
            this.previousButton.classList.add('disabled');
        };
    };
}

