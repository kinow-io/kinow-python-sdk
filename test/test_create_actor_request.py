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
from kinow_client.models.create_actor_request import CreateActorRequest


class TestCreateActorRequest(unittest.TestCase):
    """ CreateActorRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateActorRequest(self):
        """
        Test CreateActorRequest
        """
        model = kinow_client.models.create_actor_request.CreateActorRequest()


if __name__ == '__main__':
    unittest.main()