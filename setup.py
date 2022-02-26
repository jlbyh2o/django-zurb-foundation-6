# /usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="django-zurb-foundation-6",
    version="6.7.4.2",
    description="Django Zurb Foundation package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Jeremy Bywater",
    author_email="6372964+jlbyh2o@users.noreply.github.com",
    url="https://github.com/jlbyh2o/django-zurb-foundation-6",
    license='Unlicense',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 4',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: The Unlicense (Unlicense)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Topic :: Utilities'],
    python_requires=">3.6",
)
