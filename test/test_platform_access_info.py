# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.37
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.platform_access_info import PlatformAccessInfo


class TestPlatformAccessInfo(unittest.TestCase):
    """ PlatformAccessInfo unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlatformAccessInfo(self):
        """
        Test PlatformAccessInfo
        """
        model = kinow_client.models.platform_access_info.PlatformAccessInfo()


if __name__ == '__main__':
    unittest.main()
