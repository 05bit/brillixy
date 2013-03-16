# Installation and basics

For installation guide and basic docs please visit https://github.com/05bit/brillixy and watch README file.

Documentation on extra features of Birllixy are provided below. The sections:

 * Custom dashboard panels
 * Custom CSS and Javascript
 * Layout tweaks
 * Using AdminSite
 * Using ModelAdmin


# Custom dashboard panels

...


# Custom CSS and JavaScript

You are able to load you own styles and scripts on admin pages and override default ones. To do that you can define ``BRILLIXY_MEDIA`` in project settings, its default value provided below:

```python
BRILLIXY_MEDIA = {
    'default': (
        'brillixy/bootstrap/css/bootstrap.min.css',
        'brillixy/fontawesome/css/font-awesome.min.css',
        'brillixy/fontawesome/css/font-awesome-ie7.min.css',
        'brillixy/css/common.css',
        'brillixy/jquery/jquery.min.js',
        'brillixy/bootstrap/js/bootstrap.min.js',
    ),

    'index': (
        'brillixy/css/index.css',
    ),

    'change_list': (
        'brillixy/css/changelist.css',
    ),

    'change_form': (
        'brillixy/css/changeform.css',
    ),

    'history': (
        'brillixy/css/history.css',
    )

    'delete': (),
}
```

Styles and scripts in **default** list are loaded on every page of admin interface. The **change_form** list is reponsible for both add and edit object pages, and the **index** list is for dashboard admin page.


# Layout tweaks

...
