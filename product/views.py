from django.shortcuts import render , get_object_or_404
from .models import Product
from django.core.paginator import Paginator


def product_list(request):
    product_list = Product.objects.all()

    paginator = Paginator(product_list, 2) 
    page = request.GET.get('page')
    product_list = paginator.get_page(page)

    context = {'product_list' : product_list}
    return render(request , 'Product/product_list.html' , context)



def product_detail(request , slug):
    # prodcut_detail = Product.objects.get(PRDSLug=slug)
    prodcut_detail = get_object_or_404(Product ,PRDSLug=slug )
    context = {'prodcut_detail' : prodcut_detail}
    return render(request , 'Product/product_detail.html' , context)