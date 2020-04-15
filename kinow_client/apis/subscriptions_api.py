# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.64
    
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


class SubscriptionsApi(object):
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

    def get_disabled_subscriptions(self, video_id, **kwargs):
        """
        Get disabled subscriptions list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_disabled_subscriptions(video_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: Video ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: Subscriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_disabled_subscriptions_with_http_info(video_id, **kwargs)
        else:
            (data) = self.get_disabled_subscriptions_with_http_info(video_id, **kwargs)
            return data

    def get_disabled_subscriptions_with_http_info(self, video_id, **kwargs):
        """
        Get disabled subscriptions list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_disabled_subscriptions_with_http_info(video_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: Video ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: Subscriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_disabled_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params) or (params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `get_disabled_subscriptions`")


        collection_formats = {}

        resource_path = '/videos/{video_id}/disabled-subscriptions'.replace('{format}', 'json')
        path_params = {}
        if 'video_id' in params:
            path_params['video_id'] = params['video_id']

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
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Subscriptions',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_product_subscription(self, product_id, **kwargs):
        """
        Get Subscription linked to a Product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_subscription(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_product_subscription_with_http_info(product_id, **kwargs)
        else:
            (data) = self.get_product_subscription_with_http_info(product_id, **kwargs)
            return data

    def get_product_subscription_with_http_info(self, product_id, **kwargs):
        """
        Get Subscription linked to a Product
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_subscription_with_http_info(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_subscription`")


        collection_formats = {}

        resource_path = '/products/{product_id}/subscription'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

        query_params = {}

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
                                        response_type='Subscription',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_subscription(self, subscription_id, **kwargs):
        """
        Get Subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int subscription_id: Product ID to fetch (required)
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_subscription_with_http_info(subscription_id, **kwargs)
        else:
            (data) = self.get_subscription_with_http_info(subscription_id, **kwargs)
            return data

    def get_subscription_with_http_info(self, subscription_id, **kwargs):
        """
        Get Subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription_with_http_info(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int subscription_id: Product ID to fetch (required)
        :return: Subscription
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_subscription`")


        collection_formats = {}

        resource_path = '/subscriptions/{subscription_id}'.replace('{format}', 'json')
        path_params = {}
        if 'subscription_id' in params:
            path_params['subscription_id'] = params['subscription_id']

        query_params = {}

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
                                        response_type='Subscription',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_subscription_categories(self, subscription_id, **kwargs):
        """
        Get categories list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription_categories(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int subscription_id: (required)
        :param int page:
        :param int per_page:
        :param str sort_by: Sort by this attribute (id by default)
        :param str sort_direction: Sorting direction (asc by default)
        :return: Categories
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_subscription_categories_with_http_info(subscription_id, **kwargs)
        else:
            (data) = self.get_subscription_categories_with_http_info(subscription_id, **kwargs)
            return data

    def get_subscription_categories_with_http_info(self, subscription_id, **kwargs):
        """
        Get categories list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription_categories_with_http_info(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int subscription_id: (required)
        :param int page:
        :param int per_page:
        :param str sort_by: Sort by this attribute (id by default)
        :param str sort_direction: Sorting direction (asc by default)
        :return: Categories
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'page', 'per_page', 'sort_by', 'sort_direction']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscription_categories" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_subscription_categories`")


        collection_formats = {}

        resource_path = '/subscriptions/{subscription_id}/categories'.replace('{format}', 'json')
        path_params = {}
        if 'subscription_id' in params:
            path_params['subscription_id'] = params['subscription_id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'sort_by' in params:
            query_params['sort_by'] = params['sort_by']
        if 'sort_direction' in params:
            query_params['sort_direction'] = params['sort_direction']

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
                                        response_type='Categories',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_subscription_cover_image(self, subscription_id, **kwargs):
        """
        Get cover image of a subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription_cover_image(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int subscription_id: Subscription ID to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_subscription_cover_image_with_http_info(subscription_id, **kwargs)
        else:
            (data) = self.get_subscription_cover_image_with_http_info(subscription_id, **kwargs)
            return data

    def get_subscription_cover_image_with_http_info(self, subscription_id, **kwargs):
        """
        Get cover image of a subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription_cover_image_with_http_info(subscription_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int subscription_id: Subscription ID to fetch (required)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscription_cover_image" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `get_subscription_cover_image`")


        collection_formats = {}

        resource_path = '/subscriptions/{subscription_id}/cover'.replace('{format}', 'json')
        path_params = {}
        if 'subscription_id' in params:
            path_params['subscription_id'] = params['subscription_id']

        query_params = {}

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
                                        response_type='Image',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_subscriptions(self, **kwargs):
        """
        Get Subscriptions list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscriptions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: Subscriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_subscriptions_with_http_info(**kwargs)
        else:
            (data) = self.get_subscriptions_with_http_info(**kwargs)
            return data

    def get_subscriptions_with_http_info(self, **kwargs):
        """
        Get Subscriptions list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscriptions_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: Subscriptions
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/subscriptions'.replace('{format}', 'json')
        path_params = {}

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
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Subscriptions',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def upload_subscription_cover(self, subscription_id, file, hash, **kwargs):
        """
        Upload subscription cover
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload_subscription_cover(subscription_id, file, hash, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float subscription_id: Subscription ID to fetch (required)
        :param file file: (required)
        :param str hash: (required)
        :param str hash_algorithm: Hash algorithm to check the hash file (default value is: sha256)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.upload_subscription_cover_with_http_info(subscription_id, file, hash, **kwargs)
        else:
            (data) = self.upload_subscription_cover_with_http_info(subscription_id, file, hash, **kwargs)
            return data

    def upload_subscription_cover_with_http_info(self, subscription_id, file, hash, **kwargs):
        """
        Upload subscription cover
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.upload_subscription_cover_with_http_info(subscription_id, file, hash, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param float subscription_id: Subscription ID to fetch (required)
        :param file file: (required)
        :param str hash: (required)
        :param str hash_algorithm: Hash algorithm to check the hash file (default value is: sha256)
        :return: Image
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_id', 'file', 'hash', 'hash_algorithm']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_subscription_cover" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params) or (params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `upload_subscription_cover`")
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `upload_subscription_cover`")
        # verify the required parameter 'hash' is set
        if ('hash' not in params) or (params['hash'] is None):
            raise ValueError("Missing the required parameter `hash` when calling `upload_subscription_cover`")


        collection_formats = {}

        resource_path = '/subscriptions/{subscription_id}/cover'.replace('{format}', 'json')
        path_params = {}
        if 'subscription_id' in params:
            path_params['subscription_id'] = params['subscription_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'hash' in params:
            form_params.append(('hash', params['hash']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'hash_algorithm' in params:
            form_params.append(('hash-algorithm', params['hash_algorithm']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Image',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
