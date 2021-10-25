# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.57
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PrepaymentBalance(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, amount=None, amount_formatted=None, type=None):
        """
        PrepaymentBalance - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'amount': 'float',
            'amount_formatted': 'float',
            'type': 'str'
        }

        self.attribute_map = {
            'amount': 'amount',
            'amount_formatted': 'amount_formatted',
            'type': 'type'
        }

        self._amount = amount
        self._amount_formatted = amount_formatted
        self._type = type

    @property
    def amount(self):
        """
        Gets the amount of this PrepaymentBalance.

        :return: The amount of this PrepaymentBalance.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PrepaymentBalance.

        :param amount: The amount of this PrepaymentBalance.
        :type: float
        """

        self._amount = amount

    @property
    def amount_formatted(self):
        """
        Gets the amount_formatted of this PrepaymentBalance.

        :return: The amount_formatted of this PrepaymentBalance.
        :rtype: float
        """
        return self._amount_formatted

    @amount_formatted.setter
    def amount_formatted(self, amount_formatted):
        """
        Sets the amount_formatted of this PrepaymentBalance.

        :param amount_formatted: The amount_formatted of this PrepaymentBalance.
        :type: float
        """

        self._amount_formatted = amount_formatted

    @property
    def type(self):
        """
        Gets the type of this PrepaymentBalance.

        :return: The type of this PrepaymentBalance.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PrepaymentBalance.

        :param type: The type of this PrepaymentBalance.
        :type: str
        """

        self._type = type

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
