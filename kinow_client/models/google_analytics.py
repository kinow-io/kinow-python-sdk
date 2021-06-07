# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.41
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GoogleAnalytics(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, analytics_id=None, analytics_universal=None, analytics_user_id=None):
        """
        GoogleAnalytics - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'analytics_id': 'str',
            'analytics_universal': 'bool',
            'analytics_user_id': 'bool'
        }

        self.attribute_map = {
            'analytics_id': 'analytics_id',
            'analytics_universal': 'analytics_universal',
            'analytics_user_id': 'analytics_user_id'
        }

        self._analytics_id = analytics_id
        self._analytics_universal = analytics_universal
        self._analytics_user_id = analytics_user_id

    @property
    def analytics_id(self):
        """
        Gets the analytics_id of this GoogleAnalytics.

        :return: The analytics_id of this GoogleAnalytics.
        :rtype: str
        """
        return self._analytics_id

    @analytics_id.setter
    def analytics_id(self, analytics_id):
        """
        Sets the analytics_id of this GoogleAnalytics.

        :param analytics_id: The analytics_id of this GoogleAnalytics.
        :type: str
        """

        self._analytics_id = analytics_id

    @property
    def analytics_universal(self):
        """
        Gets the analytics_universal of this GoogleAnalytics.

        :return: The analytics_universal of this GoogleAnalytics.
        :rtype: bool
        """
        return self._analytics_universal

    @analytics_universal.setter
    def analytics_universal(self, analytics_universal):
        """
        Sets the analytics_universal of this GoogleAnalytics.

        :param analytics_universal: The analytics_universal of this GoogleAnalytics.
        :type: bool
        """

        self._analytics_universal = analytics_universal

    @property
    def analytics_user_id(self):
        """
        Gets the analytics_user_id of this GoogleAnalytics.

        :return: The analytics_user_id of this GoogleAnalytics.
        :rtype: bool
        """
        return self._analytics_user_id

    @analytics_user_id.setter
    def analytics_user_id(self, analytics_user_id):
        """
        Sets the analytics_user_id of this GoogleAnalytics.

        :param analytics_user_id: The analytics_user_id of this GoogleAnalytics.
        :type: bool
        """

        self._analytics_user_id = analytics_user_id

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
