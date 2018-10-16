# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.62
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CartBody(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_currency=None, id_lang=None, id_customer=None):
        """
        CartBody - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_currency': 'int',
            'id_lang': 'int',
            'id_customer': 'int'
        }

        self.attribute_map = {
            'id_currency': 'id_currency',
            'id_lang': 'id_lang',
            'id_customer': 'id_customer'
        }

        self._id_currency = id_currency
        self._id_lang = id_lang
        self._id_customer = id_customer

    @property
    def id_currency(self):
        """
        Gets the id_currency of this CartBody.

        :return: The id_currency of this CartBody.
        :rtype: int
        """
        return self._id_currency

    @id_currency.setter
    def id_currency(self, id_currency):
        """
        Sets the id_currency of this CartBody.

        :param id_currency: The id_currency of this CartBody.
        :type: int
        """

        self._id_currency = id_currency

    @property
    def id_lang(self):
        """
        Gets the id_lang of this CartBody.

        :return: The id_lang of this CartBody.
        :rtype: int
        """
        return self._id_lang

    @id_lang.setter
    def id_lang(self, id_lang):
        """
        Sets the id_lang of this CartBody.

        :param id_lang: The id_lang of this CartBody.
        :type: int
        """

        self._id_lang = id_lang

    @property
    def id_customer(self):
        """
        Gets the id_customer of this CartBody.

        :return: The id_customer of this CartBody.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this CartBody.

        :param id_customer: The id_customer of this CartBody.
        :type: int
        """

        self._id_customer = id_customer

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
