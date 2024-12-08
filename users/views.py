from django.shortcuts import render, redirect, get_object_or_404
from .models import Governates, Areas, User, Account, Transactions
from .forms import GovernateForm, AreaForm, UserForm, AccountForm, TransactionForm
from django.contrib import messages
from django.urls import reverse
from decimal import Decimal, InvalidOperation
from django.utils.timezone import now
# Create your views here.

# المحافظات 
def Governates_List(request):
    governates = Governates.objects.all()
    return render(request, 'users/governate_list.html', {'governates':governates})

def Add_Governate(request):
    if request.method == 'POST':
        form = GovernateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'create Governate successfully.')
            return redirect(reverse('governate_list'))
    else:
        form = GovernateForm()
    return render(request, 'users/add_governate.html', {'form':form})

def Edit_Governate(request, governate_id):
    governate = get_object_or_404(Governates, id=governate_id)
    if request.method == 'POST':
        form = GovernateForm(request.POST, request.FILES, instance=governate)
        if form.is_valid():
            form.save()
            messages.success(request, 'update Governate successfully.')
            return redirect('governate_list')
    else:
        form =GovernateForm(instance=governate)
    return render(request, 'users/edit_governate.html', {'form':form, 'governate':governate})

def Delete_Governate(request, governate_id):
    governate = get_object_or_404(Governates, id=governate_id)
    if request.method == 'POST':
        governate.delete()
        messages.success(request, 'delete Governate successfully.')
        return redirect(reverse('governate_list'))
    return render(request, 'users/delete_governate.html', {'governate':governate})


#المناطق 
def Areas_List(request, governate_id):
    governate = get_object_or_404(Governates, id=governate_id)
    areas = Areas.objects.filter(governates_id=governate_id)
    return render (request, 'users/areas_list.html',{'governate':governate, 'areas':areas})

    
def Add_Area(request, governate_id):
    governate = get_object_or_404(Governates, id=governate_id)
    if request.method == 'POST':
        form = AreaForm(request.POST, request.FILES)
        if form.is_valid():
            area = form.save(commit=False)
            area.governates = governate
            area.save()
            messages.success(request, 'create Area successfully.')
            return redirect(reverse('area_list', kwargs={'governate_id' : governate.id}))
    else:
        form = AreaForm()
    return render(request, 'users/add_area.html', {'form':form, 'governate':governate})

def Edit_Area(request,governate_id, area_id):
    governate = get_object_or_404(Governates, id=governate_id)
    area = get_object_or_404(Areas, id=area_id, governates=governate)
    if request.method == 'POST':
        form = AreaForm(request.POST, request.FILES, instance=area)
        if form.is_valid():
            form.save()
            messages.success(request, 'update Area successfully.')
            return redirect(reverse('area_list',kwargs={'governate_id' : governate.id}))
    else:
        form = AreaForm(instance=area)
    return render(request, 'users/edit_area.html', {'form':form, 'governate':governate, 'area':area})

def Delete_Area(request, area_id, governate_id):
    governate = get_object_or_404(Governates, id=governate_id)
    area = get_object_or_404(Areas, id=area_id, governates=governate )
    if request.method == 'POST':
        area.delete()
        messages.success(request, 'delete Area successfully.')
        return redirect(reverse('area_list', kwargs={'governate_id' : governate.id}))
    return render(request, 'users/delete_area.html', {'area':area, 'governate':governate})

#المستخدمين
def User_List(request, area_id):
    area = get_object_or_404(Areas, id=area_id)
    users = User.objects.filter(area_id=area_id)
    return render(request, 'users/users_list.html', {'users':users, 'area':area})

def Add_User(request, area_id):
    area = get_object_or_404(Areas, id=area_id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.area = area
            user.save()
            messages.success(request, 'create User successfully.')
            return redirect(reverse('user_list', kwargs={'area_id':area.id}))
    else:
        form = UserForm()
    return render(request, 'users/add_user.html', {'form':form, 'area':area})

def Edit_User(request, area_id, user_id):
    area = get_object_or_404(Areas, id=area_id)
    user = get_object_or_404(User, id=user_id, area=area)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'update User successfully.')
            return redirect(reverse('user_list', kwargs={'area_id':area.id}))
    else:
        form = UserForm(instance=user)
    return render(request, 'users/edit_user.html', {'form':form ,'user':user, 'area':area})  

