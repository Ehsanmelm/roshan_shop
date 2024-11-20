from django.contrib import admin
from .models import CategoryModel , ProductsModel , ShopCartModel

# Register your models here.

admin.site.register(CategoryModel)
admin.site.register(ProductsModel)
admin.site.register(ShopCartModel)