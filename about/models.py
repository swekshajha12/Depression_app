# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):
    usn = models.CharField(max_length=20, primary_key=True)
    sname = models.CharField(max_length=20)
    address = models.CharField(max_length=25)
    phone = models.IntegerField()
    Gender = models.CharField(max_length=2)


class Semsec(models.Model):
    ssid = models.CharField(max_length=4, primary_key=True)
    sem = models.IntegerField()
    sec = models.IntegerField()
