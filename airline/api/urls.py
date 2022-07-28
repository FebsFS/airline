from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('flyings', views.flysList.as_view()),

    path('company', views.Companylist.as_view()),
    path('auth', include('rest_framework.urls'))
]