# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.69
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.marlin_token import MarlinToken


class TestMarlinToken(unittest.TestCase):
    """ MarlinToken unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMarlinToken(self):
        """
        Test MarlinToken
        """
        model = kaemo_client.models.marlin_token.MarlinToken()


if __name__ == '__main__':
    unittest.main()
