from django import forms
from .models import Seasons, AreaSeason, Categories, Plants, Crops
from users.models import Areas
class SeasonForm(forms.ModelForm):
    class Meta:
        model = Seasons
        fields = ['season_name']

class AreaSeasonForm(forms.ModelForm):
    area = forms.ModelChoiceField(
        queryset=Areas.objects.all(),
        label='المنطقة',
        widget=forms.Select(attrs={'class':'form-control'})
    )
    class Meta:
        model = AreaSeason
        fields = ['area', 'start_date', 'end_date']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['category_name']

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plants
        fields = ['plant_name', 'water_requirement', 'fertilizer_requirement', 'harvest', 'informations', 'image', 'img1', 'img2', 'img3']

class CropForm(forms.ModelForm):
    class Meta:
        model = Crops
        fields = ['plant', 'crop_name']

class UpdateCropForm(forms.ModelForm):
    class Meta:
        model = Crops
        fields = ['status']

class WateringForm(forms.Form):
    crop_id = forms.IntegerField(widget=forms.HiddenInput)

class FertilizationForm(forms.Form):
    crop_id = forms.IntegerField(widget=forms.HiddenInput)

