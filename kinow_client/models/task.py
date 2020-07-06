# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.77
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Task(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, data=None, status=None, date_add=None):
        """
        Task - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'data': 'str',
            'status': 'str',
            'date_add': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'data': 'data',
            'status': 'status',
            'date_add': 'date_add'
        }

        self._id = id
        self._name = name
        self._data = data
        self._status = status
        self._date_add = date_add

    @property
    def id(self):
        """
        Gets the id of this Task.
        

        :return: The id of this Task.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Task.
        

        :param id: The id of this Task.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Task.
        

        :return: The name of this Task.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Task.
        

        :param name: The name of this Task.
        :type: str
        """

        self._name = name

    @property
    def data(self):
        """
        Gets the data of this Task.
        

        :return: The data of this Task.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this Task.
        

        :param data: The data of this Task.
        :type: str
        """

        self._data = data

    @property
    def status(self):
        """
        Gets the status of this Task.
        

        :return: The status of this Task.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Task.
        

        :param status: The status of this Task.
        :type: str
        """

        self._status = status

    @property
    def date_add(self):
        """
        Gets the date_add of this Task.
        

        :return: The date_add of this Task.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this Task.
        

        :param date_add: The date_add of this Task.
        :type: str
        """

        self._date_add = date_add

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
