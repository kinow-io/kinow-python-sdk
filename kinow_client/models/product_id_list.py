# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductIDList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product_ids=None, ip_address=None):
        """
        ProductIDList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'product_ids': 'str',
            'ip_address': 'str'
        }

        self.attribute_map = {
            'product_ids': 'product_ids',
            'ip_address': 'ip_address'
        }

        self._product_ids = product_ids
        self._ip_address = ip_address

    @property
    def product_ids(self):
        """
        Gets the product_ids of this ProductIDList.

        :return: The product_ids of this ProductIDList.
        :rtype: str
        """
        return self._product_ids

    @product_ids.setter
    def product_ids(self, product_ids):
        """
        Sets the product_ids of this ProductIDList.

        :param product_ids: The product_ids of this ProductIDList.
        :type: str
        """

        self._product_ids = product_ids

    @property
    def ip_address(self):
        """
        Gets the ip_address of this ProductIDList.

        :return: The ip_address of this ProductIDList.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this ProductIDList.

        :param ip_address: The ip_address of this ProductIDList.
        :type: str
        """

        self._ip_address = ip_address

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
