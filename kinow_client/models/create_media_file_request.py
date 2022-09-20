# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateMediaFileRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, filename=None, title=None, cover=None, thumbnail=None, details=None):
        """
        CreateMediaFileRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'filename': 'str',
            'title': 'str',
            'cover': 'str',
            'thumbnail': 'str',
            'details': 'str'
        }

        self.attribute_map = {
            'filename': 'filename',
            'title': 'title',
            'cover': 'cover',
            'thumbnail': 'thumbnail',
            'details': 'details'
        }

        self._filename = filename
        self._title = title
        self._cover = cover
        self._thumbnail = thumbnail
        self._details = details

    @property
    def filename(self):
        """
        Gets the filename of this CreateMediaFileRequest.

        :return: The filename of this CreateMediaFileRequest.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this CreateMediaFileRequest.

        :param filename: The filename of this CreateMediaFileRequest.
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")

        self._filename = filename

    @property
    def title(self):
        """
        Gets the title of this CreateMediaFileRequest.

        :return: The title of this CreateMediaFileRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this CreateMediaFileRequest.

        :param title: The title of this CreateMediaFileRequest.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def cover(self):
        """
        Gets the cover of this CreateMediaFileRequest.

        :return: The cover of this CreateMediaFileRequest.
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """
        Sets the cover of this CreateMediaFileRequest.

        :param cover: The cover of this CreateMediaFileRequest.
        :type: str
        """

        self._cover = cover

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this CreateMediaFileRequest.

        :return: The thumbnail of this CreateMediaFileRequest.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this CreateMediaFileRequest.

        :param thumbnail: The thumbnail of this CreateMediaFileRequest.
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def details(self):
        """
        Gets the details of this CreateMediaFileRequest.

        :return: The details of this CreateMediaFileRequest.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this CreateMediaFileRequest.

        :param details: The details of this CreateMediaFileRequest.
        :type: str
        """

        self._details = details

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
