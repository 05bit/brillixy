import types
from django.conf import settings
from django.contrib.admin import AdminSite as _AdminSite
from brillixy import views
from brillixy.panels import AllModelsPanel


def setup(site):
    """Define custom templates and wrap default
    views with extended ones.
    """
    setup_views(site)
    setup_templates(site)


def setup_templates(site):
    """Setup custom templates for admin site.
    """
    site.index_template = AdminSite.index_template
    site.login_template = AdminSite.login_template
    site.logout_template = AdminSite.logout_template
    site.password_change_template = AdminSite.password_change_template
    site.password_change_done_template = AdminSite.password_change_done_template


def setup_views(site):
    """Setup custom view methods for admin site.
    """
    if hasattr(site, 'index_base'):
        raise Exception("Site %s was already setup!" % str(site))
    # save base methods
    site.index_base = site.index
    site.get_urls_base = site.get_urls
    # add/replace with custom ones
    site.index = types.MethodType(views.index, site)    
    site.get_urls = types.MethodType(get_urls, site)
    site.get_panels = types.MethodType(get_panels, site)


def get_urls(site, urls_base=None):
    """As Django 1.5 provides some extra urls, its templates
    don't work great with Django 1.4. We're eliminating such
    minor difference.

    Extra urls added if necessary:

        - admin:view_on_site
    """
    from django.conf.urls import patterns, url, include
    urlpatterns = urls_base or site.get_urls_base()
    urlnames = [getattr(u, 'name', None) for u in urlpatterns]
    if not 'view_on_site' in urlnames:
        urlpatterns += url(r'^r/(?P<content_type_id>\d+)/(?P<object_id>.+)/$',
                           views.view_on_site,
                           name='view_on_site'),
    return urlpatterns


def get_panels(site, request):
    """Default ``get_panels`` method for site -
    returns list of panel objects for dashboard.
    """
    panels = []
    if hasattr(settings, 'BRILLIXY_INDEX'):
        for panel in settings.BRILLIXY_INDEX.get('panels', []):
            panel_mod, panel_cls = panel.rsplit('.', 1)
            module = __import__(panel_mod, fromlist=[panel_cls])
            panels.append(getattr(module, panel_cls)(site, request))
    if not panels:
        panels.append(AllModelsPanel(site, request))
    return panels


class AdminSite(_AdminSite):
    """Base class for Brillixy admin site. You can use it to setup
    custom admin interface from scratch. Probably you should not
    use it if you need only basic customizations.
    """
    index_template = 'brillixy/index.html'
    login_template = 'brillixy/login.html'
    logout_template = 'brillixy/logout.html'
    password_change_template = 'brillixy/password_change.html'
    password_change_done_template = 'brillixy/password_change_done.html'

    def get_panels(self, request):
        """Panels for admin dashboard.
        """
        return get_panels(self, request)


    def get_urls(self):
        """Admin URLs.
        """
        return get_urls(self, super(AdminSite, self).get_urls())