def Delete_User(request, area_id, user_id):
    area = get_object_or_404(Areas, id=area_id)
    user = get_object_or_404(User, id=user_id, area=area)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'delete User successfully.')
        return redirect(reverse('user_list', kwargs={'area_id':area.id}))
    return render(request, 'users/delete_user.html', {'user':user, 'area':area})

# الحسابات
def Account_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    account = get_object_or_404(Account, user=user)
    return render(request, 'users/account_list.html', {'account':account, 'user':user})


def Add_Balance(request, account_id, user_id):
    user = get_object_or_404(User, id=user_id)
    account = get_object_or_404(Account, id=account_id, user=user)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        try:
            amount = Decimal(amount)
            if amount > 100:
                account.balance += amount
                account.save()

                Add_Transaction(
                    account=account,
                    amount=amount,
                    transaction_type='deposit',
                    description=f"تم ايداع مبلغ {amount}الى الحساب"
                )
                messages.success(request, f'تم اضافة {amount} الى رصيد الحساب بنجاح')
                return redirect(reverse('account_list', kwargs={'user_id':user.id}))
            else:
                messages.error(request, 'يجب ان يكون المبلغ اكثر من المبلغ المحدد')
        except (InvalidOperation, ValueError):
            messages.error(request, 'يرجى ادخال مبلغ صالح')
    return render(request, 'users/add_balance.html', {'account':account, 'user':user})                    

def Withdraw_balance(request, user_id, account_id):
    user = get_object_or_404(User, id=user_id)
    account = get_object_or_404(Account, id=account_id, user=user)

    if request.method == 'POST':
        amount = request.POST.get('amount',0)
        try:
            amount = Decimal(amount)
            if amount < 1000:
                messages.error(request,"لا يمكنك سحب مبلغ اقل من 1000 ريال")
            elif amount > account.balance:
                messages.error(request, "رصيدك أقل من المبلغ المحدد ")
            else:
                account.balance -= amount
                account.save()

                Add_Transaction(
                    account=account,
                    amount=amount,
                    transaction_type='withdraw',
                    description=f"تم سحب مبلغ {amount} من الحساب {account.account_number}"
                )

                messages.success(
                    request,
                    f"تم سحب مبلغ {amount} من الحساب {account.account_number}. "
                    f"المتبقي من الرصيد: {account.balance}"
                )
                return redirect(reverse('account_list', kwargs={'user_id':user.id}))
        except Exception as e:
            messages.error(request, "حدث خطأ أثناء عملية السحب")
        
    return render(request, 'users/withdraw_balance.html', {'account':account, 'user':user})

#المعاملات المالية 
def Transaction_list(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    transaction = Transactions.objects.filter(account=account).order_by('-transaction_date')
    return render(request, 'users/transaction_list.html', {'account':account ,'transaction':transaction})

def Add_Transaction(account, amount, transaction_type, description=None):
    Transactions.objects.create(
        account = account,
        amount = amount,
        transaction_type = transaction_type,
        description = description,
        transaction_date =now()
    )
   
def Edit_Transaction(request, transaction_id):
    transaction = get_object_or_404(Transactions, id=transaction_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST, request.FILES, instance=transaction)
        if form.is_valid():
            form.save()
            messages.success(request, 'update Transaction successfully.')
            return redirect(reverse('transaction_list'))
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'users/edit_transaction.html', {'form':form, 'transaction':transaction})

def Delete_Transaction(request, transaction_id):
    transaction = get_object_or_404(Transactions, id=transaction_id)
    if request.method == 'POST':
       transaction.delete()
       messages.success(request, 'delete Transaction successfully.')
       return redirect(reverse('transaction_list'))
    return render (request, 'users/delete_transaction.html', {'transaction':transaction})
