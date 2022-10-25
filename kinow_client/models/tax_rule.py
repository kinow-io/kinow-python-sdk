# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TaxRule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_country=None, id_state=None, rate=None, name=None):
        """
        TaxRule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_country': 'int',
            'id_state': 'int',
            'rate': 'float',
            'name': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_country': 'id_country',
            'id_state': 'id_state',
            'rate': 'rate',
            'name': 'name'
        }

        self._id = id
        self._id_country = id_country
        self._id_state = id_state
        self._rate = rate
        self._name = name

    @property
    def id(self):
        """
        Gets the id of this TaxRule.

        :return: The id of this TaxRule.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TaxRule.

        :param id: The id of this TaxRule.
        :type: int
        """

        self._id = id

    @property
    def id_country(self):
        """
        Gets the id_country of this TaxRule.

        :return: The id_country of this TaxRule.
        :rtype: int
        """
        return self._id_country

    @id_country.setter
    def id_country(self, id_country):
        """
        Sets the id_country of this TaxRule.

        :param id_country: The id_country of this TaxRule.
        :type: int
        """

        self._id_country = id_country

    @property
    def id_state(self):
        """
        Gets the id_state of this TaxRule.

        :return: The id_state of this TaxRule.
        :rtype: int
        """
        return self._id_state

    @id_state.setter
    def id_state(self, id_state):
        """
        Sets the id_state of this TaxRule.

        :param id_state: The id_state of this TaxRule.
        :type: int
        """

        self._id_state = id_state

    @property
    def rate(self):
        """
        Gets the rate of this TaxRule.

        :return: The rate of this TaxRule.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """
        Sets the rate of this TaxRule.

        :param rate: The rate of this TaxRule.
        :type: float
        """

        self._rate = rate

    @property
    def name(self):
        """
        Gets the name of this TaxRule.

        :return: The name of this TaxRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TaxRule.

        :param name: The name of this TaxRule.
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
