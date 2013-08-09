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
    c['request_form'] = RequestForm()
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


def subscribe(request):
    if request.POST and request.POST['action'] == 'subscribe':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscribeForm()
            messages.success(request, u'Вы успешно подписались на рассылку.')
            return HttpResponseRedirect(request.POST['next'])
    raise Http404() 

def request_f(request):
    if request.POST and request.POST['action'] == 'request':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            form = RequestForm()
            messages.success(request, u'Ваша заявка отправлена.')
            return HttpResponseRedirect(request.POST['next'])
        else:
            c = get_common_context(request)
            c.update(Page.get_by_slug('home'))
            c['actions'] = Action.objects.all()
            c['request_url'] = 'home'
            c['request_form'] = form
            c['request_form_open'] = True
            return render_to_response('home.html', c, context_instance=RequestContext(request))
    raise Http404() 
    