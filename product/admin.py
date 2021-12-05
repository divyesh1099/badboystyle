from django.contrib import admin
from django.contrib.admin.options import TabularInline
from .models import *
# from tinymce.widgets import TinyMCE
# Register your models here.
# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
   list_display = ["name", "type", "stock", "price"]
   class Media:
      js = ("assets/js/tinyInject.js",)

class VariationAdmin(admin.ModelAdmin):
   readonly_fields = ["generated_variation_id"]
   
admin.site.register(ProductImage)
admin.site.register(Shipping)
admin.site.register(Variation, VariationAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Type)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Specification)