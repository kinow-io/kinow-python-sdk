# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.84
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.order_histories_api import OrderHistoriesApi


class TestOrderHistoriesApi(unittest.TestCase):
    """ OrderHistoriesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.order_histories_api.OrderHistoriesApi()

    def tearDown(self):
        pass

    def test_get_order_histories(self):
        """
        Test case for get_order_histories

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
