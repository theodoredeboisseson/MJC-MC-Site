document.addEventListener('DOMContentLoaded', function() {
    const imageInput = document.querySelector('.image-chooser-wrapper img');
    if (!imageInput) return;

    // Initialize CropperJS on the image
    const cropper = new Cropper(imageInput, {
        aspectRatio: NaN,
        viewMode: 1,
        autoCropArea: 1,
        movable: true,
        zoomable: true,
        rotatable: true,
        scalable: true,
        crop(event) {
            // You can add logic to store crop data (position, zoom, etc.)
            console.log(event.detail);
        },
    });
});