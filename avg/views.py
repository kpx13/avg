# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.contrib import messages
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
 

from pages.models import Page
from action.models import Action
from slideshow.models import Slider
from services.models import Article as ServiceArticle
from action.models import Action
from articles.models import Article as ArticleArticle
from blog.models import Article as BlogArticle
from about.models import Article as AboutArticle

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
    c['request_url'] = 'home'
    return render_to_response('home.html', c, context_instance=RequestContext(request))

def services(request, page_name=None):
    if page_name:
        c = get_common_context(request)
        c['a'] = ServiceArticle.get_by_slug(page_name)
        c['articles'] = ServiceArticle.objects.all()
        c['base_url'] = 'services'
        c['base_title'] = u'Услуги'
        return render_to_response('articles_base.html', c, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/services/%s/' % ServiceArticle.objects.all()[0].slug)
    
def actions(request, page_name=None):
    if page_name:
        c = get_common_context(request)
        c['a'] = Action.get_by_slug(page_name)
        c['articles'] = Action.objects.all()
        c['base_url'] = 'actions'
        c['base_title'] = u'Акции'
        return render_to_response('articles_base.html', c, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/actions/%s/' % Action.objects.all()[0].slug)
    
def articles(request, page_name=None):
    if page_name:
        c = get_common_context(request)
        c['a'] = ArticleArticle.get_by_slug(page_name)
        c['articles'] = ArticleArticle.objects.all()
        c['base_url'] = 'articles'
        c['base_title'] = u'Статьи'
        return render_to_response('articles_base.html', c, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/articles/%s/' % ArticleArticle.objects.all()[0].slug)
    
def blog(request, page_name=None):
    if page_name:
        c = get_common_context(request)
        c['a'] = BlogArticle.get_by_slug(page_name)
        c['articles'] = BlogArticle.objects.all()
        c['base_url'] = 'blog'
        c['base_title'] = u'Блог'
        return render_to_response('articles_base.html', c, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/blog/%s/' % BlogArticle.objects.all()[0].slug)

def about(request, page_name=None):
    if page_name:
        c = get_common_context(request)
        c['a'] = AboutArticle.get_by_slug(page_name)
        c['articles'] = AboutArticle.objects.all()
        c['base_url'] = 'about'
        c['base_title'] = u'О нас'
        return render_to_response('articles_base.html', c, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/about/%s/' % AboutArticle.objects.all()[0].slug)

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