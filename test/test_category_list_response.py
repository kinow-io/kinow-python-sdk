# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.category_list_response import CategoryListResponse


class TestCategoryListResponse(unittest.TestCase):
    """ CategoryListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCategoryListResponse(self):
        """
        Test CategoryListResponse
        """
        model = kinow_client.models.category_list_response.CategoryListResponse()


if __name__ == '__main__':
    unittest.main()
