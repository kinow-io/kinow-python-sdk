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


class GeolocationsApi(object):
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

    def geolocations(self, ip_address, **kwargs):
        """
        Check access to platform by ip
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.geolocations(ip_address, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str ip_address: address ip (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.geolocations_with_http_info(ip_address, **kwargs)
        else:
            (data) = self.geolocations_with_http_info(ip_address, **kwargs)
            return data

    def geolocations_with_http_info(self, ip_address, **kwargs):
        """
        Check access to platform by ip
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.geolocations_with_http_info(ip_address, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str ip_address: address ip (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ip_address']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method geolocations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ip_address' is set
        if ('ip_address' not in params) or (params['ip_address'] is None):
            raise ValueError("Missing the required parameter `ip_address` when calling `geolocations`")


        collection_formats = {}

        resource_path = '/geolocations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'ip_address' in params:
            form_params.append(('ip_address', params['ip_address']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')

        body_params = None
        # Authentication setting
        auth_settings = []

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

    def get_product_geolocations(self, product_id, **kwargs):
        """
        Get product geolocation restrictions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_geolocations(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: Geolocs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_product_geolocations_with_http_info(product_id, **kwargs)
        else:
            (data) = self.get_product_geolocations_with_http_info(product_id, **kwargs)
            return data

    def get_product_geolocations_with_http_info(self, product_id, **kwargs):
        """
        Get product geolocation restrictions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_geolocations_with_http_info(product_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :param int page:
        :param int per_page:
        :return: Geolocs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_geolocations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_geolocations`")


        collection_formats = {}

        resource_path = '/products/{product_id}/geolocations'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

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
                                        response_type='Geolocs',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_product_geolocations_by_ip(self, product_id, ip_address, **kwargs):
        """
        Check product access using geolocation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_geolocations_by_ip(product_id, ip_address, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :param str ip_address: address ip (required)
        :param int page:
        :param int per_page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_product_geolocations_by_ip_with_http_info(product_id, ip_address, **kwargs)
        else:
            (data) = self.get_product_geolocations_by_ip_with_http_info(product_id, ip_address, **kwargs)
            return data

    def get_product_geolocations_by_ip_with_http_info(self, product_id, ip_address, **kwargs):
        """
        Check product access using geolocation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_product_geolocations_by_ip_with_http_info(product_id, ip_address, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :param str ip_address: address ip (required)
        :param int page:
        :param int per_page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'ip_address', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_product_geolocations_by_ip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `get_product_geolocations_by_ip`")
        # verify the required parameter 'ip_address' is set
        if ('ip_address' not in params) or (params['ip_address'] is None):
            raise ValueError("Missing the required parameter `ip_address` when calling `get_product_geolocations_by_ip`")


        collection_formats = {}

        resource_path = '/products/{product_id}/geolocations'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'ip_address' in params:
            form_params.append(('ip_address', params['ip_address']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')

        body_params = None
        # Authentication setting
        auth_settings = []

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

    def get_video_geolocation_by_ip(self, video_id, ip_address, **kwargs):
        """
        Check access to a product by geolocation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_geolocation_by_ip(video_id, ip_address, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: Video ID to fetch (required)
        :param str ip_address: IP address (required)
        :param int page:
        :param int per_page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_video_geolocation_by_ip_with_http_info(video_id, ip_address, **kwargs)
        else:
            (data) = self.get_video_geolocation_by_ip_with_http_info(video_id, ip_address, **kwargs)
            return data

    def get_video_geolocation_by_ip_with_http_info(self, video_id, ip_address, **kwargs):
        """
        Check access to a product by geolocation
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_video_geolocation_by_ip_with_http_info(video_id, ip_address, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: Video ID to fetch (required)
        :param str ip_address: IP address (required)
        :param int page:
        :param int per_page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'ip_address', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_video_geolocation_by_ip" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params) or (params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `get_video_geolocation_by_ip`")
        # verify the required parameter 'ip_address' is set
        if ('ip_address' not in params) or (params['ip_address'] is None):
            raise ValueError("Missing the required parameter `ip_address` when calling `get_video_geolocation_by_ip`")


        collection_formats = {}

        resource_path = '/videos/{video_id}/geolocations/{ip_address}'.replace('{format}', 'json')
        path_params = {}
        if 'video_id' in params:
            path_params['video_id'] = params['video_id']
        if 'ip_address' in params:
            path_params['ip_address'] = params['ip_address']

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

    def set_product_geolocation(self, product_id, enabled, behavior_detected_countries, behavior_non_detected_countries, **kwargs):
        """
        Handle geolocation for products by countries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_product_geolocation(product_id, enabled, behavior_detected_countries, behavior_non_detected_countries, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :param int enabled: Enabled (required)
        :param str behavior_detected_countries: Behavior for detected countries (required)
        :param str behavior_non_detected_countries: Behavior for non-detected countries (required)
        :param str countries: IDs of the non-detected countries separated by comma
        :param int page:
        :param int per_page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_product_geolocation_with_http_info(product_id, enabled, behavior_detected_countries, behavior_non_detected_countries, **kwargs)
        else:
            (data) = self.set_product_geolocation_with_http_info(product_id, enabled, behavior_detected_countries, behavior_non_detected_countries, **kwargs)
            return data

    def set_product_geolocation_with_http_info(self, product_id, enabled, behavior_detected_countries, behavior_non_detected_countries, **kwargs):
        """
        Handle geolocation for products by countries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_product_geolocation_with_http_info(product_id, enabled, behavior_detected_countries, behavior_non_detected_countries, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int product_id: Product ID to fetch (required)
        :param int enabled: Enabled (required)
        :param str behavior_detected_countries: Behavior for detected countries (required)
        :param str behavior_non_detected_countries: Behavior for non-detected countries (required)
        :param str countries: IDs of the non-detected countries separated by comma
        :param int page:
        :param int per_page:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_id', 'enabled', 'behavior_detected_countries', 'behavior_non_detected_countries', 'countries', 'page', 'per_page']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_product_geolocation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params) or (params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `set_product_geolocation`")
        # verify the required parameter 'enabled' is set
        if ('enabled' not in params) or (params['enabled'] is None):
            raise ValueError("Missing the required parameter `enabled` when calling `set_product_geolocation`")
        # verify the required parameter 'behavior_detected_countries' is set
        if ('behavior_detected_countries' not in params) or (params['behavior_detected_countries'] is None):
            raise ValueError("Missing the required parameter `behavior_detected_countries` when calling `set_product_geolocation`")
        # verify the required parameter 'behavior_non_detected_countries' is set
        if ('behavior_non_detected_countries' not in params) or (params['behavior_non_detected_countries'] is None):
            raise ValueError("Missing the required parameter `behavior_non_detected_countries` when calling `set_product_geolocation`")


        collection_formats = {}

        resource_path = '/products/{product_id}/geolocations'.replace('{format}', 'json')
        path_params = {}
        if 'product_id' in params:
            path_params['product_id'] = params['product_id']

        query_params = {}
        if 'page' in params:
            query_params['page'] = params['page']
        if 'per_page' in params:
            query_params['per_page'] = params['per_page']

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'countries' in params:
            form_params.append(('countries', params['countries']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'enabled' in params:
            form_params.append(('enabled', params['enabled']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'behavior_detected_countries' in params:
            form_params.append(('behavior_detected_countries', params['behavior_detected_countries']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'behavior_non_detected_countries' in params:
            form_params.append(('behavior_non_detected_countries', params['behavior_non_detected_countries']))

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

    def set_video_geolocation(self, video_id, enabled, behavior_detected_countries, behavior_non_detected_countries, **kwargs):
        """
        Handle geolocation for videos by countries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_video_geolocation(video_id, enabled, behavior_detected_countries, behavior_non_detected_countries, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: Video ID to fetch (required)
        :param int enabled: Enabled (required)
        :param str behavior_detected_countries: Behavior for detected countries (required)
        :param str behavior_non_detected_countries: Behavior for non-detected countries (required)
        :param str countries: IDs of the non-detected countries separated by comma
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_video_geolocation_with_http_info(video_id, enabled, behavior_detected_countries, behavior_non_detected_countries, **kwargs)
        else:
            (data) = self.set_video_geolocation_with_http_info(video_id, enabled, behavior_detected_countries, behavior_non_detected_countries, **kwargs)
            return data

    def set_video_geolocation_with_http_info(self, video_id, enabled, behavior_detected_countries, behavior_non_detected_countries, **kwargs):
        """
        Handle geolocation for videos by countries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_video_geolocation_with_http_info(video_id, enabled, behavior_detected_countries, behavior_non_detected_countries, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int video_id: Video ID to fetch (required)
        :param int enabled: Enabled (required)
        :param str behavior_detected_countries: Behavior for detected countries (required)
        :param str behavior_non_detected_countries: Behavior for non-detected countries (required)
        :param str countries: IDs of the non-detected countries separated by comma
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['video_id', 'enabled', 'behavior_detected_countries', 'behavior_non_detected_countries', 'countries']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_video_geolocation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'video_id' is set
        if ('video_id' not in params) or (params['video_id'] is None):
            raise ValueError("Missing the required parameter `video_id` when calling `set_video_geolocation`")
        # verify the required parameter 'enabled' is set
        if ('enabled' not in params) or (params['enabled'] is None):
            raise ValueError("Missing the required parameter `enabled` when calling `set_video_geolocation`")
        # verify the required parameter 'behavior_detected_countries' is set
        if ('behavior_detected_countries' not in params) or (params['behavior_detected_countries'] is None):
            raise ValueError("Missing the required parameter `behavior_detected_countries` when calling `set_video_geolocation`")
        # verify the required parameter 'behavior_non_detected_countries' is set
        if ('behavior_non_detected_countries' not in params) or (params['behavior_non_detected_countries'] is None):
            raise ValueError("Missing the required parameter `behavior_non_detected_countries` when calling `set_video_geolocation`")


        collection_formats = {}

        resource_path = '/videos/{video_id}/geolocations'.replace('{format}', 'json')
        path_params = {}
        if 'video_id' in params:
            path_params['video_id'] = params['video_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'countries' in params:
            form_params.append(('countries', params['countries']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'enabled' in params:
            form_params.append(('enabled', params['enabled']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'behavior_detected_countries' in params:
            form_params.append(('behavior_detected_countries', params['behavior_detected_countries']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'behavior_non_detected_countries' in params:
            form_params.append(('behavior_non_detected_countries', params['behavior_non_detected_countries']))

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
