# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.prepayment_operation_response import PrepaymentOperationResponse


class TestPrepaymentOperationResponse(unittest.TestCase):
    """ PrepaymentOperationResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrepaymentOperationResponse(self):
        """
        Test PrepaymentOperationResponse
        """
        model = kinow_client.models.prepayment_operation_response.PrepaymentOperationResponse()


if __name__ == '__main__':
    unittest.main()
