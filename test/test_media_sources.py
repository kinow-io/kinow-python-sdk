# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.media_sources import MediaSources


class TestMediaSources(unittest.TestCase):
    """ MediaSources unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMediaSources(self):
        """
        Test MediaSources
        """
        model = kinow_client.models.media_sources.MediaSources()


if __name__ == '__main__':
    unittest.main()
