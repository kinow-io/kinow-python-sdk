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
from kinow_client.models.product_attribute_list_response import ProductAttributeListResponse


class TestProductAttributeListResponse(unittest.TestCase):
    """ ProductAttributeListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductAttributeListResponse(self):
        """
        Test ProductAttributeListResponse
        """
        model = kinow_client.models.product_attribute_list_response.ProductAttributeListResponse()


if __name__ == '__main__':
    unittest.main()
