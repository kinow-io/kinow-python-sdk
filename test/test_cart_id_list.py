# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.22
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.cart_id_list import CartIDList


class TestCartIDList(unittest.TestCase):
    """ CartIDList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCartIDList(self):
        """
        Test CartIDList
        """
        model = kinow_client.models.cart_id_list.CartIDList()


if __name__ == '__main__':
    unittest.main()
