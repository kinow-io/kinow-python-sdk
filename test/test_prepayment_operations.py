# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.31
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.prepayment_operations import PrepaymentOperations


class TestPrepaymentOperations(unittest.TestCase):
    """ PrepaymentOperations unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrepaymentOperations(self):
        """
        Test PrepaymentOperations
        """
        model = kinow_client.models.prepayment_operations.PrepaymentOperations()


if __name__ == '__main__':
    unittest.main()
