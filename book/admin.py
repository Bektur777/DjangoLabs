from django.contrib import admin
from book.models import *

# Register your models here.


@admin.register(Book)
class ModelBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cost', )
    list_display_links = ('title', )


@admin.register(ReviewBook)
class ModelReviewBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_review', 'rate_stars', )
    list_display_links = ('id', )
