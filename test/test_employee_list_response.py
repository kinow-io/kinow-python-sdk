# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.employee_list_response import EmployeeListResponse


class TestEmployeeListResponse(unittest.TestCase):
    """ EmployeeListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmployeeListResponse(self):
        """
        Test EmployeeListResponse
        """
        model = kinow_client.models.employee_list_response.EmployeeListResponse()


if __name__ == '__main__':
    unittest.main()
