# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.page import Page


class TestPage(unittest.TestCase):
    """ Page unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPage(self):
        """
        Test Page
        """
        model = kinow_client.models.page.Page()


if __name__ == '__main__':
    unittest.main()
