from .models import Ticket, TicketDataTable
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse


def homePage(request):
    return HttpResponse("<h1> Helo </h1>")
# Create your views here.
