# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.update_free_gift_request import UpdateFreeGiftRequest


class TestUpdateFreeGiftRequest(unittest.TestCase):
    """ UpdateFreeGiftRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateFreeGiftRequest(self):
        """
        Test UpdateFreeGiftRequest
        """
        model = kinow_client.models.update_free_gift_request.UpdateFreeGiftRequest()


if __name__ == '__main__':
    unittest.main()
