# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Attachment(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, file_name=None, mime=None, url=None, name=None, description=None):
        """
        Attachment - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'file_name': 'str',
            'mime': 'str',
            'url': 'str',
            'name': 'list[I18nField]',
            'description': 'list[I18nField]'
        }

        self.attribute_map = {
            'id': 'id',
            'file_name': 'file_name',
            'mime': 'mime',
            'url': 'url',
            'name': 'name',
            'description': 'description'
        }

        self._id = id
        self._file_name = file_name
        self._mime = mime
        self._url = url
        self._name = name
        self._description = description

    @property
    def id(self):
        """
        Gets the id of this Attachment.

        :return: The id of this Attachment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Attachment.

        :param id: The id of this Attachment.
        :type: int
        """

        self._id = id

    @property
    def file_name(self):
        """
        Gets the file_name of this Attachment.

        :return: The file_name of this Attachment.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """
        Sets the file_name of this Attachment.

        :param file_name: The file_name of this Attachment.
        :type: str
        """

        self._file_name = file_name

    @property
    def mime(self):
        """
        Gets the mime of this Attachment.

        :return: The mime of this Attachment.
        :rtype: str
        """
        return self._mime

    @mime.setter
    def mime(self, mime):
        """
        Sets the mime of this Attachment.

        :param mime: The mime of this Attachment.
        :type: str
        """

        self._mime = mime

    @property
    def url(self):
        """
        Gets the url of this Attachment.

        :return: The url of this Attachment.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Attachment.

        :param url: The url of this Attachment.
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """
        Gets the name of this Attachment.

        :return: The name of this Attachment.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Attachment.

        :param name: The name of this Attachment.
        :type: list[I18nField]
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Attachment.

        :return: The description of this Attachment.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Attachment.

        :param description: The description of this Attachment.
        :type: list[I18nField]
        """

        self._description = description

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
