# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_access_response import ProductAccessResponse


class TestProductAccessResponse(unittest.TestCase):
    """ ProductAccessResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductAccessResponse(self):
        """
        Test ProductAccessResponse
        """
        model = kinow_client.models.product_access_response.ProductAccessResponse()


if __name__ == '__main__':
    unittest.main()
