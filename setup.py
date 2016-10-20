__author__ = 'Alfredo Saglimbeni'

import os

from distutils.core import setup
from setuptools import setup, find_packages

import datetimewidget

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

def get_reqs(*fns):
    lst = []
    for fn in fns:
        for package in open(os.path.join(CURRENT_DIR, fn)).readlines():
            package = package.strip()
            if not package:
                continue
            lst.append(package.strip())
    return lst

setup(
    name="django-datetime-widget",
    version=datetimewidget.__version__,
    description="Django-datetime-widget is a simple and clean widget for DateField, Timefiled and DateTimeField  in Django framework. It is based on Bootstrap datetime picker, supports both Bootstrap 3 and Bootstrap 2",
    long_description=open('README.rst').read(),
    author="Alfredo Saglimbeni",
    author_email="alfredo.saglimbeni@gmail.com",
    url="",
    license="BSD",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        "License :: OSI Approved :: BSD License",
        'Topic :: Software Development :: Libraries :: Python Modules ',
        ],
    zip_safe=False,
    install_requires=get_reqs('pip-requirements-min-django.txt', 'pip-requirements.txt'),
    tests_require=get_reqs('pip-requirements-test.txt'),
)
