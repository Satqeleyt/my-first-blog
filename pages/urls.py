from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('index', views.about, name='anasayfa'),
    path('about', views.about, name='about'),
    path('contact',views.contact, name='contact')
    
]