from django.contrib import admin
from cloth.models import *

# Register your models here.


@admin.register(TagCL)
class ModelTagCLAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('name', )


@admin.register(CustomerCL)
class ModelCustomerCLAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'address', )
    list_display_links = ('id', )


@admin.register(ProductCL)
class ModelProductCLAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', )
    list_display_links = ('name', )


@admin.register(OrderCL)
class ModelOrderCLAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_date', 'total_amount', )
    list_display_links = ('id',)

