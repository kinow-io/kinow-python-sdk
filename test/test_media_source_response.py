# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.media_source_response import MediaSourceResponse


class TestMediaSourceResponse(unittest.TestCase):
    """ MediaSourceResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMediaSourceResponse(self):
        """
        Test MediaSourceResponse
        """
        model = kinow_client.models.media_source_response.MediaSourceResponse()


if __name__ == '__main__':
    unittest.main()
