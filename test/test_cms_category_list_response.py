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
from kinow_client.models.cms_category_list_response import CMSCategoryListResponse


class TestCMSCategoryListResponse(unittest.TestCase):
    """ CMSCategoryListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCMSCategoryListResponse(self):
        """
        Test CMSCategoryListResponse
        """
        model = kinow_client.models.cms_category_list_response.CMSCategoryListResponse()


if __name__ == '__main__':
    unittest.main()
