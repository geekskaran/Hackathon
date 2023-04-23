from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   path('TLC',views.TLC.as_view()),
   path('MHR',views.MHR.as_view()),
]
