# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.configuration_list_response import ConfigurationListResponse


class TestConfigurationListResponse(unittest.TestCase):
    """ ConfigurationListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testConfigurationListResponse(self):
        """
        Test ConfigurationListResponse
        """
        model = kinow_client.models.configuration_list_response.ConfigurationListResponse()


if __name__ == '__main__':
    unittest.main()
