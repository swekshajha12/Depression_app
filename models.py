# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class registeruser(models.Model):
    USERNAME=models.CharField(max_length=30)
    PASSWORD=models.CharField(max_length=20)
    CONFIRM_PASSWORD=models.CharField(max_length=20)





