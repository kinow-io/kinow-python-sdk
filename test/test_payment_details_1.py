# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.payment_details_1 import PaymentDetails1


class TestPaymentDetails1(unittest.TestCase):
    """ PaymentDetails1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaymentDetails1(self):
        """
        Test PaymentDetails1
        """
        model = kinow_client.models.payment_details_1.PaymentDetails1()


if __name__ == '__main__':
    unittest.main()
