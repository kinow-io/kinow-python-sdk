# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.71
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kaemo_client
from kaemo_client.rest import ApiException
from kaemo_client.models.feature import Feature


class TestFeature(unittest.TestCase):
    """ Feature unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFeature(self):
        """
        Test Feature
        """
        model = kaemo_client.models.feature.Feature()


if __name__ == '__main__':
    unittest.main()
