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
from kinow_client.models.prepayment_bonus_list_response import PrepaymentBonusListResponse


class TestPrepaymentBonusListResponse(unittest.TestCase):
    """ PrepaymentBonusListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrepaymentBonusListResponse(self):
        """
        Test PrepaymentBonusListResponse
        """
        model = kinow_client.models.prepayment_bonus_list_response.PrepaymentBonusListResponse()


if __name__ == '__main__':
    unittest.main()
