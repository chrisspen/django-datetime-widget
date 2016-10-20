# -*- coding: utf-8 -*-

import datetime

import six

from django.test import TestCase
from django.test.client import Client
from django.conf import settings

from datetimewidget import widgets

unicode = six.text_type # pylint: disable=W0622

class Tests(TestCase):
    
    def setUp(self):
        self.browser = Client(enforce_csrf_checks=False)
    
    def test_forms_v3(self):
        response = self.browser.get('/model_form_v3/')
#         print response
        self.assertEqual(response.status_code, 200)
        d = datetime.datetime.now()
        response = self.client.post(
            '/model_form_v3/',
            {
                'date_time': d.strftime('%Y-%m-%d %H:%M'),
                'date': d.strftime('%Y-%m-%d'),
                'time': d.strftime('%H:%M'),
            })
#         print response
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Validation successful' in unicode(response))
        
    def test_forms_v2(self):
        response = self.browser.get('/model_form_v2/')
#         print response
        d = datetime.datetime.now()
        response = self.client.post(
            '/model_form_v3/',
            {
                'date_time': d.strftime('%Y-%m-%d %H:%M'),
                'date': d.strftime('%Y-%m-%d'),
                'time': d.strftime('%H:%M'),
            })
#         print response
        self.assertEqual(response.status_code, 200)
        self.assertTrue('Validation successful' in unicode(response))
