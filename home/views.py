from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

def home(request):
    context={'name':'Niranjan','course':'Django'}
    return render(request, 'home.html',context)
def about(request):
    return render(request, 'about.html')
def projects(request):
    return render(request, 'projects.html')
def contact(request):
    return render(request, 'contact.html')


