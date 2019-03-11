# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.75
    
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


class ProductAccessesApi(object):
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

    def create_product_access(self, body, **kwargs):
        """
        Create new product access
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_product_access(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ProductAccess body:  (required)
        :return: ProductAccess
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_product_access_with_http_info(body, **kwargs)
        else:
            (data) = self.create_product_access_with_http_info(body, **kwargs)
            return data

    def create_product_access_with_http_info(self, body, **kwargs):
        """
        Create new product access
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_product_access_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ProductAccess body:  (required)
        :return: ProductAccess
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
                    " to method create_product_access" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_product_access`")


        collection_formats = {}

        resource_path = '/product-accesses'.replace('{format}', 'json')
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
                                        response_type='ProductAccess',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_product_access(self, product_access_id, **kwargs):
        """
        Delete product access
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_product_access(product_access_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_access_id: ID of the product access to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_product_access_with_http_info(product_access_id, **kwargs)
        else:
            (data) = self.delete_product_access_with_http_info(product_access_id, **kwargs)
            return data

    def delete_product_access_with_http_info(self, product_access_id, **kwargs):
        """
        Delete product access
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_product_access_with_http_info(product_access_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_access_id: ID of the product access to fetch (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_access_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_product_access" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_access_id' is set
        if ('product_access_id' not in params) or (params['product_access_id'] is None):
            raise ValueError("Missing the required parameter `product_access_id` when calling `delete_product_access`")


        collection_formats = {}

        resource_path = '/product-accesses/{product_access_id}'.replace('{format}', 'json')
        path_params = {}
        if 'product_access_id' in params:
            path_params['product_access_id'] = params['product_access_id']

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

    def get_customer_accesses_subscriptions(self, customer_id, **kwargs):
        """
        Get customer accesses for subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_accesses_subscriptions(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: ID of the customer to fetch (required)
        :param int page:
        :param int per_page:
        :param str filters:      ```     filters[type][value]=string&filters[type][operator]=strict&filters[cancel][value]=string&filters[cancel][operator]=contains     _______________      {     \"type\": {     \"value\": \"string\",     \"operator\": \"strict\"     },     \"cancel\": {     \"value\": \"string\",     \"operator\": \"contains\"     }     } ```Operator can be strict, contains, gt or lt.
        :return: SubscriptionAccesses
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_accesses_subscriptions_with_http_info(customer_id, **kwargs)
        else:
            (data) = self.get_customer_accesses_subscriptions_with_http_info(customer_id, **kwargs)
            return data

    def get_customer_accesses_subscriptions_with_http_info(self, customer_id, **kwargs):
        """
        Get customer accesses for subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_accesses_subscriptions_with_http_info(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: ID of the customer to fetch (required)
        :param int page:
        :param int per_page:
        :param str filters:      ```     filters[type][value]=string&filters[type][operator]=strict&filters[cancel][value]=string&filters[cancel][operator]=contains     _______________      {     \"type\": {     \"value\": \"string\",     \"operator\": \"strict\"     },     \"cancel\": {     \"value\": \"string\",     \"operator\": \"contains\"     }     } ```Operator can be strict, contains, gt or lt.
        :return: SubscriptionAccesses
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'page', 'per_page', 'filters']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_accesses_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_accesses_subscriptions`")


        collection_formats = {}

        resource_path = '/customers/{customer_id}/accesses/subscriptions'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id' in params:
            path_params['customer_id'] = params['customer_id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'filters' in params:
            query_params['filters'] = params['filters']

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
                                        response_type='SubscriptionAccesses',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_customer_accesses_videos(self, customer_id, **kwargs):
        """
        Get customer access for videos
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_accesses_videos(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: ID of the customer to fetch (required)
        :param int page:
        :param int per_page:
        :return: SubscriptionAccesses
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_accesses_videos_with_http_info(customer_id, **kwargs)
        else:
            (data) = self.get_customer_accesses_videos_with_http_info(customer_id, **kwargs)
            return data

    def get_customer_accesses_videos_with_http_info(self, customer_id, **kwargs):
        """
        Get customer access for videos
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_accesses_videos_with_http_info(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: ID of the customer to fetch (required)
        :param int page:
        :param int per_page:
        :return: SubscriptionAccesses
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_accesses_videos" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_accesses_videos`")


        collection_formats = {}

        resource_path = '/customers/{customer_id}/accesses/videos'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id' in params:
            path_params['customer_id'] = params['customer_id']

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
                                        response_type='SubscriptionAccesses',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_product_access(self, product_access_id, **kwargs):
        """
        Get product access
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_access(product_access_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_access_id: ID of the product access to fetch (required)
        :return: ProductAccess
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_product_access_with_http_info(product_access_id, **kwargs)
        else:
            (data) = self.get_product_access_with_http_info(product_access_id, **kwargs)
            return data

    def get_product_access_with_http_info(self, product_access_id, **kwargs):
        """
        Get product access
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_access_with_http_info(product_access_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_access_id: ID of the product access to fetch (required)
        :return: ProductAccess
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_access_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_access" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_access_id' is set
        if ('product_access_id' not in params) or (params['product_access_id'] is None):
            raise ValueError("Missing the required parameter `product_access_id` when calling `get_product_access`")


        collection_formats = {}

        resource_path = '/product-accesses/{product_access_id}'.replace('{format}', 'json')
        path_params = {}
        if 'product_access_id' in params:
            path_params['product_access_id'] = params['product_access_id']

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
                                        response_type='ProductAccess',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_product_accesses(self, **kwargs):
        """
        Get product accesses list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_accesses(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str type: Filter by access type, available values are: video, sub
        :param str date_add: Filter by creation date
        :param str date_add_direction: Choose the direction for date_add parameter, default value is after ,available values are: before, equal, after
        :param str date_exp: Filter by expiration date
        :param str date_exp_direction: Choose the direction for date_exp parameter, default value is after ,available values are: before, equal, after
        :return: SubscriptionAccesses
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_product_accesses_with_http_info(**kwargs)
        else:
            (data) = self.get_product_accesses_with_http_info(**kwargs)
            return data

    def get_product_accesses_with_http_info(self, **kwargs):
        """
        Get product accesses list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_accesses_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str type: Filter by access type, available values are: video, sub
        :param str date_add: Filter by creation date
        :param str date_add_direction: Choose the direction for date_add parameter, default value is after ,available values are: before, equal, after
        :param str date_exp: Filter by expiration date
        :param str date_exp_direction: Choose the direction for date_exp parameter, default value is after ,available values are: before, equal, after
        :return: SubscriptionAccesses
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page', 'type', 'date_add', 'date_add_direction', 'date_exp', 'date_exp_direction']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_accesses" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/product-accesses'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'type' in params:
            query_params['type'] = params['type']
        if 'date_add' in params:
            query_params['date_add'] = params['date_add']
        if 'date_add_direction' in params:
            query_params['date_add_direction'] = params['date_add_direction']
        if 'date_exp' in params:
            query_params['date_exp'] = params['date_exp']
        if 'date_exp_direction' in params:
            query_params['date_exp_direction'] = params['date_exp_direction']

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
                                        response_type='SubscriptionAccesses',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def stop_subscription(self, customer_id, product_access_id, **kwargs):
        """
        unsubcribe a user from a access
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.stop_subscription(customer_id, product_access_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: ID of the user to unsubscribe (required)
        :param str product_access_id: ID of the product access to unsubscribe from (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.stop_subscription_with_http_info(customer_id, product_access_id, **kwargs)
        else:
            (data) = self.stop_subscription_with_http_info(customer_id, product_access_id, **kwargs)
            return data

    def stop_subscription_with_http_info(self, customer_id, product_access_id, **kwargs):
        """
        unsubcribe a user from a access
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.stop_subscription_with_http_info(customer_id, product_access_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: ID of the user to unsubscribe (required)
        :param str product_access_id: ID of the product access to unsubscribe from (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'product_access_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stop_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `stop_subscription`")
        # verify the required parameter 'product_access_id' is set
        if ('product_access_id' not in params) or (params['product_access_id'] is None):
            raise ValueError("Missing the required parameter `product_access_id` when calling `stop_subscription`")


        collection_formats = {}

        resource_path = '/customers/{customer_id}/unsubscribe'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id' in params:
            path_params['customer_id'] = params['customer_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'product_access_id' in params:
            form_params.append(('product_access_id', params['product_access_id']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')

        body_params = None
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

    def update_product_access(self, product_access_id, body, **kwargs):
        """
        Update product access
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_product_access(product_access_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_access_id: ID of the product access to update (required)
        :param ProductAccess body:  (required)
        :return: ProductAccess
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_product_access_with_http_info(product_access_id, body, **kwargs)
        else:
            (data) = self.update_product_access_with_http_info(product_access_id, body, **kwargs)
            return data

    def update_product_access_with_http_info(self, product_access_id, body, **kwargs):
        """
        Update product access
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_product_access_with_http_info(product_access_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_access_id: ID of the product access to update (required)
        :param ProductAccess body:  (required)
        :return: ProductAccess
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_access_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_product_access" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_access_id' is set
        if ('product_access_id' not in params) or (params['product_access_id'] is None):
            raise ValueError("Missing the required parameter `product_access_id` when calling `update_product_access`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_product_access`")


        collection_formats = {}

        resource_path = '/product-accesses/{product_access_id}'.replace('{format}', 'json')
        path_params = {}
        if 'product_access_id' in params:
            path_params['product_access_id'] = params['product_access_id']

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
                                        response_type='ProductAccess',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
