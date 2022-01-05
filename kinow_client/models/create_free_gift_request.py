# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateFreeGiftRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_customer=None, id_product=None, id_product_attribute=None, firstname=None, lastname=None, email=None):
        """
        CreateFreeGiftRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_customer': 'int',
            'id_product': 'int',
            'id_product_attribute': 'int',
            'firstname': 'str',
            'lastname': 'str',
            'email': 'str'
        }

        self.attribute_map = {
            'id_customer': 'id_customer',
            'id_product': 'id_product',
            'id_product_attribute': 'id_product_attribute',
            'firstname': 'firstname',
            'lastname': 'lastname',
            'email': 'email'
        }

        self._id_customer = id_customer
        self._id_product = id_product
        self._id_product_attribute = id_product_attribute
        self._firstname = firstname
        self._lastname = lastname
        self._email = email

    @property
    def id_customer(self):
        """
        Gets the id_customer of this CreateFreeGiftRequest.
        Customer  ID to attach this Gift

        :return: The id_customer of this CreateFreeGiftRequest.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this CreateFreeGiftRequest.
        Customer  ID to attach this Gift

        :param id_customer: The id_customer of this CreateFreeGiftRequest.
        :type: int
        """
        if id_customer is None:
            raise ValueError("Invalid value for `id_customer`, must not be `None`")

        self._id_customer = id_customer

    @property
    def id_product(self):
        """
        Gets the id_product of this CreateFreeGiftRequest.
        Product ID to offer

        :return: The id_product of this CreateFreeGiftRequest.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this CreateFreeGiftRequest.
        Product ID to offer

        :param id_product: The id_product of this CreateFreeGiftRequest.
        :type: int
        """
        if id_product is None:
            raise ValueError("Invalid value for `id_product`, must not be `None`")

        self._id_product = id_product

    @property
    def id_product_attribute(self):
        """
        Gets the id_product_attribute of this CreateFreeGiftRequest.
        ID Product Attribute to offer

        :return: The id_product_attribute of this CreateFreeGiftRequest.
        :rtype: int
        """
        return self._id_product_attribute

    @id_product_attribute.setter
    def id_product_attribute(self, id_product_attribute):
        """
        Sets the id_product_attribute of this CreateFreeGiftRequest.
        ID Product Attribute to offer

        :param id_product_attribute: The id_product_attribute of this CreateFreeGiftRequest.
        :type: int
        """

        self._id_product_attribute = id_product_attribute

    @property
    def firstname(self):
        """
        Gets the firstname of this CreateFreeGiftRequest.
        Recipient firstname

        :return: The firstname of this CreateFreeGiftRequest.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this CreateFreeGiftRequest.
        Recipient firstname

        :param firstname: The firstname of this CreateFreeGiftRequest.
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this CreateFreeGiftRequest.
        Recipient lastname

        :return: The lastname of this CreateFreeGiftRequest.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this CreateFreeGiftRequest.
        Recipient lastname

        :param lastname: The lastname of this CreateFreeGiftRequest.
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")

        self._lastname = lastname

    @property
    def email(self):
        """
        Gets the email of this CreateFreeGiftRequest.
        Recipient email

        :return: The email of this CreateFreeGiftRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CreateFreeGiftRequest.
        Recipient email

        :param email: The email of this CreateFreeGiftRequest.
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
