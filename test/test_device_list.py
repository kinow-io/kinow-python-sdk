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
from kinow_client.models.device_list import DeviceList


class TestDeviceList(unittest.TestCase):
    """ DeviceList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDeviceList(self):
        """
        Test DeviceList
        """
        model = kinow_client.models.device_list.DeviceList()


if __name__ == '__main__':
    unittest.main()
