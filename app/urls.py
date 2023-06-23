from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('resume/', views.resume, name='resume'),
    path('skill/', views.skill, name='skill'),
    path('portfolio-detail/', views.portfolio_details, name='portfolio-detail'),
    path('inner-page/', views.inner_page, name='inner-page'),
]
