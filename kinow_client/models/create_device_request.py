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


class CreateDeviceRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_customer=None, fingerprint=None, type=None, os=None, application=None):
        """
        CreateDeviceRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_customer': 'int',
            'fingerprint': 'str',
            'type': 'str',
            'os': 'str',
            'application': 'str'
        }

        self.attribute_map = {
            'id_customer': 'id_customer',
            'fingerprint': 'fingerprint',
            'type': 'type',
            'os': 'os',
            'application': 'application'
        }

        self._id_customer = id_customer
        self._fingerprint = fingerprint
        self._type = type
        self._os = os
        self._application = application

    @property
    def id_customer(self):
        """
        Gets the id_customer of this CreateDeviceRequest.
        Customer ID to attach this Device

        :return: The id_customer of this CreateDeviceRequest.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this CreateDeviceRequest.
        Customer ID to attach this Device

        :param id_customer: The id_customer of this CreateDeviceRequest.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def fingerprint(self):
        """
        Gets the fingerprint of this CreateDeviceRequest.
        Uniq fingerprint to identify Device

        :return: The fingerprint of this CreateDeviceRequest.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """
        Sets the fingerprint of this CreateDeviceRequest.
        Uniq fingerprint to identify Device

        :param fingerprint: The fingerprint of this CreateDeviceRequest.
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def type(self):
        """
        Gets the type of this CreateDeviceRequest.
        Device type (eg. Desktop, mobile, STB)

        :return: The type of this CreateDeviceRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateDeviceRequest.
        Device type (eg. Desktop, mobile, STB)

        :param type: The type of this CreateDeviceRequest.
        :type: str
        """

        self._type = type

    @property
    def os(self):
        """
        Gets the os of this CreateDeviceRequest.
        Device OS (eg. Windows 10, iOS, Android)

        :return: The os of this CreateDeviceRequest.
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """
        Sets the os of this CreateDeviceRequest.
        Device OS (eg. Windows 10, iOS, Android)

        :param os: The os of this CreateDeviceRequest.
        :type: str
        """

        self._os = os

    @property
    def application(self):
        """
        Gets the application of this CreateDeviceRequest.
        Device application (eg. Chrome, Firefox)

        :return: The application of this CreateDeviceRequest.
        :rtype: str
        """
        return self._application

    @application.setter
    def application(self, application):
        """
        Sets the application of this CreateDeviceRequest.
        Device application (eg. Chrome, Firefox)

        :param application: The application of this CreateDeviceRequest.
        :type: str
        """

        self._application = application

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
