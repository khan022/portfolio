from django.contrib import admin
from django.urls import path, include
from home import views

# django admin header customization

admin.site.site_header = "DO NOT LOG INTO Jobless Khan"
admin.site.site_title = 'Nobody is welcome here! GET OUT'
admin.site.index_title = 'LEAVE!! NOW!!!!'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
]
