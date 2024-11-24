from rest_framework import serializers , status
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import CategoryModel , ProductsModel , ShopCartModel
from core.serializers import UserRegisterSerializer

class CategorySerializer(ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ['name']

    def create(self, validated_data):
        if CategoryModel.objects.filter(name=validated_data['name']).exists():
            raise ValidationError('Thre is a such a category!!' , status.HTTP_400_BAD_REQUEST   )
    
        else:
            print(f"<<<<<<<<<<<<<<<<< {validated_data} >>>>>>>>")
            return CategoryModel.objects.create(**validated_data)



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