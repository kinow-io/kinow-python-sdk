# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.58
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class RegistrationField(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, required=None, displayed=None):
        """
        RegistrationField - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'required': 'bool',
            'displayed': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'required': 'required',
            'displayed': 'displayed'
        }

        self._name = name
        self._required = required
        self._displayed = displayed

    @property
    def name(self):
        """
        Gets the name of this RegistrationField.

        :return: The name of this RegistrationField.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RegistrationField.

        :param name: The name of this RegistrationField.
        :type: str
        """

        self._name = name

    @property
    def required(self):
        """
        Gets the required of this RegistrationField.

        :return: The required of this RegistrationField.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this RegistrationField.

        :param required: The required of this RegistrationField.
        :type: bool
        """

        self._required = required

    @property
    def displayed(self):
        """
        Gets the displayed of this RegistrationField.

        :return: The displayed of this RegistrationField.
        :rtype: bool
        """
        return self._displayed

    @displayed.setter
    def displayed(self, displayed):
        """
        Sets the displayed of this RegistrationField.

        :param displayed: The displayed of this RegistrationField.
        :type: bool
        """

        self._displayed = displayed

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
