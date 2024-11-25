from django.shortcuts import render , get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated 
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from .permissions import IsAdminOrReadOnly
from .models import CategoryModel , ProductsModel , ShopCartModel
from core.models import User
from .serializers import CategorySerializer , ProductsSerializer , ShopCartSerializer

# Create your views here.

class ProductsView(ModelViewSet):

    permission_classes= [IsAuthenticated , IsAdminOrReadOnly]
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializer


class CategoryView(ModelViewSet):

    permission_classes = [IsAuthenticated , IsAdminOrReadOnly]
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer


    @action(detail=True , methods=['GET' , 'POST'] , permission_classes= [IsAuthenticated , IsAdminOrReadOnly] , serializer_class=ProductsSerializer)
    def products(self,request , pk):

        if request.method == "GET":
            products = ProductsModel.objects.filter(category_id=pk)
            serializer = ProductsSerializer(products , many=True)
        
        elif request.method == "POST":
            serializer = ProductsSerializer(data = request.data)
            serializer.is_valid(raise_exception=True)

            category = CategoryModel.objects.get(id= pk)

            serializer.validated_data['category'] = category
            serializer.save()   
        
        else:
            raise ValidationError('Not Allowed Request' , status = status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)
    

class Add2ShopCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request , pk):
        user = request.user
        product = get_object_or_404(ProductsModel , id=pk)

        if product.capacity >0 and ShopCartModel.objects.filter(user=user , product=product).exists() is False:
            ShopCartModel.objects.create(user=user , product=product)
            product.capacity -=1
            product.save()
        
        else:
            raise ValidationError('You cant add this to your cart' , status.HTTP_400_BAD_REQUEST)
        
        return Response("Add Success" , status=status.HTTP_200_OK)
    

class RemoveFromShopCartView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ShopCartSerializer

    def delete(self,request , pk):
        
        user = request.user
        product = get_object_or_404(ProductsModel , id=pk)

        if ShopCartModel.objects.filter(user=user , product=product).exists():
            cart_stuff = ShopCartModel.objects.get(user=user , product=product)
            cart_stuff.delete()

            return Response("delete Success",status=status.HTTP_204_NO_CONTENT)
            
        else:
            raise ValidationError('No such a product is in your shopping cart' , status.HTTP_400_BAD_REQUEST)
        

class ShopCartView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        queryset = ShopCartModel.objects.filter(user=request.user)
        serializer = ShopCartSerializer(queryset , many=True)

        return Response(serializer.data)    
    
class ClearShopCartView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self,request):        

        ShopCartModel.objects.filter(user=request.user).delete()

        return Response("Clear Success" , status= status.HTTP_204_NO_CONTENT)
