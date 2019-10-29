# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.30
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Pagination(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, total=None, current_page=None, per_page=None, last_page=None, next_page_url=None, prev_page_url=None, _from=None, to=None):
        """
        Pagination - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'total': 'int',
            'current_page': 'int',
            'per_page': 'int',
            'last_page': 'int',
            'next_page_url': 'str',
            'prev_page_url': 'str',
            '_from': 'int',
            'to': 'int'
        }

        self.attribute_map = {
            'total': 'total',
            'current_page': 'current_page',
            'per_page': 'per_page',
            'last_page': 'last_page',
            'next_page_url': 'next_page_url',
            'prev_page_url': 'prev_page_url',
            '_from': 'from',
            'to': 'to'
        }

        self._total = total
        self._current_page = current_page
        self._per_page = per_page
        self._last_page = last_page
        self._next_page_url = next_page_url
        self._prev_page_url = prev_page_url
        self.__from = _from
        self._to = to

    @property
    def total(self):
        """
        Gets the total of this Pagination.
        

        :return: The total of this Pagination.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this Pagination.
        

        :param total: The total of this Pagination.
        :type: int
        """

        self._total = total

    @property
    def current_page(self):
        """
        Gets the current_page of this Pagination.
        

        :return: The current_page of this Pagination.
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """
        Sets the current_page of this Pagination.
        

        :param current_page: The current_page of this Pagination.
        :type: int
        """

        self._current_page = current_page

    @property
    def per_page(self):
        """
        Gets the per_page of this Pagination.
        

        :return: The per_page of this Pagination.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """
        Sets the per_page of this Pagination.
        

        :param per_page: The per_page of this Pagination.
        :type: int
        """

        self._per_page = per_page

    @property
    def last_page(self):
        """
        Gets the last_page of this Pagination.
        

        :return: The last_page of this Pagination.
        :rtype: int
        """
        return self._last_page

    @last_page.setter
    def last_page(self, last_page):
        """
        Sets the last_page of this Pagination.
        

        :param last_page: The last_page of this Pagination.
        :type: int
        """

        self._last_page = last_page

    @property
    def next_page_url(self):
        """
        Gets the next_page_url of this Pagination.
        

        :return: The next_page_url of this Pagination.
        :rtype: str
        """
        return self._next_page_url

    @next_page_url.setter
    def next_page_url(self, next_page_url):
        """
        Sets the next_page_url of this Pagination.
        

        :param next_page_url: The next_page_url of this Pagination.
        :type: str
        """

        self._next_page_url = next_page_url

    @property
    def prev_page_url(self):
        """
        Gets the prev_page_url of this Pagination.
        

        :return: The prev_page_url of this Pagination.
        :rtype: str
        """
        return self._prev_page_url

    @prev_page_url.setter
    def prev_page_url(self, prev_page_url):
        """
        Sets the prev_page_url of this Pagination.
        

        :param prev_page_url: The prev_page_url of this Pagination.
        :type: str
        """

        self._prev_page_url = prev_page_url

    @property
    def _from(self):
        """
        Gets the _from of this Pagination.
        

        :return: The _from of this Pagination.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """
        Sets the _from of this Pagination.
        

        :param _from: The _from of this Pagination.
        :type: int
        """

        self.__from = _from

    @property
    def to(self):
        """
        Gets the to of this Pagination.
        

        :return: The to of this Pagination.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """
        Sets the to of this Pagination.
        

        :param to: The to of this Pagination.
        :type: int
        """

        self._to = to

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
