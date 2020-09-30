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


class TaskCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, data=None, id_employee=None):
        """
        TaskCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'data': 'str',
            'id_employee': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'data': 'data',
            'id_employee': 'id_employee'
        }

        self._name = name
        self._data = data
        self._id_employee = id_employee

    @property
    def name(self):
        """
        Gets the name of this TaskCreateRequest.

        :return: The name of this TaskCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TaskCreateRequest.

        :param name: The name of this TaskCreateRequest.
        :type: str
        """

        self._name = name

    @property
    def data(self):
        """
        Gets the data of this TaskCreateRequest.

        :return: The data of this TaskCreateRequest.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this TaskCreateRequest.

        :param data: The data of this TaskCreateRequest.
        :type: str
        """

        self._data = data

    @property
    def id_employee(self):
        """
        Gets the id_employee of this TaskCreateRequest.

        :return: The id_employee of this TaskCreateRequest.
        :rtype: int
        """
        return self._id_employee

    @id_employee.setter
    def id_employee(self, id_employee):
        """
        Sets the id_employee of this TaskCreateRequest.

        :param id_employee: The id_employee of this TaskCreateRequest.
        :type: int
        """

        self._id_employee = id_employee

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
