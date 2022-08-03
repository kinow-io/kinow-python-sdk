# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.16
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OrderStateResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, paid=None, deleted=None, name=None):
        """
        OrderStateResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'paid': 'bool',
            'deleted': 'bool',
            'name': 'list[I18nField]'
        }

        self.attribute_map = {
            'id': 'id',
            'paid': 'paid',
            'deleted': 'deleted',
            'name': 'name'
        }

        self._id = id
        self._paid = paid
        self._deleted = deleted
        self._name = name

    @property
    def id(self):
        """
        Gets the id of this OrderStateResponse.

        :return: The id of this OrderStateResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrderStateResponse.

        :param id: The id of this OrderStateResponse.
        :type: int
        """

        self._id = id

    @property
    def paid(self):
        """
        Gets the paid of this OrderStateResponse.

        :return: The paid of this OrderStateResponse.
        :rtype: bool
        """
        return self._paid

    @paid.setter
    def paid(self, paid):
        """
        Sets the paid of this OrderStateResponse.

        :param paid: The paid of this OrderStateResponse.
        :type: bool
        """

        self._paid = paid

    @property
    def deleted(self):
        """
        Gets the deleted of this OrderStateResponse.

        :return: The deleted of this OrderStateResponse.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """
        Sets the deleted of this OrderStateResponse.

        :param deleted: The deleted of this OrderStateResponse.
        :type: bool
        """

        self._deleted = deleted

    @property
    def name(self):
        """
        Gets the name of this OrderStateResponse.

        :return: The name of this OrderStateResponse.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrderStateResponse.

        :param name: The name of this OrderStateResponse.
        :type: list[I18nField]
        """

        self._name = name

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
