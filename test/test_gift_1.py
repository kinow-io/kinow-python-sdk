# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.38
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.gift_1 import Gift1


class TestGift1(unittest.TestCase):
    """ Gift1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGift1(self):
        """
        Test Gift1
        """
        model = kinow_client.models.gift_1.Gift1()


if __name__ == '__main__':
    unittest.main()
