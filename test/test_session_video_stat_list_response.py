# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.session_video_stat_list_response import SessionVideoStatListResponse


class TestSessionVideoStatListResponse(unittest.TestCase):
    """ SessionVideoStatListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSessionVideoStatListResponse(self):
        """
        Test SessionVideoStatListResponse
        """
        model = kinow_client.models.session_video_stat_list_response.SessionVideoStatListResponse()


if __name__ == '__main__':
    unittest.main()
