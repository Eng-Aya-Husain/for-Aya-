from django.contrib import admin
from .models import Product,Inventory,Orders,UserReview
# Register your models here.

admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Orders)
admin.site.register(UserReview)
