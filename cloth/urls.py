from django.urls import path
from cloth.views import *

urlpatterns = [
    path('', ProductView.as_view(), name='product_view'),
    path('products/filter/', FilterProductView.as_view(), name='filter'),
    path('products/order/create', order, name='order'),
]
