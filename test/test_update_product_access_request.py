# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.16
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.update_product_access_request import UpdateProductAccessRequest


class TestUpdateProductAccessRequest(unittest.TestCase):
    """ UpdateProductAccessRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateProductAccessRequest(self):
        """
        Test UpdateProductAccessRequest
        """
        model = kinow_client.models.update_product_access_request.UpdateProductAccessRequest()


if __name__ == '__main__':
    unittest.main()
