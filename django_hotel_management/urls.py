"""django_hotel_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import re_path,include
from django.urls import path
from management_app import views as my_customer

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', my_customer.index, name='home'),
    re_path(r'^(?P<customer_id>\d+)/checkin/$', my_customer.checkin, name='checkin'),
    re_path(r'^currentcheckin$', my_customer.current_checkin, name='checkinlist'),
]
