# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.27
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.video_view_informations import VideoViewInformations


class TestVideoViewInformations(unittest.TestCase):
    """ VideoViewInformations unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVideoViewInformations(self):
        """
        Test VideoViewInformations
        """
        model = kinow_client.models.video_view_informations.VideoViewInformations()


if __name__ == '__main__':
    unittest.main()
