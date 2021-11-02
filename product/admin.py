from django.contrib import admin
from .models import *
# from tinymce.widgets import TinyMCE
# Register your models here.
# admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):

   list_display = ["name", "type", "stock", "price"]
   class Media:
      js = ("assets/js/tinyInject.js",)

admin.site.register(Product, ProductAdmin)
admin.site.register(Type)
admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Specification)