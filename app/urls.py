from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('refresh',views.refresh,name='refresh'),
    path('about',views.about,name='about'),


]
