# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.16
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductPriceAttribute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, attribute_id=None, price=None, reduction=None, price_without_taxes=None, price_without_reduction=None, price_formatted=None, reduction_formatted=None, price_without_taxes_formatted=None, price_without_reduction_formatted=None, active=None):
        """
        ProductPriceAttribute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attribute_id': 'int',
            'price': 'float',
            'reduction': 'float',
            'price_without_taxes': 'float',
            'price_without_reduction': 'float',
            'price_formatted': 'str',
            'reduction_formatted': 'str',
            'price_without_taxes_formatted': 'str',
            'price_without_reduction_formatted': 'str',
            'active': 'bool'
        }

        self.attribute_map = {
            'attribute_id': 'attribute_id',
            'price': 'price',
            'reduction': 'reduction',
            'price_without_taxes': 'price_without_taxes',
            'price_without_reduction': 'price_without_reduction',
            'price_formatted': 'price_formatted',
            'reduction_formatted': 'reduction_formatted',
            'price_without_taxes_formatted': 'price_without_taxes_formatted',
            'price_without_reduction_formatted': 'price_without_reduction_formatted',
            'active': 'active'
        }

        self._attribute_id = attribute_id
        self._price = price
        self._reduction = reduction
        self._price_without_taxes = price_without_taxes
        self._price_without_reduction = price_without_reduction
        self._price_formatted = price_formatted
        self._reduction_formatted = reduction_formatted
        self._price_without_taxes_formatted = price_without_taxes_formatted
        self._price_without_reduction_formatted = price_without_reduction_formatted
        self._active = active

    @property
    def attribute_id(self):
        """
        Gets the attribute_id of this ProductPriceAttribute.

        :return: The attribute_id of this ProductPriceAttribute.
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """
        Sets the attribute_id of this ProductPriceAttribute.

        :param attribute_id: The attribute_id of this ProductPriceAttribute.
        :type: int
        """

        self._attribute_id = attribute_id

    @property
    def price(self):
        """
        Gets the price of this ProductPriceAttribute.

        :return: The price of this ProductPriceAttribute.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ProductPriceAttribute.

        :param price: The price of this ProductPriceAttribute.
        :type: float
        """

        self._price = price

    @property
    def reduction(self):
        """
        Gets the reduction of this ProductPriceAttribute.

        :return: The reduction of this ProductPriceAttribute.
        :rtype: float
        """
        return self._reduction

    @reduction.setter
    def reduction(self, reduction):
        """
        Sets the reduction of this ProductPriceAttribute.

        :param reduction: The reduction of this ProductPriceAttribute.
        :type: float
        """

        self._reduction = reduction

    @property
    def price_without_taxes(self):
        """
        Gets the price_without_taxes of this ProductPriceAttribute.

        :return: The price_without_taxes of this ProductPriceAttribute.
        :rtype: float
        """
        return self._price_without_taxes

    @price_without_taxes.setter
    def price_without_taxes(self, price_without_taxes):
        """
        Sets the price_without_taxes of this ProductPriceAttribute.

        :param price_without_taxes: The price_without_taxes of this ProductPriceAttribute.
        :type: float
        """

        self._price_without_taxes = price_without_taxes

    @property
    def price_without_reduction(self):
        """
        Gets the price_without_reduction of this ProductPriceAttribute.

        :return: The price_without_reduction of this ProductPriceAttribute.
        :rtype: float
        """
        return self._price_without_reduction

    @price_without_reduction.setter
    def price_without_reduction(self, price_without_reduction):
        """
        Sets the price_without_reduction of this ProductPriceAttribute.

        :param price_without_reduction: The price_without_reduction of this ProductPriceAttribute.
        :type: float
        """

        self._price_without_reduction = price_without_reduction

    @property
    def price_formatted(self):
        """
        Gets the price_formatted of this ProductPriceAttribute.

        :return: The price_formatted of this ProductPriceAttribute.
        :rtype: str
        """
        return self._price_formatted

    @price_formatted.setter
    def price_formatted(self, price_formatted):
        """
        Sets the price_formatted of this ProductPriceAttribute.

        :param price_formatted: The price_formatted of this ProductPriceAttribute.
        :type: str
        """

        self._price_formatted = price_formatted

    @property
    def reduction_formatted(self):
        """
        Gets the reduction_formatted of this ProductPriceAttribute.

        :return: The reduction_formatted of this ProductPriceAttribute.
        :rtype: str
        """
        return self._reduction_formatted

    @reduction_formatted.setter
    def reduction_formatted(self, reduction_formatted):
        """
        Sets the reduction_formatted of this ProductPriceAttribute.

        :param reduction_formatted: The reduction_formatted of this ProductPriceAttribute.
        :type: str
        """

        self._reduction_formatted = reduction_formatted

    @property
    def price_without_taxes_formatted(self):
        """
        Gets the price_without_taxes_formatted of this ProductPriceAttribute.

        :return: The price_without_taxes_formatted of this ProductPriceAttribute.
        :rtype: str
        """
        return self._price_without_taxes_formatted

    @price_without_taxes_formatted.setter
    def price_without_taxes_formatted(self, price_without_taxes_formatted):
        """
        Sets the price_without_taxes_formatted of this ProductPriceAttribute.

        :param price_without_taxes_formatted: The price_without_taxes_formatted of this ProductPriceAttribute.
        :type: str
        """

        self._price_without_taxes_formatted = price_without_taxes_formatted

    @property
    def price_without_reduction_formatted(self):
        """
        Gets the price_without_reduction_formatted of this ProductPriceAttribute.

        :return: The price_without_reduction_formatted of this ProductPriceAttribute.
        :rtype: str
        """
        return self._price_without_reduction_formatted

    @price_without_reduction_formatted.setter
    def price_without_reduction_formatted(self, price_without_reduction_formatted):
        """
        Sets the price_without_reduction_formatted of this ProductPriceAttribute.

        :param price_without_reduction_formatted: The price_without_reduction_formatted of this ProductPriceAttribute.
        :type: str
        """

        self._price_without_reduction_formatted = price_without_reduction_formatted

    @property
    def active(self):
        """
        Gets the active of this ProductPriceAttribute.

        :return: The active of this ProductPriceAttribute.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ProductPriceAttribute.

        :param active: The active of this ProductPriceAttribute.
        :type: bool
        """

        self._active = active

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
