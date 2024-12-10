from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from marketing.forms import InventoryForm, OrderForm, ProductForm
from marketing.models import Inventory, Orders, Product

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




def Create_Order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'تم اضافة الطلب بنجاح')
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'order/create_order.html',{'form':form})  


def Order_List(request):
    orders = Orders.object.all()
    return render(request, 'orders/order_list.html', {'orders':orders})


def Order_Detail(request, order_id):
    order = get_object_or_404(Orders, id=order_id)
    return render(request, 'orders/order_detail.html', {'order':order})


def Edit_Order(request, Order_id):
    order = get_object_or_404(Orders, id=Order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل بيانات الطلب بنجاح')
            return redirect('order_detail', Order_id=Order_id)
    else:
        form = OrderForm(instance=order)
        return render(request, 'orders/edit_order.html', {'form':form, 'order':order})
    

def Delete_Order(request, order_id):
        order = get_object_or_404(Orders, id=order_id)
        if request.method == 'POST':
            order.delete()
            messages.success(request, 'تم حذف الطلب بنجاح')
            return render(request, 'orders/delete_order.html', {'order':order})

    
    
            







