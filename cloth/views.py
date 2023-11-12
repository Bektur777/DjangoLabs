from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView

from cloth.forms import OrderForm
from cloth.models import *

# Create your views here.


class ProductFilter():
    def get_tags(self):
        return TagCL.objects.all()


class FilterProductView(ProductFilter, ListView):
    paginate_by = 3
    template_name = 'product_list.html'

    def get_queryset(self):
        if 'tags' in self.request.GET:
            queryset = ProductCL.objects.filter(
                Q(tags__in=self.request.GET.getlist("tags")),
            ).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tags'] = ''.join([f'tags={x}&' for x in self.request.GET.getlist('tags')])
        return context


class ProductView(ListView, ProductFilter):
    model = ProductCL
    queryset = ProductCL.objects.filter().order_by('-id')
    paginate_by = 3
    template_name = 'product_list.html'


@require_POST
def order(request):
    product = request.POST.get('product')
    total_amount = request.POST.get('price') * request.POST.get('count')

    make_order = OrderCL.objects.create(user=request.user, products=product, total_amount=total_amount)

    return redirect('')
