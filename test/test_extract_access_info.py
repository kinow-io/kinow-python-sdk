# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.extract_access_info import ExtractAccessInfo


class TestExtractAccessInfo(unittest.TestCase):
    """ ExtractAccessInfo unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExtractAccessInfo(self):
        """
        Test ExtractAccessInfo
        """
        model = kinow_client.models.extract_access_info.ExtractAccessInfo()


if __name__ == '__main__':
    unittest.main()
