# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.subscription import Subscription


class TestSubscription(unittest.TestCase):
    """ Subscription unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubscription(self):
        """
        Test Subscription
        """
        model = kinow_client.models.subscription.Subscription()


if __name__ == '__main__':
    unittest.main()
