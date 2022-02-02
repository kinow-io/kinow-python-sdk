# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CartPrice(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, cart_id=None, total_without_tax=None, total_tax=None, total_discount=None, total_trial=None, total=None, total_without_tax_formatted=None, total_tax_formatted=None, total_discount_formatted=None, total_trial_formatted=None, total_formatted=None, taxes=None):
        """
        CartPrice - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cart_id': 'int',
            'total_without_tax': 'float',
            'total_tax': 'float',
            'total_discount': 'float',
            'total_trial': 'float',
            'total': 'float',
            'total_without_tax_formatted': 'str',
            'total_tax_formatted': 'str',
            'total_discount_formatted': 'str',
            'total_trial_formatted': 'str',
            'total_formatted': 'str',
            'taxes': 'list[TaxPrice]'
        }

        self.attribute_map = {
            'cart_id': 'cart_id',
            'total_without_tax': 'total_without_tax',
            'total_tax': 'total_tax',
            'total_discount': 'total_discount',
            'total_trial': 'total_trial',
            'total': 'total',
            'total_without_tax_formatted': 'total_without_tax_formatted',
            'total_tax_formatted': 'total_tax_formatted',
            'total_discount_formatted': 'total_discount_formatted',
            'total_trial_formatted': 'total_trial_formatted',
            'total_formatted': 'total_formatted',
            'taxes': 'taxes'
        }

        self._cart_id = cart_id
        self._total_without_tax = total_without_tax
        self._total_tax = total_tax
        self._total_discount = total_discount
        self._total_trial = total_trial
        self._total = total
        self._total_without_tax_formatted = total_without_tax_formatted
        self._total_tax_formatted = total_tax_formatted
        self._total_discount_formatted = total_discount_formatted
        self._total_trial_formatted = total_trial_formatted
        self._total_formatted = total_formatted
        self._taxes = taxes

    @property
    def cart_id(self):
        """
        Gets the cart_id of this CartPrice.

        :return: The cart_id of this CartPrice.
        :rtype: int
        """
        return self._cart_id

    @cart_id.setter
    def cart_id(self, cart_id):
        """
        Sets the cart_id of this CartPrice.

        :param cart_id: The cart_id of this CartPrice.
        :type: int
        """

        self._cart_id = cart_id

    @property
    def total_without_tax(self):
        """
        Gets the total_without_tax of this CartPrice.

        :return: The total_without_tax of this CartPrice.
        :rtype: float
        """
        return self._total_without_tax

    @total_without_tax.setter
    def total_without_tax(self, total_without_tax):
        """
        Sets the total_without_tax of this CartPrice.

        :param total_without_tax: The total_without_tax of this CartPrice.
        :type: float
        """

        self._total_without_tax = total_without_tax

    @property
    def total_tax(self):
        """
        Gets the total_tax of this CartPrice.

        :return: The total_tax of this CartPrice.
        :rtype: float
        """
        return self._total_tax

    @total_tax.setter
    def total_tax(self, total_tax):
        """
        Sets the total_tax of this CartPrice.

        :param total_tax: The total_tax of this CartPrice.
        :type: float
        """

        self._total_tax = total_tax

    @property
    def total_discount(self):
        """
        Gets the total_discount of this CartPrice.

        :return: The total_discount of this CartPrice.
        :rtype: float
        """
        return self._total_discount

    @total_discount.setter
    def total_discount(self, total_discount):
        """
        Sets the total_discount of this CartPrice.

        :param total_discount: The total_discount of this CartPrice.
        :type: float
        """

        self._total_discount = total_discount

    @property
    def total_trial(self):
        """
        Gets the total_trial of this CartPrice.

        :return: The total_trial of this CartPrice.
        :rtype: float
        """
        return self._total_trial

    @total_trial.setter
    def total_trial(self, total_trial):
        """
        Sets the total_trial of this CartPrice.

        :param total_trial: The total_trial of this CartPrice.
        :type: float
        """

        self._total_trial = total_trial

    @property
    def total(self):
        """
        Gets the total of this CartPrice.

        :return: The total of this CartPrice.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """
        Sets the total of this CartPrice.

        :param total: The total of this CartPrice.
        :type: float
        """

        self._total = total

    @property
    def total_without_tax_formatted(self):
        """
        Gets the total_without_tax_formatted of this CartPrice.

        :return: The total_without_tax_formatted of this CartPrice.
        :rtype: str
        """
        return self._total_without_tax_formatted

    @total_without_tax_formatted.setter
    def total_without_tax_formatted(self, total_without_tax_formatted):
        """
        Sets the total_without_tax_formatted of this CartPrice.

        :param total_without_tax_formatted: The total_without_tax_formatted of this CartPrice.
        :type: str
        """

        self._total_without_tax_formatted = total_without_tax_formatted

    @property
    def total_tax_formatted(self):
        """
        Gets the total_tax_formatted of this CartPrice.

        :return: The total_tax_formatted of this CartPrice.
        :rtype: str
        """
        return self._total_tax_formatted

    @total_tax_formatted.setter
    def total_tax_formatted(self, total_tax_formatted):
        """
        Sets the total_tax_formatted of this CartPrice.

        :param total_tax_formatted: The total_tax_formatted of this CartPrice.
        :type: str
        """

        self._total_tax_formatted = total_tax_formatted

    @property
    def total_discount_formatted(self):
        """
        Gets the total_discount_formatted of this CartPrice.

        :return: The total_discount_formatted of this CartPrice.
        :rtype: str
        """
        return self._total_discount_formatted

    @total_discount_formatted.setter
    def total_discount_formatted(self, total_discount_formatted):
        """
        Sets the total_discount_formatted of this CartPrice.

        :param total_discount_formatted: The total_discount_formatted of this CartPrice.
        :type: str
        """

        self._total_discount_formatted = total_discount_formatted

    @property
    def total_trial_formatted(self):
        """
        Gets the total_trial_formatted of this CartPrice.

        :return: The total_trial_formatted of this CartPrice.
        :rtype: str
        """
        return self._total_trial_formatted

    @total_trial_formatted.setter
    def total_trial_formatted(self, total_trial_formatted):
        """
        Sets the total_trial_formatted of this CartPrice.

        :param total_trial_formatted: The total_trial_formatted of this CartPrice.
        :type: str
        """

        self._total_trial_formatted = total_trial_formatted

    @property
    def total_formatted(self):
        """
        Gets the total_formatted of this CartPrice.

        :return: The total_formatted of this CartPrice.
        :rtype: str
        """
        return self._total_formatted

    @total_formatted.setter
    def total_formatted(self, total_formatted):
        """
        Sets the total_formatted of this CartPrice.

        :param total_formatted: The total_formatted of this CartPrice.
        :type: str
        """

        self._total_formatted = total_formatted

    @property
    def taxes(self):
        """
        Gets the taxes of this CartPrice.

        :return: The taxes of this CartPrice.
        :rtype: list[TaxPrice]
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """
        Sets the taxes of this CartPrice.

        :param taxes: The taxes of this CartPrice.
        :type: list[TaxPrice]
        """

        self._taxes = taxes

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
