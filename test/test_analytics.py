# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.41
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.analytics import Analytics


class TestAnalytics(unittest.TestCase):
    """ Analytics unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAnalytics(self):
        """
        Test Analytics
        """
        model = kinow_client.models.analytics.Analytics()


if __name__ == '__main__':
    unittest.main()
