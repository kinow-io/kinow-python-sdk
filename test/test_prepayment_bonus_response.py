# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.prepayment_bonus_response import PrepaymentBonusResponse


class TestPrepaymentBonusResponse(unittest.TestCase):
    """ PrepaymentBonusResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrepaymentBonusResponse(self):
        """
        Test PrepaymentBonusResponse
        """
        model = kinow_client.models.prepayment_bonus_response.PrepaymentBonusResponse()


if __name__ == '__main__':
    unittest.main()
