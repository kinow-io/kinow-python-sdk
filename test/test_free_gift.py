# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.free_gift import FreeGift


class TestFreeGift(unittest.TestCase):
    """ FreeGift unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testFreeGift(self):
        """
        Test FreeGift
        """
        model = kinow_client.models.free_gift.FreeGift()


if __name__ == '__main__':
    unittest.main()
