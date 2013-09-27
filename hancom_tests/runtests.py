#!/usr/bin/env python
import os
import sys
import imp

from django.conf import settings


MY_INSTALLED_APPS = [
    'hancom',
    'hancom_tests',
]


try:
    imp.find_module("django_nose")
    MY_INSTALLED_APPS.append("django_nose")
except ImportError:
    pass


if not settings.configured:
    settings.configure(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
            }
        },
        INSTALLED_APPS = MY_INSTALLED_APPS,
        SITE_ID = 1,
        STATIC_URL = '/static/',
        ROOT_URLCONF = 'hancom.tests.urls',
        NOSE_ARGS = [
            "--with-xcoverage", 
            "--cover-inclusive", 
            "--with-xunit", 
            "--exe",
            "--verbosity=3", 
            "--cover-package=hancom"
        ],
        NOSE_PLUGINS = [
            'nosexcover.XCoverage',
            "nose_exclude.NoseExclude"
        ],
    )


try:
    from django_nose.runner import NoseTestSuiteRunner
except ImportError:
    from django.test.simple import DjangoTestSuiteRunner


def runtests():
    try:
        runner = NoseTestSuiteRunner()
    except NameError:
        runner = DjangoTestSuiteRunner()
    failures = runner.run_tests(['hancom_tests'])
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])
