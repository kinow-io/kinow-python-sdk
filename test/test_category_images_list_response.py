# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.category_images_list_response import CategoryImagesListResponse


class TestCategoryImagesListResponse(unittest.TestCase):
    """ CategoryImagesListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCategoryImagesListResponse(self):
        """
        Test CategoryImagesListResponse
        """
        model = kinow_client.models.category_images_list_response.CategoryImagesListResponse()


if __name__ == '__main__':
    unittest.main()
