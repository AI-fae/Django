from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('resources', views.content, name="resources"),
    path('services', views.services, name="services"),
    path('visitors/<str:pk>/', views.visitor, name="visitor"),
    path('form', views.createForm, name="form")
]
