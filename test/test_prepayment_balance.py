# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.prepayment_balance import PrepaymentBalance


class TestPrepaymentBalance(unittest.TestCase):
    """ PrepaymentBalance unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrepaymentBalance(self):
        """
        Test PrepaymentBalance
        """
        model = kinow_client.models.prepayment_balance.PrepaymentBalance()


if __name__ == '__main__':
    unittest.main()
