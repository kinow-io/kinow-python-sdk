# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.create_cart_rule_request import CreateCartRuleRequest


class TestCreateCartRuleRequest(unittest.TestCase):
    """ CreateCartRuleRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateCartRuleRequest(self):
        """
        Test CreateCartRuleRequest
        """
        model = kinow_client.models.create_cart_rule_request.CreateCartRuleRequest()


if __name__ == '__main__':
    unittest.main()
