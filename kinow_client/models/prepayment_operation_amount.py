# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.20
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PrepaymentOperationAmount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, prepayment_operation_id=None, amount=None, amount_formatted=None):
        """
        PrepaymentOperationAmount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'prepayment_operation_id': 'int',
            'amount': 'float',
            'amount_formatted': 'str'
        }

        self.attribute_map = {
            'prepayment_operation_id': 'prepayment_operation_id',
            'amount': 'amount',
            'amount_formatted': 'amount_formatted'
        }

        self._prepayment_operation_id = prepayment_operation_id
        self._amount = amount
        self._amount_formatted = amount_formatted

    @property
    def prepayment_operation_id(self):
        """
        Gets the prepayment_operation_id of this PrepaymentOperationAmount.

        :return: The prepayment_operation_id of this PrepaymentOperationAmount.
        :rtype: int
        """
        return self._prepayment_operation_id

    @prepayment_operation_id.setter
    def prepayment_operation_id(self, prepayment_operation_id):
        """
        Sets the prepayment_operation_id of this PrepaymentOperationAmount.

        :param prepayment_operation_id: The prepayment_operation_id of this PrepaymentOperationAmount.
        :type: int
        """

        self._prepayment_operation_id = prepayment_operation_id

    @property
    def amount(self):
        """
        Gets the amount of this PrepaymentOperationAmount.

        :return: The amount of this PrepaymentOperationAmount.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PrepaymentOperationAmount.

        :param amount: The amount of this PrepaymentOperationAmount.
        :type: float
        """

        self._amount = amount

    @property
    def amount_formatted(self):
        """
        Gets the amount_formatted of this PrepaymentOperationAmount.

        :return: The amount_formatted of this PrepaymentOperationAmount.
        :rtype: str
        """
        return self._amount_formatted

    @amount_formatted.setter
    def amount_formatted(self, amount_formatted):
        """
        Sets the amount_formatted of this PrepaymentOperationAmount.

        :param amount_formatted: The amount_formatted of this PrepaymentOperationAmount.
        :type: str
        """

        self._amount_formatted = amount_formatted

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
