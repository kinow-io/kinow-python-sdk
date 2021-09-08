# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.50
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.products_api import ProductsApi


class TestProductsApi(unittest.TestCase):
    """ ProductsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.products_api.ProductsApi()

    def tearDown(self):
        pass

    def test_associate_products(self):
        """
        Test case for associate_products

        
        """
        pass

    def test_attach_actor_to_product(self):
        """
        Test case for attach_actor_to_product

        
        """
        pass

    def test_attach_director_to_product(self):
        """
        Test case for attach_director_to_product

        
        """
        pass

    def test_attach_features_to_product(self):
        """
        Test case for attach_features_to_product

        
        """
        pass

    def test_attach_product_to_category(self):
        """
        Test case for attach_product_to_category

        
        """
        pass

    def test_attach_product_to_group(self):
        """
        Test case for attach_product_to_group

        
        """
        pass

    def test_attach_video_to_product(self):
        """
        Test case for attach_video_to_product

        
        """
        pass

    def test_create_product(self):
        """
        Test case for create_product

        
        """
        pass

    def test_delete_product(self):
        """
        Test case for delete_product

        
        """
        pass

    def test_detach_feature_to_product(self):
        """
        Test case for detach_feature_to_product

        
        """
        pass

    def test_detach_product_from_category(self):
        """
        Test case for detach_product_from_category

        
        """
        pass

    def test_detach_product_from_group(self):
        """
        Test case for detach_product_from_group

        
        """
        pass

    def test_get_best_sales(self):
        """
        Test case for get_best_sales

        
        """
        pass

    def test_get_category_products(self):
        """
        Test case for get_category_products

        
        """
        pass

    def test_get_customer_has_access_to_product(self):
        """
        Test case for get_customer_has_access_to_product

        
        """
        pass

    def test_get_customer_has_access_to_products(self):
        """
        Test case for get_customer_has_access_to_products

        
        """
        pass

    def test_get_most_watched(self):
        """
        Test case for get_most_watched

        
        """
        pass

    def test_get_new_products(self):
        """
        Test case for get_new_products

        
        """
        pass

    def test_get_price(self):
        """
        Test case for get_price

        
        """
        pass

    def test_get_product(self):
        """
        Test case for get_product

        
        """
        pass

    def test_get_product_actors(self):
        """
        Test case for get_product_actors

        
        """
        pass

    def test_get_product_actors_role(self):
        """
        Test case for get_product_actors_role

        
        """
        pass

    def test_get_product_attributes(self):
        """
        Test case for get_product_attributes

        
        """
        pass

    def test_get_product_availability(self):
        """
        Test case for get_product_availability

        
        """
        pass

    def test_get_product_categories(self):
        """
        Test case for get_product_categories

        
        """
        pass

    def test_get_product_cover_image(self):
        """
        Test case for get_product_cover_image

        
        """
        pass

    def test_get_product_directors(self):
        """
        Test case for get_product_directors

        
        """
        pass

    def test_get_product_directors_role(self):
        """
        Test case for get_product_directors_role

        
        """
        pass

    def test_get_product_extracts(self):
        """
        Test case for get_product_extracts

        
        """
        pass

    def test_get_product_features(self):
        """
        Test case for get_product_features

        
        """
        pass

    def test_get_product_geolocations(self):
        """
        Test case for get_product_geolocations

        
        """
        pass

    def test_get_product_geolocations_by_ip(self):
        """
        Test case for get_product_geolocations_by_ip

        
        """
        pass

    def test_get_product_groups(self):
        """
        Test case for get_product_groups

        
        """
        pass

    def test_get_product_images(self):
        """
        Test case for get_product_images

        
        """
        pass

    def test_get_product_screenshots(self):
        """
        Test case for get_product_screenshots

        
        """
        pass

    def test_get_product_subscription(self):
        """
        Test case for get_product_subscription

        
        """
        pass

    def test_get_products(self):
        """
        Test case for get_products

        
        """
        pass

    def test_get_products_from_product(self):
        """
        Test case for get_products_from_product

        
        """
        pass

    def test_get_video_groups_from_product(self):
        """
        Test case for get_video_groups_from_product

        
        """
        pass

    def test_get_videos_from_product(self):
        """
        Test case for get_videos_from_product

        
        """
        pass

    def test_search_products(self):
        """
        Test case for search_products

        
        """
        pass

    def test_set_product_geolocation(self):
        """
        Test case for set_product_geolocation

        
        """
        pass

    def test_update_product(self):
        """
        Test case for update_product

        
        """
        pass

    def test_update_product_group_restriction_behavior(self):
        """
        Test case for update_product_group_restriction_behavior

        
        """
        pass

    def test_upload_product_cover(self):
        """
        Test case for upload_product_cover

        
        """
        pass

    def test_upload_product_image(self):
        """
        Test case for upload_product_image

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
