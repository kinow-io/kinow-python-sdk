# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.prepayment_operation_id_list import PrepaymentOperationIDList


class TestPrepaymentOperationIDList(unittest.TestCase):
    """ PrepaymentOperationIDList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrepaymentOperationIDList(self):
        """
        Test PrepaymentOperationIDList
        """
        model = kinow_client.models.prepayment_operation_id_list.PrepaymentOperationIDList()


if __name__ == '__main__':
    unittest.main()
