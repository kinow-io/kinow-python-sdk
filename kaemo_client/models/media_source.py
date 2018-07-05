# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.50
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class MediaSource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, active=None, external_player=None):
        """
        MediaSource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'active': 'bool',
            'external_player': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'active': 'active',
            'external_player': 'external_player'
        }

        self._id = id
        self._name = name
        self._active = active
        self._external_player = external_player

    @property
    def id(self):
        """
        Gets the id of this MediaSource.

        :return: The id of this MediaSource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MediaSource.

        :param id: The id of this MediaSource.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this MediaSource.

        :return: The name of this MediaSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this MediaSource.

        :param name: The name of this MediaSource.
        :type: str
        """

        self._name = name

    @property
    def active(self):
        """
        Gets the active of this MediaSource.

        :return: The active of this MediaSource.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this MediaSource.

        :param active: The active of this MediaSource.
        :type: bool
        """

        self._active = active

    @property
    def external_player(self):
        """
        Gets the external_player of this MediaSource.

        :return: The external_player of this MediaSource.
        :rtype: int
        """
        return self._external_player

    @external_player.setter
    def external_player(self, external_player):
        """
        Sets the external_player of this MediaSource.

        :param external_player: The external_player of this MediaSource.
        :type: int
        """

        self._external_player = external_player

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
