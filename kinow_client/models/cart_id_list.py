# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.40
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CartIDList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cart_ids=None, currency_id=None, iso_code=None):
        """
        CartIDList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cart_ids': 'str',
            'currency_id': 'int',
            'iso_code': 'str'
        }

        self.attribute_map = {
            'cart_ids': 'cart_ids',
            'currency_id': 'currency_id',
            'iso_code': 'iso_code'
        }

        self._cart_ids = cart_ids
        self._currency_id = currency_id
        self._iso_code = iso_code

    @property
    def cart_ids(self):
        """
        Gets the cart_ids of this CartIDList.

        :return: The cart_ids of this CartIDList.
        :rtype: str
        """
        return self._cart_ids

    @cart_ids.setter
    def cart_ids(self, cart_ids):
        """
        Sets the cart_ids of this CartIDList.

        :param cart_ids: The cart_ids of this CartIDList.
        :type: str
        """

        self._cart_ids = cart_ids

    @property
    def currency_id(self):
        """
        Gets the currency_id of this CartIDList.

        :return: The currency_id of this CartIDList.
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """
        Sets the currency_id of this CartIDList.

        :param currency_id: The currency_id of this CartIDList.
        :type: int
        """

        self._currency_id = currency_id

    @property
    def iso_code(self):
        """
        Gets the iso_code of this CartIDList.

        :return: The iso_code of this CartIDList.
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code):
        """
        Sets the iso_code of this CartIDList.

        :param iso_code: The iso_code of this CartIDList.
        :type: str
        """

        self._iso_code = iso_code

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
