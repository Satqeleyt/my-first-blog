from django.shortcuts import render

# Create your views here.
def index(request):
    return  render(request,'teachers/list.html')   

def detail(request):
    return  render(request,'teachers/detail.html') 

def search(request):
    return  render(request,'teachers/search.html') 
