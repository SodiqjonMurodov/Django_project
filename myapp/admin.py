from django.contrib import admin
from django.utils.safestring import mark_safe

from myapp import models


class Main(admin.ModelAdmin):
    list_display = ('id', 'category')
    list_editable = ('category',)


class Main2(admin.ModelAdmin):
    list_display = ('name', 'price', 'kg', 'get_image')
    list_display_links = ('name', 'price', 'kg')
    list_filter = ('category', )
    search_fields = ('name', 'price', 'kg', 'category')
    list_per_page = 5

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'image'


admin.site.register(models.Categories, Main)
admin.site.register(models.Fruits, Main2)
