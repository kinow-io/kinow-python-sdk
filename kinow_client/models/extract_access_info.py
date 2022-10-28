# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ExtractAccessInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_extract=None, streaming=None, error_code=None):
        """
        ExtractAccessInfo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_extract': 'float',
            'streaming': 'bool',
            'error_code': 'float'
        }

        self.attribute_map = {
            'id_extract': 'id_extract',
            'streaming': 'streaming',
            'error_code': 'error_code'
        }

        self._id_extract = id_extract
        self._streaming = streaming
        self._error_code = error_code

    @property
    def id_extract(self):
        """
        Gets the id_extract of this ExtractAccessInfo.

        :return: The id_extract of this ExtractAccessInfo.
        :rtype: float
        """
        return self._id_extract

    @id_extract.setter
    def id_extract(self, id_extract):
        """
        Sets the id_extract of this ExtractAccessInfo.

        :param id_extract: The id_extract of this ExtractAccessInfo.
        :type: float
        """

        self._id_extract = id_extract

    @property
    def streaming(self):
        """
        Gets the streaming of this ExtractAccessInfo.

        :return: The streaming of this ExtractAccessInfo.
        :rtype: bool
        """
        return self._streaming

    @streaming.setter
    def streaming(self, streaming):
        """
        Sets the streaming of this ExtractAccessInfo.

        :param streaming: The streaming of this ExtractAccessInfo.
        :type: bool
        """

        self._streaming = streaming

    @property
    def error_code(self):
        """
        Gets the error_code of this ExtractAccessInfo.

        :return: The error_code of this ExtractAccessInfo.
        :rtype: float
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this ExtractAccessInfo.

        :param error_code: The error_code of this ExtractAccessInfo.
        :type: float
        """

        self._error_code = error_code

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
