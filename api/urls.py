from django.urls import path
from . import views


urlpatterns = [
    #path('about/', views.about, name='api-about'),
    path('', views.homePage, name='home'),
    path('pend/', views.pend, name = 'pend'),
]