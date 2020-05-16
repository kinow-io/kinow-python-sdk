# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.69
    
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


class PrepaymentsApi(object):
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

    def get_customer_prepayment_balances(self, customer_id, **kwargs):
        """
        Get PrepaymentBalances list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_prepayment_balances(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :return: list[PrepaymentBalance]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_prepayment_balances_with_http_info(customer_id, **kwargs)
        else:
            (data) = self.get_customer_prepayment_balances_with_http_info(customer_id, **kwargs)
            return data

    def get_customer_prepayment_balances_with_http_info(self, customer_id, **kwargs):
        """
        Get PrepaymentBalances list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_prepayment_balances_with_http_info(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :return: list[PrepaymentBalance]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_prepayment_balances" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_prepayment_balances`")


        collection_formats = {}

        resource_path = '/customers/{customer_id}/prepayment-balance'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id' in params:
            path_params['customer_id'] = params['customer_id']

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
                                        response_type='list[PrepaymentBalance]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_customer_prepayment_operations(self, customer_id, **kwargs):
        """
        Get PrepaymentOperations list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_prepayment_operations(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :param str type:
        :param int page:
        :param int per_page:
        :return: PrepaymentOperations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_customer_prepayment_operations_with_http_info(customer_id, **kwargs)
        else:
            (data) = self.get_customer_prepayment_operations_with_http_info(customer_id, **kwargs)
            return data

    def get_customer_prepayment_operations_with_http_info(self, customer_id, **kwargs):
        """
        Get PrepaymentOperations list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_customer_prepayment_operations_with_http_info(customer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int customer_id: Customer ID to fetch (required)
        :param str type:
        :param int page:
        :param int per_page:
        :return: PrepaymentOperations
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['customer_id', 'type', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_customer_prepayment_operations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'customer_id' is set
        if ('customer_id' not in params) or (params['customer_id'] is None):
            raise ValueError("Missing the required parameter `customer_id` when calling `get_customer_prepayment_operations`")


        collection_formats = {}

        resource_path = '/customers/{customer_id}/prepayment-operations'.replace('{format}', 'json')
        path_params = {}
        if 'customer_id' in params:
            path_params['customer_id'] = params['customer_id']

        query_params = {}
        if 'type' in params:
            query_params['type'] = params['type']
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
                                        response_type='PrepaymentOperations',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_prepayment_bonus(self, prepayment_bonus_id, **kwargs):
        """
        Get PrepaymentBonus
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_bonus(prepayment_bonus_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int prepayment_bonus_id: PrepaymentBonus ID to fetch (required)
        :return: PrepaymentBonus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_prepayment_bonus_with_http_info(prepayment_bonus_id, **kwargs)
        else:
            (data) = self.get_prepayment_bonus_with_http_info(prepayment_bonus_id, **kwargs)
            return data

    def get_prepayment_bonus_with_http_info(self, prepayment_bonus_id, **kwargs):
        """
        Get PrepaymentBonus
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_bonus_with_http_info(prepayment_bonus_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int prepayment_bonus_id: PrepaymentBonus ID to fetch (required)
        :return: PrepaymentBonus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['prepayment_bonus_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_prepayment_bonus" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'prepayment_bonus_id' is set
        if ('prepayment_bonus_id' not in params) or (params['prepayment_bonus_id'] is None):
            raise ValueError("Missing the required parameter `prepayment_bonus_id` when calling `get_prepayment_bonus`")


        collection_formats = {}

        resource_path = '/prepayment/bonus/{prepayment_bonus_id}'.replace('{format}', 'json')
        path_params = {}
        if 'prepayment_bonus_id' in params:
            path_params['prepayment_bonus_id'] = params['prepayment_bonus_id']

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
                                        response_type='PrepaymentBonus',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_prepayment_bonus_list(self, **kwargs):
        """
        Get PrepaymentBonus list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_bonus_list(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: PrepaymentBonus1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_prepayment_bonus_list_with_http_info(**kwargs)
        else:
            (data) = self.get_prepayment_bonus_list_with_http_info(**kwargs)
            return data

    def get_prepayment_bonus_list_with_http_info(self, **kwargs):
        """
        Get PrepaymentBonus list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_bonus_list_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: PrepaymentBonus1
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
                    " to method get_prepayment_bonus_list" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/prepayment/bonus'.replace('{format}', 'json')
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
                                        response_type='PrepaymentBonus1',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_prepayment_operation(self, prepayment_operation_id, **kwargs):
        """
        Get PrepaymentOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_operation(prepayment_operation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int prepayment_operation_id: PrepaymentOperation ID to fetch (required)
        :return: PrepaymentOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_prepayment_operation_with_http_info(prepayment_operation_id, **kwargs)
        else:
            (data) = self.get_prepayment_operation_with_http_info(prepayment_operation_id, **kwargs)
            return data

    def get_prepayment_operation_with_http_info(self, prepayment_operation_id, **kwargs):
        """
        Get PrepaymentOperation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_operation_with_http_info(prepayment_operation_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int prepayment_operation_id: PrepaymentOperation ID to fetch (required)
        :return: PrepaymentOperation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['prepayment_operation_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_prepayment_operation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'prepayment_operation_id' is set
        if ('prepayment_operation_id' not in params) or (params['prepayment_operation_id'] is None):
            raise ValueError("Missing the required parameter `prepayment_operation_id` when calling `get_prepayment_operation`")


        collection_formats = {}

        resource_path = '/prepayment/operations/{prepayment_operation_id}'.replace('{format}', 'json')
        path_params = {}
        if 'prepayment_operation_id' in params:
            path_params['prepayment_operation_id'] = params['prepayment_operation_id']

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
                                        response_type='PrepaymentOperation',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_prepayment_operations(self, **kwargs):
        """
        Get PrepaymentOperations list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_operations(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str type:
        :param int page:
        :param int per_page:
        :return: PrepaymentOperations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_prepayment_operations_with_http_info(**kwargs)
        else:
            (data) = self.get_prepayment_operations_with_http_info(**kwargs)
            return data

    def get_prepayment_operations_with_http_info(self, **kwargs):
        """
        Get PrepaymentOperations list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_operations_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str type:
        :param int page:
        :param int per_page:
        :return: PrepaymentOperations
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_prepayment_operations" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/prepayment/operations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'type' in params:
            query_params['type'] = params['type']
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
                                        response_type='PrepaymentOperations',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_prepayment_recharge(self, prepayment_recharge_id, **kwargs):
        """
        Get PrepaymentRecharge
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_recharge(prepayment_recharge_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int prepayment_recharge_id: PrepaymentRecharge ID to fetch (required)
        :return: PrepaymentRecharge
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_prepayment_recharge_with_http_info(prepayment_recharge_id, **kwargs)
        else:
            (data) = self.get_prepayment_recharge_with_http_info(prepayment_recharge_id, **kwargs)
            return data

    def get_prepayment_recharge_with_http_info(self, prepayment_recharge_id, **kwargs):
        """
        Get PrepaymentRecharge
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_recharge_with_http_info(prepayment_recharge_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int prepayment_recharge_id: PrepaymentRecharge ID to fetch (required)
        :return: PrepaymentRecharge
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['prepayment_recharge_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_prepayment_recharge" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'prepayment_recharge_id' is set
        if ('prepayment_recharge_id' not in params) or (params['prepayment_recharge_id'] is None):
            raise ValueError("Missing the required parameter `prepayment_recharge_id` when calling `get_prepayment_recharge`")


        collection_formats = {}

        resource_path = '/prepayment/recharges/{prepayment_recharge_id}'.replace('{format}', 'json')
        path_params = {}
        if 'prepayment_recharge_id' in params:
            path_params['prepayment_recharge_id'] = params['prepayment_recharge_id']

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
                                        response_type='PrepaymentRecharge',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_prepayment_recharges(self, **kwargs):
        """
        Get PrepaymentRecharges list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_recharges(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: PrepaymentRecharges
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_prepayment_recharges_with_http_info(**kwargs)
        else:
            (data) = self.get_prepayment_recharges_with_http_info(**kwargs)
            return data

    def get_prepayment_recharges_with_http_info(self, **kwargs):
        """
        Get PrepaymentRecharges list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_prepayment_recharges_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: PrepaymentRecharges
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
                    " to method get_prepayment_recharges" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/prepayment/recharges'.replace('{format}', 'json')
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
                                        response_type='PrepaymentRecharges',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
