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
from kinow_client.models.payment_arguments import PaymentArguments


class TestPaymentArguments(unittest.TestCase):
    """ PaymentArguments unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentArguments(self):
        """
        Test PaymentArguments
        """
        model = kinow_client.models.payment_arguments.PaymentArguments()


if __name__ == '__main__':
    unittest.main()
