from django.db.models import Max
from celery import shared_task
import csv
from .models import ProductsModel , CategoryModel

@shared_task
def list_highest_visit_product_task():
    most_view_number = ProductsModel.objects.aggregate(max_visit =Max('visit_number'))['max_visit']
    popular_products = ProductsModel.objects.filter(visit_number= most_view_number)

    with open('/app/popular_products.csv' , 'a' , newline='') as file:
        fieldnames = ['product' , 'category' , 'view']
        writer = csv.DictWriter(file , fieldnames=fieldnames)

        if file.tell() == 0:
            writer.writeheader()
        for product in popular_products:
            writer.writerow({
            'product' : product.name,
            'category' : product.category,
            'view' : product.visit_number
            })
    print(f"################ hi from task #############")