# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.prepayment_recharge_response import PrepaymentRechargeResponse


class TestPrepaymentRechargeResponse(unittest.TestCase):
    """ PrepaymentRechargeResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrepaymentRechargeResponse(self):
        """
        Test PrepaymentRechargeResponse
        """
        model = kinow_client.models.prepayment_recharge_response.PrepaymentRechargeResponse()


if __name__ == '__main__':
    unittest.main()
