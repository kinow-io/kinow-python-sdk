# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.38
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.models.playlists import Playlists


class TestPlaylists(unittest.TestCase):
    """ Playlists unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPlaylists(self):
        """
        Test Playlists
        """
        model = kinow_client.models.playlists.Playlists()


if __name__ == '__main__':
    unittest.main()
