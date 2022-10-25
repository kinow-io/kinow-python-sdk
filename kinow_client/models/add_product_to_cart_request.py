# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AddProductToCartRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product_id=None, product_attribute_id=None, gift_id=None, switch_subscription_id=None, is_gift=None, ip_address=None):
        """
        AddProductToCartRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'product_id': 'int',
            'product_attribute_id': 'int',
            'gift_id': 'int',
            'switch_subscription_id': 'int',
            'is_gift': 'bool',
            'ip_address': 'str'
        }

        self.attribute_map = {
            'product_id': 'product_id',
            'product_attribute_id': 'product_attribute_id',
            'gift_id': 'gift_id',
            'switch_subscription_id': 'switch_subscription_id',
            'is_gift': 'is_gift',
            'ip_address': 'ip_address'
        }

        self._product_id = product_id
        self._product_attribute_id = product_attribute_id
        self._gift_id = gift_id
        self._switch_subscription_id = switch_subscription_id
        self._is_gift = is_gift
        self._ip_address = ip_address

    @property
    def product_id(self):
        """
        Gets the product_id of this AddProductToCartRequest.
        Product ID to add to cart

        :return: The product_id of this AddProductToCartRequest.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this AddProductToCartRequest.
        Product ID to add to cart

        :param product_id: The product_id of this AddProductToCartRequest.
        :type: int
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")

        self._product_id = product_id

    @property
    def product_attribute_id(self):
        """
        Gets the product_attribute_id of this AddProductToCartRequest.
        ProductAttribute ID, required to add product to cart if product is not a subscription

        :return: The product_attribute_id of this AddProductToCartRequest.
        :rtype: int
        """
        return self._product_attribute_id

    @product_attribute_id.setter
    def product_attribute_id(self, product_attribute_id):
        """
        Sets the product_attribute_id of this AddProductToCartRequest.
        ProductAttribute ID, required to add product to cart if product is not a subscription

        :param product_attribute_id: The product_attribute_id of this AddProductToCartRequest.
        :type: int
        """

        self._product_attribute_id = product_attribute_id

    @property
    def gift_id(self):
        """
        Gets the gift_id of this AddProductToCartRequest.
        Gift ID linked to the item in cart

        :return: The gift_id of this AddProductToCartRequest.
        :rtype: int
        """
        return self._gift_id

    @gift_id.setter
    def gift_id(self, gift_id):
        """
        Sets the gift_id of this AddProductToCartRequest.
        Gift ID linked to the item in cart

        :param gift_id: The gift_id of this AddProductToCartRequest.
        :type: int
        """

        self._gift_id = gift_id

    @property
    def switch_subscription_id(self):
        """
        Gets the switch_subscription_id of this AddProductToCartRequest.
        When customer want to switch subscription, switch_subscription_id is the product access ID that match with the subscription to cancel

        :return: The switch_subscription_id of this AddProductToCartRequest.
        :rtype: int
        """
        return self._switch_subscription_id

    @switch_subscription_id.setter
    def switch_subscription_id(self, switch_subscription_id):
        """
        Sets the switch_subscription_id of this AddProductToCartRequest.
        When customer want to switch subscription, switch_subscription_id is the product access ID that match with the subscription to cancel

        :param switch_subscription_id: The switch_subscription_id of this AddProductToCartRequest.
        :type: int
        """

        self._switch_subscription_id = switch_subscription_id

    @property
    def is_gift(self):
        """
        Gets the is_gift of this AddProductToCartRequest.
        Allows bypass of access check (in case the current user already bought the product and it cannot be reordered)

        :return: The is_gift of this AddProductToCartRequest.
        :rtype: bool
        """
        return self._is_gift

    @is_gift.setter
    def is_gift(self, is_gift):
        """
        Sets the is_gift of this AddProductToCartRequest.
        Allows bypass of access check (in case the current user already bought the product and it cannot be reordered)

        :param is_gift: The is_gift of this AddProductToCartRequest.
        :type: bool
        """

        self._is_gift = is_gift

    @property
    def ip_address(self):
        """
        Gets the ip_address of this AddProductToCartRequest.
        IP address

        :return: The ip_address of this AddProductToCartRequest.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this AddProductToCartRequest.
        IP address

        :param ip_address: The ip_address of this AddProductToCartRequest.
        :type: str
        """

        self._ip_address = ip_address

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
