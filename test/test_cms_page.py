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
from kinow_client.models.cms_page import CMSPage


class TestCMSPage(unittest.TestCase):
    """ CMSPage unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCMSPage(self):
        """
        Test CMSPage
        """
        model = kinow_client.models.cms_page.CMSPage()


if __name__ == '__main__':
    unittest.main()
