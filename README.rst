Disclaimer
==========

Yet, Brillixy may work fine with simple projects, it's in active development at the moment to be more robust and fit more complex ones.

About
=====

Brillixy is out of box improvements for Django admin to provide modern design and straightforward customization capabilities.

Requirements
============

Django 1.4.x/1.5.x is supported and required. Actually it may work with Django 1.3.x, but it's not well tested yet.

Features
========

After installation you'll get almost fully featured Django admin with refined design powered by responsive Twitter Bootstrap layout.

All basic admin features are implemented at the moment. Also you will get some extras::

    * global header logo & text customization
    * customizable dashboard

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

    # Enable Brillixy extra customizations
    from brillixy import site as brillixy
    brillixy.setup(admin.site)

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
    }

License, commercial usage
=========================

.. image:: http://i.creativecommons.org/l/by-nc/3.0/88x31.png

Brillixy by is licensed under a Creative Commons Attribution-NonCommercial 3.0 Unported License http://creativecommons.org/licenses/by-nc/3.0/

For commercial usage you should purchase commercial license. Pricing model is in development at the moment to be fair. Currently "pay as you want" pricing model is active. You're welcome to share your considerations with us. Please contact Alexey Kinyov <rudy@05bit.com>.

Feedback
========

You're welcome to post issues at GitHub https://github.com/05bit/brillixy/issues or you may drop a line to Alexey Kinyov <rudy@05bit.com>
