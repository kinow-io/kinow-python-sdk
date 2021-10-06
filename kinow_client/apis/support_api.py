# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.53
    
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


class SupportApi(object):
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

    def create_message(self, id_lang, email, id_contact, message, **kwargs):
        """
        Create new message
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_message(id_lang, email, id_contact, message, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_lang: Language ID used by user to write his message (required)
        :param str email: User email in order to send him a response (required)
        :param int id_contact: Contact ID to send the user message (required)
        :param str message: User message (required)
        :param int id_support: Link the message to a previous message
        :param int id_product: Link the message to a product in catalog
        :param int id_order: Link the message to an existing order
        :param bool send_mail: Send confirmation email to the providen email
        :return: Support
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_message_with_http_info(id_lang, email, id_contact, message, **kwargs)
        else:
            (data) = self.create_message_with_http_info(id_lang, email, id_contact, message, **kwargs)
            return data

    def create_message_with_http_info(self, id_lang, email, id_contact, message, **kwargs):
        """
        Create new message
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_message_with_http_info(id_lang, email, id_contact, message, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id_lang: Language ID used by user to write his message (required)
        :param str email: User email in order to send him a response (required)
        :param int id_contact: Contact ID to send the user message (required)
        :param str message: User message (required)
        :param int id_support: Link the message to a previous message
        :param int id_product: Link the message to a product in catalog
        :param int id_order: Link the message to an existing order
        :param bool send_mail: Send confirmation email to the providen email
        :return: Support
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id_lang', 'email', 'id_contact', 'message', 'id_support', 'id_product', 'id_order', 'send_mail']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id_lang' is set
        if ('id_lang' not in params) or (params['id_lang'] is None):
            raise ValueError("Missing the required parameter `id_lang` when calling `create_message`")
        # verify the required parameter 'email' is set
        if ('email' not in params) or (params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `create_message`")
        # verify the required parameter 'id_contact' is set
        if ('id_contact' not in params) or (params['id_contact'] is None):
            raise ValueError("Missing the required parameter `id_contact` when calling `create_message`")
        # verify the required parameter 'message' is set
        if ('message' not in params) or (params['message'] is None):
            raise ValueError("Missing the required parameter `message` when calling `create_message`")


        collection_formats = {}

        resource_path = '/support'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'id_lang' in params:
            form_params.append(('id_lang', params['id_lang']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'id_support' in params:
            form_params.append(('id_support', params['id_support']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'email' in params:
            form_params.append(('email', params['email']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'id_contact' in params:
            form_params.append(('id_contact', params['id_contact']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'message' in params:
            form_params.append(('message', params['message']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'id_product' in params:
            form_params.append(('id_product', params['id_product']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'id_order' in params:
            form_params.append(('id_order', params['id_order']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')
        if 'send_mail' in params:
            form_params.append(('send_mail', params['send_mail']))

        self.api_client.set_default_header('Content-Type', 'application/x-www-form-urlencoded')

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
                                        response_type='Support',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_contacts(self, **kwargs):
        """
        Get contacts list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_contacts(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str sort_by: Sort by this attribute (id by default)
        :param str sort_direction: Sorting direction (asc by default)
        :return: Contacts
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_contacts_with_http_info(**kwargs)
        else:
            (data) = self.get_contacts_with_http_info(**kwargs)
            return data

    def get_contacts_with_http_info(self, **kwargs):
        """
        Get contacts list
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_contacts_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int page:
        :param int per_page:
        :param str sort_by: Sort by this attribute (id by default)
        :param str sort_direction: Sorting direction (asc by default)
        :return: Contacts
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'per_page', 'sort_by', 'sort_direction']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_contacts" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/support/contacts'.replace('{format}', 'json')
        path_params = {}

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
        auth_settings = ['ApiClientId', 'ApiClientSecret']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Contacts',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
