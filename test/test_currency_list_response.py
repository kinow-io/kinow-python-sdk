# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.currency_list_response import CurrencyListResponse


class TestCurrencyListResponse(unittest.TestCase):
    """ CurrencyListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCurrencyListResponse(self):
        """
        Test CurrencyListResponse
        """
        model = kinow_client.models.currency_list_response.CurrencyListResponse()


if __name__ == '__main__':
    unittest.main()
