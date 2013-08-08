# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField

class Action(models.Model):
    title = models.CharField(max_length=256, blank=True, verbose_name=u'заголовок')
    image = models.ImageField(upload_to= 'uploads/slider', max_length=256, verbose_name=u'картинка')
    content = RichTextField(max_length=1024, blank=True, verbose_name=u'текст')
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'порядок сортировки', help_text=u'№ акции по порядку: 1й, 2й .. 5й')
    
    class Meta:
        verbose_name = 'акция'
        verbose_name_plural = 'акции'
        ordering = ['sort_parameter']
        
    
    def __unicode__(self):
        return self.title