# -*- coding: utf-8 -*-
"""Setup file for easy installation"""
from os.path import join, dirname
from setuptools import setup, find_packages

version = '0.6.1'

LONG_DESCRIPTION = """
Brillixy is out of box improvements for Django admin to provide modern design and straightforward customization capabilities.
"""

def long_description():
    """Return long description from README.rst if it's present."""
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
    license='Creative Commons Attribution-NonCommercial 3.0 Unported License',
    keywords='django, django-admin, utils, sugar',
    url='http://05bit.com/brillixy/',
    packages=find_packages(),
    include_package_data=True,
    long_description=long_description(),
    install_requires=['Django>=1.4',],
    classifiers=['Development Status :: 3 - Alpha',
                 'Operating System :: OS Independent',
                 'License :: Free for non-commercial use',
                 'Intended Audience :: Developers',
                 'Environment :: Web Environment',
                 'Framework :: Django',
                 'Intended Audience :: Developers',
                 'Programming Language :: Python :: 2.5',
                 'Programming Language :: Python :: 2.6',
                 'Programming Language :: Python :: 2.7'])
