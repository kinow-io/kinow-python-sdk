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
from kinow_client.models.currency_list_response_1 import CurrencyListResponse1


class TestCurrencyListResponse1(unittest.TestCase):
    """ CurrencyListResponse1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCurrencyListResponse1(self):
        """
        Test CurrencyListResponse1
        """
        model = kinow_client.models.currency_list_response_1.CurrencyListResponse1()


if __name__ == '__main__':
    unittest.main()
