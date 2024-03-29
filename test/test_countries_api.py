# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.countries_api import CountriesApi


class TestCountriesApi(unittest.TestCase):
    """ CountriesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.countries_api.CountriesApi()

    def tearDown(self):
        pass

    def test_get_countries(self):
        """
        Test case for get_countries

        
        """
        pass

    def test_get_states(self):
        """
        Test case for get_states

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
