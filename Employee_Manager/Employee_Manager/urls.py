"""Employee_Manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from employee import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('emp_login/',views.emp_login,name='emp_login'),
    path('emp_home/',views.emp_home,name='emp_home'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.Logout,name='logout'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('my_experience/',views.my_experience,name='my_experience'),
    path('edit_experience',views.edit_experience,name='edit_experience'),
]
