# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.22
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.languages_api import LanguagesApi


class TestLanguagesApi(unittest.TestCase):
    """ LanguagesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.languages_api.LanguagesApi()

    def tearDown(self):
        pass

    def test_get_languages(self):
        """
        Test case for get_languages

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
