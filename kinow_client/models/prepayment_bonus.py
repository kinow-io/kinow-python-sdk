# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.35
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PrepaymentBonus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, id_product=None, id_product_attribute=None, amount=None, type=None, date_add=None, date_upd=None):
        """
        PrepaymentBonus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'id_product': 'int',
            'id_product_attribute': 'int',
            'amount': 'float',
            'type': 'str',
            'date_add': 'str',
            'date_upd': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'id_product': 'id_product',
            'id_product_attribute': 'id_product_attribute',
            'amount': 'amount',
            'type': 'type',
            'date_add': 'date_add',
            'date_upd': 'date_upd'
        }

        self._id = id
        self._name = name
        self._id_product = id_product
        self._id_product_attribute = id_product_attribute
        self._amount = amount
        self._type = type
        self._date_add = date_add
        self._date_upd = date_upd

    @property
    def id(self):
        """
        Gets the id of this PrepaymentBonus.

        :return: The id of this PrepaymentBonus.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrepaymentBonus.

        :param id: The id of this PrepaymentBonus.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this PrepaymentBonus.

        :return: The name of this PrepaymentBonus.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this PrepaymentBonus.

        :param name: The name of this PrepaymentBonus.
        :type: str
        """

        self._name = name

    @property
    def id_product(self):
        """
        Gets the id_product of this PrepaymentBonus.

        :return: The id_product of this PrepaymentBonus.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this PrepaymentBonus.

        :param id_product: The id_product of this PrepaymentBonus.
        :type: int
        """

        self._id_product = id_product

    @property
    def id_product_attribute(self):
        """
        Gets the id_product_attribute of this PrepaymentBonus.

        :return: The id_product_attribute of this PrepaymentBonus.
        :rtype: int
        """
        return self._id_product_attribute

    @id_product_attribute.setter
    def id_product_attribute(self, id_product_attribute):
        """
        Sets the id_product_attribute of this PrepaymentBonus.

        :param id_product_attribute: The id_product_attribute of this PrepaymentBonus.
        :type: int
        """

        self._id_product_attribute = id_product_attribute

    @property
    def amount(self):
        """
        Gets the amount of this PrepaymentBonus.

        :return: The amount of this PrepaymentBonus.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PrepaymentBonus.

        :param amount: The amount of this PrepaymentBonus.
        :type: float
        """

        self._amount = amount

    @property
    def type(self):
        """
        Gets the type of this PrepaymentBonus.

        :return: The type of this PrepaymentBonus.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this PrepaymentBonus.

        :param type: The type of this PrepaymentBonus.
        :type: str
        """

        self._type = type

    @property
    def date_add(self):
        """
        Gets the date_add of this PrepaymentBonus.

        :return: The date_add of this PrepaymentBonus.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this PrepaymentBonus.

        :param date_add: The date_add of this PrepaymentBonus.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this PrepaymentBonus.

        :return: The date_upd of this PrepaymentBonus.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this PrepaymentBonus.

        :param date_upd: The date_upd of this PrepaymentBonus.
        :type: str
        """

        self._date_upd = date_upd

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
