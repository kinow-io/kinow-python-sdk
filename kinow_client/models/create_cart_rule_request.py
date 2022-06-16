# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.11
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateCartRuleRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_customer=None, description=None, priority=None, partial_use=None, code=None, active=None, name=None, date_from=None, date_to=None, quantity=None, quantity_per_user=None, minimum_amount=None, minimum_amount_tax=None, minimum_amount_currency=None, every_recurring_payments=None, reduction_percent=None, reduction_amount=None, reduction_currency=None, reduction_tax=None, restriction_groups=None):
        """
        CreateCartRuleRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_customer': 'int',
            'description': 'str',
            'priority': 'int',
            'partial_use': 'bool',
            'code': 'str',
            'active': 'bool',
            'name': 'list[I18nField]',
            'date_from': 'str',
            'date_to': 'str',
            'quantity': 'int',
            'quantity_per_user': 'int',
            'minimum_amount': 'int',
            'minimum_amount_tax': 'int',
            'minimum_amount_currency': 'int',
            'every_recurring_payments': 'bool',
            'reduction_percent': 'float',
            'reduction_amount': 'float',
            'reduction_currency': 'int',
            'reduction_tax': 'int',
            'restriction_groups': 'list[CartRuleRestrictionGroup]'
        }

        self.attribute_map = {
            'id_customer': 'id_customer',
            'description': 'description',
            'priority': 'priority',
            'partial_use': 'partial_use',
            'code': 'code',
            'active': 'active',
            'name': 'name',
            'date_from': 'date_from',
            'date_to': 'date_to',
            'quantity': 'quantity',
            'quantity_per_user': 'quantity_per_user',
            'minimum_amount': 'minimum_amount',
            'minimum_amount_tax': 'minimum_amount_tax',
            'minimum_amount_currency': 'minimum_amount_currency',
            'every_recurring_payments': 'every_recurring_payments',
            'reduction_percent': 'reduction_percent',
            'reduction_amount': 'reduction_amount',
            'reduction_currency': 'reduction_currency',
            'reduction_tax': 'reduction_tax',
            'restriction_groups': 'restriction_groups'
        }

        self._id_customer = id_customer
        self._description = description
        self._priority = priority
        self._partial_use = partial_use
        self._code = code
        self._active = active
        self._name = name
        self._date_from = date_from
        self._date_to = date_to
        self._quantity = quantity
        self._quantity_per_user = quantity_per_user
        self._minimum_amount = minimum_amount
        self._minimum_amount_tax = minimum_amount_tax
        self._minimum_amount_currency = minimum_amount_currency
        self._every_recurring_payments = every_recurring_payments
        self._reduction_percent = reduction_percent
        self._reduction_amount = reduction_amount
        self._reduction_currency = reduction_currency
        self._reduction_tax = reduction_tax
        self._restriction_groups = restriction_groups

    @property
    def id_customer(self):
        """
        Gets the id_customer of this CreateCartRuleRequest.
        Limit to a single user

        :return: The id_customer of this CreateCartRuleRequest.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this CreateCartRuleRequest.
        Limit to a single user

        :param id_customer: The id_customer of this CreateCartRuleRequest.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def description(self):
        """
        Gets the description of this CreateCartRuleRequest.
        For your eyes only. This will never be displayed to the customer

        :return: The description of this CreateCartRuleRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateCartRuleRequest.
        For your eyes only. This will never be displayed to the customer

        :param description: The description of this CreateCartRuleRequest.
        :type: str
        """

        self._description = description

    @property
    def priority(self):
        """
        Gets the priority of this CreateCartRuleRequest.
        Rules are applied by priority. A rule with a priority of \"1\" will be processed before one with a priority of \"2\"

        :return: The priority of this CreateCartRuleRequest.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this CreateCartRuleRequest.
        Rules are applied by priority. A rule with a priority of \"1\" will be processed before one with a priority of \"2\"

        :param priority: The priority of this CreateCartRuleRequest.
        :type: int
        """

        self._priority = priority

    @property
    def partial_use(self):
        """
        Gets the partial_use of this CreateCartRuleRequest.
        Allow to partial use this cart rule. If cart rule amount is greater than total customer order, a new cart rule will be created with the remainder amount.

        :return: The partial_use of this CreateCartRuleRequest.
        :rtype: bool
        """
        return self._partial_use

    @partial_use.setter
    def partial_use(self, partial_use):
        """
        Sets the partial_use of this CreateCartRuleRequest.
        Allow to partial use this cart rule. If cart rule amount is greater than total customer order, a new cart rule will be created with the remainder amount.

        :param partial_use: The partial_use of this CreateCartRuleRequest.
        :type: bool
        """

        self._partial_use = partial_use

    @property
    def code(self):
        """
        Gets the code of this CreateCartRuleRequest.
        Code used by customer to add it on his cart summary. Caution: rule will automatically be applied to everyone if you leave it blank

        :return: The code of this CreateCartRuleRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this CreateCartRuleRequest.
        Code used by customer to add it on his cart summary. Caution: rule will automatically be applied to everyone if you leave it blank

        :param code: The code of this CreateCartRuleRequest.
        :type: str
        """

        self._code = code

    @property
    def active(self):
        """
        Gets the active of this CreateCartRuleRequest.
        Status of the cart rule

        :return: The active of this CreateCartRuleRequest.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this CreateCartRuleRequest.
        Status of the cart rule

        :param active: The active of this CreateCartRuleRequest.
        :type: bool
        """

        self._active = active

    @property
    def name(self):
        """
        Gets the name of this CreateCartRuleRequest.
        This will be displayed in the cart summary, as well as on the invoice

        :return: The name of this CreateCartRuleRequest.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateCartRuleRequest.
        This will be displayed in the cart summary, as well as on the invoice

        :param name: The name of this CreateCartRuleRequest.
        :type: list[I18nField]
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def date_from(self):
        """
        Gets the date_from of this CreateCartRuleRequest.
        Rule starts when this date is reached

        :return: The date_from of this CreateCartRuleRequest.
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """
        Sets the date_from of this CreateCartRuleRequest.
        Rule starts when this date is reached

        :param date_from: The date_from of this CreateCartRuleRequest.
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """
        Gets the date_to of this CreateCartRuleRequest.
        Rule ends when this date is reached

        :return: The date_to of this CreateCartRuleRequest.
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """
        Sets the date_to of this CreateCartRuleRequest.
        Rule ends when this date is reached

        :param date_to: The date_to of this CreateCartRuleRequest.
        :type: str
        """

        self._date_to = date_to

    @property
    def quantity(self):
        """
        Gets the quantity of this CreateCartRuleRequest.
        The cart rule will be applied to the first \"X\" orders only

        :return: The quantity of this CreateCartRuleRequest.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """
        Sets the quantity of this CreateCartRuleRequest.
        The cart rule will be applied to the first \"X\" orders only

        :param quantity: The quantity of this CreateCartRuleRequest.
        :type: int
        """

        self._quantity = quantity

    @property
    def quantity_per_user(self):
        """
        Gets the quantity_per_user of this CreateCartRuleRequest.
        A customer will only be able to use the cart rule \"X\" time(s)

        :return: The quantity_per_user of this CreateCartRuleRequest.
        :rtype: int
        """
        return self._quantity_per_user

    @quantity_per_user.setter
    def quantity_per_user(self, quantity_per_user):
        """
        Sets the quantity_per_user of this CreateCartRuleRequest.
        A customer will only be able to use the cart rule \"X\" time(s)

        :param quantity_per_user: The quantity_per_user of this CreateCartRuleRequest.
        :type: int
        """

        self._quantity_per_user = quantity_per_user

    @property
    def minimum_amount(self):
        """
        Gets the minimum_amount of this CreateCartRuleRequest.
        You can choose a minimum amount for the cart, either with taxes or not

        :return: The minimum_amount of this CreateCartRuleRequest.
        :rtype: int
        """
        return self._minimum_amount

    @minimum_amount.setter
    def minimum_amount(self, minimum_amount):
        """
        Sets the minimum_amount of this CreateCartRuleRequest.
        You can choose a minimum amount for the cart, either with taxes or not

        :param minimum_amount: The minimum_amount of this CreateCartRuleRequest.
        :type: int
        """

        self._minimum_amount = minimum_amount

    @property
    def minimum_amount_tax(self):
        """
        Gets the minimum_amount_tax of this CreateCartRuleRequest.

        :return: The minimum_amount_tax of this CreateCartRuleRequest.
        :rtype: int
        """
        return self._minimum_amount_tax

    @minimum_amount_tax.setter
    def minimum_amount_tax(self, minimum_amount_tax):
        """
        Sets the minimum_amount_tax of this CreateCartRuleRequest.

        :param minimum_amount_tax: The minimum_amount_tax of this CreateCartRuleRequest.
        :type: int
        """

        self._minimum_amount_tax = minimum_amount_tax

    @property
    def minimum_amount_currency(self):
        """
        Gets the minimum_amount_currency of this CreateCartRuleRequest.
        Currency ID

        :return: The minimum_amount_currency of this CreateCartRuleRequest.
        :rtype: int
        """
        return self._minimum_amount_currency

    @minimum_amount_currency.setter
    def minimum_amount_currency(self, minimum_amount_currency):
        """
        Sets the minimum_amount_currency of this CreateCartRuleRequest.
        Currency ID

        :param minimum_amount_currency: The minimum_amount_currency of this CreateCartRuleRequest.
        :type: int
        """

        self._minimum_amount_currency = minimum_amount_currency

    @property
    def every_recurring_payments(self):
        """
        Gets the every_recurring_payments of this CreateCartRuleRequest.
        If customer cart contains a subscription, select if cart rule will apply on recurring payments

        :return: The every_recurring_payments of this CreateCartRuleRequest.
        :rtype: bool
        """
        return self._every_recurring_payments

    @every_recurring_payments.setter
    def every_recurring_payments(self, every_recurring_payments):
        """
        Sets the every_recurring_payments of this CreateCartRuleRequest.
        If customer cart contains a subscription, select if cart rule will apply on recurring payments

        :param every_recurring_payments: The every_recurring_payments of this CreateCartRuleRequest.
        :type: bool
        """

        self._every_recurring_payments = every_recurring_payments

    @property
    def reduction_percent(self):
        """
        Gets the reduction_percent of this CreateCartRuleRequest.
        Discount applied to cart when rule is added (in %).

        :return: The reduction_percent of this CreateCartRuleRequest.
        :rtype: float
        """
        return self._reduction_percent

    @reduction_percent.setter
    def reduction_percent(self, reduction_percent):
        """
        Sets the reduction_percent of this CreateCartRuleRequest.
        Discount applied to cart when rule is added (in %).

        :param reduction_percent: The reduction_percent of this CreateCartRuleRequest.
        :type: float
        """

        self._reduction_percent = reduction_percent

    @property
    def reduction_amount(self):
        """
        Gets the reduction_amount of this CreateCartRuleRequest.
        Discount applied to cart when rule is added (in currency)

        :return: The reduction_amount of this CreateCartRuleRequest.
        :rtype: float
        """
        return self._reduction_amount

    @reduction_amount.setter
    def reduction_amount(self, reduction_amount):
        """
        Sets the reduction_amount of this CreateCartRuleRequest.
        Discount applied to cart when rule is added (in currency)

        :param reduction_amount: The reduction_amount of this CreateCartRuleRequest.
        :type: float
        """

        self._reduction_amount = reduction_amount

    @property
    def reduction_currency(self):
        """
        Gets the reduction_currency of this CreateCartRuleRequest.
        Currency ID for reduction amount

        :return: The reduction_currency of this CreateCartRuleRequest.
        :rtype: int
        """
        return self._reduction_currency

    @reduction_currency.setter
    def reduction_currency(self, reduction_currency):
        """
        Sets the reduction_currency of this CreateCartRuleRequest.
        Currency ID for reduction amount

        :param reduction_currency: The reduction_currency of this CreateCartRuleRequest.
        :type: int
        """

        self._reduction_currency = reduction_currency

    @property
    def reduction_tax(self):
        """
        Gets the reduction_tax of this CreateCartRuleRequest.
        Tax application for currency discount

        :return: The reduction_tax of this CreateCartRuleRequest.
        :rtype: int
        """
        return self._reduction_tax

    @reduction_tax.setter
    def reduction_tax(self, reduction_tax):
        """
        Sets the reduction_tax of this CreateCartRuleRequest.
        Tax application for currency discount

        :param reduction_tax: The reduction_tax of this CreateCartRuleRequest.
        :type: int
        """

        self._reduction_tax = reduction_tax

    @property
    def restriction_groups(self):
        """
        Gets the restriction_groups of this CreateCartRuleRequest.

        :return: The restriction_groups of this CreateCartRuleRequest.
        :rtype: list[CartRuleRestrictionGroup]
        """
        return self._restriction_groups

    @restriction_groups.setter
    def restriction_groups(self, restriction_groups):
        """
        Sets the restriction_groups of this CreateCartRuleRequest.

        :param restriction_groups: The restriction_groups of this CreateCartRuleRequest.
        :type: list[CartRuleRestrictionGroup]
        """

        self._restriction_groups = restriction_groups

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
