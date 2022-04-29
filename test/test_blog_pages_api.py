# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.blog_pages_api import BlogPagesApi


class TestBlogPagesApi(unittest.TestCase):
    """ BlogPagesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.blog_pages_api.BlogPagesApi()

    def tearDown(self):
        pass

    def test_attach_product_to_blog_page(self):
        """
        Test case for attach_product_to_blog_page

        
        """
        pass

    def test_detach_product_from_blog_page(self):
        """
        Test case for detach_product_from_blog_page

        
        """
        pass

    def test_get_blog_page(self):
        """
        Test case for get_blog_page

        
        """
        pass

    def test_get_blog_page_products(self):
        """
        Test case for get_blog_page_products

        
        """
        pass

    def test_get_blog_pages(self):
        """
        Test case for get_blog_pages

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
