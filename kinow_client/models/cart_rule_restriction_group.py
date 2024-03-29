# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CartRuleRestrictionGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, quantity=None, items=None):
        """
        CartRuleRestrictionGroup - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'quantity': 'int',
            'items': 'list[CartRuleRestrictionGroupItem]'
        }

        self.attribute_map = {
            'quantity': 'quantity',
            'items': 'items'
        }

        self._quantity = quantity
        self._items = items

    @property
    def quantity(self):
        """
        Gets the quantity of this CartRuleRestrictionGroup.
        Cart must contain at least product(s) \"X\" matching the following restrictions:

        :return: The quantity of this CartRuleRestrictionGroup.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this CartRuleRestrictionGroup.
        Cart must contain at least product(s) \"X\" matching the following restrictions:

        :param quantity: The quantity of this CartRuleRestrictionGroup.
        :type: int
        """

        self._quantity = quantity

    @property
    def items(self):
        """
        Gets the items of this CartRuleRestrictionGroup.

        :return: The items of this CartRuleRestrictionGroup.
        :rtype: list[CartRuleRestrictionGroupItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this CartRuleRestrictionGroup.

        :param items: The items of this CartRuleRestrictionGroup.
        :type: list[CartRuleRestrictionGroupItem]
        """

        self._items = items

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
