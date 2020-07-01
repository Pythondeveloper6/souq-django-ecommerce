from .models import Product, ProductImage
from django.contrib import admin

from product.models import ProductImage , Category , Product_Alternative , Product_Accessories


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_Alternative)
admin.site.register(Product_Accessories)