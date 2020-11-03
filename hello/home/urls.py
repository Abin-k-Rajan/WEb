from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("home", views.index, name='home'),
    path("picture", views.pic, name='picture'),
    path("about",views.about, name='about'),
    path("feedback", views.feedback, name='feedback')
]