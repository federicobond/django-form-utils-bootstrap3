django-form-utils-bootstrap3
============================

.. image:: https://img.shields.io/pypi/v/django-form-utils-bootstrap3.svg
    :target: https://pypi.python.org/pypi/django-form-utils-bootstrap3
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/federicobond/django-form-utils-bootstrap3.png
   :target: https://travis-ci.org/federicobond/django-form-utils-bootstrap3
   :alt: Latest Travis CI build status

Render forms with fieldsets using Bootstrap markup via django-form-utils and django-bootstrap3

Configuration
------------

Modify your Django project settings to include:

````
BOOTSTRAP3 = {
    'form_renderers': {
        'default': 'form_utils_bootstrap3.renderers.BetterFormRenderer'
    }
}
````

Installation
------------

````
pip install django-form-utils-bootstrap3
````

Requirements
^^^^^^^^^^^^

A Django project using:

 * django-form-utils
 * django-bootstrap3

Compatibility
-------------

Licence
-------

MIT

Authors
-------

`django-form-utils-bootstrap3` was written by `Federico Bond <federicobond@gmail.com>`_.
