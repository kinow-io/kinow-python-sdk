# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.48
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.apis.stats_api import StatsApi


class TestStatsApi(unittest.TestCase):
    """ StatsApi unit test stubs """

    def setUp(self):
        self.api = kaemo_client.apis.stats_api.StatsApi()

    def tearDown(self):
        pass

    def test_get_video_stats_by_customers(self):
        """
        Test case for get_video_stats_by_customers

        
        """
        pass

    def test_get_video_stats_by_video(self):
        """
        Test case for get_video_stats_by_video

        
        """
        pass

    def test_get_video_stats_sessions(self):
        """
        Test case for get_video_stats_sessions

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
