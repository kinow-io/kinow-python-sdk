# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.22
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Currency(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, iso_code=None, iso_code_num=None, sign=None, conversion_rate=None, format=None, blank=None, decimals=None):
        """
        Currency - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'iso_code': 'str',
            'iso_code_num': 'str',
            'sign': 'str',
            'conversion_rate': 'float',
            'format': 'int',
            'blank': 'int',
            'decimals': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'iso_code': 'iso_code',
            'iso_code_num': 'iso_code_num',
            'sign': 'sign',
            'conversion_rate': 'conversion_rate',
            'format': 'format',
            'blank': 'blank',
            'decimals': 'decimals'
        }

        self._id = id
        self._name = name
        self._iso_code = iso_code
        self._iso_code_num = iso_code_num
        self._sign = sign
        self._conversion_rate = conversion_rate
        self._format = format
        self._blank = blank
        self._decimals = decimals

    @property
    def id(self):
        """
        Gets the id of this Currency.

        :return: The id of this Currency.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Currency.

        :param id: The id of this Currency.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Currency.

        :return: The name of this Currency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Currency.

        :param name: The name of this Currency.
        :type: str
        """

        self._name = name

    @property
    def iso_code(self):
        """
        Gets the iso_code of this Currency.

        :return: The iso_code of this Currency.
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code):
        """
        Sets the iso_code of this Currency.

        :param iso_code: The iso_code of this Currency.
        :type: str
        """

        self._iso_code = iso_code

    @property
    def iso_code_num(self):
        """
        Gets the iso_code_num of this Currency.

        :return: The iso_code_num of this Currency.
        :rtype: str
        """
        return self._iso_code_num

    @iso_code_num.setter
    def iso_code_num(self, iso_code_num):
        """
        Sets the iso_code_num of this Currency.

        :param iso_code_num: The iso_code_num of this Currency.
        :type: str
        """

        self._iso_code_num = iso_code_num

    @property
    def sign(self):
        """
        Gets the sign of this Currency.

        :return: The sign of this Currency.
        :rtype: str
        """
        return self._sign

    @sign.setter
    def sign(self, sign):
        """
        Sets the sign of this Currency.

        :param sign: The sign of this Currency.
        :type: str
        """

        self._sign = sign

    @property
    def conversion_rate(self):
        """
        Gets the conversion_rate of this Currency.

        :return: The conversion_rate of this Currency.
        :rtype: float
        """
        return self._conversion_rate

    @conversion_rate.setter
    def conversion_rate(self, conversion_rate):
        """
        Sets the conversion_rate of this Currency.

        :param conversion_rate: The conversion_rate of this Currency.
        :type: float
        """

        self._conversion_rate = conversion_rate

    @property
    def format(self):
        """
        Gets the format of this Currency.

        :return: The format of this Currency.
        :rtype: int
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this Currency.

        :param format: The format of this Currency.
        :type: int
        """

        self._format = format

    @property
    def blank(self):
        """
        Gets the blank of this Currency.

        :return: The blank of this Currency.
        :rtype: int
        """
        return self._blank

    @blank.setter
    def blank(self, blank):
        """
        Sets the blank of this Currency.

        :param blank: The blank of this Currency.
        :type: int
        """

        self._blank = blank

    @property
    def decimals(self):
        """
        Gets the decimals of this Currency.

        :return: The decimals of this Currency.
        :rtype: int
        """
        return self._decimals

    @decimals.setter
    def decimals(self, decimals):
        """
        Sets the decimals of this Currency.

        :param decimals: The decimals of this Currency.
        :type: int
        """

        self._decimals = decimals

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
