# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.7
    
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


class CMSCategoriesApi(object):
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

    def create_cms_category(self, body, **kwargs):
        """
        Create cms category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_cms_category(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CMSCategory body:  (required)
        :return: CMSCategory
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_cms_category_with_http_info(body, **kwargs)
        else:
            (data) = self.create_cms_category_with_http_info(body, **kwargs)
            return data

    def create_cms_category_with_http_info(self, body, **kwargs):
        """
        Create cms category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_cms_category_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param CMSCategory body:  (required)
        :return: CMSCategory
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
                    " to method create_cms_category" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_cms_category`")


        collection_formats = {}

        resource_path = '/cms-categories'.replace('{format}', 'json')
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
                                        response_type='CMSCategory',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_cms_categories(self, **kwargs):
        """
        Get cms categories
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_cms_categories(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str filters:   ```  name[value]=string&name[operator]=contains&date_add[value]=string&date_add[operator]=lt  _______________    {      \"name\": {          \"value\": \"string\",          \"operator\": \"contains\"      },      \"date_add\": {          \"value\": \"string\",          \"operator\": \"lt\"      }  } ```  Operator can be: strict, contains, between, in, gt (greater than), lt (lower than).
        :param str sort_by: Sort by this attribute (id by default)
        :param str sort_direction: Sorting direction (asc by default)
        :return: CMSCategoriesLists
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_cms_categories_with_http_info(**kwargs)
        else:
            (data) = self.get_cms_categories_with_http_info(**kwargs)
            return data

    def get_cms_categories_with_http_info(self, **kwargs):
        """
        Get cms categories
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_cms_categories_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str filters:   ```  name[value]=string&name[operator]=contains&date_add[value]=string&date_add[operator]=lt  _______________    {      \"name\": {          \"value\": \"string\",          \"operator\": \"contains\"      },      \"date_add\": {          \"value\": \"string\",          \"operator\": \"lt\"      }  } ```  Operator can be: strict, contains, between, in, gt (greater than), lt (lower than).
        :param str sort_by: Sort by this attribute (id by default)
        :param str sort_direction: Sorting direction (asc by default)
        :return: CMSCategoriesLists
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
                    " to method get_cms_categories" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/cms-categories'.replace('{format}', 'json')
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
                                        response_type='CMSCategoriesLists',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_cms_category(self, cms_category_id, body, **kwargs):
        """
        Update cms category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_cms_category(cms_category_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cms_category_id: CMS category ID to update (required)
        :param CMSCategory body:  (required)
        :return: CMSCategory
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_cms_category_with_http_info(cms_category_id, body, **kwargs)
        else:
            (data) = self.update_cms_category_with_http_info(cms_category_id, body, **kwargs)
            return data

    def update_cms_category_with_http_info(self, cms_category_id, body, **kwargs):
        """
        Update cms category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_cms_category_with_http_info(cms_category_id, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int cms_category_id: CMS category ID to update (required)
        :param CMSCategory body:  (required)
        :return: CMSCategory
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cms_category_id', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_cms_category" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'cms_category_id' is set
        if ('cms_category_id' not in params) or (params['cms_category_id'] is None):
            raise ValueError("Missing the required parameter `cms_category_id` when calling `update_cms_category`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_cms_category`")


        collection_formats = {}

        resource_path = '/cms-categories/{cms_category_id}'.replace('{format}', 'json')
        path_params = {}
        if 'cms_category_id' in params:
            path_params['cms_category_id'] = params['cms_category_id']

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
                                        response_type='CMSCategory',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
