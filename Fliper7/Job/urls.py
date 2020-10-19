"""Fliper7 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views


app_name ="Job"
urlpatterns = [
    path('',views.LR,name="LR" ),
    path('home/',views.home,name="home"),
    path('filter/',views.filter, name="filter"),
    path('test/',views.test,name="test"),
    path('login/',views.login_view,name="login"),
    path('register/',views.reg_view,name="register"),
    path('logout/',views.logout_view,name="logout"),
    path('<int:user_id>/<int:data_id>/jsp', views.jsp,name="jsp"),
    path('<int:user_id>/user_job', views.user_job, name="user_job"),
    path('filtered/',views.filtered,name="filtered")

]
