# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Address1(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, company=None, address1=None, postcode=None, city=None, id_state=None, id_country=None):
        """
        Address1 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'company': 'str',
            'address1': 'str',
            'postcode': 'str',
            'city': 'str',
            'id_state': 'int',
            'id_country': 'int'
        }

        self.attribute_map = {
            'company': 'company',
            'address1': 'address1',
            'postcode': 'postcode',
            'city': 'city',
            'id_state': 'id_state',
            'id_country': 'id_country'
        }

        self._company = company
        self._address1 = address1
        self._postcode = postcode
        self._city = city
        self._id_state = id_state
        self._id_country = id_country

    @property
    def company(self):
        """
        Gets the company of this Address1.
        Company

        :return: The company of this Address1.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this Address1.
        Company

        :param company: The company of this Address1.
        :type: str
        """

        self._company = company

    @property
    def address1(self):
        """
        Gets the address1 of this Address1.
        Address

        :return: The address1 of this Address1.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Address1.
        Address

        :param address1: The address1 of this Address1.
        :type: str
        """

        self._address1 = address1

    @property
    def postcode(self):
        """
        Gets the postcode of this Address1.
        Postcode

        :return: The postcode of this Address1.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """
        Sets the postcode of this Address1.
        Postcode

        :param postcode: The postcode of this Address1.
        :type: str
        """

        self._postcode = postcode

    @property
    def city(self):
        """
        Gets the city of this Address1.
        City

        :return: The city of this Address1.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Address1.
        City

        :param city: The city of this Address1.
        :type: str
        """

        self._city = city

    @property
    def id_state(self):
        """
        Gets the id_state of this Address1.
        State ID

        :return: The id_state of this Address1.
        :rtype: int
        """
        return self._id_state

    @id_state.setter
    def id_state(self, id_state):
        """
        Sets the id_state of this Address1.
        State ID

        :param id_state: The id_state of this Address1.
        :type: int
        """

        self._id_state = id_state

    @property
    def id_country(self):
        """
        Gets the id_country of this Address1.
        Country ID

        :return: The id_country of this Address1.
        :rtype: int
        """
        return self._id_country

    @id_country.setter
    def id_country(self, id_country):
        """
        Sets the id_country of this Address1.
        Country ID

        :param id_country: The id_country of this Address1.
        :type: int
        """

        self._id_country = id_country

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
