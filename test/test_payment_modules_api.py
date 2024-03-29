# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.payment_modules_api import PaymentModulesApi


class TestPaymentModulesApi(unittest.TestCase):
    """ PaymentModulesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.payment_modules_api.PaymentModulesApi()

    def tearDown(self):
        pass

    def test_get_cart_payment_modules(self):
        """
        Test case for get_cart_payment_modules

        
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

    def test_get_payment_modules(self):
        """
        Test case for get_payment_modules

        
        """
        pass

    def test_get_payment_token(self):
        """
        Test case for get_payment_token

        
        """
        pass

    def test_get_payment_url(self):
        """
        Test case for get_payment_url

        
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

    def test_prepare_payment(self):
        """
        Test case for prepare_payment

        
        """
        pass

    def test_recurring_payment(self):
        """
        Test case for recurring_payment

        
        """
        pass

    def test_update_payment_method(self):
        """
        Test case for update_payment_method

        
        """
        pass

    def test_validate_free_order(self):
        """
        Test case for validate_free_order

        
        """
        pass

    def test_validate_payment(self):
        """
        Test case for validate_payment

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
