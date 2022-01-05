# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.configuration_api import ConfigurationApi


class TestConfigurationApi(unittest.TestCase):
    """ ConfigurationApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.configuration_api.ConfigurationApi()

    def tearDown(self):
        pass

    def test_get_configuration(self):
        """
        Test case for get_configuration

        
        """
        pass

    def test_get_configuration_analytics(self):
        """
        Test case for get_configuration_analytics

        
        """
        pass

    def test_get_configuration_by_name(self):
        """
        Test case for get_configuration_by_name

        
        """
        pass

    def test_get_configuration_logo(self):
        """
        Test case for get_configuration_logo

        
        """
        pass

    def test_get_configuration_social(self):
        """
        Test case for get_configuration_social

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
