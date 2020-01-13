# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.43
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductAttribute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, price=None, price_noreduc=None, type=None, quality=None, active=None):
        """
        ProductAttribute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'price': 'float',
            'price_noreduc': 'float',
            'type': 'str',
            'quality': 'str',
            'active': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'price': 'price',
            'price_noreduc': 'price_noreduc',
            'type': 'type',
            'quality': 'quality',
            'active': 'active'
        }

        self._id = id
        self._name = name
        self._price = price
        self._price_noreduc = price_noreduc
        self._type = type
        self._quality = quality
        self._active = active

    @property
    def id(self):
        """
        Gets the id of this ProductAttribute.
        

        :return: The id of this ProductAttribute.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductAttribute.
        

        :param id: The id of this ProductAttribute.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ProductAttribute.
        

        :return: The name of this ProductAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProductAttribute.
        

        :param name: The name of this ProductAttribute.
        :type: str
        """

        self._name = name

    @property
    def price(self):
        """
        Gets the price of this ProductAttribute.
        

        :return: The price of this ProductAttribute.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ProductAttribute.
        

        :param price: The price of this ProductAttribute.
        :type: float
        """

        self._price = price

    @property
    def price_noreduc(self):
        """
        Gets the price_noreduc of this ProductAttribute.
        

        :return: The price_noreduc of this ProductAttribute.
        :rtype: float
        """
        return self._price_noreduc

    @price_noreduc.setter
    def price_noreduc(self, price_noreduc):
        """
        Sets the price_noreduc of this ProductAttribute.
        

        :param price_noreduc: The price_noreduc of this ProductAttribute.
        :type: float
        """

        self._price_noreduc = price_noreduc

    @property
    def type(self):
        """
        Gets the type of this ProductAttribute.
        

        :return: The type of this ProductAttribute.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProductAttribute.
        

        :param type: The type of this ProductAttribute.
        :type: str
        """

        self._type = type

    @property
    def quality(self):
        """
        Gets the quality of this ProductAttribute.
        

        :return: The quality of this ProductAttribute.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """
        Sets the quality of this ProductAttribute.
        

        :param quality: The quality of this ProductAttribute.
        :type: str
        """

        self._quality = quality

    @property
    def active(self):
        """
        Gets the active of this ProductAttribute.
        

        :return: The active of this ProductAttribute.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ProductAttribute.
        

        :param active: The active of this ProductAttribute.
        :type: int
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
