import re
from django import template
from django.conf import settings
from django.contrib.admin.views.main import PAGE_VAR
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from brillixy import defaults


register = template.Library()


@register.filter
def regroup_apps(apps, groups):
    if groups:
        # ``app_url`` is like '/admin/auth/', so tag is 'auth'
        apps_tags = map(lambda app: app['app_url'].split('/')[-2], apps)
        apps_regroup = []
        for group_name, group in groups:
            base_index = None
            for app_tag in group:
                try:
                    app_index = apps_tags.index(app_tag)
                except ValueError:
                    continue
                
                if not base_index is None:
                    app = apps[app_index]
                    apps_regroup[-1]['models'] += app['models'][:]
                else:
                    base_index = app_index
                    app = apps[base_index].copy()
                    app['models'] = app['models'][:]
                    app['name'] = group_name
                    apps_regroup.append(app)
        return apps_regroup
    else:
        return apps


@register.filter
def user_nice_name(user):
    for method in ('get_short_name', 'get_username', 'get_full_name'):
        if hasattr(user, method):
            name = getattr(user, method)()
            if name:
                return name
    return user.username


@register.simple_tag
def branding_logo():
    # default = '%sbrillixy/logo.png' % settings.STATIC_URL
    if hasattr(settings, 'BRILLIXY_BRANDING'):
        src = settings.BRILLIXY_BRANDING.get('logo', None)
    else:
        src = None
    return src and mark_safe('<img src="%s">' % src) or u''


@register.simple_tag
def branding_title():
    default = _('Django administration')
    if hasattr(settings, 'BRILLIXY_BRANDING'):
        return mark_safe(settings.BRILLIXY_BRANDING.get('title', default))
    return default


@register.simple_tag
def page_number(cl, i):
    if i == '.':
        return '... '
    elif i == cl.page_num:
        return mark_safe('<a class="btn btn-primary this-page">%s</a> ' % (i+1))
    else:
        return mark_safe('<a href="%s" class="btn">%s</a> ' % (
           cl.get_query_string({PAGE_VAR: i}), i+1))


@register.simple_tag
def media_for(name):
    """ Get CSS and JavaScript inclusion code for page by ``name``.
    """
    media = []
    # unknown = []
    config = getattr(settings, 'BRILLIXY_MEDIA', defaults.BRILLIXY_MEDIA)
    for item in config.get(name, ()):
        if callable(item):
            item = item(name)
        if item.startswith('<'):
            media.append(item)
        else:
            item_type = item.rsplit('.', 1)[-1].lower()
            item_path = '://' in item and item or (settings.STATIC_URL + item)

            if item_type == 'js':
                item_str = '<script type="text/javascript" src="%s"></script>' % item_path
            elif item_type == 'css':
                item_str = '<link rel="stylesheet" type="text/css" href="%s" />' % item_path
            elif item_type == 'less':
                item_str = '<link rel="stylesheet/less" type="text/css" href="%s" />' % item_path
            else:
                raise Exception("Unknown meida type for item: %s" % item)
                # unknown.append((item_type, item))

            ie_match = re.search(r'-(ie(\d))', item, re.IGNORECASE)
            if ie_match:
                media.append('<!--[if IE %s]>%s<![endif]-->' % (ie_match.groups()[1], item_str))
            else:
                media.append(item_str)
    return mark_safe('\n'.join(media))
