# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.39
    
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
