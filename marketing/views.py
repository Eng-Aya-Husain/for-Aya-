from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from marketing.forms import InventoryForm, ProductForm
from marketing.models import Inventory, Product

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

   #from her 
def Create_Inventory(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم اضافة المخزون بنجاح')
            return redirect('inventory_list')
    else:
        form = InventoryForm()
    return render(request,'marketing/create_inventory.html',{'form':form})


def Inventory_List(request):
    inventories = Inventory.object.all()
    return render(request, 'marketing/inventory_list.html',{'inventories':inventories})


def inventory_detail(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    return render(request, 'marketing/inventory_detail.html',{'inventory':inventory})


def Edit_Inventory(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    if request.method == 'POST':
        form = InventoryForm(request.POST, request.FILES, instance=inventory)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم  تعديل بيانات العنصر بنجاح')
            return redirect('inventory_detail', inventory_id=inventory.id)
    else:
        form = InventoryForm(instance=inventory)
    return render(request,'marketing/edit_inventory.html',{'form':form, 'inventory':inventory})


def Delete_Inventory(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    if request.method == 'POST':
        inventory.delete()
        messages.success(request, 'تم حذف العنصر من المخزون بنجاح')
        return redirect('inventory_list')
    return render(request, 'marketing/delete_inventory.html', {'inventory':inventory})












