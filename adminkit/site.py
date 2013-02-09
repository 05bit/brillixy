import types
from django.contrib.admin import AdminSite
from adminkit import views


def setup(site):
    """Define custom templates and wrap default
    views with extended ones.
    """
    setup_views(site)
    setup_templates(site)


def setup_templates(site):
    site.index_template = 'adminkit/index.html'


def setup_views(site):
    if not hasattr(site, 'index_base'):
        site.index_base = site.index
        site.index = types.MethodType(views.index, site)
