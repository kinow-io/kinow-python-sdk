# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.actor_product_role_list_response import ActorProductRoleListResponse


class TestActorProductRoleListResponse(unittest.TestCase):
    """ ActorProductRoleListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testActorProductRoleListResponse(self):
        """
        Test ActorProductRoleListResponse
        """
        model = kinow_client.models.actor_product_role_list_response.ActorProductRoleListResponse()


if __name__ == '__main__':
    unittest.main()
