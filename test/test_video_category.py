# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.41
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.video_category import VideoCategory


class TestVideoCategory(unittest.TestCase):
    """ VideoCategory unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVideoCategory(self):
        """
        Test VideoCategory
        """
        model = kinow_client.models.video_category.VideoCategory()


if __name__ == '__main__':
    unittest.main()
