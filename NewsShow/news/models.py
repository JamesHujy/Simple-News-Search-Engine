# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class news(models.Model):
	title = models.CharField(max_length = 50)
	time = models.CharField(max_length = 14)
	author = models.CharField(max_length = 20)
	body = models.TextField()
	breakwords = models.TextField()
	keywords = models.TextField()
	recommend = models.TextField()
	def __str__(self):
		return self.title


# Create your models here.
