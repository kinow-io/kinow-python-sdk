# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.media_source_list_response import MediaSourceListResponse


class TestMediaSourceListResponse(unittest.TestCase):
    """ MediaSourceListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMediaSourceListResponse(self):
        """
        Test MediaSourceListResponse
        """
        model = kinow_client.models.media_source_list_response.MediaSourceListResponse()


if __name__ == '__main__':
    unittest.main()
