from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import CategoryModel , ProductsModel , ShopCartModel
from core.serializers import UserRegisterSerializer
class CategorySerializer(ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ['name']



class ProductsSerializer(ModelSerializer):
    # category = serializers.SerializerMethodField(method_name= "category_fields")
    class Meta:
        model = ProductsModel
        fields = ['id' , 'name' , 'description' , 'price' , 'capacity' , 'category' , 'visit_number']

    # def category_fields(self,obj):
        # return obj.category.name

class ShopCartSerializer(ModelSerializer):
    user = UserRegisterSerializer(read_only = True)
    product = ProductsSerializer()

    class Meta:
        model = ShopCartModel
        fields = ['id' , 'user' , 'product']