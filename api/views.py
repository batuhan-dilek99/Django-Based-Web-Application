from .models import Ticket, TicketDataTable, Operations, Status
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse


def homePage(request):
    tickets = TicketDataTable.objects.all()
    context = {
        'tickets' : tickets
    }
    return render(request, 'api/home.html', context)


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