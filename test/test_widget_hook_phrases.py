# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.22
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.widget_hook_phrases import WidgetHookPhrases


class TestWidgetHookPhrases(unittest.TestCase):
    """ WidgetHookPhrases unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidgetHookPhrases(self):
        """
        Test WidgetHookPhrases
        """
        model = kinow_client.models.widget_hook_phrases.WidgetHookPhrases()


if __name__ == '__main__':
    unittest.main()
