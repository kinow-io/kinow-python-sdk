# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.subscriptions_api import SubscriptionsApi


class TestSubscriptionsApi(unittest.TestCase):
    """ SubscriptionsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.subscriptions_api.SubscriptionsApi()

    def tearDown(self):
        pass

    def test_get_disabled_subscriptions(self):
        """
        Test case for get_disabled_subscriptions

        
        """
        pass

    def test_get_product_subscription(self):
        """
        Test case for get_product_subscription

        
        """
        pass

    def test_get_subscription(self):
        """
        Test case for get_subscription

        
        """
        pass

    def test_get_subscription_categories(self):
        """
        Test case for get_subscription_categories

        
        """
        pass

    def test_get_subscription_cover_image(self):
        """
        Test case for get_subscription_cover_image

        
        """
        pass

    def test_get_subscriptions(self):
        """
        Test case for get_subscriptions

        
        """
        pass

    def test_upload_subscription_cover(self):
        """
        Test case for upload_subscription_cover

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
