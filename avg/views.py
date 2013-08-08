# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
 

from pages.models import Page
from action.models import Action
from slideshow.models import Slider

from subscribe.forms import SubscribeForm
from request.forms import RequestForm

import config
from livesettings import config_value


def get_common_context(request):
    c = {}
    c['request_url'] = request.path
    c['subscribe_form'] = SubscribeForm()
    c['slideshow'] = Slider.objects.all()
    c.update(csrf(request))
    return c

def page(request, page_name):
    c = get_common_context(request)
    try:
        c.update(Page.get_by_slug(page_name))
        return render_to_response('page.html', c, context_instance=RequestContext(request))
    except:
        raise Http404()

def home(request):
    c = get_common_context(request)
    c.update(Page.get_by_slug('home'))
    c['actions'] = Action.objects.all()
    return render_to_response('home.html', c, context_instance=RequestContext(request))

"""
def call(request):
    c = get_common_context(request)
    if request.POST and request.POST['action'] == 'call':
        call_form = RequestForm(request.POST)
        if call_form.is_valid():
            call_form.save()
            call_form = RequestForm()
            #messages.success(request, u'Спасибо! В ближайшее время мы Вам перезвоним.')
            return HttpResponseRedirect(request.POST['next'])
    raise Http404() 

def request_f(request):
    c = get_common_context(request)
    if request.POST and request.POST['action'] == 'request':
        call_form = RegisterForm(request.POST)
        if call_form.is_valid():
            call_form.save()
            call_form = RegisterForm()
            #messages.success(request, u'Спасибо! В ближайшее время мы Вам перезвоним.')
            return HttpResponseRedirect(request.POST['next'])
    raise Http404() 
    

def bonuses(request):
    c = get_common_context(request)
    c['bonuses'] = Article.objects.all()
    return render_to_response('bonuses.html', c, context_instance=RequestContext(request))

def bonuses_in(request, page_name):
    c = get_common_context(request)
    c['bonus'] = Article.get_by_slug(page_name)
    return render_to_response('bonuses_in.html', c, context_instance=RequestContext(request))


def contacts(request):
    c = get_common_context(request)
    return render_to_response('contacts.html', c, context_instance=RequestContext(request))

def about(request):
    c = get_common_context(request)
    c.update(Page.get_by_slug('about'))
    return render_to_response('about.html', c, context_instance=RequestContext(request))

def products(request):
    c = get_common_context(request)
    c['products'] = Product.objects.all()
    return render_to_response('products.html', c, context_instance=RequestContext(request))

def products_in(request, page_name):
    c = get_common_context(request)
    c['product'] = Product.get_by_slug(page_name)
    return render_to_response('products_in.html', c, context_instance=RequestContext(request))    

def services(request):
    c = get_common_context(request)
    c.update(Page.get_by_slug('services'))
    return render_to_response('services.html', c, context_instance=RequestContext(request))
"""