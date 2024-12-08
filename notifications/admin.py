from django.contrib import admin
from .models import Notifications,TransactinAlert,SeasonAlert,CropAlert
# Register your models here.

admin.site.register(Notifications)
admin.site.register(TransactinAlert)
admin.site.register(SeasonAlert)
admin.site.register(CropAlert)
