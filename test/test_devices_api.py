# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.45
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.devices_api import DevicesApi


class TestDevicesApi(unittest.TestCase):
    """ DevicesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.devices_api.DevicesApi()

    def tearDown(self):
        pass

    def test_create_devices(self):
        """
        Test case for create_devices

        
        """
        pass

    def test_delete_device(self):
        """
        Test case for delete_device

        
        """
        pass

    def test_get_customer_devices(self):
        """
        Test case for get_customer_devices

        
        """
        pass


if __name__ == '__main__':
    unittest.main()