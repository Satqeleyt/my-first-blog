from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def anasayfa(request):
    return  HttpResponse('<h1> Ana Sayfaya Hoş Geldiniz. </h1>')