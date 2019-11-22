# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.32
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.geolocations_api import GeolocationsApi


class TestGeolocationsApi(unittest.TestCase):
    """ GeolocationsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.geolocations_api.GeolocationsApi()

    def tearDown(self):
        pass

    def test_geolocations(self):
        """
        Test case for geolocations

        
        """
        pass

    def test_get_ip_location(self):
        """
        Test case for get_ip_location

        
        """
        pass

    def test_get_product_geolocations(self):
        """
        Test case for get_product_geolocations

        
        """
        pass

    def test_get_product_geolocations_by_ip(self):
        """
        Test case for get_product_geolocations_by_ip

        
        """
        pass

    def test_get_video_geolocation_by_ip(self):
        """
        Test case for get_video_geolocation_by_ip

        
        """
        pass

    def test_set_product_geolocation(self):
        """
        Test case for set_product_geolocation

        
        """
        pass

    def test_set_video_geolocation(self):
        """
        Test case for set_video_geolocation

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
