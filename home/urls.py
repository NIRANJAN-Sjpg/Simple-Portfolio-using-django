from django.urls import path
from. import views   # ✅ ADD THIS

urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact')
    
    ]

