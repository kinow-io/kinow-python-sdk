# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.39
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.o_auth_api import OAuthApi


class TestOAuthApi(unittest.TestCase):
    """ OAuthApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.o_auth_api.OAuthApi()

    def tearDown(self):
        pass

    def test_get_token(self):
        """
        Test case for get_token

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
