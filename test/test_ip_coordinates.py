# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.ip_coordinates import IPCoordinates


class TestIPCoordinates(unittest.TestCase):
    """ IPCoordinates unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIPCoordinates(self):
        """
        Test IPCoordinates
        """
        model = kinow_client.models.ip_coordinates.IPCoordinates()


if __name__ == '__main__':
    unittest.main()
