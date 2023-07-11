from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('upc', 'category', 'name', 'artist', 'country',
                    'price', 'rating', 'image'
                    )

    ordering = ('category', 'name')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
