# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.actor_list_response import ActorListResponse


class TestActorListResponse(unittest.TestCase):
    """ ActorListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testActorListResponse(self):
        """
        Test ActorListResponse
        """
        model = kinow_client.models.actor_list_response.ActorListResponse()


if __name__ == '__main__':
    unittest.main()
