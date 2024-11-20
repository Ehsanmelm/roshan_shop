from django.db import models
from django.conf import settings
# Create your models here.


class CategoryModel(models.Model):
    name = models.CharField(max_length=255 )

    def __str__(self):
        return f'{self.name}'
    

class ProductsModel(models.Model):
    category = models.ForeignKey(CategoryModel , on_delete= models.CASCADE)

    name = models.CharField(max_length=255)
    description = models.TextField()
    capacity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10 , decimal_places=2)

    def __str__(self):
        return f'{self.name}'
    
class ShopCartModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE)
    product = models.ForeignKey(ProductsModel , on_delete= models.CASCADE)