# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.media_file_response import MediaFileResponse


class TestMediaFileResponse(unittest.TestCase):
    """ MediaFileResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMediaFileResponse(self):
        """
        Test MediaFileResponse
        """
        model = kinow_client.models.media_file_response.MediaFileResponse()


if __name__ == '__main__':
    unittest.main()
