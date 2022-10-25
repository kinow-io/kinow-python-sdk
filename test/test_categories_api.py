# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.categories_api import CategoriesApi


class TestCategoriesApi(unittest.TestCase):
    """ CategoriesApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.categories_api.CategoriesApi()

    def tearDown(self):
        pass

    def test_attach_actor_to_category(self):
        """
        Test case for attach_actor_to_category

        
        """
        pass

    def test_attach_director_to_category(self):
        """
        Test case for attach_director_to_category

        
        """
        pass

    def test_attach_features_to_category(self):
        """
        Test case for attach_features_to_category

        
        """
        pass

    def test_create_category(self):
        """
        Test case for create_category

        
        """
        pass

    def test_delete_category(self):
        """
        Test case for delete_category

        
        """
        pass

    def test_detach_actor_from_category(self):
        """
        Test case for detach_actor_from_category

        
        """
        pass

    def test_detach_director_from_category(self):
        """
        Test case for detach_director_from_category

        
        """
        pass

    def test_get_available_category(self):
        """
        Test case for get_available_category

        
        """
        pass

    def test_get_categories(self):
        """
        Test case for get_categories

        
        """
        pass

    def test_get_categories_from_category(self):
        """
        Test case for get_categories_from_category

        
        """
        pass

    def test_get_category(self):
        """
        Test case for get_category

        
        """
        pass

    def test_get_category_actors(self):
        """
        Test case for get_category_actors

        
        """
        pass

    def test_get_category_banner(self):
        """
        Test case for get_category_banner

        
        """
        pass

    def test_get_category_directors(self):
        """
        Test case for get_category_directors

        
        """
        pass

    def test_get_category_features(self):
        """
        Test case for get_category_features

        
        """
        pass

    def test_get_category_images(self):
        """
        Test case for get_category_images

        
        """
        pass

    def test_get_category_player(self):
        """
        Test case for get_category_player

        
        """
        pass

    def test_get_category_products(self):
        """
        Test case for get_category_products

        
        """
        pass

    def test_get_category_video_subtitles(self):
        """
        Test case for get_category_video_subtitles

        
        """
        pass

    def test_get_product_categories(self):
        """
        Test case for get_product_categories

        
        """
        pass

    def test_get_subscription_categories(self):
        """
        Test case for get_subscription_categories

        
        """
        pass

    def test_get_videos_from_categories(self):
        """
        Test case for get_videos_from_categories

        
        """
        pass

    def test_get_videos_from_category(self):
        """
        Test case for get_videos_from_category

        
        """
        pass

    def test_update_category(self):
        """
        Test case for update_category

        
        """
        pass

    def test_upload_category_cover(self):
        """
        Test case for upload_category_cover

        
        """
        pass

    def test_upload_category_image(self):
        """
        Test case for upload_category_image

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
