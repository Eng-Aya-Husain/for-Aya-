from django.shortcuts import render, redirect, get_object_or_404
from .models import Seasons, AreaSeason, Categories, Plants, Crops
from .forms import SeasonForm, AreaSeasonForm, CategoryForm, PlantForm, CropForm, UpdateCropForm, WateringForm, FertilizationForm
from django.contrib import messages
from django.urls import reverse
from users.models import Areas,User
from datetime import date, timedelta

# Create your views here.

#المواسم الزراعية
def Season_list(request):
    seasons = Seasons.objects.all()
    return render(request, 'plantations/season_list.html', {'seasons':seasons})

def Add_season(request):
    if request.method == 'POST':
        form = SeasonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة الموسم بنجاح')
            return redirect(reverse('season_list'))
    else:
        form = SeasonForm()
    return render(request, 'plantations/add_season.html', {'form':form})

def Edit_season(request, season_id):
    season = get_object_or_404(Seasons, id=season_id)
    if request.method == 'POST':
        form = SeasonForm(request.POST, request.FILES, instance=season)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث بيانات الموسم بنجاح')
            return redirect(reverse('season_list'))
    else:
        form = SeasonForm(instance=season)
    return render(request, 'plantations/edit_season.html', {'form':form, 'season':season})

def Delete_season(request, season_id):
    season = get_object_or_404(Seasons, id=season_id)
    if request.method == 'POST':
        season.delete()
        messages.success(request, 'تم حذف الموسم بنجاح')
        return redirect(reverse('season_list'))
    return render(request, 'plantations/delete_season.html', {'season':season})


#مواسم المنطقة
def Area_season_list(request, season_id):
    season = get_object_or_404(Seasons, id=season_id)
    area_season = AreaSeason.objects.filter(season=season).select_related('area')
    return render(request, 'plantations/area_season_list.html',{'season':season, 'area_season':area_season})

def Add_area_season(request, season_id):
    season = get_object_or_404(Seasons, id=season_id)
    if request.method == 'POST':
        form = AreaSeasonForm(request.POST, request.FILES)
        if form.is_valid():

            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            if start_date >= end_date:
                messages.error(request, 'لا يمكن ان تكون نهاية الموسم قبل بدايته')
            else:
                area_season = form.save(commit=False)
                area_season.season = season
                area_season.save()
                messages.success(request, 'تم إضافة موسم المنطقة بنجاح')
                return redirect(reverse('area_season_list', kwargs={'season_id':season.id}))
        else:
            messages.error(request, 'تنسيق التاريخ الذي قمت بادخاله غير صحيح')
    else:
        form = AreaSeasonForm()
    return render(request, 'plantations/add_area_season.html', {'form':form, 'season':season})
    
def Edit_area_season(request, season_id, area_season_id):
    season = get_object_or_404(Seasons, id=season_id)
    area_season = get_object_or_404(AreaSeason, id=area_season_id, season=season)
    if request.method == 'POST':
        form = AreaSeasonForm(request.POST, request.FILES, instance=area_season)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل بيانات موسم المنطقة بنجاح')
            return redirect(reverse('area_season_list', kwargs={'season_id':season.id}))
    else:
        form = AreaSeasonForm(instance=area_season)
        return render(request, 'plantations/edit_area_season.html',{'form':form, 'season':season, 'area_season':area_season})
    
def Delete_area_season(request, season_id, area_season_id):
    season = get_object_or_404(Seasons, id=season_id)
    area_season = get_object_or_404(AreaSeason, id=area_season_id, season=season)
    if request.method == 'POST':
        area_season.delete()
        messages.success(request, 'تم الحذف بنجاح')
        return redirect(reverse('area_season_list', kwargs={'season_id':season.id}))
    return render(request, 'plantations/delete_area_season.html', {'season':season, 'area_season':area_season})

#أصناف النباتات
def Category_list(request):
    category = Categories.objects.prefetch_related('plants').all()
    return render(request, 'plantations/category_list.html', {'category':category})

def Add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة الصنف بنجاح')
            return redirect(reverse('category_list'))
    else:
        form = CategoryForm()
    return render(request, 'plantations/add_category.html',{'form':form})

