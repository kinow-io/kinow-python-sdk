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
from kinow_client.models.create_cart_request import CreateCartRequest


class TestCreateCartRequest(unittest.TestCase):
    """ CreateCartRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateCartRequest(self):
        """
        Test CreateCartRequest
        """
        model = kinow_client.models.create_cart_request.CreateCartRequest()


if __name__ == '__main__':
    unittest.main()
