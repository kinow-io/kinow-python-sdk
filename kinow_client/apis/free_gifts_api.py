# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.20
    
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


class FreeGiftsApi(object):
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

    def consume_free_gift(self, free_gift_id, customer_id, **kwargs):
        """
        Consume free Gift
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consume_free_gift(free_gift_id, customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int free_gift_id: Free Gift ID to fetch (required)
        :param int customer_id: Customer ID to fetch (required)
        :param str token: Free Gift token to check (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.consume_free_gift_with_http_info(free_gift_id, customer_id, **kwargs)
        else:
            (data) = self.consume_free_gift_with_http_info(free_gift_id, customer_id, **kwargs)
            return data

    def consume_free_gift_with_http_info(self, free_gift_id, customer_id, **kwargs):
        """
        Consume free Gift
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.consume_free_gift_with_http_info(free_gift_id, customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int free_gift_id: Free Gift ID to fetch (required)
        :param int customer_id: Customer ID to fetch (required)
        :param str token: Free Gift token to check (optional)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['free_gift_id', 'customer_id', 'token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consume_free_gift" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'free_gift_id' is set
        if ('free_gift_id' not in params) or (params['free_gift_id'] is None):
            raise ValueError("Missing the required parameter `free_gift_id` when calling `consume_free_gift`")
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `consume_free_gift`")


        collection_formats = {}

        resource_path = '/free-gifts/{free_gift_id}/consume'.replace('{format}', 'json')
        path_params = {}
        if 'free_gift_id' in params:
            path_params['free_gift_id'] = params['free_gift_id']

        query_params = {}
        if 'customer_id' in params:
            query_params['customer_id'] = params['customer_id']
        if 'token' in params:
            query_params['token'] = params['token']

        header_params = {}

        form_params = []
        local_var_files = {}

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

    def create_free_gift(self, body, **kwargs):
        """
        Create free Gift
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_free_gift(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateFreeGiftRequest body: Free Gift settings (required)
        :return: FreeGift
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_free_gift_with_http_info(body, **kwargs)
        else:
            (data) = self.create_free_gift_with_http_info(body, **kwargs)
            return data

    def create_free_gift_with_http_info(self, body, **kwargs):
        """
        Create free Gift
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_free_gift_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CreateFreeGiftRequest body: Free Gift settings (required)
        :return: FreeGift
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
                    " to method create_free_gift" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_free_gift`")


        collection_formats = {}

        resource_path = '/free-gifts'.replace('{format}', 'json')
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
        auth_settings = ['ApiClientId', 'ApiClientSecret']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='FreeGift',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_free_gift(self, free_gift_id, **kwargs):
        """
        Delete free Gift
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_free_gift(free_gift_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int free_gift_id: Free Gift ID to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_free_gift_with_http_info(free_gift_id, **kwargs)
        else:
            (data) = self.delete_free_gift_with_http_info(free_gift_id, **kwargs)
            return data

    def delete_free_gift_with_http_info(self, free_gift_id, **kwargs):
        """
        Delete free Gift
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_free_gift_with_http_info(free_gift_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int free_gift_id: Free Gift ID to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['free_gift_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_free_gift" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'free_gift_id' is set
        if ('free_gift_id' not in params) or (params['free_gift_id'] is None):
            raise ValueError("Missing the required parameter `free_gift_id` when calling `delete_free_gift`")


        collection_formats = {}

        resource_path = '/free-gifts/{free_gift_id}'.replace('{format}', 'json')
        path_params = {}
        if 'free_gift_id' in params:
            path_params['free_gift_id'] = params['free_gift_id']

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

    def get_free_gift(self, free_gift_id, **kwargs):
        """
        Get free Gift
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_free_gift(free_gift_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int free_gift_id: Free Gift ID to fetch (required)
        :return: FreeGiftResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_free_gift_with_http_info(free_gift_id, **kwargs)
        else:
            (data) = self.get_free_gift_with_http_info(free_gift_id, **kwargs)
            return data

    def get_free_gift_with_http_info(self, free_gift_id, **kwargs):
        """
        Get free Gift
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_free_gift_with_http_info(free_gift_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int free_gift_id: Free Gift ID to fetch (required)
        :return: FreeGiftResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['free_gift_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_free_gift" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'free_gift_id' is set
        if ('free_gift_id' not in params) or (params['free_gift_id'] is None):
            raise ValueError("Missing the required parameter `free_gift_id` when calling `get_free_gift`")


        collection_formats = {}

        resource_path = '/free-gifts/{free_gift_id}'.replace('{format}', 'json')
        path_params = {}
        if 'free_gift_id' in params:
            path_params['free_gift_id'] = params['free_gift_id']

        query_params = {}

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
                                        response_type='FreeGiftResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_free_gift_token(self, free_gift_id, **kwargs):
        """
        Get free Gift token
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_free_gift_token(free_gift_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int free_gift_id: Free Gift ID to fetch (required)
        :return: GiftToken
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_free_gift_token_with_http_info(free_gift_id, **kwargs)
        else:
            (data) = self.get_free_gift_token_with_http_info(free_gift_id, **kwargs)
            return data

    def get_free_gift_token_with_http_info(self, free_gift_id, **kwargs):
        """
        Get free Gift token
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_free_gift_token_with_http_info(free_gift_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int free_gift_id: Free Gift ID to fetch (required)
        :return: GiftToken
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['free_gift_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_free_gift_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'free_gift_id' is set
        if ('free_gift_id' not in params) or (params['free_gift_id'] is None):
            raise ValueError("Missing the required parameter `free_gift_id` when calling `get_free_gift_token`")


        collection_formats = {}

        resource_path = '/free-gifts/{free_gift_id}/token'.replace('{format}', 'json')
        path_params = {}
        if 'free_gift_id' in params:
            path_params['free_gift_id'] = params['free_gift_id']

        query_params = {}

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
                                        response_type='GiftToken',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_free_gifts(self, **kwargs):
        """
        Get free Gifts
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_free_gifts(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int unused_only: Only unused Gifts
        :return: FreeGiftListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_free_gifts_with_http_info(**kwargs)
        else:
            (data) = self.get_free_gifts_with_http_info(**kwargs)
            return data

    def get_free_gifts_with_http_info(self, **kwargs):
        """
        Get free Gifts
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_free_gifts_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int unused_only: Only unused Gifts
        :return: FreeGiftListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['unused_only']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_free_gifts" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/free-gifts'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'unused_only' in params:
            query_params['unused_only'] = params['unused_only']

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
                                        response_type='FreeGiftListResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def send_free_gift(self, free_gift_id, **kwargs):
        """
        Send free Gift
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send_free_gift(free_gift_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int free_gift_id: Free Gift ID to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.send_free_gift_with_http_info(free_gift_id, **kwargs)
        else:
            (data) = self.send_free_gift_with_http_info(free_gift_id, **kwargs)
            return data

    def send_free_gift_with_http_info(self, free_gift_id, **kwargs):
        """
        Send free Gift
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send_free_gift_with_http_info(free_gift_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int free_gift_id: Free Gift ID to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['free_gift_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_free_gift" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'free_gift_id' is set
        if ('free_gift_id' not in params) or (params['free_gift_id'] is None):
            raise ValueError("Missing the required parameter `free_gift_id` when calling `send_free_gift`")


        collection_formats = {}

        resource_path = '/free-gifts/{free_gift_id}/send'.replace('{format}', 'json')
        path_params = {}
        if 'free_gift_id' in params:
            path_params['free_gift_id'] = params['free_gift_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiClientId', 'ApiClientSecret']

        return self.api_client.call_api(resource_path, 'POST',
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
