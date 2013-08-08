# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Subscribe


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'date',)
    ordering = ('date', )

admin.site.register(Subscribe, SubscribeAdmin)