# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.45
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductAttributeCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product_id=None, type=None, quality=None, price=None):
        """
        ProductAttributeCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'product_id': 'int',
            'type': 'str',
            'quality': 'str',
            'price': 'float'
        }

        self.attribute_map = {
            'product_id': 'product_id',
            'type': 'type',
            'quality': 'quality',
            'price': 'price'
        }

        self._product_id = product_id
        self._type = type
        self._quality = quality
        self._price = price

    @property
    def product_id(self):
        """
        Gets the product_id of this ProductAttributeCreateRequest.
        Product ID to attach this attribute

        :return: The product_id of this ProductAttributeCreateRequest.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this ProductAttributeCreateRequest.
        Product ID to attach this attribute

        :param product_id: The product_id of this ProductAttributeCreateRequest.
        :type: int
        """

        self._product_id = product_id

    @property
    def type(self):
        """
        Gets the type of this ProductAttributeCreateRequest.
        BOTH (Streaming & Download), STREAMING or DOWNLOAD

        :return: The type of this ProductAttributeCreateRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProductAttributeCreateRequest.
        BOTH (Streaming & Download), STREAMING or DOWNLOAD

        :param type: The type of this ProductAttributeCreateRequest.
        :type: str
        """

        self._type = type

    @property
    def quality(self):
        """
        Gets the quality of this ProductAttributeCreateRequest.
        ALL, HD or SD

        :return: The quality of this ProductAttributeCreateRequest.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """
        Sets the quality of this ProductAttributeCreateRequest.
        ALL, HD or SD

        :param quality: The quality of this ProductAttributeCreateRequest.
        :type: str
        """

        self._quality = quality

    @property
    def price(self):
        """
        Gets the price of this ProductAttributeCreateRequest.
        Final price of the product

        :return: The price of this ProductAttributeCreateRequest.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ProductAttributeCreateRequest.
        Final price of the product

        :param price: The price of this ProductAttributeCreateRequest.
        :type: float
        """

        self._price = price

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