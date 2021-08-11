# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.45
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.orders_api import OrdersApi


class TestOrdersApi(unittest.TestCase):
    """ OrdersApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.orders_api.OrdersApi()

    def tearDown(self):
        pass

    def test_get_customer_orders(self):
        """
        Test case for get_customer_orders

        
        """
        pass

    def test_get_order(self):
        """
        Test case for get_order

        
        """
        pass

    def test_get_order_histories(self):
        """
        Test case for get_order_histories

        
        """
        pass

    def test_get_order_invoice(self):
        """
        Test case for get_order_invoice

        
        """
        pass

    def test_get_orders(self):
        """
        Test case for get_orders

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
