# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.41
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.contact import Contact


class TestContact(unittest.TestCase):
    """ Contact unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContact(self):
        """
        Test Contact
        """
        model = kinow_client.models.contact.Contact()


if __name__ == '__main__':
    unittest.main()
