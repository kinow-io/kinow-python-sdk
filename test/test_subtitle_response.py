# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.subtitle_response import SubtitleResponse


class TestSubtitleResponse(unittest.TestCase):
    """ SubtitleResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubtitleResponse(self):
        """
        Test SubtitleResponse
        """
        model = kinow_client.models.subtitle_response.SubtitleResponse()


if __name__ == '__main__':
    unittest.main()
