# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.gift_token import GiftToken


class TestGiftToken(unittest.TestCase):
    """ GiftToken unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGiftToken(self):
        """
        Test GiftToken
        """
        model = kinow_client.models.gift_token.GiftToken()


if __name__ == '__main__':
    unittest.main()
