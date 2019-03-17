"""meituan1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from user.views import homepage_view, account_login_view, account_create_view, customer_create_view, \
    shipper_create_view, restaurant_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("/",homepage_view),
    path("/login/",account_login_view),
    path("/register_customer",customer_create_view),
    path("/register_account",account_create_view),
    path("/register_shipper",shipper_create_view),
    path("/register_restaurant",restaurant_create_view),

]
