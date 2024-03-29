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


class LogoSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, url=None, favicon_16=None):
        """
        LogoSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'favicon_16': 'str'
        }

        self.attribute_map = {
            'url': 'url',
            'favicon_16': 'favicon_16'
        }

        self._url = url
        self._favicon_16 = favicon_16

    @property
    def url(self):
        """
        Gets the url of this LogoSettings.

        :return: The url of this LogoSettings.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this LogoSettings.

        :param url: The url of this LogoSettings.
        :type: str
        """

        self._url = url

    @property
    def favicon_16(self):
        """
        Gets the favicon_16 of this LogoSettings.

        :return: The favicon_16 of this LogoSettings.
        :rtype: str
        """
        return self._favicon_16

    @favicon_16.setter
    def favicon_16(self, favicon_16):
        """
        Sets the favicon_16 of this LogoSettings.

        :param favicon_16: The favicon_16 of this LogoSettings.
        :type: str
        """

        self._favicon_16 = favicon_16

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
