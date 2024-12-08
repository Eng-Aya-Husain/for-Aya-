from django import forms
from .models import Notifications, TransactinAlert, SeasonAlert, CropAlert

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notifications
        fields = ['title', 'message']

class TransactionAlertForm(forms.ModelForm):
    class Meta:
        model = TransactinAlert
        fields = ['notification', 'transaction']

class SeasonAlertForm(forms.ModelForm):
    class Meta:
        model = SeasonAlert
        fields = ['notification', 'season'] 

class CropAlertForm(forms.ModelForm):
    class Meta:
        model = CropAlert
        fields = ['notification', 'crop']
        