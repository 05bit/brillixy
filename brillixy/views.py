from django.views.decorators.cache import never_cache


@never_cache
def index(site, request, extra_context=None):
    """Admin site index view."""
    extra_context = {
        # 'title': 'lalal',
        'panels': site.get_panels(request)
    }
    return site.index_base(request, extra_context)


@never_cache
def view_on_site(site, request, content_type_id, object_id):
    """Admin view on site view. Actually, such view is provided
    since Django 1.5 and we only need it here to work with
    Django 1.4.x.
    """
    from django.contrib.contenttypes.views import shortcut
    return shortcut(request, content_type_id, object_id)
