# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.order_state_response import OrderStateResponse


class TestOrderStateResponse(unittest.TestCase):
    """ OrderStateResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrderStateResponse(self):
        """
        Test OrderStateResponse
        """
        model = kinow_client.models.order_state_response.OrderStateResponse()


if __name__ == '__main__':
    unittest.main()
