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
from kinow_client.models.image_response import ImageResponse


class TestImageResponse(unittest.TestCase):
    """ ImageResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testImageResponse(self):
        """
        Test ImageResponse
        """
        model = kinow_client.models.image_response.ImageResponse()


if __name__ == '__main__':
    unittest.main()
