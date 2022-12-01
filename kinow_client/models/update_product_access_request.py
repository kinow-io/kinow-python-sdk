# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.22
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateProductAccessRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_customer=None, id_product=None, id_product_attribute=None, type=None, active=None, date_exp=None):
        """
        UpdateProductAccessRequest - a model defined in Swagger

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
        Gets the id_customer of this UpdateProductAccessRequest.

        :return: The id_customer of this UpdateProductAccessRequest.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this UpdateProductAccessRequest.

        :param id_customer: The id_customer of this UpdateProductAccessRequest.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def id_product(self):
        """
        Gets the id_product of this UpdateProductAccessRequest.

        :return: The id_product of this UpdateProductAccessRequest.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this UpdateProductAccessRequest.

        :param id_product: The id_product of this UpdateProductAccessRequest.
        :type: int
        """

        self._id_product = id_product

    @property
    def id_product_attribute(self):
        """
        Gets the id_product_attribute of this UpdateProductAccessRequest.

        :return: The id_product_attribute of this UpdateProductAccessRequest.
        :rtype: int
        """
        return self._id_product_attribute

    @id_product_attribute.setter
    def id_product_attribute(self, id_product_attribute):
        """
        Sets the id_product_attribute of this UpdateProductAccessRequest.

        :param id_product_attribute: The id_product_attribute of this UpdateProductAccessRequest.
        :type: int
        """

        self._id_product_attribute = id_product_attribute

    @property
    def type(self):
        """
        Gets the type of this UpdateProductAccessRequest.

        :return: The type of this UpdateProductAccessRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UpdateProductAccessRequest.

        :param type: The type of this UpdateProductAccessRequest.
        :type: str
        """

        self._type = type

    @property
    def active(self):
        """
        Gets the active of this UpdateProductAccessRequest.

        :return: The active of this UpdateProductAccessRequest.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this UpdateProductAccessRequest.

        :param active: The active of this UpdateProductAccessRequest.
        :type: int
        """

        self._active = active

    @property
    def date_exp(self):
        """
        Gets the date_exp of this UpdateProductAccessRequest.

        :return: The date_exp of this UpdateProductAccessRequest.
        :rtype: str
        """
        return self._date_exp

    @date_exp.setter
    def date_exp(self, date_exp):
        """
        Sets the date_exp of this UpdateProductAccessRequest.

        :param date_exp: The date_exp of this UpdateProductAccessRequest.
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
