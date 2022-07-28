# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('tickets/', views.getTickets, name = 'getTickets'),
    path('ticket/<str:pk>', views.getSingleTicket, name = 'getSingleTicket'),
    path('pend/', views.pend, name = 'pend'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
