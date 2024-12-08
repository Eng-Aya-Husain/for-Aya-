from django.urls import path
from .views import Create_Inventory, Create_Product, Delete_Inventory, Inventory_List,Product_list,Update_Product,Delete_Product, inventory_detail,Edit_Inventory

urlpatterns = [
    path('products/', Product_list, name='product_list'),
    path('products/create/', Create_Product, name='create_proudct'),
    path('products/update/<int:product_id>/', Update_Product, name='update_product'),
    path('products/delete/<int:product_id>/', Delete_Product, name='delete_product'),

    path('inventory/', Inventory_List, name='inventory_list'),
    path('inventory/create/', Create_Inventory, name='create_inventory'),
    path('inventory/edit/<int:inventory_id>/', Edit_Inventory, name='inventory_Update'),
    path('inventory/delete/<int:inventory_id>/', Delete_Inventory, name='Delete_Inventory'),
    path('inventory/delete/<int:inventory_id>/',inventory_detail, name='inventory_detail'),

]   





