# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_access_info_response import ProductAccessInfoResponse


class TestProductAccessInfoResponse(unittest.TestCase):
    """ ProductAccessInfoResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductAccessInfoResponse(self):
        """
        Test ProductAccessInfoResponse
        """
        model = kinow_client.models.product_access_info_response.ProductAccessInfoResponse()


if __name__ == '__main__':
    unittest.main()
