# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.69
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.widget_top_menu import WidgetTopMenu


class TestWidgetTopMenu(unittest.TestCase):
    """ WidgetTopMenu unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testWidgetTopMenu(self):
        """
        Test WidgetTopMenu
        """
        model = kinow_client.models.widget_top_menu.WidgetTopMenu()


if __name__ == '__main__':
    unittest.main()
