# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductPrice(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_product=None, prices=None):
        """
        ProductPrice - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_product': 'int',
            'prices': 'list[ProductPricePrices]'
        }

        self.attribute_map = {
            'id_product': 'id_product',
            'prices': 'prices'
        }

        self._id_product = id_product
        self._prices = prices

    @property
    def id_product(self):
        """
        Gets the id_product of this ProductPrice.
        

        :return: The id_product of this ProductPrice.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this ProductPrice.
        

        :param id_product: The id_product of this ProductPrice.
        :type: int
        """

        self._id_product = id_product

    @property
    def prices(self):
        """
        Gets the prices of this ProductPrice.

        :return: The prices of this ProductPrice.
        :rtype: list[ProductPricePrices]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """
        Sets the prices of this ProductPrice.

        :param prices: The prices of this ProductPrice.
        :type: list[ProductPricePrices]
        """

        self._prices = prices

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
