# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_categories import ProductCategories


class TestProductCategories(unittest.TestCase):
    """ ProductCategories unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductCategories(self):
        """
        Test ProductCategories
        """
        model = kinow_client.models.product_categories.ProductCategories()


if __name__ == '__main__':
    unittest.main()
