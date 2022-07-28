# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FreeGiftResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_customer=None, id_product=None, id_product_attribute=None, firstname=None, lastname=None, email=None, used=None, date_send=None):
        """
        FreeGiftResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_customer': 'int',
            'id_product': 'int',
            'id_product_attribute': 'int',
            'firstname': 'str',
            'lastname': 'str',
            'email': 'str',
            'used': 'bool',
            'date_send': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_customer': 'id_customer',
            'id_product': 'id_product',
            'id_product_attribute': 'id_product_attribute',
            'firstname': 'firstname',
            'lastname': 'lastname',
            'email': 'email',
            'used': 'used',
            'date_send': 'date_send'
        }

        self._id = id
        self._id_customer = id_customer
        self._id_product = id_product
        self._id_product_attribute = id_product_attribute
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._used = used
        self._date_send = date_send

    @property
    def id(self):
        """
        Gets the id of this FreeGiftResponse.

        :return: The id of this FreeGiftResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FreeGiftResponse.

        :param id: The id of this FreeGiftResponse.
        :type: int
        """

        self._id = id

    @property
    def id_customer(self):
        """
        Gets the id_customer of this FreeGiftResponse.

        :return: The id_customer of this FreeGiftResponse.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this FreeGiftResponse.

        :param id_customer: The id_customer of this FreeGiftResponse.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def id_product(self):
        """
        Gets the id_product of this FreeGiftResponse.

        :return: The id_product of this FreeGiftResponse.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this FreeGiftResponse.

        :param id_product: The id_product of this FreeGiftResponse.
        :type: int
        """

        self._id_product = id_product

    @property
    def id_product_attribute(self):
        """
        Gets the id_product_attribute of this FreeGiftResponse.

        :return: The id_product_attribute of this FreeGiftResponse.
        :rtype: int
        """
        return self._id_product_attribute

    @id_product_attribute.setter
    def id_product_attribute(self, id_product_attribute):
        """
        Sets the id_product_attribute of this FreeGiftResponse.

        :param id_product_attribute: The id_product_attribute of this FreeGiftResponse.
        :type: int
        """

        self._id_product_attribute = id_product_attribute

    @property
    def firstname(self):
        """
        Gets the firstname of this FreeGiftResponse.

        :return: The firstname of this FreeGiftResponse.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this FreeGiftResponse.

        :param firstname: The firstname of this FreeGiftResponse.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this FreeGiftResponse.

        :return: The lastname of this FreeGiftResponse.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this FreeGiftResponse.

        :param lastname: The lastname of this FreeGiftResponse.
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """
        Gets the email of this FreeGiftResponse.

        :return: The email of this FreeGiftResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this FreeGiftResponse.

        :param email: The email of this FreeGiftResponse.
        :type: str
        """

        self._email = email

    @property
    def used(self):
        """
        Gets the used of this FreeGiftResponse.

        :return: The used of this FreeGiftResponse.
        :rtype: bool
        """
        return self._used

    @used.setter
    def used(self, used):
        """
        Sets the used of this FreeGiftResponse.

        :param used: The used of this FreeGiftResponse.
        :type: bool
        """

        self._used = used

    @property
    def date_send(self):
        """
        Gets the date_send of this FreeGiftResponse.

        :return: The date_send of this FreeGiftResponse.
        :rtype: str
        """
        return self._date_send

    @date_send.setter
    def date_send(self, date_send):
        """
        Sets the date_send of this FreeGiftResponse.

        :param date_send: The date_send of this FreeGiftResponse.
        :type: str
        """

        self._date_send = date_send

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
