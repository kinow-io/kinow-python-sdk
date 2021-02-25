# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.36
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CredentialsValidation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, valid=None, customer_id=None):
        """
        CredentialsValidation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'valid': 'bool',
            'customer_id': 'int'
        }

        self.attribute_map = {
            'valid': 'valid',
            'customer_id': 'customer_id'
        }

        self._valid = valid
        self._customer_id = customer_id

    @property
    def valid(self):
        """
        Gets the valid of this CredentialsValidation.

        :return: The valid of this CredentialsValidation.
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """
        Sets the valid of this CredentialsValidation.

        :param valid: The valid of this CredentialsValidation.
        :type: bool
        """

        self._valid = valid

    @property
    def customer_id(self):
        """
        Gets the customer_id of this CredentialsValidation.

        :return: The customer_id of this CredentialsValidation.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this CredentialsValidation.

        :param customer_id: The customer_id of this CredentialsValidation.
        :type: int
        """

        self._customer_id = customer_id

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