def Edit_category(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل الصنف بنجاح')
            return redirect(reverse('category_list'))
    else:
        form = CategoryForm(instance=category)
    return render(request, 'plantations/edit_category.html',{'form':form, 'category':category})

def Delete_category(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'تم حذف الصنف بنجاح')
        return redirect(reverse('category_list'))
    return render(request, 'plantations/delete_category.html', {'category':category})

#النباتات
def Plant_list(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    plants = Plants.objects.filter(category=category)
    return render(request, 'plantations/plant_list.html', {'category':category, 'plants':plants})

def Plant_detail(request, category_id, plant_id):
    category =get_object_or_404(Categories, id=category_id)
    plant = get_object_or_404(Plants, id=plant_id, category=category)
    return render(request, 'plantations/plant_detail.html', {'category':category, 'plant':plant})

def Add_plant(request, category_id):
    category = get_object_or_404(Categories, id=category_id)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            plant = form.save(commit=False)
            plant.category = category
            plant.save()
            messages.success(request, 'تم إضاة النبات بنجاح')
            return redirect(reverse('plant_list', kwargs={'category_id':category.id}))
    else:
        form = PlantForm()
    return render(request, 'plantations/add_plant.html', {'form':form, 'category':category})

def Edit_plant(request, category_id, plant_id):
    category = get_object_or_404(Categories, id=category_id)
    plant = get_object_or_404(Plants, id=plant_id, category=category)
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل بيانات النبات بنجاح')
            return redirect(reverse('plant_detail', kwargs={'category_id':category.id, 'plant_id':plant.id}))
    else:
        form = PlantForm(instance=plant)
    return render(request, 'plantations/edit_plant.html', {'form':form, 'category':category, 'plant':plant})

def Delete_plant(request, category_id, plant_id):
    category = get_object_or_404(Categories, id=category_id)
    plant = get_object_or_404(Plants, id=plant_id, category=category)
    if request.method == 'POST':
        plant.delete()
        messages.success(request, 'تم حذف النبات بنجاح')
        return redirect(reverse('plant_list', kwargs={'category_id':category}))
    return render(request, 'plantations/delete_plant.html', {'category':category, 'plant':plant})

#crops
def Crop_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    crops = Crops.objects.filter(user=user)
    context = {'user':user ,'crops':crops}
    return render(request, 'plantations/crop_list.html', context ) 

def Add_crop(request ,user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = CropForm(request.POST, request.FILES)
        if form.is_valid():
            crop = form.save(commit=False)
            crop.user = user
            crop.save()
            messages.success(request,'تم الحفظ بنجاح')
            return redirect(reverse('crop_list',kwargs={'user_id':user.id}))
    else:
        form = CropForm()
    context = {'form':form ,'user':user}
    return render(request , 'plantations/add_crop.html' , context)      


def Crop_details(request, crop_id, user_id):
    user = get_object_or_404(User, id=user_id)
    crop = get_object_or_404(Crops , id=crop_id, user=user)
    crop.calculate_next_dates()
    crop.save()

    days_until_watering = (crop.next_watering_date - date.today()).days if crop.next_watering_date else None
    days_until_fertilization = (crop.next_fertilization_date - date.today()).days if crop.next_fertilization_date else None
    days_until_harvest = (crop.harvest_date - date.today()).days if crop.harvest_date else None

    watering_form = WateringForm(initial={'crop_id':crop.id})
    fertilization_form = FertilizationForm(initial={'crop_id':crop.id})
    update_form = UpdateCropForm(instance=crop)
    
    context = {
        'user':user,
        'crop':crop,
        'days_until_watering':days_until_watering,
        'days_until_fertilization':days_until_fertilization,
        'days_until_harvest':days_until_harvest,
        'watering_form':watering_form,
        'fertilization_form':fertilization_form,
        'update_form':update_form,
        }
    return render(request, 'plantations/crop_details.html' ,context)


def Record_watering(request, user_id, crop_id):
    user = get_object_or_404(User, id=user_id)
    crop = get_object_or_404(Crops, id=crop_id)
    if request.method == 'POST':
        form = WateringForm(request.POST)
        if form.is_valid():
            crop = get_object_or_404(Crops, id=form.cleaned_data['crop_id'])
            crop.next_watering_date =date.today() + timedelta(days=crop.plant.water_requirement)
            crop.save()
    return redirect(reverse('crop_details', kwargs={'user_id':user.id,'crop_id':crop.id}))


def Record_fertilization(request, user_id, crop_id):
    user = get_object_or_404(User, id=user_id)
    crop = get_object_or_404(Crops, id=crop_id)
    if request.method == 'POST':
        form = FertilizationForm(request.POST)
        if form.is_valid():
            crop = get_object_or_404(Crops, id=form.cleaned_data['crop_id'])
            crop.next_fertilization_date = date.today() + timedelta(days=crop.plant.fertilizer_requirement)
            crop.save()
    return redirect(reverse('crop_details', kwargs={'user_id':user.id,'crop_id':crop.id}))


def Update_crop_status(request, crop_id, user_id):
    user = get_object_or_404(User, id=user_id)
    crop = get_object_or_404(Crops, id=crop_id)
    if request.method == 'POST':
        form = UpdateCropForm(request.POST, instance=crop)
        if form.is_valid():
            form.save()
    return redirect(reverse('crop_details', kwargs={'user_id':user.id, 'crop_id': crop.id}))

def Edit_crop(request ,crop_id, user_id):
    user = get_object_or_404(User, id=user_id)
    crop = get_object_or_404(Crops, id=crop_id, user=user)
    if request.method == 'POST':
        form = CropForm(request.POST,request.FILES, instance=crop )
        if form.is_valid():
            form.save()
            messages.success(request,'تم التعديل بنجاح')
            return redirect(reverse('crop_details',kwargs={'user_id':user.id, 'crop_id': crop.id}))
    else:
        form = CropForm(instance=crop)
    context = {'user':user, 'form':form , 'crop':crop }
    return render(request, 'plantations/edit_crop.html', context)

def Delete_crop(request, crop_id, user_id):
    user = get_object_or_404(User, id=user_id)
    crop = get_object_or_404(Crops ,id=crop_id, user=user)
    if request.method == 'POST':
        crop.delete()
        messages.success(request,'تم الحذف بنجاح')
        return redirect(reverse('crop_list', kwargs={'user_id':user.id}))
    context = {'user':user, 'crop':crop}
    return render(request,'plantations/delete_crop.html', context)
       
