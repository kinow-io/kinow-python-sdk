# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class State(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_country=None, iso_code=None, name=None):
        """
        State - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_country': 'int',
            'iso_code': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_country': 'id_country',
            'iso_code': 'iso_code',
            'name': 'name'
        }

        self._id = id
        self._id_country = id_country
        self._iso_code = iso_code
        self._name = name

    @property
    def id(self):
        """
        Gets the id of this State.

        :return: The id of this State.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this State.

        :param id: The id of this State.
        :type: int
        """

        self._id = id

    @property
    def id_country(self):
        """
        Gets the id_country of this State.

        :return: The id_country of this State.
        :rtype: int
        """
        return self._id_country

    @id_country.setter
    def id_country(self, id_country):
        """
        Sets the id_country of this State.

        :param id_country: The id_country of this State.
        :type: int
        """

        self._id_country = id_country

    @property
    def iso_code(self):
        """
        Gets the iso_code of this State.

        :return: The iso_code of this State.
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code):
        """
        Sets the iso_code of this State.

        :param iso_code: The iso_code of this State.
        :type: str
        """

        self._iso_code = iso_code

    @property
    def name(self):
        """
        Gets the name of this State.

        :return: The name of this State.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this State.

        :param name: The name of this State.
        :type: str
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
