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


class AddressResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_customer=None, company=None, address1=None, postcode=None, city=None, id_country=None, id_state=None, date_add=None, date_upd=None):
        """
        AddressResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_customer': 'int',
            'company': 'str',
            'address1': 'str',
            'postcode': 'str',
            'city': 'str',
            'id_country': 'int',
            'id_state': 'int',
            'date_add': 'str',
            'date_upd': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_customer': 'id_customer',
            'company': 'company',
            'address1': 'address1',
            'postcode': 'postcode',
            'city': 'city',
            'id_country': 'id_country',
            'id_state': 'id_state',
            'date_add': 'date_add',
            'date_upd': 'date_upd'
        }

        self._id = id
        self._id_customer = id_customer
        self._company = company
        self._address1 = address1
        self._postcode = postcode
        self._city = city
        self._id_country = id_country
        self._id_state = id_state
        self._date_add = date_add
        self._date_upd = date_upd

    @property
    def id(self):
        """
        Gets the id of this AddressResponse.

        :return: The id of this AddressResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AddressResponse.

        :param id: The id of this AddressResponse.
        :type: int
        """

        self._id = id

    @property
    def id_customer(self):
        """
        Gets the id_customer of this AddressResponse.

        :return: The id_customer of this AddressResponse.
        :rtype: int
        """
        return self._id_customer

    @id_customer.setter
    def id_customer(self, id_customer):
        """
        Sets the id_customer of this AddressResponse.

        :param id_customer: The id_customer of this AddressResponse.
        :type: int
        """

        self._id_customer = id_customer

    @property
    def company(self):
        """
        Gets the company of this AddressResponse.

        :return: The company of this AddressResponse.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this AddressResponse.

        :param company: The company of this AddressResponse.
        :type: str
        """

        self._company = company

    @property
    def address1(self):
        """
        Gets the address1 of this AddressResponse.

        :return: The address1 of this AddressResponse.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this AddressResponse.

        :param address1: The address1 of this AddressResponse.
        :type: str
        """

        self._address1 = address1

    @property
    def postcode(self):
        """
        Gets the postcode of this AddressResponse.

        :return: The postcode of this AddressResponse.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """
        Sets the postcode of this AddressResponse.

        :param postcode: The postcode of this AddressResponse.
        :type: str
        """

        self._postcode = postcode

    @property
    def city(self):
        """
        Gets the city of this AddressResponse.

        :return: The city of this AddressResponse.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this AddressResponse.

        :param city: The city of this AddressResponse.
        :type: str
        """

        self._city = city

    @property
    def id_country(self):
        """
        Gets the id_country of this AddressResponse.

        :return: The id_country of this AddressResponse.
        :rtype: int
        """
        return self._id_country

    @id_country.setter
    def id_country(self, id_country):
        """
        Sets the id_country of this AddressResponse.

        :param id_country: The id_country of this AddressResponse.
        :type: int
        """

        self._id_country = id_country

    @property
    def id_state(self):
        """
        Gets the id_state of this AddressResponse.

        :return: The id_state of this AddressResponse.
        :rtype: int
        """
        return self._id_state

    @id_state.setter
    def id_state(self, id_state):
        """
        Sets the id_state of this AddressResponse.

        :param id_state: The id_state of this AddressResponse.
        :type: int
        """

        self._id_state = id_state

    @property
    def date_add(self):
        """
        Gets the date_add of this AddressResponse.

        :return: The date_add of this AddressResponse.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this AddressResponse.

        :param date_add: The date_add of this AddressResponse.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this AddressResponse.

        :return: The date_upd of this AddressResponse.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this AddressResponse.

        :param date_upd: The date_upd of this AddressResponse.
        :type: str
        """

        self._date_upd = date_upd

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
