# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.57
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kinow_client
from kinow_client.rest import ApiException
from kinow_client.apis.actors_api import ActorsApi


class TestActorsApi(unittest.TestCase):
    """ ActorsApi unit test stubs """

    def setUp(self):
        self.api = kinow_client.apis.actors_api.ActorsApi()

    def tearDown(self):
        pass

    def test_attach_actor_to_category(self):
        """
        Test case for attach_actor_to_category

        
        """
        pass

    def test_attach_actor_to_product(self):
        """
        Test case for attach_actor_to_product

        
        """
        pass

    def test_create_actor(self):
        """
        Test case for create_actor

        
        """
        pass

    def test_delete_actor(self):
        """
        Test case for delete_actor

        
        """
        pass

    def test_detach_actor_from_category(self):
        """
        Test case for detach_actor_from_category

        
        """
        pass

    def test_get_actor(self):
        """
        Test case for get_actor

        
        """
        pass

    def test_get_actor_cover_image(self):
        """
        Test case for get_actor_cover_image

        
        """
        pass

    def test_get_actor_products(self):
        """
        Test case for get_actor_products

        
        """
        pass

    def test_get_actor_products_role(self):
        """
        Test case for get_actor_products_role

        
        """
        pass

    def test_get_actors(self):
        """
        Test case for get_actors

        
        """
        pass

    def test_get_category_actors(self):
        """
        Test case for get_category_actors

        
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

    def test_update_actor(self):
        """
        Test case for update_actor

        
        """
        pass

    def test_upload_actor_cover(self):
        """
        Test case for upload_actor_cover

        
        """
        pass


if __name__ == '__main__':
    unittest.main()
