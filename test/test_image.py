# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.3.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.image import Image


class TestImage(unittest.TestCase):
    """ Image unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testImage(self):
        """
        Test Image
        """
        model = kinow_client.models.image.Image()


if __name__ == '__main__':
    unittest.main()
