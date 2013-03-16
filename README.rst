Overview
========

Brillixy is out of box improvements for Django admin to provide modern design and straightforward customization capabilities. Official home page: http://05bit.com/brillixy/.

Requirements
============

Django 1.4.x/1.5.x is supported. Django 1.3.x support is not available at the moment.

Features
========

After installation you'll get fully featured Django admin with refined design powered by responsive Twitter Bootstrap layout. And yet, Brillixy may work fine with simple projects, it's in active development at the moment to be more robust and fit more complex ones.

All basic admin features are implemented at the moment. Also you will get some extras:

* global header logo & text customization
* custom dashboard panels API

Installation
============

Standard Django admin should be enabled and configured as usually.

1. Install using ``pip``::

    pip install brillixy

2. Add ``brillixy`` to ``INSTALLED_APPS`` before ``django.contrib.admin``:

.. sourcecode:: python

    INSTALLED_APPS = (
        # ...
        
        'brillixy',
        
        # Uncomment the next line to enable the admin:
        'django.contrib.admin',

        # ...
    )

3. Add initialization code to ``urls.py`` right after Django admin autodiscover code:

.. sourcecode:: python

    # Uncomment the next two lines to enable the admin:
    from django.contrib import admin
    admin.autodiscover()

    # Setup Brillixy views & templates
    import brillixy.site
    brillixy.site.setup(admin.site)

Customization
=============

Here's basic example of customization code in settings file from ``example`` project provided with the source code of Brillixy:

.. sourcecode:: python

    # Brillixy settings
    BRILLIXY_INDEX = {
        'panels': [
            'example_core.admin.MyModelsPanel',
            'brillixy.panels.AllModelsPanel',
        ]
    }

    BRILLIXY_BRANDING = {
        'logo': '%slogo.png' % STATIC_URL,
        'title': u"Brillixy Demo",
    }

Read more about extra customizations in docs: https://github.com/05bit/brillixy/tree/master/docs.

Troubleshooting
===============

If you see old or broken admin interface that may be custom admin templates that overrides Brillixy's templates.

Please make sure:

* you don't have 'admin/\*' templates in paths defined in ``TEMPLATE_DIRS``
* you don't have apps before ``brillixy`` in ``INSTALLED_APPS`` that overrides 'admin/\*' templates
* you don't have ModelAdmin or inlines that use custom templates based on default admin templates

License, commercial usage
=========================

.. image:: http://i.creativecommons.org/l/by-nc/3.0/88x31.png

Brillixy by is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported License http://creativecommons.org/licenses/by-nc/3.0/

For commercial usage we're selling commercial license at our official site http://05bit.com/brillixy/. You're welcome!

Feedback
========

You're welcome to post issues at GitHub https://github.com/05bit/brillixy/issues or you may drop a line to Alexey Kinyov <rudy@05bit.com>
