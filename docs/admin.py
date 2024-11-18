from pydoc import Doc
from django.contrib import admin

from docs.models import Category, Product, Doctor, Record


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Doctor)
admin.site.register(Record)