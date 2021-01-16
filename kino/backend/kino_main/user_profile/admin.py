from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "get_image")
    list_display_links = ("user",)
    
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="100" height="100"')
    get_image.short_description = "Ава"