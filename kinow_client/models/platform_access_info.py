# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.22
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PlatformAccessInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, can_access=None, can_buy=None):
        """
        PlatformAccessInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'can_access': 'bool',
            'can_buy': 'bool'
        }

        self.attribute_map = {
            'can_access': 'can_access',
            'can_buy': 'can_buy'
        }

        self._can_access = can_access
        self._can_buy = can_buy

    @property
    def can_access(self):
        """
        Gets the can_access of this PlatformAccessInfo.

        :return: The can_access of this PlatformAccessInfo.
        :rtype: bool
        """
        return self._can_access

    @can_access.setter
    def can_access(self, can_access):
        """
        Sets the can_access of this PlatformAccessInfo.

        :param can_access: The can_access of this PlatformAccessInfo.
        :type: bool
        """

        self._can_access = can_access

    @property
    def can_buy(self):
        """
        Gets the can_buy of this PlatformAccessInfo.

        :return: The can_buy of this PlatformAccessInfo.
        :rtype: bool
        """
        return self._can_buy

    @can_buy.setter
    def can_buy(self, can_buy):
        """
        Sets the can_buy of this PlatformAccessInfo.

        :param can_buy: The can_buy of this PlatformAccessInfo.
        :type: bool
        """

        self._can_buy = can_buy

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
