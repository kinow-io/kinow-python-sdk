# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_price_response import ProductPriceResponse


class TestProductPriceResponse(unittest.TestCase):
    """ ProductPriceResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductPriceResponse(self):
        """
        Test ProductPriceResponse
        """
        model = kinow_client.models.product_price_response.ProductPriceResponse()


if __name__ == '__main__':
    unittest.main()
