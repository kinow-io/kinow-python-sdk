# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ConvertMediaLiveRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, stream_id=None, live_id=None, date_from=None, date_to=None):
        """
        ConvertMediaLiveRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'stream_id': 'str',
            'live_id': 'str',
            'date_from': 'str',
            'date_to': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'stream_id': 'stream_id',
            'live_id': 'live_id',
            'date_from': 'date_from',
            'date_to': 'date_to'
        }

        self._name = name
        self._stream_id = stream_id
        self._live_id = live_id
        self._date_from = date_from
        self._date_to = date_to

    @property
    def name(self):
        """
        Gets the name of this ConvertMediaLiveRequest.
        Required to setup video asset name

        :return: The name of this ConvertMediaLiveRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConvertMediaLiveRequest.
        Required to setup video asset name

        :param name: The name of this ConvertMediaLiveRequest.
        :type: str
        """

        self._name = name

    @property
    def stream_id(self):
        """
        Gets the stream_id of this ConvertMediaLiveRequest.
        Required if live_id is not given. Is not compatible with date

        :return: The stream_id of this ConvertMediaLiveRequest.
        :rtype: str
        """
        return self._stream_id

    @stream_id.setter
    def stream_id(self, stream_id):
        """
        Sets the stream_id of this ConvertMediaLiveRequest.
        Required if live_id is not given. Is not compatible with date

        :param stream_id: The stream_id of this ConvertMediaLiveRequest.
        :type: str
        """
        if stream_id is None:
            raise ValueError("Invalid value for `stream_id`, must not be `None`")

        self._stream_id = stream_id

    @property
    def live_id(self):
        """
        Gets the live_id of this ConvertMediaLiveRequest.
        Required if stream_id is not given. Date are required with this parameter

        :return: The live_id of this ConvertMediaLiveRequest.
        :rtype: str
        """
        return self._live_id

    @live_id.setter
    def live_id(self, live_id):
        """
        Sets the live_id of this ConvertMediaLiveRequest.
        Required if stream_id is not given. Date are required with this parameter

        :param live_id: The live_id of this ConvertMediaLiveRequest.
        :type: str
        """

        self._live_id = live_id

    @property
    def date_from(self):
        """
        Gets the date_from of this ConvertMediaLiveRequest.
        Required with live_id

        :return: The date_from of this ConvertMediaLiveRequest.
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """
        Sets the date_from of this ConvertMediaLiveRequest.
        Required with live_id

        :param date_from: The date_from of this ConvertMediaLiveRequest.
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """
        Gets the date_to of this ConvertMediaLiveRequest.
        Required with live_id

        :return: The date_to of this ConvertMediaLiveRequest.
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """
        Sets the date_to of this ConvertMediaLiveRequest.
        Required with live_id

        :param date_to: The date_to of this ConvertMediaLiveRequest.
        :type: str
        """

        self._date_to = date_to

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
