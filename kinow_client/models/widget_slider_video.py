# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WidgetSliderVideo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_media_source=None, filename=None):
        """
        WidgetSliderVideo - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_media_source': 'int',
            'filename': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_media_source': 'id_media_source',
            'filename': 'filename'
        }

        self._id = id
        self._id_media_source = id_media_source
        self._filename = filename

    @property
    def id(self):
        """
        Gets the id of this WidgetSliderVideo.

        :return: The id of this WidgetSliderVideo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WidgetSliderVideo.

        :param id: The id of this WidgetSliderVideo.
        :type: int
        """

        self._id = id

    @property
    def id_media_source(self):
        """
        Gets the id_media_source of this WidgetSliderVideo.

        :return: The id_media_source of this WidgetSliderVideo.
        :rtype: int
        """
        return self._id_media_source

    @id_media_source.setter
    def id_media_source(self, id_media_source):
        """
        Sets the id_media_source of this WidgetSliderVideo.

        :param id_media_source: The id_media_source of this WidgetSliderVideo.
        :type: int
        """

        self._id_media_source = id_media_source

    @property
    def filename(self):
        """
        Gets the filename of this WidgetSliderVideo.

        :return: The filename of this WidgetSliderVideo.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this WidgetSliderVideo.

        :param filename: The filename of this WidgetSliderVideo.
        :type: str
        """

        self._filename = filename

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
