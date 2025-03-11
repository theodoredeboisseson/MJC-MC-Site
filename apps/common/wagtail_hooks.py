from laces.components import Component
from wagtail import hooks
import shutil

class StorageLimitPanel(Component):
    order = 9999
    
    def render_html(self, parent_context):
        total, used, free = shutil.disk_usage("/")
        total_gb = total // (2 ** 30)
        used_gb = used // (2 ** 30)
        free_gb = free // (2 ** 30)
        used_percentage = int((used / total) * 100)
        from django.template.loader import render_to_string
        
        return render_to_string('common/components/storage_limit_panel.html', {
            'total_gb': total_gb,
            'used_gb': used_gb,
            'free_gb': free_gb,
            'used_percentage': used_percentage,
        })

@hooks.register("construct_homepage_panels")
def add_storage_limit_panel(request, panels):
    panels.append(StorageLimitPanel())