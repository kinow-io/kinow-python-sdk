# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.83
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.category_images import CategoryImages


class TestCategoryImages(unittest.TestCase):
    """ CategoryImages unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCategoryImages(self):
        """
        Test CategoryImages
        """
        model = kinow_client.models.category_images.CategoryImages()


if __name__ == '__main__':
    unittest.main()
