# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class OrderResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_order_renew=None, id_cart=None, id_currency=None, id_customer=None, current_state=None, payment=None, module=None, total_discounts=None, total_discounts_tax_incl=None, total_discounts_tax_excl=None, total_paid=None, total_paid_tax_incl=None, total_paid_tax_excl=None, total_products=None, total_products_wt=None, conversion_rate=None, invoice_number=None, invoice_date=None, valid=None, reference=None, date_add=None, date_upd=None, histories=None):
        """
        OrderResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_order_renew': 'int',
            'id_cart': 'int',
            'id_currency': 'int',
            'id_customer': 'int',
            'current_state': 'int',
            'payment': 'str',
            'module': 'str',
            'total_discounts': 'float',
            'total_discounts_tax_incl': 'float',
            'total_discounts_tax_excl': 'float',
            'total_paid': 'float',
            'total_paid_tax_incl': 'float',
            'total_paid_tax_excl': 'float',
            'total_products': 'float',
            'total_products_wt': 'float',
            'conversion_rate': 'float',
            'invoice_number': 'int',
            'invoice_date': 'str',
            'valid': 'bool',
            'reference': 'str',
            'date_add': 'str',
            'date_upd': 'str',
            'histories': 'list[OrderHistory]'
        }

        self.attribute_map = {
            'id': 'id',
            'id_order_renew': 'id_order_renew',
            'id_cart': 'id_cart',
            'id_currency': 'id_currency',
            'id_customer': 'id_customer',
            'current_state': 'current_state',
            'payment': 'payment',
            'module': 'module',
            'total_discounts': 'total_discounts',
            'total_discounts_tax_incl': 'total_discounts_tax_incl',
            'total_discounts_tax_excl': 'total_discounts_tax_excl',
            'total_paid': 'total_paid',
            'total_paid_tax_incl': 'total_paid_tax_incl',
            'total_paid_tax_excl': 'total_paid_tax_excl',
            'total_products': 'total_products',
            'total_products_wt': 'total_products_wt',
            'conversion_rate': 'conversion_rate',
            'invoice_number': 'invoice_number',
            'invoice_date': 'invoice_date',
            'valid': 'valid',
            'reference': 'reference',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'histories': 'histories'
        }

        self._id = id
        self._id_order_renew = id_order_renew
        self._id_cart = id_cart
        self._id_currency = id_currency
        self._id_customer = id_customer
        self._current_state = current_state
        self._payment = payment
        self._module = module
        self._total_discounts = total_discounts
        self._total_discounts_tax_incl = total_discounts_tax_incl
        self._total_discounts_tax_excl = total_discounts_tax_excl
        self._total_paid = total_paid
        self._total_paid_tax_incl = total_paid_tax_incl
        self._total_paid_tax_excl = total_paid_tax_excl
        self._total_products = total_products
        self._total_products_wt = total_products_wt
        self._conversion_rate = conversion_rate
        self._invoice_number = invoice_number
        self._invoice_date = invoice_date
        self._valid = valid
        self._reference = reference
        self._date_add = date_add
        self._date_upd = date_upd
        self._histories = histories

    @property
    def id(self):
        """
        Gets the id of this OrderResponse.

        :return: The id of this OrderResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OrderResponse.

        :param id: The id of this OrderResponse.
        :type: int
        """

        self._id = id

    @property
    def id_order_renew(self):
        """
        Gets the id_order_renew of this OrderResponse.

        :return: The id_order_renew of this OrderResponse.
        :rtype: int
        """
        return self._id_order_renew

    @id_order_renew.setter
    def id_order_renew(self, id_order_renew):
        """
        Sets the id_order_renew of this OrderResponse.

        :param id_order_renew: The id_order_renew of this OrderResponse.
        :type: int
        """

        self._id_order_renew = id_order_renew

    @property
    def id_cart(self):
        """
        Gets the id_cart of this OrderResponse.

        :return: The id_cart of this OrderResponse.
        :rtype: int
        """
        return self._id_cart

    @id_cart.setter
    def id_cart(self, id_cart):
        """
        Sets the id_cart of this OrderResponse.

        :param id_cart: The id_cart of this OrderResponse.
        :type: int
        """

        self._id_cart = id_cart

    @property
    def id_currency(self):
        """
        Gets the id_currency of this OrderResponse.

        :return: The id_currency of this OrderResponse.
        :rtype: int
        """
        return self._id_currency

    @id_currency.setter
    def id_currency(self, id_currency):
        """
        Sets the id_currency of this OrderResponse.

        :param id_currency: The id_currency of this OrderResponse.
        :type: int
        """

        self._id_currency = id_currency

    @property
    def id_customer(self):
        """
        Gets the id_customer of this OrderResponse.

        :return: The id_customer of this OrderResponse.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this OrderResponse.

        :param id_customer: The id_customer of this OrderResponse.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def current_state(self):
        """
        Gets the current_state of this OrderResponse.

        :return: The current_state of this OrderResponse.
        :rtype: int
        """
        return self._current_state

    @current_state.setter
    def current_state(self, current_state):
        """
        Sets the current_state of this OrderResponse.

        :param current_state: The current_state of this OrderResponse.
        :type: int
        """

        self._current_state = current_state

    @property
    def payment(self):
        """
        Gets the payment of this OrderResponse.

        :return: The payment of this OrderResponse.
        :rtype: str
        """
        return self._payment

    @payment.setter
    def payment(self, payment):
        """
        Sets the payment of this OrderResponse.

        :param payment: The payment of this OrderResponse.
        :type: str
        """

        self._payment = payment

    @property
    def module(self):
        """
        Gets the module of this OrderResponse.

        :return: The module of this OrderResponse.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module):
        """
        Sets the module of this OrderResponse.

        :param module: The module of this OrderResponse.
        :type: str
        """

        self._module = module

    @property
    def total_discounts(self):
        """
        Gets the total_discounts of this OrderResponse.

        :return: The total_discounts of this OrderResponse.
        :rtype: float
        """
        return self._total_discounts

    @total_discounts.setter
    def total_discounts(self, total_discounts):
        """
        Sets the total_discounts of this OrderResponse.

        :param total_discounts: The total_discounts of this OrderResponse.
        :type: float
        """

        self._total_discounts = total_discounts

    @property
    def total_discounts_tax_incl(self):
        """
        Gets the total_discounts_tax_incl of this OrderResponse.

        :return: The total_discounts_tax_incl of this OrderResponse.
        :rtype: float
        """
        return self._total_discounts_tax_incl

    @total_discounts_tax_incl.setter
    def total_discounts_tax_incl(self, total_discounts_tax_incl):
        """
        Sets the total_discounts_tax_incl of this OrderResponse.

        :param total_discounts_tax_incl: The total_discounts_tax_incl of this OrderResponse.
        :type: float
        """

        self._total_discounts_tax_incl = total_discounts_tax_incl

    @property
    def total_discounts_tax_excl(self):
        """
        Gets the total_discounts_tax_excl of this OrderResponse.

        :return: The total_discounts_tax_excl of this OrderResponse.
        :rtype: float
        """
        return self._total_discounts_tax_excl

    @total_discounts_tax_excl.setter
    def total_discounts_tax_excl(self, total_discounts_tax_excl):
        """
        Sets the total_discounts_tax_excl of this OrderResponse.

        :param total_discounts_tax_excl: The total_discounts_tax_excl of this OrderResponse.
        :type: float
        """

        self._total_discounts_tax_excl = total_discounts_tax_excl

    @property
    def total_paid(self):
        """
        Gets the total_paid of this OrderResponse.

        :return: The total_paid of this OrderResponse.
        :rtype: float
        """
        return self._total_paid

    @total_paid.setter
    def total_paid(self, total_paid):
        """
        Sets the total_paid of this OrderResponse.

        :param total_paid: The total_paid of this OrderResponse.
        :type: float
        """

        self._total_paid = total_paid

    @property
    def total_paid_tax_incl(self):
        """
        Gets the total_paid_tax_incl of this OrderResponse.

        :return: The total_paid_tax_incl of this OrderResponse.
        :rtype: float
        """
        return self._total_paid_tax_incl

    @total_paid_tax_incl.setter
    def total_paid_tax_incl(self, total_paid_tax_incl):
        """
        Sets the total_paid_tax_incl of this OrderResponse.

        :param total_paid_tax_incl: The total_paid_tax_incl of this OrderResponse.
        :type: float
        """

        self._total_paid_tax_incl = total_paid_tax_incl

    @property
    def total_paid_tax_excl(self):
        """
        Gets the total_paid_tax_excl of this OrderResponse.

        :return: The total_paid_tax_excl of this OrderResponse.
        :rtype: float
        """
        return self._total_paid_tax_excl

    @total_paid_tax_excl.setter
    def total_paid_tax_excl(self, total_paid_tax_excl):
        """
        Sets the total_paid_tax_excl of this OrderResponse.

        :param total_paid_tax_excl: The total_paid_tax_excl of this OrderResponse.
        :type: float
        """

        self._total_paid_tax_excl = total_paid_tax_excl

    @property
    def total_products(self):
        """
        Gets the total_products of this OrderResponse.

        :return: The total_products of this OrderResponse.
        :rtype: float
        """
        return self._total_products

    @total_products.setter
    def total_products(self, total_products):
        """
        Sets the total_products of this OrderResponse.

        :param total_products: The total_products of this OrderResponse.
        :type: float
        """

        self._total_products = total_products

    @property
    def total_products_wt(self):
        """
        Gets the total_products_wt of this OrderResponse.

        :return: The total_products_wt of this OrderResponse.
        :rtype: float
        """
        return self._total_products_wt

    @total_products_wt.setter
    def total_products_wt(self, total_products_wt):
        """
        Sets the total_products_wt of this OrderResponse.

        :param total_products_wt: The total_products_wt of this OrderResponse.
        :type: float
        """

        self._total_products_wt = total_products_wt

    @property
    def conversion_rate(self):
        """
        Gets the conversion_rate of this OrderResponse.

        :return: The conversion_rate of this OrderResponse.
        :rtype: float
        """
        return self._conversion_rate

    @conversion_rate.setter
    def conversion_rate(self, conversion_rate):
        """
        Sets the conversion_rate of this OrderResponse.

        :param conversion_rate: The conversion_rate of this OrderResponse.
        :type: float
        """

        self._conversion_rate = conversion_rate

    @property
    def invoice_number(self):
        """
        Gets the invoice_number of this OrderResponse.

        :return: The invoice_number of this OrderResponse.
        :rtype: int
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """
        Sets the invoice_number of this OrderResponse.

        :param invoice_number: The invoice_number of this OrderResponse.
        :type: int
        """

        self._invoice_number = invoice_number

    @property
    def invoice_date(self):
        """
        Gets the invoice_date of this OrderResponse.

        :return: The invoice_date of this OrderResponse.
        :rtype: str
        """
        return self._invoice_date

    @invoice_date.setter
    def invoice_date(self, invoice_date):
        """
        Sets the invoice_date of this OrderResponse.

        :param invoice_date: The invoice_date of this OrderResponse.
        :type: str
        """

        self._invoice_date = invoice_date

    @property
    def valid(self):
        """
        Gets the valid of this OrderResponse.

        :return: The valid of this OrderResponse.
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """
        Sets the valid of this OrderResponse.

        :param valid: The valid of this OrderResponse.
        :type: bool
        """

        self._valid = valid

    @property
    def reference(self):
        """
        Gets the reference of this OrderResponse.

        :return: The reference of this OrderResponse.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this OrderResponse.

        :param reference: The reference of this OrderResponse.
        :type: str
        """

        self._reference = reference

    @property
    def date_add(self):
        """
        Gets the date_add of this OrderResponse.

        :return: The date_add of this OrderResponse.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this OrderResponse.

        :param date_add: The date_add of this OrderResponse.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this OrderResponse.

        :return: The date_upd of this OrderResponse.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this OrderResponse.

        :param date_upd: The date_upd of this OrderResponse.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def histories(self):
        """
        Gets the histories of this OrderResponse.

        :return: The histories of this OrderResponse.
        :rtype: list[OrderHistory]
        """
        return self._histories

    @histories.setter
    def histories(self, histories):
        """
        Sets the histories of this OrderResponse.

        :param histories: The histories of this OrderResponse.
        :type: list[OrderHistory]
        """

        self._histories = histories

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
