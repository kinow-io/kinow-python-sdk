# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.prepayment_balance_list_response import PrepaymentBalanceListResponse


class TestPrepaymentBalanceListResponse(unittest.TestCase):
    """ PrepaymentBalanceListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrepaymentBalanceListResponse(self):
        """
        Test PrepaymentBalanceListResponse
        """
        model = kinow_client.models.prepayment_balance_list_response.PrepaymentBalanceListResponse()


if __name__ == '__main__':
    unittest.main()
