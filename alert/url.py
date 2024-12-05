from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('alert_home/', login_required(views.alert_home), name='alert_home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)