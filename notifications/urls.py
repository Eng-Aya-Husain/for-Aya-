from django.urls import path # type: ignore
from .views import (
    Create_Notification,Notification_List,Notification_Detail,Edit_Notification,Delete_Notification,

    Create_Transaction_Alert,Transaction_Alert_List,Transaction_Alert_Detail,Edit_Transaction_Alert,Delete_Transaction_Alert,

    Create_Season_Alert,Season_Alert_List,Season_Alert_Detail,Edit_Season_Alert,Delete_Season_Alert,

    Create_Crop_Alert,Crop_Alert_List,Crop_Alert_Detail,Edit_Crop_Alert,Delete_Crop_Alert,
)

urlpatterns = [
    path('notifications/', Notification_List, name='notification_list'),
    path('notifications/create/', Create_Notification, name='create_notification'),
    path('notifications/<int:notification_id>/', Notification_Detail, name='notification_detail'),
    path('notifications/<int:notification_id>/edit/', Edit_Notification, name='edit_notification'),
    path('notifications/<int:notification_id>/delete/', Delete_Notification, name='delete_notification'),

    path('transaction_alerts/', Transaction_Alert_List, name='transaction_alert_list'),
    path('transaction_alerts/create/', Create_Transaction_Alert, name='create_transaction_alert'),
    path('transaction_alerts/<int:alert_id>/', Transaction_Alert_Detail, name='transaction_alert_detail'),
    path('transaction_alerts/<int:alert_id>/edit/', Edit_Transaction_Alert, name='edit_transaction_alert'),
    path('transaction_alerts/<int:alert_id>/delete/', Delete_Transaction_Alert, name='delete_transaction_alert'),

    path('season_alerts/', Season_Alert_List, name='season_alert_list'),
    path('season_alerts/create/', Create_Season_Alert, name='create_season_alert'),
    path('season_alerts/<int:alert_id>/', Season_Alert_Detail, name='season_alert_detail'),
    path('season_alerts/<int:alert_id>/edit/', Edit_Season_Alert, name='edit_season_alert'),
    path('season_alerts/<int:alert_id>/delete/', Delete_Season_Alert, name='delete_season_alert'),

     path('crop_alerts/', Crop_Alert_List, name='crop_alert_list'),
    path('crop_alerts/create/', Create_Crop_Alert, name='create_crop_alert'),
    path('crop_alerts/<int:alert_id>/', Crop_Alert_Detail, name='crop_alert_detail'),
    path('crop_alerts/<int:alert_id>/edit/', Edit_Crop_Alert, name='edit_crop_alert'),
    path('crop_alerts/<int:alert_id>/delete/', Delete_Crop_Alert, name='delete_crop_alert'),
]


