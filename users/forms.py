from django import forms
from.models import Governates, Areas, User, Account, Transactions

class GovernateForm(forms.ModelForm):
    class Meta:
        model = Governates
        fields = ['gv_name']

class AreaForm(forms.ModelForm):
    class Meta:
        model = Areas
        fields = ['area_name',]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'user_type', 'phone_number', 'password', 'image', 'status']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['balance']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ['account', 'transaction_type', 'amount', 'description']

