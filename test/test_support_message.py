# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.support_message import SupportMessage


class TestSupportMessage(unittest.TestCase):
    """ SupportMessage unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSupportMessage(self):
        """
        Test SupportMessage
        """
        model = kinow_client.models.support_message.SupportMessage()


if __name__ == '__main__':
    unittest.main()
