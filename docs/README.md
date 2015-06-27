# Installation and basics

For installation guide and basic docs please visit https://github.com/05bit/brillixy and watch README.


# Contents

Documentation on extra features are provided below. The sections:

 * [Custom dashboard panels](#custom-dashboard-panels)
 * [Custom CSS and Javascript](#custom-css-and-javascript)
 * Layout tweaks
 * Using AdminSite
 * Using ModelAdmin


# Custom dashboard panels

You may place custom panels to admin dashboard. Panels are represented by classes subclassed from `brillixy.panels.BasePanel` and are rendered as grid blocks ([read about Bootstrap grid](http://twitter.github.com/bootstrap/scaffolding.html#gridSystem)).

Panels list is defined by `BRILLIXY_INDEX` in settings, default value is:

```python
BRILLIXY_INDEX = {
    'panels': [
        'brillixy.panels.AllModelsPanel',
    ]
}
```

#### brillixy.panels.BasePanel

Class attributes:

 * **template** - template used to render panel
 * **title** - title for rendering panel
 * **permissions** - list of permissions required to see the panel, default is empty value, so every user with access to admin interface can see it
 * **span** - integer number, the width of span, e.g. `span = 6` (default) means rendering with `span6` css class
 * **styles** - string with extra css classes for panel

Instance variables and methods:

 * `__init__`(self, *site*, *request*) - class constructor gets `AdminSite` instance and `request` object, don't forget to call `super` if you'll override this method!
 * **has_perm** - boolean flag if user has permission to see the panel

**Panel rendering.** Panel template is rendered with `{{ panel }}` instance variable and in has access to global admin index page context.

#### brillixy.panels.AllModelsPanel

This panel is included by default in `BRILLIXY_INDEX` setting and renders all models grouped by apps on admin dashboard. You can subclass from this class to make a panel with regrouped apps.

 * `app_groups`(self) - this method returns list or tuple of 2-tuples ('Group name', [apps list]), so apps are regrouped on render.

 * **styles** - can be empty or set to 'panel-big' for larger fonts

 Here's example of panel class wich groups `django.contrib.auth` and `django.contrib.sites` together:

```python
class MyModelsPanel(AllModelsPanel):
    styles = 'panel-big'

    def app_groups(self):
        return (
            # No title for group
            (u"", ('core',)),

            # With title for group
            (u"Auth & Sites", ('auth', 'sites')),
        )
```

# Custom CSS and JavaScript

You are able to load you own styles and scripts on admin pages and override default ones. To do that you can define ``BRILLIXY_MEDIA`` in project settings, its default value provided below:

```python
BRILLIXY_MEDIA = {
    'default': (
        # 3rd party libs
        'brillixy/bootstrap/css/bootstrap.min.css',
        'brillixy/fontawesome/css/font-awesome.min.css',
        'brillixy/fontawesome/css/font-awesome-ie7.min.css',
        'brillixy/jquery/jquery.min.js',
        'brillixy/bootstrap/js/bootstrap.min.js',
        # custom
        'brillixy/css/common.css',
    ),

    'index': (
        'brillixy/css/index.css',
    ),

    'change_list': (
        'brillixy/css/changelist.css',
        'brillixy/js/changelist.js',
    ),

    'change_form': (
        'brillixy/css/changeform.css',
        'brillixy/js/changeform.js',
    ),

    'history': (
        'brillixy/css/history.css',
    )

    'delete': (),
}
```

Styles and scripts in **default** list are loaded on every page of admin interface. Thus you can easily override Bootstrap css & js with your own customized ones.

The **change_form** list is reponsible for both add and edit object pages, and the **index** list is for dashboard admin page, etc.


# Layout tweaks

...
