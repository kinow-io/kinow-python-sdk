# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_attribute_create_request_1 import ProductAttributeCreateRequest1


class TestProductAttributeCreateRequest1(unittest.TestCase):
    """ ProductAttributeCreateRequest1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductAttributeCreateRequest1(self):
        """
        Test ProductAttributeCreateRequest1
        """
        model = kinow_client.models.product_attribute_create_request_1.ProductAttributeCreateRequest1()


if __name__ == '__main__':
    unittest.main()
