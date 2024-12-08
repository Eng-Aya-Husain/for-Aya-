from django import forms
from .models import Product, Inventory, Orders, UserReview

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['crop', 'user', 'categories', 'product_name', 'product_image', 'quantity', 'unite', 'unite_price', 'ex_date', 'product_state']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['user', 'type', 'image', 'quantity', 'unit', 'unite_price', 'pr_date', 'ex_date', 'inventory_state']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['user', 'type', 'quantity', 'unit', 'total_price', 'status']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        fields = ['revewer', 'valuation', 'comment', 'review_date']

