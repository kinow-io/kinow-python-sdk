# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.order_state_list_response import OrderStateListResponse


class TestOrderStateListResponse(unittest.TestCase):
    """ OrderStateListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrderStateListResponse(self):
        """
        Test OrderStateListResponse
        """
        model = kinow_client.models.order_state_list_response.OrderStateListResponse()


if __name__ == '__main__':
    unittest.main()
