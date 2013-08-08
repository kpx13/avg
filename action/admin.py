# -*- coding: utf-8 -*-
from django.contrib import admin
import models

class ActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'sort_parameter')
    ordering = ('sort_parameter', )
    
admin.site.register(models.Action, ActionAdmin)