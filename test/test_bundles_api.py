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
from kinow_client.apis.bundles_api import BundlesApi


class TestBundlesApi(unittest.TestCase):
    """ BundlesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.bundles_api.BundlesApi()

    def tearDown(self):
        pass

    def test_add_product_to_bundle(self):
        """
        Test case for add_product_to_bundle

        
        """
        pass

    def test_get_bundle_products(self):
        """
        Test case for get_bundle_products

        
        """
        pass

    def test_remove_product_from_bundle(self):
        """
        Test case for remove_product_from_bundle

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
