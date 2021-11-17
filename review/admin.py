from django.contrib import admin
from django.db import models
from .models import Review, ReviewImage
# Register your models here.

class ReviewImageAdmin(admin.StackedInline):
    model = ReviewImage

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "rating", "edited"]
    inlines = [ReviewImageAdmin]

admin.site.register(ReviewImage)
admin.site.register(Review, ReviewAdmin)