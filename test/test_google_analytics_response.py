# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.google_analytics_response import GoogleAnalyticsResponse


class TestGoogleAnalyticsResponse(unittest.TestCase):
    """ GoogleAnalyticsResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGoogleAnalyticsResponse(self):
        """
        Test GoogleAnalyticsResponse
        """
        model = kinow_client.models.google_analytics_response.GoogleAnalyticsResponse()


if __name__ == '__main__':
    unittest.main()
