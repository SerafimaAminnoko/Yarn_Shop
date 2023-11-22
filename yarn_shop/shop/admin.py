from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Producer)
class ProducerAdmin(admin.ModelAdmin):
    list_display = ['prod',]


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['count',]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'cat', 'url']
    list_display_links = ('cat',)
    prepopulated_fields = {'url': ('cat',)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'url', 'price', 'cat', 'image', 'get_image',]
    list_display_links = ['name', ]
    prepopulated_fields = {'url': ('name',)}
    readonly_fields = ('get_image',)
    list_filter = ('prod', 'price', 'count')
    search_fields = ('name',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" />')

    get_image.short_description = "Image"


@admin.register(YarnImages)
class YarnImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'subcat', 'image', 'get_image']
    list_display_links = ('title',)
    readonly_fields = ('get_image',)
    list_filter = ('subcat',)
    search_fields = ('title',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" />')

    get_image.short_description = "Image"


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['col',]
    list_display_links = ['col',]


@admin.register(Yarn)
class YarnAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_image', 'col', 'time_add', 'time_update', 'availability']
    list_display_links = ('name',)
    prepopulated_fields = {'url': ('name',)}
    readonly_fields = ('get_image',)
    list_editable = ('availability',)
    list_filter = ('col', 'availability', 'subcat',
                   'subcat__prod', 'subcat__price', 'subcat__count'
                   )
    search_fields = ('name',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" />')

    get_image.short_description = "Image"













