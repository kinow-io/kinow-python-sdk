# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PaymentDetailsResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, identifier=None, metadata=None, id_order=None, id_customer=None):
        """
        PaymentDetailsResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'identifier': 'str',
            'metadata': 'str',
            'id_order': 'int',
            'id_customer': 'int'
        }

        self.attribute_map = {
            'identifier': 'identifier',
            'metadata': 'metadata',
            'id_order': 'id_order',
            'id_customer': 'id_customer'
        }

        self._identifier = identifier
        self._metadata = metadata
        self._id_order = id_order
        self._id_customer = id_customer

    @property
    def identifier(self):
        """
        Gets the identifier of this PaymentDetailsResponse.

        :return: The identifier of this PaymentDetailsResponse.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this PaymentDetailsResponse.

        :param identifier: The identifier of this PaymentDetailsResponse.
        :type: str
        """

        self._identifier = identifier

    @property
    def metadata(self):
        """
        Gets the metadata of this PaymentDetailsResponse.

        :return: The metadata of this PaymentDetailsResponse.
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this PaymentDetailsResponse.

        :param metadata: The metadata of this PaymentDetailsResponse.
        :type: str
        """

        self._metadata = metadata

    @property
    def id_order(self):
        """
        Gets the id_order of this PaymentDetailsResponse.

        :return: The id_order of this PaymentDetailsResponse.
        :rtype: int
        """
        return self._id_order

    @id_order.setter
    def id_order(self, id_order):
        """
        Sets the id_order of this PaymentDetailsResponse.

        :param id_order: The id_order of this PaymentDetailsResponse.
        :type: int
        """

        self._id_order = id_order

    @property
    def id_customer(self):
        """
        Gets the id_customer of this PaymentDetailsResponse.

        :return: The id_customer of this PaymentDetailsResponse.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this PaymentDetailsResponse.

        :param id_customer: The id_customer of this PaymentDetailsResponse.
        :type: int
        """

        self._id_customer = id_customer

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
