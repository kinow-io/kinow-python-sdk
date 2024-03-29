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


class CreateProductAccessRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_customer=None, id_product=None, id_product_attribute=None, type=None, active=None, date_exp=None):
        """
        CreateProductAccessRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_customer': 'int',
            'id_product': 'int',
            'id_product_attribute': 'int',
            'type': 'str',
            'active': 'int',
            'date_exp': 'str'
        }

        self.attribute_map = {
            'id_customer': 'id_customer',
            'id_product': 'id_product',
            'id_product_attribute': 'id_product_attribute',
            'type': 'type',
            'active': 'active',
            'date_exp': 'date_exp'
        }

        self._id_customer = id_customer
        self._id_product = id_product
        self._id_product_attribute = id_product_attribute
        self._type = type
        self._active = active
        self._date_exp = date_exp

    @property
    def id_customer(self):
        """
        Gets the id_customer of this CreateProductAccessRequest.

        :return: The id_customer of this CreateProductAccessRequest.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this CreateProductAccessRequest.

        :param id_customer: The id_customer of this CreateProductAccessRequest.
        :type: int
        """
        if id_customer is None:
            raise ValueError("Invalid value for `id_customer`, must not be `None`")

        self._id_customer = id_customer

    @property
    def id_product(self):
        """
        Gets the id_product of this CreateProductAccessRequest.

        :return: The id_product of this CreateProductAccessRequest.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this CreateProductAccessRequest.

        :param id_product: The id_product of this CreateProductAccessRequest.
        :type: int
        """
        if id_product is None:
            raise ValueError("Invalid value for `id_product`, must not be `None`")

        self._id_product = id_product

    @property
    def id_product_attribute(self):
        """
        Gets the id_product_attribute of this CreateProductAccessRequest.

        :return: The id_product_attribute of this CreateProductAccessRequest.
        :rtype: int
        """
        return self._id_product_attribute

    @id_product_attribute.setter
    def id_product_attribute(self, id_product_attribute):
        """
        Sets the id_product_attribute of this CreateProductAccessRequest.

        :param id_product_attribute: The id_product_attribute of this CreateProductAccessRequest.
        :type: int
        """

        self._id_product_attribute = id_product_attribute

    @property
    def type(self):
        """
        Gets the type of this CreateProductAccessRequest.

        :return: The type of this CreateProductAccessRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateProductAccessRequest.

        :param type: The type of this CreateProductAccessRequest.
        :type: str
        """

        self._type = type

    @property
    def active(self):
        """
        Gets the active of this CreateProductAccessRequest.

        :return: The active of this CreateProductAccessRequest.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this CreateProductAccessRequest.

        :param active: The active of this CreateProductAccessRequest.
        :type: int
        """

        self._active = active

    @property
    def date_exp(self):
        """
        Gets the date_exp of this CreateProductAccessRequest.

        :return: The date_exp of this CreateProductAccessRequest.
        :rtype: str
        """
        return self._date_exp

    @date_exp.setter
    def date_exp(self, date_exp):
        """
        Sets the date_exp of this CreateProductAccessRequest.

        :param date_exp: The date_exp of this CreateProductAccessRequest.
        :type: str
        """

        self._date_exp = date_exp

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
