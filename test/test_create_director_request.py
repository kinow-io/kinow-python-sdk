# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.create_director_request import CreateDirectorRequest


class TestCreateDirectorRequest(unittest.TestCase):
    """ CreateDirectorRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateDirectorRequest(self):
        """
        Test CreateDirectorRequest
        """
        model = kinow_client.models.create_director_request.CreateDirectorRequest()


if __name__ == '__main__':
    unittest.main()
