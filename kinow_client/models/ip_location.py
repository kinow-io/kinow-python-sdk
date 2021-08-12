# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.46
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class IPLocation(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, ip=None, continent=None, country=None, time_zone=None, coordinates=None, is_vpn_or_proxy=None):
        """
        IPLocation - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ip': 'str',
            'continent': 'str',
            'country': 'str',
            'time_zone': 'str',
            'coordinates': 'IPCoordinates',
            'is_vpn_or_proxy': 'bool'
        }

        self.attribute_map = {
            'ip': 'ip',
            'continent': 'continent',
            'country': 'country',
            'time_zone': 'time_zone',
            'coordinates': 'coordinates',
            'is_vpn_or_proxy': 'isVpnOrProxy'
        }

        self._ip = ip
        self._continent = continent
        self._country = country
        self._time_zone = time_zone
        self._coordinates = coordinates
        self._is_vpn_or_proxy = is_vpn_or_proxy

    @property
    def ip(self):
        """
        Gets the ip of this IPLocation.

        :return: The ip of this IPLocation.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """
        Sets the ip of this IPLocation.

        :param ip: The ip of this IPLocation.
        :type: str
        """

        self._ip = ip

    @property
    def continent(self):
        """
        Gets the continent of this IPLocation.

        :return: The continent of this IPLocation.
        :rtype: str
        """
        return self._continent

    @continent.setter
    def continent(self, continent):
        """
        Sets the continent of this IPLocation.

        :param continent: The continent of this IPLocation.
        :type: str
        """

        self._continent = continent

    @property
    def country(self):
        """
        Gets the country of this IPLocation.

        :return: The country of this IPLocation.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this IPLocation.

        :param country: The country of this IPLocation.
        :type: str
        """

        self._country = country

    @property
    def time_zone(self):
        """
        Gets the time_zone of this IPLocation.

        :return: The time_zone of this IPLocation.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """
        Sets the time_zone of this IPLocation.

        :param time_zone: The time_zone of this IPLocation.
        :type: str
        """

        self._time_zone = time_zone

    @property
    def coordinates(self):
        """
        Gets the coordinates of this IPLocation.

        :return: The coordinates of this IPLocation.
        :rtype: IPCoordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """
        Sets the coordinates of this IPLocation.

        :param coordinates: The coordinates of this IPLocation.
        :type: IPCoordinates
        """

        self._coordinates = coordinates

    @property
    def is_vpn_or_proxy(self):
        """
        Gets the is_vpn_or_proxy of this IPLocation.

        :return: The is_vpn_or_proxy of this IPLocation.
        :rtype: bool
        """
        return self._is_vpn_or_proxy

    @is_vpn_or_proxy.setter
    def is_vpn_or_proxy(self, is_vpn_or_proxy):
        """
        Sets the is_vpn_or_proxy of this IPLocation.

        :param is_vpn_or_proxy: The is_vpn_or_proxy of this IPLocation.
        :type: bool
        """

        self._is_vpn_or_proxy = is_vpn_or_proxy

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
