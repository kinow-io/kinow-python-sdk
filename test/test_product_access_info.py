# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_access_info import ProductAccessInfo


class TestProductAccessInfo(unittest.TestCase):
    """ ProductAccessInfo unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductAccessInfo(self):
        """
        Test ProductAccessInfo
        """
        model = kinow_client.models.product_access_info.ProductAccessInfo()


if __name__ == '__main__':
    unittest.main()
