# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.52
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.analytic import Analytic


class TestAnalytic(unittest.TestCase):
    """ Analytic unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAnalytic(self):
        """
        Test Analytic
        """
        model = kinow_client.models.analytic.Analytic()


if __name__ == '__main__':
    unittest.main()
