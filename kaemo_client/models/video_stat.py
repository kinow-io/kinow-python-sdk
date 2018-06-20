# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.45
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VideoStat(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, video_id=None, played=None, duration=None, views=None):
        """
        VideoStat - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'video_id': 'int',
            'played': 'int',
            'duration': 'float',
            'views': 'int'
        }

        self.attribute_map = {
            'video_id': 'video_id',
            'played': 'played',
            'duration': 'duration',
            'views': 'views'
        }

        self._video_id = video_id
        self._played = played
        self._duration = duration
        self._views = views

    @property
    def video_id(self):
        """
        Gets the video_id of this VideoStat.

        :return: The video_id of this VideoStat.
        :rtype: int
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """
        Sets the video_id of this VideoStat.

        :param video_id: The video_id of this VideoStat.
        :type: int
        """

        self._video_id = video_id

    @property
    def played(self):
        """
        Gets the played of this VideoStat.

        :return: The played of this VideoStat.
        :rtype: int
        """
        return self._played

    @played.setter
    def played(self, played):
        """
        Sets the played of this VideoStat.

        :param played: The played of this VideoStat.
        :type: int
        """

        self._played = played

    @property
    def duration(self):
        """
        Gets the duration of this VideoStat.

        :return: The duration of this VideoStat.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this VideoStat.

        :param duration: The duration of this VideoStat.
        :type: float
        """

        self._duration = duration

    @property
    def views(self):
        """
        Gets the views of this VideoStat.

        :return: The views of this VideoStat.
        :rtype: int
        """
        return self._views

    @views.setter
    def views(self, views):
        """
        Sets the views of this VideoStat.

        :param views: The views of this VideoStat.
        :type: int
        """

        self._views = views

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
