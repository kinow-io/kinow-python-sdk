# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.55
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Employee(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, email=None, firstname=None, lastname=None, active=None):
        """
        Employee - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'email': 'str',
            'firstname': 'str',
            'lastname': 'str',
            'active': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'email': 'email',
            'firstname': 'firstname',
            'lastname': 'lastname',
            'active': 'active'
        }

        self._id = id
        self._email = email
        self._firstname = firstname
        self._lastname = lastname
        self._active = active

    @property
    def id(self):
        """
        Gets the id of this Employee.

        :return: The id of this Employee.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Employee.

        :param id: The id of this Employee.
        :type: int
        """

        self._id = id

    @property
    def email(self):
        """
        Gets the email of this Employee.

        :return: The email of this Employee.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Employee.

        :param email: The email of this Employee.
        :type: str
        """

        self._email = email

    @property
    def firstname(self):
        """
        Gets the firstname of this Employee.

        :return: The firstname of this Employee.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this Employee.

        :param firstname: The firstname of this Employee.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this Employee.

        :return: The lastname of this Employee.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this Employee.

        :param lastname: The lastname of this Employee.
        :type: str
        """

        self._lastname = lastname

    @property
    def active(self):
        """
        Gets the active of this Employee.

        :return: The active of this Employee.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Employee.

        :param active: The active of this Employee.
        :type: bool
        """

        self._active = active

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
