# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.25
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.tax_rules_api import TaxRulesApi


class TestTaxRulesApi(unittest.TestCase):
    """ TaxRulesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.tax_rules_api.TaxRulesApi()

    def tearDown(self):
        pass

    def test_get_tax_rules(self):
        """
        Test case for get_tax_rules

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
