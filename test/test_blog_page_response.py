# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.blog_page_response import BlogPageResponse


class TestBlogPageResponse(unittest.TestCase):
    """ BlogPageResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBlogPageResponse(self):
        """
        Test BlogPageResponse
        """
        model = kinow_client.models.blog_page_response.BlogPageResponse()


if __name__ == '__main__':
    unittest.main()