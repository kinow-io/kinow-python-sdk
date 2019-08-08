# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DirectorsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_director(self, body, **kwargs):
        """
        Create new director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_director(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Director body: (required)
        :return: Director
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_director_with_http_info(body, **kwargs)
        else:
            (data) = self.create_director_with_http_info(body, **kwargs)
            return data

    def create_director_with_http_info(self, body, **kwargs):
        """
        Create new director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_director_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Director body: (required)
        :return: Director
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_director" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_director`")


        collection_formats = {}

        resource_path = '/directors'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        self.api_client.set_default_header('Content-Type', 'application/json')
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Director',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_director(self, director_id, **kwargs):
        """
        Delete director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_director(director_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int director_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_director_with_http_info(director_id, **kwargs)
        else:
            (data) = self.delete_director_with_http_info(director_id, **kwargs)
            return data

    def delete_director_with_http_info(self, director_id, **kwargs):
        """
        Delete director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_director_with_http_info(director_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int director_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['director_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_director" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'director_id' is set
        if ('director_id' not in params) or (params['director_id'] is None):
            raise ValueError("Missing the required parameter `director_id` when calling `delete_director`")


        collection_formats = {}

        resource_path = '/directors/{director_id}'.replace('{format}', 'json')
        path_params = {}
        if 'director_id' in params:
            path_params['director_id'] = params['director_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_director(self, director_id, **kwargs):
        """
        Get director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_director(director_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int director_id: Director ID to fetch (required)
        :param str image_type:
        :return: Director
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_director_with_http_info(director_id, **kwargs)
        else:
            (data) = self.get_director_with_http_info(director_id, **kwargs)
            return data

    def get_director_with_http_info(self, director_id, **kwargs):
        """
        Get director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_director_with_http_info(director_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int director_id: Director ID to fetch (required)
        :param str image_type:
        :return: Director
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['director_id', 'image_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_director" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'director_id' is set
        if ('director_id' not in params) or (params['director_id'] is None):
            raise ValueError("Missing the required parameter `director_id` when calling `get_director`")


        collection_formats = {}

        resource_path = '/directors/{director_id}'.replace('{format}', 'json')
        path_params = {}
        if 'director_id' in params:
            path_params['director_id'] = params['director_id']

        query_params = {}
        if 'image_type' in params:
            query_params['image_type'] = params['image_type']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Director',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_directors(self, **kwargs):
        """
        Get directors list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_directors(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str image_type:
        :return: Director1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_directors_with_http_info(**kwargs)
        else:
            (data) = self.get_directors_with_http_info(**kwargs)
            return data

    def get_directors_with_http_info(self, **kwargs):
        """
        Get directors list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_directors_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str image_type:
        :return: Director1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page', 'image_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_directors" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/directors'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'image_type' in params:
            query_params['image_type'] = params['image_type']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Director1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_product_directors(self, product_id, **kwargs):
        """
        Get directors of a product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_directors(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :param int page:
        :param int per_page:
        :param str image_type:
        :return: Director1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_product_directors_with_http_info(product_id, **kwargs)
        else:
            (data) = self.get_product_directors_with_http_info(product_id, **kwargs)
            return data

    def get_product_directors_with_http_info(self, product_id, **kwargs):
        """
        Get directors of a product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_directors_with_http_info(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :param int page:
        :param int per_page:
        :param str image_type:
        :return: Director1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'page', 'per_page', 'image_type']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_directors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_directors`")


        collection_formats = {}

        resource_path = '/products/{product_id}/directors'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'image_type' in params:
            query_params['image_type'] = params['image_type']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Director1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_director(self, director_id, body, **kwargs):
        """
        Update director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_director(director_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int director_id: (required)
        :param Director body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_director_with_http_info(director_id, body, **kwargs)
        else:
            (data) = self.update_director_with_http_info(director_id, body, **kwargs)
            return data

    def update_director_with_http_info(self, director_id, body, **kwargs):
        """
        Update director
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_director_with_http_info(director_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int director_id: (required)
        :param Director body: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['director_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_director" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'director_id' is set
        if ('director_id' not in params) or (params['director_id'] is None):
            raise ValueError("Missing the required parameter `director_id` when calling `update_director`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_director`")


        collection_formats = {}

        resource_path = '/directors/{director_id}'.replace('{format}', 'json')
        path_params = {}
        if 'director_id' in params:
            path_params['director_id'] = params['director_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        self.api_client.set_default_header('Content-Type', 'application/json')
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
