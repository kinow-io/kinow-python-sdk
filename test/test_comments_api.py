# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.comments_api import CommentsApi


class TestCommentsApi(unittest.TestCase):
    """ CommentsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.comments_api.CommentsApi()

    def tearDown(self):
        pass

    def test_create_product_comment(self):
        """
        Test case for create_product_comment

        
        """
        pass

    def test_get_comment(self):
        """
        Test case for get_comment

        
        """
        pass

    def test_get_comments(self):
        """
        Test case for get_comments

        
        """
        pass

    def test_get_customer_comments(self):
        """
        Test case for get_customer_comments

        
        """
        pass

    def test_get_product_comments(self):
        """
        Test case for get_product_comments

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
