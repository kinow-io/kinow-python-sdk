# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.56
    
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


class ConfigurationApi(object):
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

    def get_configuration(self, **kwargs):
        """
              Get configuration by name.      Available :         - PLATFORM_NAME         - ACTIVE         - LANG_DEFAULT         - CURRENCY_DEFAULT         - COUNTRY_DEFAULT         - TIMEZONE         - COPYRIGHT         - COOKIE_WARNING         - RECAPTCHA_KEY         - CUSTOMER_REGISTRATION         - CATALOG_RESTRICTED         - CATALOG_SUBSCRIPTION         - PRODUCTS_ORDER_BY         - PRODUCTS_ORDER_WAY         - PRODUCTS_RAIL_NB         - PRODUCTS_NEW_DAYS         - FORCE_TAX_ID         - CMS_CONDITIONS_ID         - GEOLOCATION_WHITELIST         - PASSWORD_MIN_LENGTH         - PASSWORD_MIN_CAPITALIZE         - PASSWORD_MIN_NUMERIC         - PASSWORD_MIN_SPECIAL      
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_configuration(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: ConfigurationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_configuration_with_http_info(**kwargs)
        else:
            (data) = self.get_configuration_with_http_info(**kwargs)
            return data

    def get_configuration_with_http_info(self, **kwargs):
        """
              Get configuration by name.      Available :         - PLATFORM_NAME         - ACTIVE         - LANG_DEFAULT         - CURRENCY_DEFAULT         - COUNTRY_DEFAULT         - TIMEZONE         - COPYRIGHT         - COOKIE_WARNING         - RECAPTCHA_KEY         - CUSTOMER_REGISTRATION         - CATALOG_RESTRICTED         - CATALOG_SUBSCRIPTION         - PRODUCTS_ORDER_BY         - PRODUCTS_ORDER_WAY         - PRODUCTS_RAIL_NB         - PRODUCTS_NEW_DAYS         - FORCE_TAX_ID         - CMS_CONDITIONS_ID         - GEOLOCATION_WHITELIST         - PASSWORD_MIN_LENGTH         - PASSWORD_MIN_CAPITALIZE         - PASSWORD_MIN_NUMERIC         - PASSWORD_MIN_SPECIAL      
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_configuration_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: ConfigurationList
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
                    " to method get_configuration" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/configuration'.replace('{format}', 'json')
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
        auth_settings = ['ApiClientId', 'ApiClientSecret']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ConfigurationList',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_configuration_analytics(self, **kwargs):
        """
        Get analytics configuration
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_configuration_analytics(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: Analytics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_configuration_analytics_with_http_info(**kwargs)
        else:
            (data) = self.get_configuration_analytics_with_http_info(**kwargs)
            return data

    def get_configuration_analytics_with_http_info(self, **kwargs):
        """
        Get analytics configuration
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_configuration_analytics_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :return: Analytics
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
                    " to method get_configuration_analytics" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/configuration/analytics'.replace('{format}', 'json')
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
        auth_settings = ['ApiClientId', 'ApiClientSecret']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Analytics',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_configuration_by_name(self, configuration_name, **kwargs):
        """
             Get configuration by name.     Available :     - LANG_DEFAULT     - CURRENCY_DEFAULT     - COUNTRY_DEFAULT     - TIMEZONE     
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_configuration_by_name(configuration_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str configuration_name: (required)
        :return: Configuration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_configuration_by_name_with_http_info(configuration_name, **kwargs)
        else:
            (data) = self.get_configuration_by_name_with_http_info(configuration_name, **kwargs)
            return data

    def get_configuration_by_name_with_http_info(self, configuration_name, **kwargs):
        """
             Get configuration by name.     Available :     - LANG_DEFAULT     - CURRENCY_DEFAULT     - COUNTRY_DEFAULT     - TIMEZONE     
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_configuration_by_name_with_http_info(configuration_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str configuration_name: (required)
        :return: Configuration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['configuration_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_configuration_by_name" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'configuration_name' is set
        if ('configuration_name' not in params) or (params['configuration_name'] is None):
            raise ValueError("Missing the required parameter `configuration_name` when calling `get_configuration_by_name`")


        collection_formats = {}

        resource_path = '/configuration/{configuration_name}'.replace('{format}', 'json')
        path_params = {}
        if 'configuration_name' in params:
            path_params['configuration_name'] = params['configuration_name']

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
                                        response_type='Configuration',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_configuration_logo(self, **kwargs):
        """
        Get logo settings
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_configuration_logo(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: LogoSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_configuration_logo_with_http_info(**kwargs)
        else:
            (data) = self.get_configuration_logo_with_http_info(**kwargs)
            return data

    def get_configuration_logo_with_http_info(self, **kwargs):
        """
        Get logo settings
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_configuration_logo_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: LogoSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_configuration_logo" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/configuration/logo'.replace('{format}', 'json')
        path_params = {}

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
                                        response_type='LogoSettings',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_configuration_social(self, **kwargs):
        """
        Get social networks settings
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_configuration_social(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: SocialSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_configuration_social_with_http_info(**kwargs)
        else:
            (data) = self.get_configuration_social_with_http_info(**kwargs)
            return data

    def get_configuration_social_with_http_info(self, **kwargs):
        """
        Get social networks settings
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_configuration_social_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: SocialSettings
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_configuration_social" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/configuration/social'.replace('{format}', 'json')
        path_params = {}

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
                                        response_type='SocialSettings',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
