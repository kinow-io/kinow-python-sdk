# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.product_images_response import ProductImagesResponse


class TestProductImagesResponse(unittest.TestCase):
    """ ProductImagesResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProductImagesResponse(self):
        """
        Test ProductImagesResponse
        """
        model = kinow_client.models.product_images_response.ProductImagesResponse()


if __name__ == '__main__':
    unittest.main()
