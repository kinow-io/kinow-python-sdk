# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.blog_page_list_response import BlogPageListResponse


class TestBlogPageListResponse(unittest.TestCase):
    """ BlogPageListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBlogPageListResponse(self):
        """
        Test BlogPageListResponse
        """
        model = kinow_client.models.blog_page_list_response.BlogPageListResponse()


if __name__ == '__main__':
    unittest.main()
