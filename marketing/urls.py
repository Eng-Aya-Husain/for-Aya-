from django.urls import path
from .views import Create_Product,Product_list,Update_Product,Delete_Product

urlpatterns = [
    path('marketing/', Product_list, name='product_list'),
    path('marketing/create/', Create_Product, name='create_proudct'),
    path('marketing/update/<int:product_id>/', Update_Product, name='update_product'),
    path('marketing/delete/<int:product_id>/', Delete_Product, name='delete_product'),
]
