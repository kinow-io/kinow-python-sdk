# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.customer_group_video_stats_list_response import CustomerGroupVideoStatsListResponse


class TestCustomerGroupVideoStatsListResponse(unittest.TestCase):
    """ CustomerGroupVideoStatsListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerGroupVideoStatsListResponse(self):
        """
        Test CustomerGroupVideoStatsListResponse
        """
        model = kinow_client.models.customer_group_video_stats_list_response.CustomerGroupVideoStatsListResponse()


if __name__ == '__main__':
    unittest.main()
