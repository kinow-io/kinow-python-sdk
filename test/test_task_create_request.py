# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.40
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.task_create_request import TaskCreateRequest


class TestTaskCreateRequest(unittest.TestCase):
    """ TaskCreateRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTaskCreateRequest(self):
        """
        Test TaskCreateRequest
        """
        model = kinow_client.models.task_create_request.TaskCreateRequest()


if __name__ == '__main__':
    unittest.main()
