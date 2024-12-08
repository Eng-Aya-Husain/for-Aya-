from django.db import models
from users.models import Areas,User
from django.core.validators import RegexValidator
from datetime import timedelta, date
from django.utils import timezone

# Create your models here.

class Seasons(models.Model):
    season_name = models.CharField(max_length=255)

    def __str__(self):
        return self.season_name
    
class AreaSeason(models.Model):
    area = models.ForeignKey(Areas, on_delete=models.CASCADE)
    season = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    start_date = models.CharField(max_length=5, validators=[RegexValidator(regex=r'^\d{2}-\d{2}$')])
    end_date = models.CharField(max_length=5, validators=[RegexValidator(regex=r'^\d{2}-\d{2}$')])

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['area','season'], name='unique_area_season')
        ]

    def __str__(self):
        return f"season {self.season.season_name} in {self.area.area_name}"

class Categories(models.Model):
    TYPE_CHOICES = [
        ('frute','الفواكه'),
        ('vegetable','الخضار'),
        ('grain','الحبوب'),
        ('herbs','الاعشاب'),
        ('ornamental','الزينة'),
    ]

    category_name = models.CharField(max_length=255, choices=TYPE_CHOICES)

    def __str__(self):
        return self.category_name


class Plants(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='plants')
    plant_name = models.CharField(max_length=255)
    water_requirement = models.IntegerField()
    fertilizer_requirement = models.IntegerField()
    harvest = models.IntegerField()
    informations = models.TextField()
    image = models.ImageField(upload_to='photo/%y/%m/%d')
    img1 = models.ImageField(upload_to='photo/%y/%m/%d')
    img2 = models.ImageField(upload_to='photo/%y/%m/%d')
    img3 = models.ImageField(upload_to='photo/%y/%m/%d')

    def __str__(self):
        return self.plant_name
    
class Crops(models.Model):
    STATUS_CHOICES = [
        ('qrowing','ينمو'),
        ('harvested','تم الحصاد'),
        ('failed','تالف'),
    ]

    plant = models.ForeignKey(Plants, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crop_name = models.CharField(max_length=255)
    planting_date = models.DateField(default=timezone.now)
    next_watering_date = models.DateField(null=True, blank=True)
    next_fertilization_date = models.DateField(null=True, blank=True)
    harvest_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='growing')


    def calculate_next_dates(self):
        if not self.next_watering_date:
            self.next_watering_date = self.planting_date + timedelta(days=self.plant.water_requirement)
        if not self.next_fertilization_date:
            self.next_fertilization_date = self.planting_date + timedelta(days=self.plant.fertilizer_requirement)
        if not self.harvest_date:
            self.harvest_date = self.planting_date + timedelta(days=self.plant.harvest)

    def __str__(self):
        return self.crop_name