from django.urls import path
from . import views
from .views import Home

urlpatterns = [
    path('', Home.as_view()),
    path('', views.index),
    path('index', views.index),
    path('contact', views.contact),
    path('about', views.about),
]
