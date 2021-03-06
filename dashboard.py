# -*- coding: utf-8 -*-

"""
This file was generated with the customdashboard management command, it
contains the two classes for the main dashboard and app index dashboard.
You can customize these classes as you want.

To activate your index dashboard add the following to your settings.py::
    ADMIN_TOOLS_INDEX_DASHBOARD = 'navaz.dashboard.CustomIndexDashboard'

And to activate the app index dashboard::
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'navaz.dashboard.CustomAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from admin_tools.utils import get_admin_site_name

class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for navaz.
    """
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)
        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick links'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [u'Настройки сайта', '/settings/MyApp'],
                [_('Return to site'), '/'],
                [_('Change password'),
                 reverse('%s:password_change' % site_name)],
                [_('Log out'), reverse('%s:logout' % site_name)],
            ]
        ))
        
        
        self.children.append(
            modules.ModelList(
                title = u'Страницы. Текстовая инфа',
                models=(
                    'pages.models.Page',
                ),
            )
        )
        
        self.children.append(
            modules.ModelList(
                title = u'Страницы в О нас',
                models=(
                    'about.models.Article',
                ),
            )
        )
        
        self.children.append(
            modules.ModelList(
                title = u'Акции',
                models=(
                    'action.models.Action',
                ),
            )
        )
        
        self.children.append(
            modules.ModelList(
                title = u'Статьи',
                models=(
                    'articles.models.Article',
                ),
            )
        )
        
        self.children.append(
            modules.ModelList(
                title = u'Блог',
                models=(
                    'blog.models.Article',
                ),
            )
        )
        
        self.children.append(
            modules.ModelList(
                title = u'Услуги',
                models=(
                    'services.models.Article',
                ),
            )
        )

        
        self.children.append(
            modules.ModelList(
                title = u'Заявки',
                models=(
                    'request.models.Request',
                ),
            )
        )

        
        self.children.append(
            modules.ModelList(
                title = u'Подписки',
                models=(
                    'subscribe.models.Subscribe',
                ),
            )
        )
        
        self.children.append(
            modules.ModelList(
                title = u'Слайдшоу',
                models=(
                    'slideshow.models.Slider',
                ),
            )
        )
        # append a recent actions module
        self.children.append(modules.RecentActions(_('Recent Actions'), 5))

        self.children.append(
            modules.ModelList(
                title = u'Пользователи',
                models=(
                    'django.contrib.auth.*',
                    'users.models.Profile',
                ),
            )
        )
        


class CustomAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for navaz.
    """

    # we disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        AppIndexDashboard.__init__(self, *args, **kwargs)

        # append a model list module and a recent actions module
        self.children += [
            modules.ModelList(self.app_title, self.models),
            modules.RecentActions(
                _('Recent Actions'),
                include_list=self.get_app_content_types(),
                limit=5
            )
        ]

    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(CustomAppIndexDashboard, self).init_with_context(context)
