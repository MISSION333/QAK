from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('prompt/', views.prompt),
    path('generate/', views.genrator)
]
