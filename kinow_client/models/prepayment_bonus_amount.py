# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PrepaymentBonusAmount(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, prepayment_bonus_id=None, amount=None, amount_formatted=None):
        """
        PrepaymentBonusAmount - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'prepayment_bonus_id': 'int',
            'amount': 'float',
            'amount_formatted': 'str'
        }

        self.attribute_map = {
            'prepayment_bonus_id': 'prepayment_bonus_id',
            'amount': 'amount',
            'amount_formatted': 'amount_formatted'
        }

        self._prepayment_bonus_id = prepayment_bonus_id
        self._amount = amount
        self._amount_formatted = amount_formatted

    @property
    def prepayment_bonus_id(self):
        """
        Gets the prepayment_bonus_id of this PrepaymentBonusAmount.

        :return: The prepayment_bonus_id of this PrepaymentBonusAmount.
        :rtype: int
        """
        return self._prepayment_bonus_id

    @prepayment_bonus_id.setter
    def prepayment_bonus_id(self, prepayment_bonus_id):
        """
        Sets the prepayment_bonus_id of this PrepaymentBonusAmount.

        :param prepayment_bonus_id: The prepayment_bonus_id of this PrepaymentBonusAmount.
        :type: int
        """

        self._prepayment_bonus_id = prepayment_bonus_id

    @property
    def amount(self):
        """
        Gets the amount of this PrepaymentBonusAmount.

        :return: The amount of this PrepaymentBonusAmount.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """
        Sets the amount of this PrepaymentBonusAmount.

        :param amount: The amount of this PrepaymentBonusAmount.
        :type: float
        """

        self._amount = amount

    @property
    def amount_formatted(self):
        """
        Gets the amount_formatted of this PrepaymentBonusAmount.

        :return: The amount_formatted of this PrepaymentBonusAmount.
        :rtype: str
        """
        return self._amount_formatted

    @amount_formatted.setter
    def amount_formatted(self, amount_formatted):
        """
        Sets the amount_formatted of this PrepaymentBonusAmount.

        :param amount_formatted: The amount_formatted of this PrepaymentBonusAmount.
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
