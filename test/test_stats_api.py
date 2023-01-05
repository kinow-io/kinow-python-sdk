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
from kinow_client.apis.stats_api import StatsApi


class TestStatsApi(unittest.TestCase):
    """ StatsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.stats_api.StatsApi()

    def tearDown(self):
        pass

    def test_create_video_stat_session(self):
        """
        Test case for create_video_stat_session

        
        """
        pass

    def test_get_customer_group_total_watched(self):
        """
        Test case for get_customer_group_total_watched

        
        """
        pass

    def test_get_customer_sessions(self):
        """
        Test case for get_customer_sessions

        
        """
        pass

    def test_get_customer_sessions_multiple(self):
        """
        Test case for get_customer_sessions_multiple

        
        """
        pass

    def test_get_customer_video_stats(self):
        """
        Test case for get_customer_video_stats

        
        """
        pass

    def test_get_customer_videos_view_informations(self):
        """
        Test case for get_customer_videos_view_informations

        
        """
        pass

    def test_get_products_watched(self):
        """
        Test case for get_products_watched

        
        """
        pass

    def test_get_video_stats(self):
        """
        Test case for get_video_stats

        
        """
        pass

    def test_get_videos_watching(self):
        """
        Test case for get_videos_watching

        
        """
        pass

    def test_set_customer_video_view_informations(self):
        """
        Test case for set_customer_video_view_informations

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
