# coding: utf-8

"""
    Kinow API

    Client API for Kinow Rest API

    OpenAPI spec version: 1.4.32
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.device import Device


class TestDevice(unittest.TestCase):
    """ Device unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDevice(self):
        """
        Test Device
        """
        model = kinow_client.models.device.Device()


if __name__ == '__main__':
    unittest.main()
