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


class Gender(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, type=None, name=None):
        """
        Gender - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'type': 'int',
            'name': 'list[I18nField]'
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'name': 'name'
        }

        self._id = id
        self._type = type
        self._name = name

    @property
    def id(self):
        """
        Gets the id of this Gender.

        :return: The id of this Gender.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Gender.

        :param id: The id of this Gender.
        :type: int
        """

        self._id = id

    @property
    def type(self):
        """
        Gets the type of this Gender.

        :return: The type of this Gender.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Gender.

        :param type: The type of this Gender.
        :type: int
        """

        self._type = type

    @property
    def name(self):
        """
        Gets the name of this Gender.

        :return: The name of this Gender.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Gender.

        :param name: The name of this Gender.
        :type: list[I18nField]
        """

        self._name = name

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
