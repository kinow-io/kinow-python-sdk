# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.75
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.customers_api import CustomersApi


class TestCustomersApi(unittest.TestCase):
    """ CustomersApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.customers_api.CustomersApi()

    def tearDown(self):
        pass

    def test_attach_cart_to_customer(self):
        """
        Test case for attach_cart_to_customer

        
        """
        pass

    def test_check_customer_credentials(self):
        """
        Test case for check_customer_credentials

        
        """
        pass

    def test_create_customer(self):
        """
        Test case for create_customer

        
        """
        pass

    def test_create_facebook_id(self):
        """
        Test case for create_facebook_id

        
        """
        pass

    def test_delete_customer(self):
        """
        Test case for delete_customer

        
        """
        pass

    def test_generate_authentication_token(self):
        """
        Test case for generate_authentication_token

        
        """
        pass

    def test_get_customer(self):
        """
        Test case for get_customer

        
        """
        pass

    def test_get_customer_accesses_subscriptions(self):
        """
        Test case for get_customer_accesses_subscriptions

        
        """
        pass

    def test_get_customer_accesses_videos(self):
        """
        Test case for get_customer_accesses_videos

        
        """
        pass

    def test_get_customer_address(self):
        """
        Test case for get_customer_address

        
        """
        pass

    def test_get_customer_can_see_product(self):
        """
        Test case for get_customer_can_see_product

        
        """
        pass

    def test_get_customer_current_views(self):
        """
        Test case for get_customer_current_views

        
        """
        pass

    def test_get_customer_groups(self):
        """
        Test case for get_customer_groups

        
        """
        pass

    def test_get_customer_has_access_to_product(self):
        """
        Test case for get_customer_has_access_to_product

        
        """
        pass

    def test_get_customer_has_access_to_video(self):
        """
        Test case for get_customer_has_access_to_video

        
        """
        pass

    def test_get_customer_orders(self):
        """
        Test case for get_customer_orders

        
        """
        pass

    def test_get_customers(self):
        """
        Test case for get_customers

        
        """
        pass

    def test_get_download_url(self):
        """
        Test case for get_download_url

        
        """
        pass

    def test_get_marlin_token(self):
        """
        Test case for get_marlin_token

        
        """
        pass

    def test_get_payment_customer_id(self):
        """
        Test case for get_payment_customer_id

        
        """
        pass

    def test_get_player_url(self):
        """
        Test case for get_player_url

        
        """
        pass

    def test_update_customer(self):
        """
        Test case for update_customer

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
