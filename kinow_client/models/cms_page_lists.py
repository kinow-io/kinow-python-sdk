# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.44
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CMSPageLists(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, pagination=None, data=None):
        """
        CMSPageLists - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'pagination': 'Pagination',
            'data': 'list[CMSPage]'
        }

        self.attribute_map = {
            'pagination': 'pagination',
            'data': 'data'
        }

        self._pagination = pagination
        self._data = data

    @property
    def pagination(self):
        """
        Gets the pagination of this CMSPageLists.

        :return: The pagination of this CMSPageLists.
        :rtype: Pagination
        """
        return self._pagination

    @pagination.setter
    def pagination(self, pagination):
        """
        Sets the pagination of this CMSPageLists.

        :param pagination: The pagination of this CMSPageLists.
        :type: Pagination
        """

        self._pagination = pagination

    @property
    def data(self):
        """
        Gets the data of this CMSPageLists.

        :return: The data of this CMSPageLists.
        :rtype: list[CMSPage]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this CMSPageLists.

        :param data: The data of this CMSPageLists.
        :type: list[CMSPage]
        """

        self._data = data

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
