# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import pytils

class Action(models.Model):
    title = models.CharField(max_length=256, blank=True, verbose_name=u'заголовок')
    slug = models.SlugField(verbose_name=u'слаг', unique=True, blank=True, help_text=u'Заполнять не нужно')
    image = models.ImageField(upload_to= 'uploads/slider', max_length=256, verbose_name=u'картинка')
    content = RichTextField(max_length=1024, blank=True, verbose_name=u'текст')
    sort_parameter = models.IntegerField(default=0, blank=True, verbose_name=u'порядок сортировки', help_text=u'№ акции по порядку: 1й, 2й .. 5й')
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=pytils.translit.slugify(self.title)
        super(Action, self).save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'акция'
        verbose_name_plural = 'акции'
        ordering = ['sort_parameter']
        
    
    def __unicode__(self):
        return self.title
    
    @staticmethod
    def get_by_slug(page_name):
        try:
            return Action.objects.get(slug=page_name)
        except:
            return None