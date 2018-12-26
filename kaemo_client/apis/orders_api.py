# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.68
    
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


class OrdersApi(object):
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

    def get_customer_orders(self, customer_id, **kwargs):
        """
        Get customer orders
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_orders(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: ID of the customer to fetch (required)
        :param int page:
        :param int per_page:
        :return: Orders
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_orders_with_http_info(customer_id, **kwargs)
        else:
            (data) = self.get_customer_orders_with_http_info(customer_id, **kwargs)
            return data

    def get_customer_orders_with_http_info(self, customer_id, **kwargs):
        """
        Get customer orders
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_orders_with_http_info(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: ID of the customer to fetch (required)
        :param int page:
        :param int per_page:
        :return: Orders
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
                    " to method get_customer_orders" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_orders`")


        collection_formats = {}

        resource_path = '/customers/{customer_id}/orders'.replace('{format}', 'json')
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
                                        response_type='Orders',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_order(self, order_id, **kwargs):
        """
        Get order
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_order(order_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int order_id: ID of the order to fetch (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_order_with_http_info(order_id, **kwargs)
        else:
            (data) = self.get_order_with_http_info(order_id, **kwargs)
            return data

    def get_order_with_http_info(self, order_id, **kwargs):
        """
        Get order
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_order_with_http_info(order_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int order_id: ID of the order to fetch (required)
        :return: Order
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params) or (params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `get_order`")


        collection_formats = {}

        resource_path = '/orders/{order_id}'.replace('{format}', 'json')
        path_params = {}
        if 'order_id' in params:
            path_params['order_id'] = params['order_id']

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
                                        response_type='Order',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_order_histories(self, order_id, **kwargs):
        """
        Get order histories
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_order_histories(order_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int order_id: ID of the order to fetch (required)
        :param int page:
        :param int per_page:
        :return: OrderHistories
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_order_histories_with_http_info(order_id, **kwargs)
        else:
            (data) = self.get_order_histories_with_http_info(order_id, **kwargs)
            return data

    def get_order_histories_with_http_info(self, order_id, **kwargs):
        """
        Get order histories
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_order_histories_with_http_info(order_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int order_id: ID of the order to fetch (required)
        :param int page:
        :param int per_page:
        :return: OrderHistories
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_histories" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params) or (params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `get_order_histories`")


        collection_formats = {}

        resource_path = '/orders/{order_id}/histories'.replace('{format}', 'json')
        path_params = {}
        if 'order_id' in params:
            path_params['order_id'] = params['order_id']

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
                                        response_type='OrderHistories',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_order_invoice(self, order_id, **kwargs):
        """
        Get order invoice
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_order_invoice(order_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int order_id: ID of the order to fetch (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_order_invoice_with_http_info(order_id, **kwargs)
        else:
            (data) = self.get_order_invoice_with_http_info(order_id, **kwargs)
            return data

    def get_order_invoice_with_http_info(self, order_id, **kwargs):
        """
        Get order invoice
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_order_invoice_with_http_info(order_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int order_id: ID of the order to fetch (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['order_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_order_invoice" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'order_id' is set
        if ('order_id' not in params) or (params['order_id'] is None):
            raise ValueError("Missing the required parameter `order_id` when calling `get_order_invoice`")


        collection_formats = {}

        resource_path = '/orders/{order_id}/invoice'.replace('{format}', 'json')
        path_params = {}
        if 'order_id' in params:
            path_params['order_id'] = params['order_id']

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
                                        response_type='str',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_orders(self, **kwargs):
        """
        Get order list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_orders(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str filters:  filters[email][value]=string&filters[email][operator]=strict&filters[firstname][value]=string&filters[firstname][operator]=contains  ``` {     \"email\": {         \"value\": \"string\",         \"operator\": \"strict\"     },     \"firstname\": {         \"value\": \"string\",         \"operator\": \"contains\"     },     \"invoice_date\": {         \"value\": [\"Y-m-d\", \"Y-m-d\"],         \"operator\": \"between\"     } }``` Operator can be strict, contains, between, gt or lt.
        :param str sort_by: Sort by this attribute (id by default)
        :param str sort_direction: Sorting direction (asc by default)
        :return: Orders
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_orders_with_http_info(**kwargs)
        else:
            (data) = self.get_orders_with_http_info(**kwargs)
            return data

    def get_orders_with_http_info(self, **kwargs):
        """
        Get order list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_orders_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str filters:  filters[email][value]=string&filters[email][operator]=strict&filters[firstname][value]=string&filters[firstname][operator]=contains  ``` {     \"email\": {         \"value\": \"string\",         \"operator\": \"strict\"     },     \"firstname\": {         \"value\": \"string\",         \"operator\": \"contains\"     },     \"invoice_date\": {         \"value\": [\"Y-m-d\", \"Y-m-d\"],         \"operator\": \"between\"     } }``` Operator can be strict, contains, between, gt or lt.
        :param str sort_by: Sort by this attribute (id by default)
        :param str sort_direction: Sorting direction (asc by default)
        :return: Orders
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page', 'filters', 'sort_by', 'sort_direction']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_orders" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/orders'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']
        if 'filters' in params:
            query_params['filters'] = params['filters']
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
                                        response_type='Orders',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
