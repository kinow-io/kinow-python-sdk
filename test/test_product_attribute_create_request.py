# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.53
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.product_attribute_create_request import ProductAttributeCreateRequest


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
        model = kaemo_client.models.product_attribute_create_request.ProductAttributeCreateRequest()


if __name__ == '__main__':
    unittest.main()
