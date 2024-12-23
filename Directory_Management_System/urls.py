"""Directory_Management_System URL Configuration

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
from directory.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', Login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('add_Directory', add_Directory, name='add_Directory'),
    path('manage_Directory', manage_Directory, name='manage_Directory'),
    path('edit_Directory/<int:pid>', edit_Directory, name='edit_Directory'),
    path('deleteDirectory/<int:pid>', deleteDirectory, name='deleteDirectory'),
    path('search_Directory', search_Directory, name='search_Directory'),
    path('allRecord', allRecord, name='allRecord'),
    path('privateRecord', privateRecord, name='privateRecord'),
    path('publicRecord', publicRecord, name='publicRecord'),
    path('viewallRecord/<int:pid>', viewallRecord, name='viewallRecord'),
    path('viewSearchData/<int:pid>', viewSearchData, name='viewSearchData'),
    path('changePassword', changePassword, name='changePassword'),
    path('logout/', Logout, name='logout')

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
