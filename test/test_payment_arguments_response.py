# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.payment_arguments_response import PaymentArgumentsResponse


class TestPaymentArgumentsResponse(unittest.TestCase):
    """ PaymentArgumentsResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentArgumentsResponse(self):
        """
        Test PaymentArgumentsResponse
        """
        model = kinow_client.models.payment_arguments_response.PaymentArgumentsResponse()


if __name__ == '__main__':
    unittest.main()
