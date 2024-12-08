from django.urls import path
from . import views

urlpatterns = [
    #المحافظات 
    path('governates/',views.Governates_List , name='governate_list'),
    path('governates/new/',views.Add_Governate , name='add_governate'),
    path('governates/edit/<int:governate_id>/',views.Edit_Governate , name='edit_governate'),
    path('governates/delete/<int:governate_id>/',views.Delete_Governate , name='delete_governate'),

    #path('governates/<int:governate_id>/areas/', views.Area_by_Gv, name='areas_by_governate'),
    #المناطق
    path('governates/<int:governate_id>/areas/',views.Areas_List , name='area_list'),
    path('governate/<int:governate_id>/areas/new/',views.Add_Area , name='add_area'),
    path('governate/<int:governate_id>/areas/edit/<int:area_id>/',views.Edit_Area , name='edit_area'),
    path('governate/<int:governate_id>/areas/delete/<int:area_id>/',views.Delete_Area , name='delete_area'),


    #المستخدمين
    path('areas/<int:area_id>/users/',views.User_List , name='user_list'),
    path('areas/<int:area_id>/users/new/',views.Add_User , name='add_user'),
    path('areas/<int:area_id>/users/edit/<int:user_id>/',views.Edit_User , name='edit_user'),
    path('areas/<int:area_id>/users/delete/<int:user_id>/',views.Delete_User , name='delete_user'),


    #الحسابات
    path('users/<int:user_id>/accounts/',views.Account_list , name='account_list'),
    path('users/<int:user_id>/accounts/add/<int:account_id>/',views.Add_Balance , name='add_balance'),
    path('users/<int:user_id>/accounts/withdraw/<int:account_id>/',views.Withdraw_balance , name='withdraw_balance'),



    #المعاملات المالية
    path('aaounts/<int:account_id>/transactions/',views.Transaction_list , name='transaction_list'),
    path('transactions/new/',views.Add_Transaction , name='add_transaction'),
    path('transactions/edit/<int:transaction_id>/',views.Edit_Transaction , name='edit_transaction'),
    path('transactions/delete/<int:transaction_id>/',views.Delete_Transaction , name='delete_transaction'),


]