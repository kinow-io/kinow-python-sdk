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
from kinow_client.models.video_access_info import VideoAccessInfo


class TestVideoAccessInfo(unittest.TestCase):
    """ VideoAccessInfo unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVideoAccessInfo(self):
        """
        Test VideoAccessInfo
        """
        model = kinow_client.models.video_access_info.VideoAccessInfo()


if __name__ == '__main__':
    unittest.main()
