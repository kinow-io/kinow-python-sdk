# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.40
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.apis.languages_api import LanguagesApi


class TestLanguagesApi(unittest.TestCase):
    """ LanguagesApi unit test stubs """

    def setUp(self):
        self.api = kaemo_client.apis.languages_api.LanguagesApi()

    def tearDown(self):
        pass

    def test_get_languages(self):
        """
        Test case for get_languages

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
