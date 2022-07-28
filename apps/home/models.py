# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django_enumfield import enum


class Ticket(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    scenario = models.CharField(max_length=2000)
    date = models.DateTimeField()
    email = models.EmailField(null=True)


class Operations(enum.Enum):
    Untouched = 0
    Cleaned = 1
    Rejected = 2


class Status(enum.Enum):
    Done = 1
    Waiting = 0


class TicketDataTable(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    scenario = models.CharField(max_length=2000)
    date = models.DateTimeField()
    operation_flag = enum.EnumField(Operations)
    status_flag = enum.EnumField(Status)
    email = models.EmailField(null=True)
    domain = models.CharField(null = True, max_length = 255)

# Create your models here.

