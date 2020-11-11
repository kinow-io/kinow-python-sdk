# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Player1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, url=None, manifest=None, session_id=None):
        """
        Player1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'manifest': 'object',
            'session_id': 'str'
        }

        self.attribute_map = {
            'url': 'url',
            'manifest': 'manifest',
            'session_id': 'session_id'
        }

        self._url = url
        self._manifest = manifest
        self._session_id = session_id

    @property
    def url(self):
        """
        Gets the url of this Player1.

        :return: The url of this Player1.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Player1.

        :param url: The url of this Player1.
        :type: str
        """

        self._url = url

    @property
    def manifest(self):
        """
        Gets the manifest of this Player1.

        :return: The manifest of this Player1.
        :rtype: object
        """
        return self._manifest

    @manifest.setter
    def manifest(self, manifest):
        """
        Sets the manifest of this Player1.

        :param manifest: The manifest of this Player1.
        :type: object
        """

        self._manifest = manifest

    @property
    def session_id(self):
        """
        Gets the session_id of this Player1.

        :return: The session_id of this Player1.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """
        Sets the session_id of this Player1.

        :param session_id: The session_id of this Player1.
        :type: str
        """

        self._session_id = session_id

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
