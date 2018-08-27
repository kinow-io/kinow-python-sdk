# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.54
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PlayerConfiguration(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, url=None, html=None, conf=None):
        """
        PlayerConfiguration - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'html': 'object',
            'conf': 'object'
        }

        self.attribute_map = {
            'url': 'url',
            'html': 'html',
            'conf': 'conf'
        }

        self._url = url
        self._html = html
        self._conf = conf

    @property
    def url(self):
        """
        Gets the url of this PlayerConfiguration.

        :return: The url of this PlayerConfiguration.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this PlayerConfiguration.

        :param url: The url of this PlayerConfiguration.
        :type: str
        """

        self._url = url

    @property
    def html(self):
        """
        Gets the html of this PlayerConfiguration.

        :return: The html of this PlayerConfiguration.
        :rtype: object
        """
        return self._html

    @html.setter
    def html(self, html):
        """
        Sets the html of this PlayerConfiguration.

        :param html: The html of this PlayerConfiguration.
        :type: object
        """

        self._html = html

    @property
    def conf(self):
        """
        Gets the conf of this PlayerConfiguration.

        :return: The conf of this PlayerConfiguration.
        :rtype: object
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        """
        Sets the conf of this PlayerConfiguration.

        :param conf: The conf of this PlayerConfiguration.
        :type: object
        """

        self._conf = conf

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
