# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.38
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.media_files import MediaFiles


class TestMediaFiles(unittest.TestCase):
    """ MediaFiles unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMediaFiles(self):
        """
        Test MediaFiles
        """
        model = kinow_client.models.media_files.MediaFiles()


if __name__ == '__main__':
    unittest.main()
