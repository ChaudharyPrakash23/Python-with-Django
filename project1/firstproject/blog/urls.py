from .import views
from django.urls import path
from blog import views

urlpatterns=[
    path('',views.Home,name='Home'),
    path('about',views.about,name='about')
]