# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.country_list_response import CountryListResponse


class TestCountryListResponse(unittest.TestCase):
    """ CountryListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCountryListResponse(self):
        """
        Test CountryListResponse
        """
        model = kinow_client.models.country_list_response.CountryListResponse()


if __name__ == '__main__':
    unittest.main()
