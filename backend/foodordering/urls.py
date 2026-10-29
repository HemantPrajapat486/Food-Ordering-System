
from django.urls import path
from .views import admin_login_api

urlpatterns = [
    path('admin_login_api/' , admin_login_api , name='admin_login_api')
]