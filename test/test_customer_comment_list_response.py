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
from kinow_client.models.customer_comment_list_response import CustomerCommentListResponse


class TestCustomerCommentListResponse(unittest.TestCase):
    """ CustomerCommentListResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerCommentListResponse(self):
        """
        Test CustomerCommentListResponse
        """
        model = kinow_client.models.customer_comment_list_response.CustomerCommentListResponse()


if __name__ == '__main__':
    unittest.main()
