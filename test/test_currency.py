# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.58
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.currency import Currency


class TestCurrency(unittest.TestCase):
    """ Currency unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCurrency(self):
        """
        Test Currency
        """
        model = kinow_client.models.currency.Currency()


if __name__ == '__main__':
    unittest.main()
