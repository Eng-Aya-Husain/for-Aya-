from django.db import models
import random
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Governates(models.Model):
    gv_name = models.CharField(max_length=255)

    def __str__(self):
        return self.gv_name
    
class Areas(models.Model):
    governates = models.ForeignKey(Governates, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=255)

    def __str__(self):
        return self.area_name
    
class User(models.Model):
    USER_TYPE = [
        ('farmer','مزارع'),
        ('merchant','تاجر'),
        ('customer','عميل')    
    ]

    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    user_type = models.CharField(max_length=100, choices=USER_TYPE)
    phone_number = models.IntegerField(unique=True)
    password = models.IntegerField()
    image = models.ImageField(upload_to='photo/%y/%m/%d', null=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    account_number = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return f"Account {self.account_number} for {self.user.username}"

def generate_account_number():
    while True:
        account_number = ''.join(random.choices('0123456789', k=8))
        if not Account.objects.filter(account_number=account_number).exists():
            return account_number
        
@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance, account_number=generate_account_number())

class Transactions(models.Model):
    TRANSACTION_TYPE = [
        ('deposit','ايداع'),
        ('withdraw','خصم'),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=100, choices=TRANSACTION_TYPE)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.transaction_type} of {self.amount} on {self.transaction_date}"