from django.db import models
from django_enumfield import enum

class Ticket(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    subject = models.CharField(max_length = 255)
    scenario = models.CharField(max_length = 2000)
    date = models.DateTimeField()


class Operations(enum.Enum):
    Untouched : 0
    Cleaned : 1
    Rejected : 2

class Status(enum.Enum):
    Processed : 1
    Unprocessed : 0

class TicketDataTable(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)
    subject = models.CharField(max_length = 255)
    scenario = models.CharField(max_length = 2000)
    date = models.DateTimeField()
    operation_flag = enum.EnumField(Operations)
    status_flag = enum.EnumField(Status)
# Create your models here.
