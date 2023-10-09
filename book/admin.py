from django.contrib import admin
from book.models import *

# Register your models here.


@admin.register(Book)
class ModelNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cost', )
    list_display_links = ('title', )
