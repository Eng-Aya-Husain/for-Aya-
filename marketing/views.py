from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from marketing.forms import ProductForm
from marketing.models import Product

# Create your views here.

def Create_Product(request):
    if request.method=='POST':
        form = ProductForm (request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم اضافة المنتج بنجاح')
            return redirect('product_list') 
    else:
        form = ProductForm()
    return render(request, 'marketing/create_product.html',{'form':form})  
           
def Product_list(request):
    products = Product.objects.all()
    return render(request, 'marketing/product_list.html',{'products':products})

def Update_Product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل المنتج بنجاح')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'marketing/update_product.html',{'form':form, 'product':product})
    
def Delete_Product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'تم الحذف بنجاح')
        return redirect('product_list')
    return render(request, 'marketing/delete_product.html',{'product':product})  

   