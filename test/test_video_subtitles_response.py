# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.39
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.video_subtitles_response import VideoSubtitlesResponse


class TestVideoSubtitlesResponse(unittest.TestCase):
    """ VideoSubtitlesResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVideoSubtitlesResponse(self):
        """
        Test VideoSubtitlesResponse
        """
        model = kinow_client.models.video_subtitles_response.VideoSubtitlesResponse()


if __name__ == '__main__':
    unittest.main()
