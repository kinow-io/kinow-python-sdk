# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.feature_values_api import FeatureValuesApi


class TestFeatureValuesApi(unittest.TestCase):
    """ FeatureValuesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.feature_values_api.FeatureValuesApi()

    def tearDown(self):
        pass

    def test_attach_features_to_category(self):
        """
        Test case for attach_features_to_category

        
        """
        pass

    def test_attach_features_to_extract(self):
        """
        Test case for attach_features_to_extract

        
        """
        pass

    def test_attach_features_to_product(self):
        """
        Test case for attach_features_to_product

        
        """
        pass

    def test_attach_features_to_video(self):
        """
        Test case for attach_features_to_video

        
        """
        pass

    def test_detach_feature_to_product(self):
        """
        Test case for detach_feature_to_product

        
        """
        pass

    def test_get_feature_values(self):
        """
        Test case for get_feature_values

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
