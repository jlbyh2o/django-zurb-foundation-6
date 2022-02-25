# /usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import find_packages, setup

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name="django-zurb-foundation-6",
    version="6.7.4",
    description="Django Zurb Foundation package.",
    author="Jeremy Bywater",
    author_email="jeremy@bywater.me",
    url="https://github.com/jlbyh2o/django-zurb-foundation-6",
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities'],
    install_requires=[

    ],
)
