from django.urls import path
from . import views
#from users import views 

urlpatterns = [
    #seasons
    path('seasons/', views.Season_list ,name='season_list'),
    path('seasons/new/', views.Add_season ,name='add_season'),
    path('seasons/edit/<int:season_id>/', views.Edit_season ,name='edit_season'),
    path('seasons/delete/<int:season_id>/', views.Delete_season ,name='delete_season'),
   
   #area_seasons
    path('seasons/<int:season_id>/area_season/', views.Area_season_list, name='area_season_list'),
    path('seasons/<int:season_id>/area_season/new', views.Add_area_season, name='add_area_season'),
    path('seasons/<int:season_id>/area_season/edit/<int:area_season_id>/', views.Edit_area_season, name='edit_area_season'),
    path('seasons/<int:season_id>/area_season/delete/<int:area_season_id>/', views.Delete_area_season, name='delete_area_season'),

    #categories
    path('categories/', views.Category_list ,name='category_list'),
    path('categories/new/', views.Add_category ,name='add_category'),
    path('categories/edit/<int:category_id>/', views.Edit_category ,name='edit_category'),
    path('categories/delete/<int:category_id>/', views.Delete_category ,name='delete_category'),

    path('categories/<int:category_id>/plants/', views.Plant_list ,name='plant_list'),
    path('categories/<int:category_id>/plants/detail/<int:plant_id>/', views.Plant_detail ,name='plant_detail'),
    path('categories/<int:category_id>/plants/new/', views.Add_plant ,name='add_plant'),
    path('categories/<int:category_id>/plants/detail/edit/<int:plant_id>/', views.Edit_plant ,name='edit_plant'),
    path('categories/<int:category_id>/plants/detail/delete/<int:plant_id>/', views.Delete_plant ,name='delete_plant'),

    #path('users/', views.User_List, name='user_list'),
    path('user/<int:user_id>/crops/', views.Crop_list , name='crop_list'),
    path('user/<int:user_id>/crops/add_crop/', views.Add_crop , name='add_crop'),
    path('user/<int:user_id>/crops/details/<int:crop_id>/', views.Crop_details , name='crop_details'),
    path('user/<int:user_id>/crops/edit_crop/<int:crop_id>/', views.Edit_crop , name='edit_crop'),
    path('user/<int:user_id>/crops/delete_crop/<int:crop_id>/', views.Delete_crop , name='delete_crop'),
    path('user/<int:user_id>/record_watering/<int:crop_id>/', views.Record_watering , name='record_watering'),
    path('user/<int:user_id>/record_fertilization/<int:crop_id>/', views.Record_fertilization , name='record_fertilization'),
    path('user/<int:user_id>/update_status/<int:crop_id>/', views.Update_crop_status , name='update_crop_status'),

]