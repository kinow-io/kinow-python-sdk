# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.media_source import MediaSource


class TestMediaSource(unittest.TestCase):
    """ MediaSource unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMediaSource(self):
        """
        Test MediaSource
        """
        model = kinow_client.models.media_source.MediaSource()


if __name__ == '__main__':
    unittest.main()
