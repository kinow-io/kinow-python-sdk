# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.67
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.apis.tasks_api import TasksApi


class TestTasksApi(unittest.TestCase):
    """ TasksApi unit test stubs """

    def setUp(self):
        self.api = kaemo_client.apis.tasks_api.TasksApi()

    def tearDown(self):
        pass

    def test_create_task(self):
        """
        Test case for create_task

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
