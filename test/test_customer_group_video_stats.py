# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.customer_group_video_stats import CustomerGroupVideoStats


class TestCustomerGroupVideoStats(unittest.TestCase):
    """ CustomerGroupVideoStats unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerGroupVideoStats(self):
        """
        Test CustomerGroupVideoStats
        """
        model = kinow_client.models.customer_group_video_stats.CustomerGroupVideoStats()


if __name__ == '__main__':
    unittest.main()
