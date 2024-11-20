from . import views
from django.urls import path 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products' , views.ProductsView , basename='products')
router.register('categories' , views.CategoryView , basename='categories')

urlpatterns = [
    path('cart/add/<int:pk>/' , views.Add2ShopCartView.as_view() , name = 'add_to_shop_cart'),
    path('cart/remove/<int:pk>/' , views.RemoveFromShopCartView.as_view() , name = 'remove_from_shop_cart'),
    path('cart/' , views.ShopCartView.as_view() , name = 'shop_cart'),
    path('cart/clear' , views.ClearShopCartView.as_view() , name = 'clear_shopp_cart'),
]

urlpatterns += router.urls