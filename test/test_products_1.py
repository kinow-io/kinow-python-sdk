# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.69
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.products_1 import Products1


class TestProducts1(unittest.TestCase):
    """ Products1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProducts1(self):
        """
        Test Products1
        """
        model = kinow_client.models.products_1.Products1()


if __name__ == '__main__':
    unittest.main()
