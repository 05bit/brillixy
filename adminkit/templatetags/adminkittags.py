from django import template

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
                    apps_regroup[-1]['models'] += app['models']
                else:
                    base_index = app_index
                    app = apps[base_index]
                    app['name'] = group_name
                    apps_regroup.append(app)

        return apps_regroup
    else:
        return apps
