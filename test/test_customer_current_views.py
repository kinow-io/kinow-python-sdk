# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.57
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.customer_current_views import CustomerCurrentViews


class TestCustomerCurrentViews(unittest.TestCase):
    """ CustomerCurrentViews unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerCurrentViews(self):
        """
        Test CustomerCurrentViews
        """
        model = kinow_client.models.customer_current_views.CustomerCurrentViews()


if __name__ == '__main__':
    unittest.main()
