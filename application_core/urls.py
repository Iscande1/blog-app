from django.urls import path
from . import views

urlpatterns = [
    path('', views.sneaker_page, name='sneaker_page'),
]