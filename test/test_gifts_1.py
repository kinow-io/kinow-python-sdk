# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.35
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.gifts_1 import Gifts1


class TestGifts1(unittest.TestCase):
    """ Gifts1 unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGifts1(self):
        """
        Test Gifts1
        """
        model = kinow_client.models.gifts_1.Gifts1()


if __name__ == '__main__':
    unittest.main()
