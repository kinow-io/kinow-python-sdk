# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.create_product_request import CreateProductRequest


class TestCreateProductRequest(unittest.TestCase):
    """ CreateProductRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateProductRequest(self):
        """
        Test CreateProductRequest
        """
        model = kinow_client.models.create_product_request.CreateProductRequest()


if __name__ == '__main__':
    unittest.main()
