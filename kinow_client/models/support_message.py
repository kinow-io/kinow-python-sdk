# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SupportMessage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_support=None, message=None, private=None, date_add=None, date_upd=None):
        """
        SupportMessage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_support': 'int',
            'message': 'str',
            'private': 'bool',
            'date_add': 'str',
            'date_upd': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_support': 'id_support',
            'message': 'message',
            'private': 'private',
            'date_add': 'date_add',
            'date_upd': 'date_upd'
        }

        self._id = id
        self._id_support = id_support
        self._message = message
        self._private = private
        self._date_add = date_add
        self._date_upd = date_upd

    @property
    def id(self):
        """
        Gets the id of this SupportMessage.

        :return: The id of this SupportMessage.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SupportMessage.

        :param id: The id of this SupportMessage.
        :type: int
        """

        self._id = id

    @property
    def id_support(self):
        """
        Gets the id_support of this SupportMessage.

        :return: The id_support of this SupportMessage.
        :rtype: int
        """
        return self._id_support

    @id_support.setter
    def id_support(self, id_support):
        """
        Sets the id_support of this SupportMessage.

        :param id_support: The id_support of this SupportMessage.
        :type: int
        """

        self._id_support = id_support

    @property
    def message(self):
        """
        Gets the message of this SupportMessage.

        :return: The message of this SupportMessage.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this SupportMessage.

        :param message: The message of this SupportMessage.
        :type: str
        """

        self._message = message

    @property
    def private(self):
        """
        Gets the private of this SupportMessage.

        :return: The private of this SupportMessage.
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """
        Sets the private of this SupportMessage.

        :param private: The private of this SupportMessage.
        :type: bool
        """

        self._private = private

    @property
    def date_add(self):
        """
        Gets the date_add of this SupportMessage.

        :return: The date_add of this SupportMessage.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this SupportMessage.

        :param date_add: The date_add of this SupportMessage.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this SupportMessage.

        :return: The date_upd of this SupportMessage.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this SupportMessage.

        :param date_upd: The date_upd of this SupportMessage.
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
