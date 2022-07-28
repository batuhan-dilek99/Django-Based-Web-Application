# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Ticket, TicketDataTable, Operations, Status
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-POST METHODS-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*


# ------handling json input from client--------

class Payload(object):

    def __init__(self, j):
        self.__dict__ = json.loads(j)


@api_view(['POST'])
@csrf_exempt
def pend(request):
    if (request.body != None):
        p = Payload(request.body)

    ticket = Ticket(firstname=p.firstname, lastname=p.lastname, email=p.email, subject=p.subjects, scenario=p.scenario,date=p.date)
    ticket.save()

    tdt = TicketDataTable(firstname = ticket.firstname, lastname = ticket.lastname, email = ticket.email, 
        subject = ticket.subject, scenario = ticket.scenario, 
        date = ticket.date, operation_flag = Operations.get(0), status_flag = Status.get(0))
    tdt.save()
    print()
    print(ticket.firstname, ticket.lastname, ticket.subject, ticket.scenario)
    print()
    print(tdt.firstname, tdt.lastname, tdt.subject, tdt.operation_flag, tdt.status_flag)
    print()
    # Refresh
    print()
    return Response()

#*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

#-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-GET METHODS-*-*-*-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*
def getTickets(request):
    tickets = TicketDataTable.objects.all()
    context =  {
        'TDT' : tickets,
    }

    return render(request, "home/ui-tables.html",context)

def getSingleTicket(request, pk):
    ticket = TicketDataTable.objects.get(id = pk)

    context = {
        'ticket' : ticket
    }
    return render(request, 'home/individualTicket.html', context)