from django.conf import settings
from django.views.decorators.cache import never_cache
from brillixy.panels import AllModelsPanel


@never_cache
def index(site, request, extra_context=None):
    """Admin site index view."""
    extra_context = {
        # 'title': 'lalal',
        'panels': site.get_panels(request)
    }
    return site.index_base(request, extra_context)
