# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.67
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductAccessInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_product=None, can_see=None, can_buy=None, can_watch=None):
        """
        ProductAccessInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_product': 'float',
            'can_see': 'bool',
            'can_buy': 'bool',
            'can_watch': 'bool'
        }

        self.attribute_map = {
            'id_product': 'id_product',
            'can_see': 'can_see',
            'can_buy': 'can_buy',
            'can_watch': 'can_watch'
        }

        self._id_product = id_product
        self._can_see = can_see
        self._can_buy = can_buy
        self._can_watch = can_watch

    @property
    def id_product(self):
        """
        Gets the id_product of this ProductAccessInfo.
        

        :return: The id_product of this ProductAccessInfo.
        :rtype: float
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this ProductAccessInfo.
        

        :param id_product: The id_product of this ProductAccessInfo.
        :type: float
        """

        self._id_product = id_product

    @property
    def can_see(self):
        """
        Gets the can_see of this ProductAccessInfo.
        

        :return: The can_see of this ProductAccessInfo.
        :rtype: bool
        """
        return self._can_see

    @can_see.setter
    def can_see(self, can_see):
        """
        Sets the can_see of this ProductAccessInfo.
        

        :param can_see: The can_see of this ProductAccessInfo.
        :type: bool
        """

        self._can_see = can_see

    @property
    def can_buy(self):
        """
        Gets the can_buy of this ProductAccessInfo.
        

        :return: The can_buy of this ProductAccessInfo.
        :rtype: bool
        """
        return self._can_buy

    @can_buy.setter
    def can_buy(self, can_buy):
        """
        Sets the can_buy of this ProductAccessInfo.
        

        :param can_buy: The can_buy of this ProductAccessInfo.
        :type: bool
        """

        self._can_buy = can_buy

    @property
    def can_watch(self):
        """
        Gets the can_watch of this ProductAccessInfo.
        

        :return: The can_watch of this ProductAccessInfo.
        :rtype: bool
        """
        return self._can_watch

    @can_watch.setter
    def can_watch(self, can_watch):
        """
        Sets the can_watch of this ProductAccessInfo.
        

        :param can_watch: The can_watch of this ProductAccessInfo.
        :type: bool
        """

        self._can_watch = can_watch

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
