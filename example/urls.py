from django.conf import settings
from django.conf.urls import patterns, include, url
import example.core.views
import django.views.static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Enable Brillixy extra customizations
import brillixy.site
brillixy.site.setup(admin.site)

urlpatterns = patterns('',
    # Examples:
    url(r'^$', example.core.views.home, name='home'),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# Serve media for development mode
if settings.DEBUG or getattr(settings, 'SERVE_MEDIA', False):
    urlpatterns += patterns('',
        url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
            django.views.static.serve,
            {'document_root': settings.MEDIA_ROOT}),
    )
