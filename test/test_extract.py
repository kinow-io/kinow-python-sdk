# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.75
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.extract import Extract


class TestExtract(unittest.TestCase):
    """ Extract unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testExtract(self):
        """
        Test Extract
        """
        model = kinow_client.models.extract.Extract()


if __name__ == '__main__':
    unittest.main()
