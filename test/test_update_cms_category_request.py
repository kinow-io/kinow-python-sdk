# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.update_cms_category_request import UpdateCMSCategoryRequest


class TestUpdateCMSCategoryRequest(unittest.TestCase):
    """ UpdateCMSCategoryRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUpdateCMSCategoryRequest(self):
        """
        Test UpdateCMSCategoryRequest
        """
        model = kinow_client.models.update_cms_category_request.UpdateCMSCategoryRequest()


if __name__ == '__main__':
    unittest.main()
