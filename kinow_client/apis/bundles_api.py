# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.10
    
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


class BundlesApi(object):
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

    def add_product_to_bundle(self, bundle_id, product_id, position, **kwargs):
        """
        Add product to bundle
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_product_to_bundle(bundle_id, product_id, position, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int bundle_id: Bundle ID to fetch (required)
        :param int product_id: Product ID to add (required)
        :param int position: Product position (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_product_to_bundle_with_http_info(bundle_id, product_id, position, **kwargs)
        else:
            (data) = self.add_product_to_bundle_with_http_info(bundle_id, product_id, position, **kwargs)
            return data

    def add_product_to_bundle_with_http_info(self, bundle_id, product_id, position, **kwargs):
        """
        Add product to bundle
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_product_to_bundle_with_http_info(bundle_id, product_id, position, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int bundle_id: Bundle ID to fetch (required)
        :param int product_id: Product ID to add (required)
        :param int position: Product position (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bundle_id', 'product_id', 'position']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_product_to_bundle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bundle_id' is set
        if ('bundle_id' not in params) or (params['bundle_id'] is None):
            raise ValueError("Missing the required parameter `bundle_id` when calling `add_product_to_bundle`")
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `add_product_to_bundle`")
        # verify the required parameter 'position' is set
        if ('position' not in params) or (params['position'] is None):
            raise ValueError("Missing the required parameter `position` when calling `add_product_to_bundle`")


        collection_formats = {}

        resource_path = '/bundles/{bundle_id}'.replace('{format}', 'json')
        path_params = {}
        if 'bundle_id' in params:
            path_params['bundle_id'] = params['bundle_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'product_id' in params:
            form_params.append(('product_id', params['product_id']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'position' in params:
            form_params.append(('position', params['position']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')

        body_params = None
        # Authentication setting
        auth_settings = ['ApiClientId', 'ApiClientSecret']

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

    def get_bundle_products(self, bundle_id, **kwargs):
        """
        Get products from bundle
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_bundle_products(bundle_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int bundle_id: Bundle ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: BlogPageProductsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_bundle_products_with_http_info(bundle_id, **kwargs)
        else:
            (data) = self.get_bundle_products_with_http_info(bundle_id, **kwargs)
            return data

    def get_bundle_products_with_http_info(self, bundle_id, **kwargs):
        """
        Get products from bundle
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_bundle_products_with_http_info(bundle_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int bundle_id: Bundle ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: BlogPageProductsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bundle_id', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bundle_products" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bundle_id' is set
        if ('bundle_id' not in params) or (params['bundle_id'] is None):
            raise ValueError("Missing the required parameter `bundle_id` when calling `get_bundle_products`")


        collection_formats = {}

        resource_path = '/bundles/{bundle_id}/products'.replace('{format}', 'json')
        path_params = {}
        if 'bundle_id' in params:
            path_params['bundle_id'] = params['bundle_id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiClientId', 'ApiClientSecret']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='BlogPageProductsResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def remove_product_from_bundle(self, bundle_id, product_id, **kwargs):
        """
        Remove product from bundle
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_product_from_bundle(bundle_id, product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int bundle_id: Bundle ID to fetch (required)
        :param int product_id: Product ID to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.remove_product_from_bundle_with_http_info(bundle_id, product_id, **kwargs)
        else:
            (data) = self.remove_product_from_bundle_with_http_info(bundle_id, product_id, **kwargs)
            return data

    def remove_product_from_bundle_with_http_info(self, bundle_id, product_id, **kwargs):
        """
        Remove product from bundle
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.remove_product_from_bundle_with_http_info(bundle_id, product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int bundle_id: Bundle ID to fetch (required)
        :param int product_id: Product ID to remove (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bundle_id', 'product_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_product_from_bundle" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bundle_id' is set
        if ('bundle_id' not in params) or (params['bundle_id'] is None):
            raise ValueError("Missing the required parameter `bundle_id` when calling `remove_product_from_bundle`")
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `remove_product_from_bundle`")


        collection_formats = {}

        resource_path = '/bundles/{bundle_id}/{product_id}'.replace('{format}', 'json')
        path_params = {}
        if 'bundle_id' in params:
            path_params['bundle_id'] = params['bundle_id']
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiClientId', 'ApiClientSecret']

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
