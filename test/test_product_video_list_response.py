# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_video_list_response import ProductVideoListResponse


class TestProductVideoListResponse(unittest.TestCase):
    """ ProductVideoListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductVideoListResponse(self):
        """
        Test ProductVideoListResponse
        """
        model = kinow_client.models.product_video_list_response.ProductVideoListResponse()


if __name__ == '__main__':
    unittest.main()
