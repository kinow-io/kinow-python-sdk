# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.subscriptions import Subscriptions


class TestSubscriptions(unittest.TestCase):
    """ Subscriptions unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubscriptions(self):
        """
        Test Subscriptions
        """
        model = kinow_client.models.subscriptions.Subscriptions()


if __name__ == '__main__':
    unittest.main()
