# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.76
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.manufacturers_api import ManufacturersApi


class TestManufacturersApi(unittest.TestCase):
    """ ManufacturersApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.manufacturers_api.ManufacturersApi()

    def tearDown(self):
        pass

    def test_get_manufacturer_cover_image(self):
        """
        Test case for get_manufacturer_cover_image

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
