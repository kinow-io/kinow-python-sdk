# coding: utf-8

"""
    Kinow API

    Client API for Kinow Rest API

    OpenAPI spec version: 1.4.32
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.prepayment_recharges import PrepaymentRecharges


class TestPrepaymentRecharges(unittest.TestCase):
    """ PrepaymentRecharges unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPrepaymentRecharges(self):
        """
        Test PrepaymentRecharges
        """
        model = kinow_client.models.prepayment_recharges.PrepaymentRecharges()


if __name__ == '__main__':
    unittest.main()
