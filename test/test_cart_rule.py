# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.40
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.cart_rule import CartRule


class TestCartRule(unittest.TestCase):
    """ CartRule unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCartRule(self):
        """
        Test CartRule
        """
        model = kinow_client.models.cart_rule.CartRule()


if __name__ == '__main__':
    unittest.main()
