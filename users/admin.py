from django.contrib import admin
from .models import Governates,Areas,User,Account,Transactions
# Register your models here.

admin.site.register(Governates)
admin.site.register(Areas)
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Transactions)