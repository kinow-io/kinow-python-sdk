# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.54
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.category_directors_response import CategoryDirectorsResponse


class TestCategoryDirectorsResponse(unittest.TestCase):
    """ CategoryDirectorsResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCategoryDirectorsResponse(self):
        """
        Test CategoryDirectorsResponse
        """
        model = kinow_client.models.category_directors_response.CategoryDirectorsResponse()


if __name__ == '__main__':
    unittest.main()
