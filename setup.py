# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup

version = '0.5a'

LONG_DESCRIPTION = """
Brillixy is out of box improvements for Django admin to provide modern design and straightforward customization capabilities.
"""

def long_description():
    """Return long description from README.md if it's present
    because it doesn't get installed."""
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return LONG_DESCRIPTION

setup(
    name='brillixy',
    version=version,
    author='Alexey Kinyov',
    author_email='rudy@05bit.com',
    description='Customizations for Django admin interface.',
    license='MIT',
    keywords='django, django-admin, utils, sugar',
    url='https://github.com/05bit/brillixy',
    packages=['brillixy',],
    long_description=long_description(),
    install_requires=['Django>=1.4',],
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Operating System :: OS Independent',
                 'License :: OSI Approved :: MIT License',
                 'Intended Audience :: Developers',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python :: 2.5',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7'])
