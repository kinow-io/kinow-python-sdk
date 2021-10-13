# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.54
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductIDList1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product_ids=None, currency_id=None, customer_id=None, iso_code=None):
        """
        ProductIDList1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'product_ids': 'str',
            'currency_id': 'int',
            'customer_id': 'int',
            'iso_code': 'str'
        }

        self.attribute_map = {
            'product_ids': 'product_ids',
            'currency_id': 'currency_id',
            'customer_id': 'customer_id',
            'iso_code': 'iso_code'
        }

        self._product_ids = product_ids
        self._currency_id = currency_id
        self._customer_id = customer_id
        self._iso_code = iso_code

    @property
    def product_ids(self):
        """
        Gets the product_ids of this ProductIDList1.

        :return: The product_ids of this ProductIDList1.
        :rtype: str
        """
        return self._product_ids

    @product_ids.setter
    def product_ids(self, product_ids):
        """
        Sets the product_ids of this ProductIDList1.

        :param product_ids: The product_ids of this ProductIDList1.
        :type: str
        """

        self._product_ids = product_ids

    @property
    def currency_id(self):
        """
        Gets the currency_id of this ProductIDList1.

        :return: The currency_id of this ProductIDList1.
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """
        Sets the currency_id of this ProductIDList1.

        :param currency_id: The currency_id of this ProductIDList1.
        :type: int
        """

        self._currency_id = currency_id

    @property
    def customer_id(self):
        """
        Gets the customer_id of this ProductIDList1.

        :return: The customer_id of this ProductIDList1.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this ProductIDList1.

        :param customer_id: The customer_id of this ProductIDList1.
        :type: int
        """

        self._customer_id = customer_id

    @property
    def iso_code(self):
        """
        Gets the iso_code of this ProductIDList1.
        Required when Customer ID is empty

        :return: The iso_code of this ProductIDList1.
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code):
        """
        Sets the iso_code of this ProductIDList1.
        Required when Customer ID is empty

        :param iso_code: The iso_code of this ProductIDList1.
        :type: str
        """

        self._iso_code = iso_code

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
