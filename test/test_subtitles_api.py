# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.25
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.subtitles_api import SubtitlesApi


class TestSubtitlesApi(unittest.TestCase):
    """ SubtitlesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.subtitles_api.SubtitlesApi()

    def tearDown(self):
        pass

    def test_create_extract_subtitle(self):
        """
        Test case for create_extract_subtitle

        
        """
        pass

    def test_create_video_subtitle(self):
        """
        Test case for create_video_subtitle

        
        """
        pass

    def test_get_category_video_subtitles(self):
        """
        Test case for get_category_video_subtitles

        
        """
        pass

    def test_get_extract_subtitles(self):
        """
        Test case for get_extract_subtitles

        
        """
        pass

    def test_get_subtitles(self):
        """
        Test case for get_subtitles

        
        """
        pass

    def test_get_video_subtitles(self):
        """
        Test case for get_video_subtitles

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
