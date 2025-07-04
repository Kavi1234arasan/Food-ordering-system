"""
URL configuration for foodorder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from chrome import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),
    path('addData', views.addData, name='addData'),
    path('updateData/<int:id>/', views.updateData, name='updateData'),
    path('deleteData/<int:id>/', views.deleteData, name='deleteData'),
    path('order/', views.place_order, name='place_order'),
    path('order_success/', views.order_success, name='order_success'),



]
