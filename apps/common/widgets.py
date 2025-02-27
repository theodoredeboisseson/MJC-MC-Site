from wagtail.images.widgets import AdminImageChooser

class RepositionableImageWidget(AdminImageChooser):
    class Media:
        css = {
            'all': ['css/components/cropper.css']
        }
        js = ['js/cropper.min.js', 'js/reposition_image.js']