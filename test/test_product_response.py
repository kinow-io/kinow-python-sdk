# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_response import ProductResponse


class TestProductResponse(unittest.TestCase):
    """ ProductResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductResponse(self):
        """
        Test ProductResponse
        """
        model = kinow_client.models.product_response.ProductResponse()


if __name__ == '__main__':
    unittest.main()
