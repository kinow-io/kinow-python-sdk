# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateGiftRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_cart=None, id_product=None, id_product_attribute=None, firstname=None, lastname=None, email=None, message=None, custom=None, date_send=None, auto_link=None):
        """
        CreateGiftRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_cart': 'int',
            'id_product': 'int',
            'id_product_attribute': 'int',
            'firstname': 'str',
            'lastname': 'str',
            'email': 'str',
            'message': 'str',
            'custom': 'str',
            'date_send': 'str',
            'auto_link': 'bool'
        }

        self.attribute_map = {
            'id_cart': 'id_cart',
            'id_product': 'id_product',
            'id_product_attribute': 'id_product_attribute',
            'firstname': 'firstname',
            'lastname': 'lastname',
            'email': 'email',
            'message': 'message',
            'custom': 'custom',
            'date_send': 'date_send',
            'auto_link': 'auto_link'
        }

        self._id_cart = id_cart
        self._id_product = id_product
        self._id_product_attribute = id_product_attribute
        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._message = message
        self._custom = custom
        self._date_send = date_send
        self._auto_link = auto_link

    @property
    def id_cart(self):
        """
        Gets the id_cart of this CreateGiftRequest.
        Cart ID to attach this Gift

        :return: The id_cart of this CreateGiftRequest.
        :rtype: int
        """
        return self._id_cart

    @id_cart.setter
    def id_cart(self, id_cart):
        """
        Sets the id_cart of this CreateGiftRequest.
        Cart ID to attach this Gift

        :param id_cart: The id_cart of this CreateGiftRequest.
        :type: int
        """
        if id_cart is None:
            raise ValueError("Invalid value for `id_cart`, must not be `None`")

        self._id_cart = id_cart

    @property
    def id_product(self):
        """
        Gets the id_product of this CreateGiftRequest.
        Product ID to offer

        :return: The id_product of this CreateGiftRequest.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this CreateGiftRequest.
        Product ID to offer

        :param id_product: The id_product of this CreateGiftRequest.
        :type: int
        """
        if id_product is None:
            raise ValueError("Invalid value for `id_product`, must not be `None`")

        self._id_product = id_product

    @property
    def id_product_attribute(self):
        """
        Gets the id_product_attribute of this CreateGiftRequest.
        ID Product Attribute to offer

        :return: The id_product_attribute of this CreateGiftRequest.
        :rtype: int
        """
        return self._id_product_attribute

    @id_product_attribute.setter
    def id_product_attribute(self, id_product_attribute):
        """
        Sets the id_product_attribute of this CreateGiftRequest.
        ID Product Attribute to offer

        :param id_product_attribute: The id_product_attribute of this CreateGiftRequest.
        :type: int
        """

        self._id_product_attribute = id_product_attribute

    @property
    def firstname(self):
        """
        Gets the firstname of this CreateGiftRequest.
        Recipient firstname

        :return: The firstname of this CreateGiftRequest.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this CreateGiftRequest.
        Recipient firstname

        :param firstname: The firstname of this CreateGiftRequest.
        :type: str
        """
        if firstname is None:
            raise ValueError("Invalid value for `firstname`, must not be `None`")

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this CreateGiftRequest.
        Recipient lastname

        :return: The lastname of this CreateGiftRequest.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this CreateGiftRequest.
        Recipient lastname

        :param lastname: The lastname of this CreateGiftRequest.
        :type: str
        """
        if lastname is None:
            raise ValueError("Invalid value for `lastname`, must not be `None`")

        self._lastname = lastname

    @property
    def email(self):
        """
        Gets the email of this CreateGiftRequest.
        Recipient email

        :return: The email of this CreateGiftRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CreateGiftRequest.
        Recipient email

        :param email: The email of this CreateGiftRequest.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def message(self):
        """
        Gets the message of this CreateGiftRequest.
        Message for the recipient

        :return: The message of this CreateGiftRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CreateGiftRequest.
        Message for the recipient

        :param message: The message of this CreateGiftRequest.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def custom(self):
        """
        Gets the custom of this CreateGiftRequest.
        Custom data

        :return: The custom of this CreateGiftRequest.
        :rtype: str
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """
        Sets the custom of this CreateGiftRequest.
        Custom data

        :param custom: The custom of this CreateGiftRequest.
        :type: str
        """

        self._custom = custom

    @property
    def date_send(self):
        """
        Gets the date_send of this CreateGiftRequest.
        Date to send the Gift to the recipient

        :return: The date_send of this CreateGiftRequest.
        :rtype: str
        """
        return self._date_send

    @date_send.setter
    def date_send(self, date_send):
        """
        Sets the date_send of this CreateGiftRequest.
        Date to send the Gift to the recipient

        :param date_send: The date_send of this CreateGiftRequest.
        :type: str
        """

        self._date_send = date_send

    @property
    def auto_link(self):
        """
        Gets the auto_link of this CreateGiftRequest.
        Auto-link Gift to an existing Product in Cart with same IDs - true by default

        :return: The auto_link of this CreateGiftRequest.
        :rtype: bool
        """
        return self._auto_link

    @auto_link.setter
    def auto_link(self, auto_link):
        """
        Sets the auto_link of this CreateGiftRequest.
        Auto-link Gift to an existing Product in Cart with same IDs - true by default

        :param auto_link: The auto_link of this CreateGiftRequest.
        :type: bool
        """

        self._auto_link = auto_link

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