# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.45
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.address_1 import Address1


class TestAddress1(unittest.TestCase):
    """ Address1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAddress1(self):
        """
        Test Address1
        """
        model = kinow_client.models.address_1.Address1()


if __name__ == '__main__':
    unittest.main()