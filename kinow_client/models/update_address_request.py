# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateAddressRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, company=None, address1=None, postcode=None, city=None, id_country=None, id_state=None):
        """
        UpdateAddressRequest - a model defined in Swagger

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
            'id_country': 'int',
            'id_state': 'int'
        }

        self.attribute_map = {
            'company': 'company',
            'address1': 'address1',
            'postcode': 'postcode',
            'city': 'city',
            'id_country': 'id_country',
            'id_state': 'id_state'
        }

        self._company = company
        self._address1 = address1
        self._postcode = postcode
        self._city = city
        self._id_country = id_country
        self._id_state = id_state

    @property
    def company(self):
        """
        Gets the company of this UpdateAddressRequest.

        :return: The company of this UpdateAddressRequest.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this UpdateAddressRequest.

        :param company: The company of this UpdateAddressRequest.
        :type: str
        """

        self._company = company

    @property
    def address1(self):
        """
        Gets the address1 of this UpdateAddressRequest.

        :return: The address1 of this UpdateAddressRequest.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this UpdateAddressRequest.

        :param address1: The address1 of this UpdateAddressRequest.
        :type: str
        """

        self._address1 = address1

    @property
    def postcode(self):
        """
        Gets the postcode of this UpdateAddressRequest.

        :return: The postcode of this UpdateAddressRequest.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """
        Sets the postcode of this UpdateAddressRequest.

        :param postcode: The postcode of this UpdateAddressRequest.
        :type: str
        """

        self._postcode = postcode

    @property
    def city(self):
        """
        Gets the city of this UpdateAddressRequest.

        :return: The city of this UpdateAddressRequest.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this UpdateAddressRequest.

        :param city: The city of this UpdateAddressRequest.
        :type: str
        """

        self._city = city

    @property
    def id_country(self):
        """
        Gets the id_country of this UpdateAddressRequest.

        :return: The id_country of this UpdateAddressRequest.
        :rtype: int
        """
        return self._id_country

    @id_country.setter
    def id_country(self, id_country):
        """
        Sets the id_country of this UpdateAddressRequest.

        :param id_country: The id_country of this UpdateAddressRequest.
        :type: int
        """

        self._id_country = id_country

    @property
    def id_state(self):
        """
        Gets the id_state of this UpdateAddressRequest.

        :return: The id_state of this UpdateAddressRequest.
        :rtype: int
        """
        return self._id_state

    @id_state.setter
    def id_state(self, id_state):
        """
        Sets the id_state of this UpdateAddressRequest.

        :param id_state: The id_state of this UpdateAddressRequest.
        :type: int
        """

        self._id_state = id_state

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