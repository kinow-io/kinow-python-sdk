# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.57
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.prepayment_bonus_amount import PrepaymentBonusAmount


class TestPrepaymentBonusAmount(unittest.TestCase):
    """ PrepaymentBonusAmount unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrepaymentBonusAmount(self):
        """
        Test PrepaymentBonusAmount
        """
        model = kinow_client.models.prepayment_bonus_amount.PrepaymentBonusAmount()


if __name__ == '__main__':
    unittest.main()
