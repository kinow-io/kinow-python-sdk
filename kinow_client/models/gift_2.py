# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.39
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Gift2(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, firstname=None, lastname=None, email=None, message=None, custom=None, date_send=None):
        """
        Gift2 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'firstname': 'str',
            'lastname': 'str',
            'email': 'str',
            'message': 'str',
            'custom': 'str',
            'date_send': 'str'
        }

        self.attribute_map = {
            'firstname': 'firstname',
            'lastname': 'lastname',
            'email': 'email',
            'message': 'message',
            'custom': 'custom',
            'date_send': 'date_send'
        }

        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._message = message
        self._custom = custom
        self._date_send = date_send

    @property
    def firstname(self):
        """
        Gets the firstname of this Gift2.
        Recipient firstname

        :return: The firstname of this Gift2.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this Gift2.
        Recipient firstname

        :param firstname: The firstname of this Gift2.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this Gift2.
        Recipient lastname

        :return: The lastname of this Gift2.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this Gift2.
        Recipient lastname

        :param lastname: The lastname of this Gift2.
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """
        Gets the email of this Gift2.
        Recipient email

        :return: The email of this Gift2.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Gift2.
        Recipient email

        :param email: The email of this Gift2.
        :type: str
        """

        self._email = email

    @property
    def message(self):
        """
        Gets the message of this Gift2.
        Message for the recipient

        :return: The message of this Gift2.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this Gift2.
        Message for the recipient

        :param message: The message of this Gift2.
        :type: str
        """

        self._message = message

    @property
    def custom(self):
        """
        Gets the custom of this Gift2.
        Custom data

        :return: The custom of this Gift2.
        :rtype: str
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """
        Sets the custom of this Gift2.
        Custom data

        :param custom: The custom of this Gift2.
        :type: str
        """

        self._custom = custom

    @property
    def date_send(self):
        """
        Gets the date_send of this Gift2.
        Date to send the Gift to the recipient

        :return: The date_send of this Gift2.
        :rtype: str
        """
        return self._date_send

    @date_send.setter
    def date_send(self, date_send):
        """
        Sets the date_send of this Gift2.
        Date to send the Gift to the recipient

        :param date_send: The date_send of this Gift2.
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
