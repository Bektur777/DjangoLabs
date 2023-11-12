from django import forms

from cloth.models import OrderCL


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderCL
        fields = ['user', 'products', 'total_amount']
