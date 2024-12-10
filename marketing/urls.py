from django.urls import path
from . import views
urlpatterns = [
    path('products/', views.Product_list, name='product_list'),
    path('products/create/', views.Create_Product, name='create_proudct'),
    path('products/update/<int:product_id>/', views.Update_Product, name='update_product'),
    path('products/delete/<int:product_id>/', views.Delete_Product, name='delete_product'),

    path('inventory/',views.Inventory_List, name='inventory_list'),
    path('inventory/create/',views. Create_Inventory, name='create_inventory'),
    path('inventory/edit/<int:inventory_id>/',views. Edit_Inventory, name='inventory_Update'),
    path('inventory/delete/<int:inventory_id>/', views.Delete_Inventory, name='Delete_Inventory'),
    path('inventory/delete/<int:inventory_id>/',views.inventory_detail, name='inventory_detail'),


   

    path('orders/',views.Order_List, name='order_list'),
    path('orders/create/', views.Create_Order, name='create_order'),
    path('orders/<int:order_id>/',views.Order_Detail, name='order_detail'),
    path('orders/<int:order_id>/edit/',views.Edit_Order, name='edit_order'),
    path('orders/<int:order_id>/delete/', views.Delete_Order, name='delete_order'),


]   





