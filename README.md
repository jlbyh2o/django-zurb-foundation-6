django-zurb-foundation-6 (6.7.4)
============================

Django Zurb Foundation 6 package for Django 4.

Version of this package is equal to the version of Zurb Foundation it provides.

Installation
============
**Install with pip:**
```sh
pip install --upgrade django-zurb-foundation-6
```

Usage
=====

- Add `foundation` to your `INSTALLED_APPS`.
- If you want to use the provided base template, extend from `foundation/base.html`. If you want to write one from scratch, see the example template.
- If you want to test if foundation works, include `foundation.urls` in your urls.py and visit the path. You should see the Foundation test page.

Foundation icons
================
- If you have added `foundation.urls` to your urls.py visit `icons/` on that path to see them.