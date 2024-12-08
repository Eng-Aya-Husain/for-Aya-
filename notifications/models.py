from django.db import models
from users.models import Transactions
from plantations.models import AreaSeason,Crops
# Create your models here.

class Notifications(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.title
    
class TransactinAlert(models.Model):
    notification = models.ForeignKey(Notifications, on_delete=models.CASCADE)
    transaction = models.ForeignKey(Transactions, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notification for transaction {self.transaction.pk}"
    
class SeasonAlert(models.Model):
    notification = models.ForeignKey(Notifications, on_delete=models.CASCADE)
    season = models.ForeignKey(AreaSeason, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notification for season {self.season.season.season_name}"
    
class CropAlert(models.Model):
    notification = models.ForeignKey(Notifications, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crops, on_delete=models.CASCADE)

    def __str__(self):
        return f"Notificaton for crop {self.crop.crop_name}"
