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
from kinow_client.apis.customers_api import CustomersApi


class TestCustomersApi(unittest.TestCase):
    """ CustomersApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.customers_api.CustomersApi()

    def tearDown(self):
        pass

    def test_attach_bookmark_to_customer(self):
        """
        Test case for attach_bookmark_to_customer

        
        """
        pass

    def test_attach_cart_to_customer(self):
        """
        Test case for attach_cart_to_customer

        
        """
        pass

    def test_check_authentication_token(self):
        """
        Test case for check_authentication_token

        
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

    def test_create_google_id(self):
        """
        Test case for create_google_id

        
        """
        pass

    def test_delete_customer(self):
        """
        Test case for delete_customer

        
        """
        pass

    def test_detach_bookmark_from_customer(self):
        """
        Test case for detach_bookmark_from_customer

        
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

    def test_get_customer_bookmarks(self):
        """
        Test case for get_customer_bookmarks

        
        """
        pass

    def test_get_customer_can_see_product(self):
        """
        Test case for get_customer_can_see_product

        
        """
        pass

    def test_get_customer_carts(self):
        """
        Test case for get_customer_carts

        
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

    def test_get_customer_has_access_to_products(self):
        """
        Test case for get_customer_has_access_to_products

        
        """
        pass

    def test_get_customer_has_access_to_video(self):
        """
        Test case for get_customer_has_access_to_video

        
        """
        pass

    def test_get_customer_has_access_to_videos(self):
        """
        Test case for get_customer_has_access_to_videos

        
        """
        pass

    def test_get_customer_orders(self):
        """
        Test case for get_customer_orders

        
        """
        pass

    def test_get_customer_playlists(self):
        """
        Test case for get_customer_playlists

        
        """
        pass

    def test_get_customer_prepayment_balances(self):
        """
        Test case for get_customer_prepayment_balances

        
        """
        pass

    def test_get_customer_prepayment_operations(self):
        """
        Test case for get_customer_prepayment_operations

        
        """
        pass

    def test_get_customers(self):
        """
        Test case for get_customers

        
        """
        pass

    def test_get_facebook_customer(self):
        """
        Test case for get_facebook_customer

        
        """
        pass

    def test_get_google_customer(self):
        """
        Test case for get_google_customer

        
        """
        pass

    def test_get_payment_methods(self):
        """
        Test case for get_payment_methods

        
        """
        pass

    def test_get_payment_methods_with_ip(self):
        """
        Test case for get_payment_methods_with_ip

        
        """
        pass

    def test_get_pending_payments(self):
        """
        Test case for get_pending_payments

        
        """
        pass

    def test_get_pending_payments_with_ip(self):
        """
        Test case for get_pending_payments_with_ip

        
        """
        pass

    def test_get_registration_fields(self):
        """
        Test case for get_registration_fields

        
        """
        pass

    def test_login_with_facebook(self):
        """
        Test case for login_with_facebook

        
        """
        pass

    def test_login_with_google(self):
        """
        Test case for login_with_google

        
        """
        pass

    def test_password_token(self):
        """
        Test case for password_token

        
        """
        pass

    def test_password_token_consume(self):
        """
        Test case for password_token_consume

        
        """
        pass

    def test_stop_subscription(self):
        """
        Test case for stop_subscription

        
        """
        pass

    def test_update_customer(self):
        """
        Test case for update_customer

        
        """
        pass

    def test_update_payment_method(self):
        """
        Test case for update_payment_method

        
        """
        pass

    def test_validate_customer_credentials(self):
        """
        Test case for validate_customer_credentials

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
