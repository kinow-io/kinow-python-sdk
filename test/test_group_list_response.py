# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.group_list_response import GroupListResponse


class TestGroupListResponse(unittest.TestCase):
    """ GroupListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGroupListResponse(self):
        """
        Test GroupListResponse
        """
        model = kinow_client.models.group_list_response.GroupListResponse()


if __name__ == '__main__':
    unittest.main()