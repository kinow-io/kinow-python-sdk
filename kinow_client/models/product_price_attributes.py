# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductPriceAttributes(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, attribute_id=None, price=None, price_without_reduction=None, reduction=None, price_formatted=None, price_without_reduction_formatted=None, reduction_formatted=None):
        """
        ProductPriceAttributes - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'attribute_id': 'float',
            'price': 'float',
            'price_without_reduction': 'float',
            'reduction': 'float',
            'price_formatted': 'str',
            'price_without_reduction_formatted': 'str',
            'reduction_formatted': 'str'
        }

        self.attribute_map = {
            'attribute_id': 'attribute_id',
            'price': 'price',
            'price_without_reduction': 'price_without_reduction',
            'reduction': 'reduction',
            'price_formatted': 'price_formatted',
            'price_without_reduction_formatted': 'price_without_reduction_formatted',
            'reduction_formatted': 'reduction_formatted'
        }

        self._attribute_id = attribute_id
        self._price = price
        self._price_without_reduction = price_without_reduction
        self._reduction = reduction
        self._price_formatted = price_formatted
        self._price_without_reduction_formatted = price_without_reduction_formatted
        self._reduction_formatted = reduction_formatted

    @property
    def attribute_id(self):
        """
        Gets the attribute_id of this ProductPriceAttributes.

        :return: The attribute_id of this ProductPriceAttributes.
        :rtype: float
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """
        Sets the attribute_id of this ProductPriceAttributes.

        :param attribute_id: The attribute_id of this ProductPriceAttributes.
        :type: float
        """

        self._attribute_id = attribute_id

    @property
    def price(self):
        """
        Gets the price of this ProductPriceAttributes.

        :return: The price of this ProductPriceAttributes.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ProductPriceAttributes.

        :param price: The price of this ProductPriceAttributes.
        :type: float
        """

        self._price = price

    @property
    def price_without_reduction(self):
        """
        Gets the price_without_reduction of this ProductPriceAttributes.

        :return: The price_without_reduction of this ProductPriceAttributes.
        :rtype: float
        """
        return self._price_without_reduction

    @price_without_reduction.setter
    def price_without_reduction(self, price_without_reduction):
        """
        Sets the price_without_reduction of this ProductPriceAttributes.

        :param price_without_reduction: The price_without_reduction of this ProductPriceAttributes.
        :type: float
        """

        self._price_without_reduction = price_without_reduction

    @property
    def reduction(self):
        """
        Gets the reduction of this ProductPriceAttributes.

        :return: The reduction of this ProductPriceAttributes.
        :rtype: float
        """
        return self._reduction

    @reduction.setter
    def reduction(self, reduction):
        """
        Sets the reduction of this ProductPriceAttributes.

        :param reduction: The reduction of this ProductPriceAttributes.
        :type: float
        """

        self._reduction = reduction

    @property
    def price_formatted(self):
        """
        Gets the price_formatted of this ProductPriceAttributes.

        :return: The price_formatted of this ProductPriceAttributes.
        :rtype: str
        """
        return self._price_formatted

    @price_formatted.setter
    def price_formatted(self, price_formatted):
        """
        Sets the price_formatted of this ProductPriceAttributes.

        :param price_formatted: The price_formatted of this ProductPriceAttributes.
        :type: str
        """

        self._price_formatted = price_formatted

    @property
    def price_without_reduction_formatted(self):
        """
        Gets the price_without_reduction_formatted of this ProductPriceAttributes.

        :return: The price_without_reduction_formatted of this ProductPriceAttributes.
        :rtype: str
        """
        return self._price_without_reduction_formatted

    @price_without_reduction_formatted.setter
    def price_without_reduction_formatted(self, price_without_reduction_formatted):
        """
        Sets the price_without_reduction_formatted of this ProductPriceAttributes.

        :param price_without_reduction_formatted: The price_without_reduction_formatted of this ProductPriceAttributes.
        :type: str
        """

        self._price_without_reduction_formatted = price_without_reduction_formatted

    @property
    def reduction_formatted(self):
        """
        Gets the reduction_formatted of this ProductPriceAttributes.

        :return: The reduction_formatted of this ProductPriceAttributes.
        :rtype: str
        """
        return self._reduction_formatted

    @reduction_formatted.setter
    def reduction_formatted(self, reduction_formatted):
        """
        Sets the reduction_formatted of this ProductPriceAttributes.

        :param reduction_formatted: The reduction_formatted of this ProductPriceAttributes.
        :type: str
        """

        self._reduction_formatted = reduction_formatted

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