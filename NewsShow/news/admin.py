# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import news

#class newsAdmin(admin.ModelAdmin):
#	list_display('title','time','body')

admin.site.register(news)

# Register your models here.
