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
from kinow_client.models.customer_current_views_response import CustomerCurrentViewsResponse


class TestCustomerCurrentViewsResponse(unittest.TestCase):
    """ CustomerCurrentViewsResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerCurrentViewsResponse(self):
        """
        Test CustomerCurrentViewsResponse
        """
        model = kinow_client.models.customer_current_views_response.CustomerCurrentViewsResponse()


if __name__ == '__main__':
    unittest.main()
