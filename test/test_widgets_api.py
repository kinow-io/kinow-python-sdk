# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.85
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.widgets_api import WidgetsApi


class TestWidgetsApi(unittest.TestCase):
    """ WidgetsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.widgets_api.WidgetsApi()

    def tearDown(self):
        pass

    def test_get_intro_image(self):
        """
        Test case for get_intro_image

        
        """
        pass

    def test_get_widget_footer_menu(self):
        """
        Test case for get_widget_footer_menu

        
        """
        pass

    def test_get_widget_slider(self):
        """
        Test case for get_widget_slider

        
        """
        pass

    def test_get_widget_slider_item(self):
        """
        Test case for get_widget_slider_item

        
        """
        pass

    def test_get_widget_top_menu(self):
        """
        Test case for get_widget_top_menu

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
