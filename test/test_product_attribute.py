# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_attribute import ProductAttribute


class TestProductAttribute(unittest.TestCase):
    """ ProductAttribute unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductAttribute(self):
        """
        Test ProductAttribute
        """
        model = kinow_client.models.product_attribute.ProductAttribute()


if __name__ == '__main__':
    unittest.main()
