# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TaxPrice(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, amount=None, amount_formatted=None):
        """
        TaxPrice - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'amount': 'float',
            'amount_formatted': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'amount': 'amount',
            'amount_formatted': 'amount_formatted'
        }

        self._name = name
        self._amount = amount
        self._amount_formatted = amount_formatted

    @property
    def name(self):
        """
        Gets the name of this TaxPrice.

        :return: The name of this TaxPrice.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TaxPrice.

        :param name: The name of this TaxPrice.
        :type: str
        """

        self._name = name

    @property
    def amount(self):
        """
        Gets the amount of this TaxPrice.

        :return: The amount of this TaxPrice.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this TaxPrice.

        :param amount: The amount of this TaxPrice.
        :type: float
        """

        self._amount = amount

    @property
    def amount_formatted(self):
        """
        Gets the amount_formatted of this TaxPrice.

        :return: The amount_formatted of this TaxPrice.
        :rtype: str
        """
        return self._amount_formatted

    @amount_formatted.setter
    def amount_formatted(self, amount_formatted):
        """
        Sets the amount_formatted of this TaxPrice.

        :param amount_formatted: The amount_formatted of this TaxPrice.
        :type: str
        """

        self._amount_formatted = amount_formatted

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
