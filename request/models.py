# -*- coding: utf-8 -*-
from django.db import models
from pytils import dt

class Request(models.Model):
    first_name  = models.CharField(u'имя*', max_length=255)
    last_name  = models.CharField(u'фамилия*', max_length=255)
    middle_name  = models.CharField(u'отчество', blank=True, max_length=255)
    phone  = models.CharField(u'телефон*', max_length=255)
    email  = models.CharField(u'e-mail*', max_length=255)
    car = models.CharField(u'марка*', max_length=255)
    year = models.CharField(u'год выпуска*', max_length=255)
    msg = models.TextField(u'Сообщение*')
    request_date = models.DateTimeField(u'дата заявки', auto_now_add=True)
                    
    class Meta:
        verbose_name = u'заявка'
        verbose_name_plural = u'заявки'
        ordering = ['-request_date']

    def __unicode__(self):
        return u'№ %s от %s' % (self.id, dt.ru_strftime(u"%d %B %Y", self.request_date))
