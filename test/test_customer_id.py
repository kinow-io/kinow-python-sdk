# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.customer_id import CustomerId


class TestCustomerId(unittest.TestCase):
    """ CustomerId unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerId(self):
        """
        Test CustomerId
        """
        model = kinow_client.models.customer_id.CustomerId()


if __name__ == '__main__':
    unittest.main()
