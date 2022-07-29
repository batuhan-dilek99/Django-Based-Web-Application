
from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('tickets/', views.getTickets, name = 'getTickets'),
    path('ticket/<str:pk>', views.getSingleTicket, name = 'getSingleTicket'),
    path('pend/', views.pend, name = 'pend'),
    path('create/', views.createTicket, name = 'create'),
    path('updateTickets/', views.updateTickets, name = 'updateTickets'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
