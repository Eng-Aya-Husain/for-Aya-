from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.contrib import messages # type: ignore
from .models import CropAlert, Notifications, SeasonAlert, TransactinAlert
from .forms import CropAlertForm, NotificationForm, SeasonAlertForm, TransactionAlertForm

# Create Notification

def Create_Notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة الإشعار بنجاح.')
            return redirect('notification_list')
    else:
        form = NotificationForm()
    return render(request, 'notifications/create_notification.html', {'form': form})


def Notification_List(request):
    notifications = Notifications.objects.all()
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})


def Notification_Detail(request, notification_id):
    notification = get_object_or_404(Notifications, id=notification_id)
    return render(request, 'notifications/notification_detail.html', {'notification': notification})


def Edit_Notification(request, notification_id):
    notification = get_object_or_404(Notifications, id=notification_id)
    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل بيانات الإشعار بنجاح.')
            return redirect('notification_detail', notification_id=notification.id)
    else:
        form = NotificationForm(instance=notification)
    return render(request, 'notifications/edit_notification.html', {'form': form, 'notification': notification})


def Delete_Notification(request, notification_id):
    notification = get_object_or_404(Notifications, id=notification_id)
    if request.method == 'POST':
        notification.delete()
        messages.success(request, 'تم حذف الإشعار بنجاح.')
        return redirect('notification_list')
    return render(request, 'notifications/delete_notification.html', {'notification': notification})


def Create_Transaction_Alert(request):
    if request.method == 'POST':
        form = TransactionAlertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة تنبيه المعاملة بنجاح.')
            return redirect('transaction_alert_list')
    else:
        form = TransactionAlertForm()
    return render(request, 'transaction_alerts/create_transaction_alert.html', {'form': form})


def Transaction_Alert_List(request):
    transaction_alerts = TransactinAlert.objects.all()
    return render(request, 'transaction_alerts/transaction_alert_list.html', {'transaction_alerts': transaction_alerts})


def Transaction_Alert_Detail(request, alert_id):
    transaction_alert = get_object_or_404(TransactinAlert, id=alert_id)
    return render(request, 'transaction_alerts/transaction_alert_detail.html', {'transaction_alert': transaction_alert})


def Edit_Transaction_Alert(request, alert_id):
    transaction_alert = get_object_or_404(TransactinAlert, id=alert_id)
    if request.method == 'POST':
        form = TransactionAlertForm(request.POST, instance=transaction_alert)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل بيانات تنبيه المعاملة بنجاح.')
            return redirect('transaction_alert_detail', alert_id=transaction_alert.id)
    else:
        form = TransactionAlertForm(instance=transaction_alert)
    return render(request, 'transaction_alerts/edit_transaction_alert.html', {'form': form, 'transaction_alert': transaction_alert})


def Delete_Transaction_Alert(request, alert_id):
    transaction_alert = get_object_or_404(TransactinAlert, id=alert_id)
    if request.method == 'POST':
        transaction_alert.delete()
        messages.success(request, 'تم حذف تنبيه المعاملة بنجاح.')
        return redirect('transaction_alert_list')
    return render(request, 'transaction_alerts/delete_transaction_alert.html', {'transaction_alert': transaction_alert})


def Create_Season_Alert(request):
    if request.method == 'POST':
        form = SeasonAlertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة تنبيه الموسم بنجاح.')
            return redirect('season_alert_list')
    else:
        form = SeasonAlertForm()
    return render(request, 'season_alerts/create_season_alert.html', {'form': form})


def Season_Alert_List(request):
    season_alerts = SeasonAlert.objects.all()
    return render(request, 'season_alerts/season_alert_list.html', {'season_alerts': season_alerts})


def Season_Alert_Detail(request, alert_id):
    season_alert = get_object_or_404(SeasonAlert, id=alert_id)
    return render(request, 'season_alerts/season_alert_detail.html', {'season_alert': season_alert})


def Edit_Season_Alert(request, alert_id):
    season_alert = get_object_or_404(SeasonAlert, id=alert_id)
    if request.method == 'POST':
        form = SeasonAlertForm(request.POST, instance=season_alert)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل بيانات تنبيه الموسم بنجاح.')
            return redirect('season_alert_detail', alert_id=season_alert.id)
    else:
        form = SeasonAlertForm(instance=season_alert)
    return render(request, 'season_alerts/edit_season_alert.html', {'form': form, 'season_alert': season_alert})


def Delete_Season_Alert(request, alert_id):
    season_alert = get_object_or_404(SeasonAlert, id=alert_id)
    if request.method == 'POST':
        season_alert.delete()
        messages.success(request, 'تم حذف تنبيه الموسم بنجاح.')
        return redirect('season_alert_list')
    return render(request, 'season_alerts/delete_season_alert.html', {'season_alert': season_alert})


def Create_Crop_Alert(request):
    if request.method == 'POST':
        form = CropAlertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إضافة إشعار المحصول بنجاح.')
            return redirect('crop_alert_list')
    else:
        form = CropAlertForm()
    return render(request, 'crop_alerts/create_crop_alert.html', {'form': form})


def Crop_Alert_List(request):
    crop_alerts = CropAlert.objects.all()
    return render(request, 'crop_alerts/crop_alert_list.html', {'crop_alerts': crop_alerts})


def Crop_Alert_Detail(request, alert_id):
    crop_alert = get_object_or_404(CropAlert, id=alert_id)
    return render(request, 'crop_alerts/crop_alert_detail.html', {'crop_alert': crop_alert})


def Edit_Crop_Alert(request, alert_id):
    crop_alert = get_object_or_404(CropAlert, id=alert_id)
    if request.method == 'POST':
        form = CropAlertForm(request.POST, instance=crop_alert)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تعديل بيانات إشعار المحصول بنجاح.')
            return redirect('crop_alert_detail', alert_id=crop_alert.id)
    else:
        form = CropAlertForm(instance=crop_alert)
    return render(request, 'crop_alerts/edit_crop_alert.html', {'form': form, 'crop_alert': crop_alert})


def Delete_Crop_Alert(request, alert_id):
    crop_alert = get_object_or_404(CropAlert, id=alert_id)
    if request.method == 'POST':
        crop_alert.delete()
        messages.success(request, 'تم حذف إشعار المحصول بنجاح.')
        return redirect('crop_alert_list')
    return render(request, 'crop_alerts/delete_crop_alert.html', {'crop_alert': crop_alert})
