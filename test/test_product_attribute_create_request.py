# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_attribute_create_request import ProductAttributeCreateRequest


class TestProductAttributeCreateRequest(unittest.TestCase):
    """ ProductAttributeCreateRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductAttributeCreateRequest(self):
        """
        Test ProductAttributeCreateRequest
        """
        model = kinow_client.models.product_attribute_create_request.ProductAttributeCreateRequest()


if __name__ == '__main__':
    unittest.main()
