# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.playlists_api import PlaylistsApi


class TestPlaylistsApi(unittest.TestCase):
    """ PlaylistsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.playlists_api.PlaylistsApi()

    def tearDown(self):
        pass

    def test_attach_bookmark_to_playlist(self):
        """
        Test case for attach_bookmark_to_playlist

        
        """
        pass

    def test_create_playlist(self):
        """
        Test case for create_playlist

        
        """
        pass

    def test_delete_playlist(self):
        """
        Test case for delete_playlist

        
        """
        pass

    def test_detach_bookmark_from_playlist(self):
        """
        Test case for detach_bookmark_from_playlist

        
        """
        pass

    def test_get_customer_playlists(self):
        """
        Test case for get_customer_playlists

        
        """
        pass

    def test_get_playlist(self):
        """
        Test case for get_playlist

        
        """
        pass

    def test_get_playlist_bookmarks(self):
        """
        Test case for get_playlist_bookmarks

        
        """
        pass

    def test_get_playlists(self):
        """
        Test case for get_playlists

        
        """
        pass

    def test_update_playlist(self):
        """
        Test case for update_playlist

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
