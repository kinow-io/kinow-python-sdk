# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.23
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.employees_api import EmployeesApi


class TestEmployeesApi(unittest.TestCase):
    """ EmployeesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.employees_api.EmployeesApi()

    def tearDown(self):
        pass

    def test_get_employee(self):
        """
        Test case for get_employee

        
        """
        pass

    def test_get_employees(self):
        """
        Test case for get_employees

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
