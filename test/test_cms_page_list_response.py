# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.cms_page_list_response import CMSPageListResponse


class TestCMSPageListResponse(unittest.TestCase):
    """ CMSPageListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCMSPageListResponse(self):
        """
        Test CMSPageListResponse
        """
        model = kinow_client.models.cms_page_list_response.CMSPageListResponse()


if __name__ == '__main__':
    unittest.main()
