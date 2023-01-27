# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.groups_api import GroupsApi


class TestGroupsApi(unittest.TestCase):
    """ GroupsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.groups_api.GroupsApi()

    def tearDown(self):
        pass

    def test_attach_customer_to_group(self):
        """
        Test case for attach_customer_to_group

        
        """
        pass

    def test_create_group(self):
        """
        Test case for create_group

        
        """
        pass

    def test_detach_customer_from_group(self):
        """
        Test case for detach_customer_from_group

        
        """
        pass

    def test_get_group(self):
        """
        Test case for get_group

        
        """
        pass

    def test_get_group_customers(self):
        """
        Test case for get_group_customers

        
        """
        pass

    def test_get_groups(self):
        """
        Test case for get_groups

        
        """
        pass

    def test_get_product_groups(self):
        """
        Test case for get_product_groups

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
