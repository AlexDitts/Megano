from django.contrib import admin
from .models import Category, Goods


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class GoodsAdmin(admin.ModelAdmin):
    list_display = ["title", 'activity']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)