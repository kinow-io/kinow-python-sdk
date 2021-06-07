# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.41
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Promotion(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, id_country=None, date_from=None, date_to=None, date_add=None, date_upd=None):
        """
        Promotion - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'id_country': 'int',
            'date_from': 'str',
            'date_to': 'str',
            'date_add': 'str',
            'date_upd': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'id_country': 'id_country',
            'date_from': 'date_from',
            'date_to': 'date_to',
            'date_add': 'date_add',
            'date_upd': 'date_upd'
        }

        self._id = id
        self._name = name
        self._id_country = id_country
        self._date_from = date_from
        self._date_to = date_to
        self._date_add = date_add
        self._date_upd = date_upd

    @property
    def id(self):
        """
        Gets the id of this Promotion.

        :return: The id of this Promotion.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Promotion.

        :param id: The id of this Promotion.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Promotion.

        :return: The name of this Promotion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Promotion.

        :param name: The name of this Promotion.
        :type: str
        """

        self._name = name

    @property
    def id_country(self):
        """
        Gets the id_country of this Promotion.

        :return: The id_country of this Promotion.
        :rtype: int
        """
        return self._id_country

    @id_country.setter
    def id_country(self, id_country):
        """
        Sets the id_country of this Promotion.

        :param id_country: The id_country of this Promotion.
        :type: int
        """

        self._id_country = id_country

    @property
    def date_from(self):
        """
        Gets the date_from of this Promotion.
        Promotion starts when this date is reached

        :return: The date_from of this Promotion.
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """
        Sets the date_from of this Promotion.
        Promotion starts when this date is reached

        :param date_from: The date_from of this Promotion.
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """
        Gets the date_to of this Promotion.
        Promotion ends when this date is reached

        :return: The date_to of this Promotion.
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """
        Sets the date_to of this Promotion.
        Promotion ends when this date is reached

        :param date_to: The date_to of this Promotion.
        :type: str
        """

        self._date_to = date_to

    @property
    def date_add(self):
        """
        Gets the date_add of this Promotion.

        :return: The date_add of this Promotion.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this Promotion.

        :param date_add: The date_add of this Promotion.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this Promotion.

        :return: The date_upd of this Promotion.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this Promotion.

        :param date_upd: The date_upd of this Promotion.
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
