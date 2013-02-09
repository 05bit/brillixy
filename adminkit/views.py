from django.conf import settings
from django.views.decorators.cache import never_cache
from adminkit.panels import AllModelsPanel


@never_cache
def index(site, request, extra_context=None):
    """Admin site index view."""
    if hasattr(site, 'panels'):
        panels = site.panels
    elif hasattr(settings, 'ADMINKIT_INDEX') and \
        settings.ADMINKIT_INDEX['panels']:
            panels = []
            for panel in settings.ADMINKIT_INDEX['panels']:
                panel_mod, panel_cls = panel.rsplit('.', 1)
                mod = __import__(panel_mod, fromlist=[panel_cls])
                panels.append(getattr(mod, panel_cls)())
    else:
        panels = [AllModelsPanel()]

    extra_context = {
        # 'title': 'lalal',
        'panels': panels
    }
    return site.index_base(request, extra_context)
