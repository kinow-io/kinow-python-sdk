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
from kinow_client.models.registration_field import RegistrationField


class TestRegistrationField(unittest.TestCase):
    """ RegistrationField unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRegistrationField(self):
        """
        Test RegistrationField
        """
        model = kinow_client.models.registration_field.RegistrationField()


if __name__ == '__main__':
    unittest.main()
