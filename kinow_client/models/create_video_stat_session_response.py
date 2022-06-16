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


class CreateVideoStatSessionResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, customer_id=None, video_id=None, date=None, watched_time=None, user_agent=None, iso_code=None, group_id=None, access_id=None, device_id=None, seek=None):
        """
        CreateVideoStatSessionResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'customer_id': 'int',
            'video_id': 'int',
            'date': 'str',
            'watched_time': 'int',
            'user_agent': 'str',
            'iso_code': 'str',
            'group_id': 'int',
            'access_id': 'int',
            'device_id': 'int',
            'seek': 'float'
        }

        self.attribute_map = {
            'customer_id': 'customer_id',
            'video_id': 'video_id',
            'date': 'date',
            'watched_time': 'watched_time',
            'user_agent': 'user_agent',
            'iso_code': 'iso_code',
            'group_id': 'group_id',
            'access_id': 'access_id',
            'device_id': 'device_id',
            'seek': 'seek'
        }

        self._customer_id = customer_id
        self._video_id = video_id
        self._date = date
        self._watched_time = watched_time
        self._user_agent = user_agent
        self._iso_code = iso_code
        self._group_id = group_id
        self._access_id = access_id
        self._device_id = device_id
        self._seek = seek

    @property
    def customer_id(self):
        """
        Gets the customer_id of this CreateVideoStatSessionResponse.

        :return: The customer_id of this CreateVideoStatSessionResponse.
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """
        Sets the customer_id of this CreateVideoStatSessionResponse.

        :param customer_id: The customer_id of this CreateVideoStatSessionResponse.
        :type: int
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")

        self._customer_id = customer_id

    @property
    def video_id(self):
        """
        Gets the video_id of this CreateVideoStatSessionResponse.

        :return: The video_id of this CreateVideoStatSessionResponse.
        :rtype: int
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """
        Sets the video_id of this CreateVideoStatSessionResponse.

        :param video_id: The video_id of this CreateVideoStatSessionResponse.
        :type: int
        """
        if video_id is None:
            raise ValueError("Invalid value for `video_id`, must not be `None`")

        self._video_id = video_id

    @property
    def date(self):
        """
        Gets the date of this CreateVideoStatSessionResponse.

        :return: The date of this CreateVideoStatSessionResponse.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this CreateVideoStatSessionResponse.

        :param date: The date of this CreateVideoStatSessionResponse.
        :type: str
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")

        self._date = date

    @property
    def watched_time(self):
        """
        Gets the watched_time of this CreateVideoStatSessionResponse.

        :return: The watched_time of this CreateVideoStatSessionResponse.
        :rtype: int
        """
        return self._watched_time

    @watched_time.setter
    def watched_time(self, watched_time):
        """
        Sets the watched_time of this CreateVideoStatSessionResponse.

        :param watched_time: The watched_time of this CreateVideoStatSessionResponse.
        :type: int
        """
        if watched_time is None:
            raise ValueError("Invalid value for `watched_time`, must not be `None`")

        self._watched_time = watched_time

    @property
    def user_agent(self):
        """
        Gets the user_agent of this CreateVideoStatSessionResponse.

        :return: The user_agent of this CreateVideoStatSessionResponse.
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """
        Sets the user_agent of this CreateVideoStatSessionResponse.

        :param user_agent: The user_agent of this CreateVideoStatSessionResponse.
        :type: str
        """
        if user_agent is None:
            raise ValueError("Invalid value for `user_agent`, must not be `None`")

        self._user_agent = user_agent

    @property
    def iso_code(self):
        """
        Gets the iso_code of this CreateVideoStatSessionResponse.

        :return: The iso_code of this CreateVideoStatSessionResponse.
        :rtype: str
        """
        return self._iso_code

    @iso_code.setter
    def iso_code(self, iso_code):
        """
        Sets the iso_code of this CreateVideoStatSessionResponse.

        :param iso_code: The iso_code of this CreateVideoStatSessionResponse.
        :type: str
        """

        self._iso_code = iso_code

    @property
    def group_id(self):
        """
        Gets the group_id of this CreateVideoStatSessionResponse.

        :return: The group_id of this CreateVideoStatSessionResponse.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """
        Sets the group_id of this CreateVideoStatSessionResponse.

        :param group_id: The group_id of this CreateVideoStatSessionResponse.
        :type: int
        """

        self._group_id = group_id

    @property
    def access_id(self):
        """
        Gets the access_id of this CreateVideoStatSessionResponse.

        :return: The access_id of this CreateVideoStatSessionResponse.
        :rtype: int
        """
        return self._access_id

    @access_id.setter
    def access_id(self, access_id):
        """
        Sets the access_id of this CreateVideoStatSessionResponse.

        :param access_id: The access_id of this CreateVideoStatSessionResponse.
        :type: int
        """

        self._access_id = access_id

    @property
    def device_id(self):
        """
        Gets the device_id of this CreateVideoStatSessionResponse.

        :return: The device_id of this CreateVideoStatSessionResponse.
        :rtype: int
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this CreateVideoStatSessionResponse.

        :param device_id: The device_id of this CreateVideoStatSessionResponse.
        :type: int
        """

        self._device_id = device_id

    @property
    def seek(self):
        """
        Gets the seek of this CreateVideoStatSessionResponse.

        :return: The seek of this CreateVideoStatSessionResponse.
        :rtype: float
        """
        return self._seek

    @seek.setter
    def seek(self, seek):
        """
        Sets the seek of this CreateVideoStatSessionResponse.

        :param seek: The seek of this CreateVideoStatSessionResponse.
        :type: float
        """

        self._seek = seek

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
