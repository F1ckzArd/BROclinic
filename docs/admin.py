from pydoc import Doc
from django.contrib import admin

# Register your models here.
from docs.models import Category, Product, Doctor, Record

#admin.site.register(Categories)
#admin.site.register(Products)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Doctor)
admin.site.register(Record)