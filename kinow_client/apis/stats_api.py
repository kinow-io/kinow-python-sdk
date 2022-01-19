# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.1
    
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


class StatsApi(object):
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

    def get_customer_group_total_watched(self, group_id, **kwargs):
        """
        Get video statistics for a given customer group
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_group_total_watched(group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int group_id: Customer group ID to fecth (required)
        :param str date_from: Search entries from this date
        :param str date_to: Search entries to this date
        :param int page:
        :param int per_page:
        :return: CustomerGroupVideoStatsListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_group_total_watched_with_http_info(group_id, **kwargs)
        else:
            (data) = self.get_customer_group_total_watched_with_http_info(group_id, **kwargs)
            return data

    def get_customer_group_total_watched_with_http_info(self, group_id, **kwargs):
        """
        Get video statistics for a given customer group
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_group_total_watched_with_http_info(group_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int group_id: Customer group ID to fecth (required)
        :param str date_from: Search entries from this date
        :param str date_to: Search entries to this date
        :param int page:
        :param int per_page:
        :return: CustomerGroupVideoStatsListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['group_id', 'date_from', 'date_to', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_group_total_watched" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'group_id' is set
        if ('group_id' not in params) or (params['group_id'] is None):
            raise ValueError("Missing the required parameter `group_id` when calling `get_customer_group_total_watched`")


        collection_formats = {}

        resource_path = '/video-stats/customer-group'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'group_id' in params:
            query_params['group_id'] = params['group_id']
        if 'date_from' in params:
            query_params['date_from'] = params['date_from']
        if 'date_to' in params:
            query_params['date_to'] = params['date_to']
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
                                        response_type='CustomerGroupVideoStatsListResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_customer_sessions(self, **kwargs):
        """
        Get Customer video sessions statistics
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_sessions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch
        :param int group_id: Group ID to fetch
        :param int video_id: Video ID to fetch
        :param str date_from: Search entries from this date
        :param str date_to: Search entries to this date
        :param int page:
        :param int per_page:
        :return: SessionVideoStatListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_sessions_with_http_info(**kwargs)
        else:
            (data) = self.get_customer_sessions_with_http_info(**kwargs)
            return data

    def get_customer_sessions_with_http_info(self, **kwargs):
        """
        Get Customer video sessions statistics
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_sessions_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch
        :param int group_id: Group ID to fetch
        :param int video_id: Video ID to fetch
        :param str date_from: Search entries from this date
        :param str date_to: Search entries to this date
        :param int page:
        :param int per_page:
        :return: SessionVideoStatListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'group_id', 'video_id', 'date_from', 'date_to', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_sessions" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/video-stats/sessions'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'customer_id' in params:
            query_params['customer_id'] = params['customer_id']
        if 'group_id' in params:
            query_params['group_id'] = params['group_id']
        if 'video_id' in params:
            query_params['video_id'] = params['video_id']
        if 'date_from' in params:
            query_params['date_from'] = params['date_from']
        if 'date_to' in params:
            query_params['date_to'] = params['date_to']
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
                                        response_type='SessionVideoStatListResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_customer_sessions_multiple(self, customer_id, body, **kwargs):
        """
        Get Customer sessions statistics for multiple videos
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_sessions_multiple(customer_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :param VideoIDList1 body: List of Video IDs separated by comma, eg. '42,21,84' (required)
        :return: list[SessionVideoStatResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_sessions_multiple_with_http_info(customer_id, body, **kwargs)
        else:
            (data) = self.get_customer_sessions_multiple_with_http_info(customer_id, body, **kwargs)
            return data

    def get_customer_sessions_multiple_with_http_info(self, customer_id, body, **kwargs):
        """
        Get Customer sessions statistics for multiple videos
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_sessions_multiple_with_http_info(customer_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :param VideoIDList1 body: List of Video IDs separated by comma, eg. '42,21,84' (required)
        :return: list[SessionVideoStatResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_sessions_multiple" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_sessions_multiple`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `get_customer_sessions_multiple`")


        collection_formats = {}

        resource_path = '/video-stats/{customer_id}/sessions'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id' in params:
            path_params['customer_id'] = params['customer_id']

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
                                        response_type='list[SessionVideoStatResponse]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_customer_video_stats(self, customer_id, **kwargs):
        """
        Get customer video statistics
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_video_stats(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :param str date_from: Search entries from this date
        :param str date_to: Search entries to this date
        :param int page:
        :param int per_page:
        :return: CustomerVideoStatsListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_video_stats_with_http_info(customer_id, **kwargs)
        else:
            (data) = self.get_customer_video_stats_with_http_info(customer_id, **kwargs)
            return data

    def get_customer_video_stats_with_http_info(self, customer_id, **kwargs):
        """
        Get customer video statistics
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_video_stats_with_http_info(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :param str date_from: Search entries from this date
        :param str date_to: Search entries to this date
        :param int page:
        :param int per_page:
        :return: CustomerVideoStatsListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'date_from', 'date_to', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_video_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_video_stats`")


        collection_formats = {}

        resource_path = '/video-stats/customers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'customer_id' in params:
            query_params['customer_id'] = params['customer_id']
        if 'date_from' in params:
            query_params['date_from'] = params['date_from']
        if 'date_to' in params:
            query_params['date_to'] = params['date_to']
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
                                        response_type='CustomerVideoStatsListResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_video_stats(self, **kwargs):
        """
        Get video statistics
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_stats(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: Video ID to fetch
        :param str date_from: Search entries from this date
        :param str date_to: Search entries to this date
        :param int page:
        :return: VideoStatListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_video_stats_with_http_info(**kwargs)
        else:
            (data) = self.get_video_stats_with_http_info(**kwargs)
            return data

    def get_video_stats_with_http_info(self, **kwargs):
        """
        Get video statistics
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_stats_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: Video ID to fetch
        :param str date_from: Search entries from this date
        :param str date_to: Search entries to this date
        :param int page:
        :return: VideoStatListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'date_from', 'date_to', 'page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_stats" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/video-stats/videos'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'video_id' in params:
            query_params['video_id'] = params['video_id']
        if 'date_from' in params:
            query_params['date_from'] = params['date_from']
        if 'date_to' in params:
            query_params['date_to'] = params['date_to']
        if 'page' in params:
            query_params['page'] = params['page']

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
                                        response_type='VideoStatListResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
