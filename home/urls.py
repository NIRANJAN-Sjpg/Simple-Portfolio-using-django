from django.urls import path,include
from django.contrib import admin
from. import views   # ✅ ADD THIS


admin.site.site_header="Developer Niranjan"
admin.site.site_title="welcome to niranjans dashboard"
admin.site.index_title="welcome to portal"
urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact')
    
    ]

