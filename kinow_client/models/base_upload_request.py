# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BaseUploadRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, file=None, hash=None, hash_algorithm=None):
        """
        BaseUploadRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'file': 'file',
            'hash': 'str',
            'hash_algorithm': 'str'
        }

        self.attribute_map = {
            'file': 'file',
            'hash': 'hash',
            'hash_algorithm': 'hash_algorithm'
        }

        self._file = file
        self._hash = hash
        self._hash_algorithm = hash_algorithm

    @property
    def file(self):
        """
        Gets the file of this BaseUploadRequest.

        :return: The file of this BaseUploadRequest.
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):
        """
        Sets the file of this BaseUploadRequest.

        :param file: The file of this BaseUploadRequest.
        :type: file
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")

        self._file = file

    @property
    def hash(self):
        """
        Gets the hash of this BaseUploadRequest.

        :return: The hash of this BaseUploadRequest.
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this BaseUploadRequest.

        :param hash: The hash of this BaseUploadRequest.
        :type: str
        """
        if hash is None:
            raise ValueError("Invalid value for `hash`, must not be `None`")

        self._hash = hash

    @property
    def hash_algorithm(self):
        """
        Gets the hash_algorithm of this BaseUploadRequest.
        Hash algorithm to check the hash file (default value is: sha256)

        :return: The hash_algorithm of this BaseUploadRequest.
        :rtype: str
        """
        return self._hash_algorithm

    @hash_algorithm.setter
    def hash_algorithm(self, hash_algorithm):
        """
        Sets the hash_algorithm of this BaseUploadRequest.
        Hash algorithm to check the hash file (default value is: sha256)

        :param hash_algorithm: The hash_algorithm of this BaseUploadRequest.
        :type: str
        """
        allowed_values = ["sha256", "md5"]
        if hash_algorithm not in allowed_values:
            raise ValueError(
                "Invalid value for `hash_algorithm` ({0}), must be one of {1}"
                .format(hash_algorithm, allowed_values)
            )

        self._hash_algorithm = hash_algorithm

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
