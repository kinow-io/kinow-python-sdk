# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FreeGift1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_product=None, id_customer=None, firstname=None, lastname=None, email=None):
        """
        FreeGift1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_product': 'int',
            'id_customer': 'int',
            'firstname': 'str',
            'lastname': 'str',
            'email': 'str'
        }

        self.attribute_map = {
            'id_product': 'id_product',
            'id_customer': 'id_customer',
            'firstname': 'firstname',
            'lastname': 'lastname',
            'email': 'email'
        }

        self._id_product = id_product
        self._id_customer = id_customer
        self._firstname = firstname
        self._lastname = lastname
        self._email = email

    @property
    def id_product(self):
        """
        Gets the id_product of this FreeGift1.
        Product ID to offer

        :return: The id_product of this FreeGift1.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this FreeGift1.
        Product ID to offer

        :param id_product: The id_product of this FreeGift1.
        :type: int
        """
        if id_product is None:
            raise ValueError("Invalid value for `id_product`, must not be `None`")

        self._id_product = id_product

    @property
    def id_customer(self):
        """
        Gets the id_customer of this FreeGift1.
        Sender Customer ID

        :return: The id_customer of this FreeGift1.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this FreeGift1.
        Sender Customer ID

        :param id_customer: The id_customer of this FreeGift1.
        :type: int
        """
        if id_customer is None:
            raise ValueError("Invalid value for `id_customer`, must not be `None`")

        self._id_customer = id_customer

    @property
    def firstname(self):
        """
        Gets the firstname of this FreeGift1.
        Recipient firstname

        :return: The firstname of this FreeGift1.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this FreeGift1.
        Recipient firstname

        :param firstname: The firstname of this FreeGift1.
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this FreeGift1.
        Recipient lastname

        :return: The lastname of this FreeGift1.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this FreeGift1.
        Recipient lastname

        :param lastname: The lastname of this FreeGift1.
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")

        self._lastname = lastname

    @property
    def email(self):
        """
        Gets the email of this FreeGift1.
        Recipient email

        :return: The email of this FreeGift1.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this FreeGift1.
        Recipient email

        :param email: The email of this FreeGift1.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

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
