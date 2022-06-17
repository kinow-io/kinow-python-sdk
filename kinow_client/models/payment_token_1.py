# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PaymentToken1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, token=None, id_cart=None):
        """
        PaymentToken1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'token': 'str',
            'id_cart': 'str'
        }

        self.attribute_map = {
            'token': 'token',
            'id_cart': 'id_cart'
        }

        self._token = token
        self._id_cart = id_cart

    @property
    def token(self):
        """
        Gets the token of this PaymentToken1.

        :return: The token of this PaymentToken1.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this PaymentToken1.

        :param token: The token of this PaymentToken1.
        :type: str
        """

        self._token = token

    @property
    def id_cart(self):
        """
        Gets the id_cart of this PaymentToken1.

        :return: The id_cart of this PaymentToken1.
        :rtype: str
        """
        return self._id_cart

    @id_cart.setter
    def id_cart(self, id_cart):
        """
        Sets the id_cart of this PaymentToken1.

        :param id_cart: The id_cart of this PaymentToken1.
        :type: str
        """

        self._id_cart = id_cart

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
