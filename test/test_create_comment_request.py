# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.create_comment_request import CreateCommentRequest


class TestCreateCommentRequest(unittest.TestCase):
    """ CreateCommentRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateCommentRequest(self):
        """
        Test CreateCommentRequest
        """
        model = kinow_client.models.create_comment_request.CreateCommentRequest()


if __name__ == '__main__':
    unittest.main()
