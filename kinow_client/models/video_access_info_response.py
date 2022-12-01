# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.22
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VideoAccessInfoResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_video=None, streaming=None, download=None, maximum_watched=None, maximum_viewing=None, quality_hd=None, quality_sd=None, expires=None, play_duration=None, error_code=None):
        """
        VideoAccessInfoResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_video': 'float',
            'streaming': 'bool',
            'download': 'bool',
            'maximum_watched': 'bool',
            'maximum_viewing': 'bool',
            'quality_hd': 'bool',
            'quality_sd': 'bool',
            'expires': 'str',
            'play_duration': 'float',
            'error_code': 'float'
        }

        self.attribute_map = {
            'id_video': 'id_video',
            'streaming': 'streaming',
            'download': 'download',
            'maximum_watched': 'maximum_watched',
            'maximum_viewing': 'maximum_viewing',
            'quality_hd': 'quality_hd',
            'quality_sd': 'quality_sd',
            'expires': 'expires',
            'play_duration': 'play_duration',
            'error_code': 'error_code'
        }

        self._id_video = id_video
        self._streaming = streaming
        self._download = download
        self._maximum_watched = maximum_watched
        self._maximum_viewing = maximum_viewing
        self._quality_hd = quality_hd
        self._quality_sd = quality_sd
        self._expires = expires
        self._play_duration = play_duration
        self._error_code = error_code

    @property
    def id_video(self):
        """
        Gets the id_video of this VideoAccessInfoResponse.

        :return: The id_video of this VideoAccessInfoResponse.
        :rtype: float
        """
        return self._id_video

    @id_video.setter
    def id_video(self, id_video):
        """
        Sets the id_video of this VideoAccessInfoResponse.

        :param id_video: The id_video of this VideoAccessInfoResponse.
        :type: float
        """

        self._id_video = id_video

    @property
    def streaming(self):
        """
        Gets the streaming of this VideoAccessInfoResponse.

        :return: The streaming of this VideoAccessInfoResponse.
        :rtype: bool
        """
        return self._streaming

    @streaming.setter
    def streaming(self, streaming):
        """
        Sets the streaming of this VideoAccessInfoResponse.

        :param streaming: The streaming of this VideoAccessInfoResponse.
        :type: bool
        """

        self._streaming = streaming

    @property
    def download(self):
        """
        Gets the download of this VideoAccessInfoResponse.

        :return: The download of this VideoAccessInfoResponse.
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        """
        Sets the download of this VideoAccessInfoResponse.

        :param download: The download of this VideoAccessInfoResponse.
        :type: bool
        """

        self._download = download

    @property
    def maximum_watched(self):
        """
        Gets the maximum_watched of this VideoAccessInfoResponse.

        :return: The maximum_watched of this VideoAccessInfoResponse.
        :rtype: bool
        """
        return self._maximum_watched

    @maximum_watched.setter
    def maximum_watched(self, maximum_watched):
        """
        Sets the maximum_watched of this VideoAccessInfoResponse.

        :param maximum_watched: The maximum_watched of this VideoAccessInfoResponse.
        :type: bool
        """

        self._maximum_watched = maximum_watched

    @property
    def maximum_viewing(self):
        """
        Gets the maximum_viewing of this VideoAccessInfoResponse.

        :return: The maximum_viewing of this VideoAccessInfoResponse.
        :rtype: bool
        """
        return self._maximum_viewing

    @maximum_viewing.setter
    def maximum_viewing(self, maximum_viewing):
        """
        Sets the maximum_viewing of this VideoAccessInfoResponse.

        :param maximum_viewing: The maximum_viewing of this VideoAccessInfoResponse.
        :type: bool
        """

        self._maximum_viewing = maximum_viewing

    @property
    def quality_hd(self):
        """
        Gets the quality_hd of this VideoAccessInfoResponse.

        :return: The quality_hd of this VideoAccessInfoResponse.
        :rtype: bool
        """
        return self._quality_hd

    @quality_hd.setter
    def quality_hd(self, quality_hd):
        """
        Sets the quality_hd of this VideoAccessInfoResponse.

        :param quality_hd: The quality_hd of this VideoAccessInfoResponse.
        :type: bool
        """

        self._quality_hd = quality_hd

    @property
    def quality_sd(self):
        """
        Gets the quality_sd of this VideoAccessInfoResponse.

        :return: The quality_sd of this VideoAccessInfoResponse.
        :rtype: bool
        """
        return self._quality_sd

    @quality_sd.setter
    def quality_sd(self, quality_sd):
        """
        Sets the quality_sd of this VideoAccessInfoResponse.

        :param quality_sd: The quality_sd of this VideoAccessInfoResponse.
        :type: bool
        """

        self._quality_sd = quality_sd

    @property
    def expires(self):
        """
        Gets the expires of this VideoAccessInfoResponse.

        :return: The expires of this VideoAccessInfoResponse.
        :rtype: str
        """
        return self._expires

    @expires.setter
    def expires(self, expires):
        """
        Sets the expires of this VideoAccessInfoResponse.

        :param expires: The expires of this VideoAccessInfoResponse.
        :type: str
        """

        self._expires = expires

    @property
    def play_duration(self):
        """
        Gets the play_duration of this VideoAccessInfoResponse.

        :return: The play_duration of this VideoAccessInfoResponse.
        :rtype: float
        """
        return self._play_duration

    @play_duration.setter
    def play_duration(self, play_duration):
        """
        Sets the play_duration of this VideoAccessInfoResponse.

        :param play_duration: The play_duration of this VideoAccessInfoResponse.
        :type: float
        """

        self._play_duration = play_duration

    @property
    def error_code(self):
        """
        Gets the error_code of this VideoAccessInfoResponse.

        :return: The error_code of this VideoAccessInfoResponse.
        :rtype: float
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """
        Sets the error_code of this VideoAccessInfoResponse.

        :param error_code: The error_code of this VideoAccessInfoResponse.
        :type: float
        """

        self._error_code = error_code

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
