# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.27
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.blog_category import BlogCategory


class TestBlogCategory(unittest.TestCase):
    """ BlogCategory unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBlogCategory(self):
        """
        Test BlogCategory
        """
        model = kinow_client.models.blog_category.BlogCategory()


if __name__ == '__main__':
    unittest.main()
