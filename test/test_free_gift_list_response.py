# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.free_gift_list_response import FreeGiftListResponse


class TestFreeGiftListResponse(unittest.TestCase):
    """ FreeGiftListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFreeGiftListResponse(self):
        """
        Test FreeGiftListResponse
        """
        model = kinow_client.models.free_gift_list_response.FreeGiftListResponse()


if __name__ == '__main__':
    unittest.main()
