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
from kinow_client.models.group_create_request import GroupCreateRequest


class TestGroupCreateRequest(unittest.TestCase):
    """ GroupCreateRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGroupCreateRequest(self):
        """
        Test GroupCreateRequest
        """
        model = kinow_client.models.group_create_request.GroupCreateRequest()


if __name__ == '__main__':
    unittest.main()
