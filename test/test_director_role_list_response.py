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
from kinow_client.models.director_role_list_response import DirectorRoleListResponse


class TestDirectorRoleListResponse(unittest.TestCase):
    """ DirectorRoleListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDirectorRoleListResponse(self):
        """
        Test DirectorRoleListResponse
        """
        model = kinow_client.models.director_role_list_response.DirectorRoleListResponse()


if __name__ == '__main__':
    unittest.main()
