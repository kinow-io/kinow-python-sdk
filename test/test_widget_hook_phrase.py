# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.64
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.widget_hook_phrase import WidgetHookPhrase


class TestWidgetHookPhrase(unittest.TestCase):
    """ WidgetHookPhrase unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidgetHookPhrase(self):
        """
        Test WidgetHookPhrase
        """
        model = kinow_client.models.widget_hook_phrase.WidgetHookPhrase()


if __name__ == '__main__':
    unittest.main()
