# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.6
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.contacts import Contacts


class TestContacts(unittest.TestCase):
    """ Contacts unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testContacts(self):
        """
        Test Contacts
        """
        model = kinow_client.models.contacts.Contacts()


if __name__ == '__main__':
    unittest.main()
