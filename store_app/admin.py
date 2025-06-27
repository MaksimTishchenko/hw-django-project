from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    prepopulated_fields = {'description': ('name',)}  # опционально

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)