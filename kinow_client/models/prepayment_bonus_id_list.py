# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PrepaymentBonusIDList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, prepayment_bonus_ids=None, currency_id=None):
        """
        PrepaymentBonusIDList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'prepayment_bonus_ids': 'str',
            'currency_id': 'int'
        }

        self.attribute_map = {
            'prepayment_bonus_ids': 'prepayment_bonus_ids',
            'currency_id': 'currency_id'
        }

        self._prepayment_bonus_ids = prepayment_bonus_ids
        self._currency_id = currency_id

    @property
    def prepayment_bonus_ids(self):
        """
        Gets the prepayment_bonus_ids of this PrepaymentBonusIDList.

        :return: The prepayment_bonus_ids of this PrepaymentBonusIDList.
        :rtype: str
        """
        return self._prepayment_bonus_ids

    @prepayment_bonus_ids.setter
    def prepayment_bonus_ids(self, prepayment_bonus_ids):
        """
        Sets the prepayment_bonus_ids of this PrepaymentBonusIDList.

        :param prepayment_bonus_ids: The prepayment_bonus_ids of this PrepaymentBonusIDList.
        :type: str
        """

        self._prepayment_bonus_ids = prepayment_bonus_ids

    @property
    def currency_id(self):
        """
        Gets the currency_id of this PrepaymentBonusIDList.

        :return: The currency_id of this PrepaymentBonusIDList.
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """
        Sets the currency_id of this PrepaymentBonusIDList.

        :param currency_id: The currency_id of this PrepaymentBonusIDList.
        :type: int
        """

        self._currency_id = currency_id

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
