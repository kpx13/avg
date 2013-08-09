# -*- coding: utf-8 -*-
from django.db import models

class Subscribe(models.Model):
    email  = models.EmailField(u'email', max_length=255)
    date = models.DateTimeField(u'дата подписки', auto_now_add=True)
                    
    class Meta:
        verbose_name = u'подписка'
        verbose_name_plural = u'подписки'
        ordering = ['-date']

    def __unicode__(self):
        return self.email
