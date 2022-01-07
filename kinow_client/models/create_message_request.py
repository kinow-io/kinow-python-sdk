# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateMessageRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_lang=None, id_support=None, email=None, id_contact=None, message=None, id_product=None, id_order=None, send_mail=None):
        """
        CreateMessageRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_lang': 'int',
            'id_support': 'int',
            'email': 'str',
            'id_contact': 'int',
            'message': 'str',
            'id_product': 'int',
            'id_order': 'int',
            'send_mail': 'bool'
        }

        self.attribute_map = {
            'id_lang': 'id_lang',
            'id_support': 'id_support',
            'email': 'email',
            'id_contact': 'id_contact',
            'message': 'message',
            'id_product': 'id_product',
            'id_order': 'id_order',
            'send_mail': 'send_mail'
        }

        self._id_lang = id_lang
        self._id_support = id_support
        self._email = email
        self._id_contact = id_contact
        self._message = message
        self._id_product = id_product
        self._id_order = id_order
        self._send_mail = send_mail

    @property
    def id_lang(self):
        """
        Gets the id_lang of this CreateMessageRequest.
        Language ID used by user to write his message

        :return: The id_lang of this CreateMessageRequest.
        :rtype: int
        """
        return self._id_lang

    @id_lang.setter
    def id_lang(self, id_lang):
        """
        Sets the id_lang of this CreateMessageRequest.
        Language ID used by user to write his message

        :param id_lang: The id_lang of this CreateMessageRequest.
        :type: int
        """
        if id_lang is None:
            raise ValueError("Invalid value for `id_lang`, must not be `None`")

        self._id_lang = id_lang

    @property
    def id_support(self):
        """
        Gets the id_support of this CreateMessageRequest.
        Link the message to a previous message

        :return: The id_support of this CreateMessageRequest.
        :rtype: int
        """
        return self._id_support

    @id_support.setter
    def id_support(self, id_support):
        """
        Sets the id_support of this CreateMessageRequest.
        Link the message to a previous message

        :param id_support: The id_support of this CreateMessageRequest.
        :type: int
        """

        self._id_support = id_support

    @property
    def email(self):
        """
        Gets the email of this CreateMessageRequest.
        User email in order to send him a response

        :return: The email of this CreateMessageRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CreateMessageRequest.
        User email in order to send him a response

        :param email: The email of this CreateMessageRequest.
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")

        self._email = email

    @property
    def id_contact(self):
        """
        Gets the id_contact of this CreateMessageRequest.
        Contact ID to send the user message

        :return: The id_contact of this CreateMessageRequest.
        :rtype: int
        """
        return self._id_contact

    @id_contact.setter
    def id_contact(self, id_contact):
        """
        Sets the id_contact of this CreateMessageRequest.
        Contact ID to send the user message

        :param id_contact: The id_contact of this CreateMessageRequest.
        :type: int
        """
        if id_contact is None:
            raise ValueError("Invalid value for `id_contact`, must not be `None`")

        self._id_contact = id_contact

    @property
    def message(self):
        """
        Gets the message of this CreateMessageRequest.
        User message

        :return: The message of this CreateMessageRequest.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this CreateMessageRequest.
        User message

        :param message: The message of this CreateMessageRequest.
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def id_product(self):
        """
        Gets the id_product of this CreateMessageRequest.
        Link the message to a product in catalog

        :return: The id_product of this CreateMessageRequest.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this CreateMessageRequest.
        Link the message to a product in catalog

        :param id_product: The id_product of this CreateMessageRequest.
        :type: int
        """

        self._id_product = id_product

    @property
    def id_order(self):
        """
        Gets the id_order of this CreateMessageRequest.
        Link the message to an existing order

        :return: The id_order of this CreateMessageRequest.
        :rtype: int
        """
        return self._id_order

    @id_order.setter
    def id_order(self, id_order):
        """
        Sets the id_order of this CreateMessageRequest.
        Link the message to an existing order

        :param id_order: The id_order of this CreateMessageRequest.
        :type: int
        """

        self._id_order = id_order

    @property
    def send_mail(self):
        """
        Gets the send_mail of this CreateMessageRequest.
        Send confirmation email to the providen email

        :return: The send_mail of this CreateMessageRequest.
        :rtype: bool
        """
        return self._send_mail

    @send_mail.setter
    def send_mail(self, send_mail):
        """
        Sets the send_mail of this CreateMessageRequest.
        Send confirmation email to the providen email

        :param send_mail: The send_mail of this CreateMessageRequest.
        :type: bool
        """

        self._send_mail = send_mail

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
