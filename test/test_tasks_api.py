# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.tasks_api import TasksApi


class TestTasksApi(unittest.TestCase):
    """ TasksApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.tasks_api.TasksApi()

    def tearDown(self):
        pass

    def test_create_task(self):
        """
        Test case for create_task

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
