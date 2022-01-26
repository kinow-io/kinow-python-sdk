# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VideoCategory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_category=None, id_media_source=None, filename=None, cover=None, thumbnail=None, date_add=None, date_upd=None):
        """
        VideoCategory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_category': 'int',
            'id_media_source': 'int',
            'filename': 'str',
            'cover': 'str',
            'thumbnail': 'str',
            'date_add': 'str',
            'date_upd': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_category': 'id_category',
            'id_media_source': 'id_media_source',
            'filename': 'filename',
            'cover': 'cover',
            'thumbnail': 'thumbnail',
            'date_add': 'date_add',
            'date_upd': 'date_upd'
        }

        self._id = id
        self._id_category = id_category
        self._id_media_source = id_media_source
        self._filename = filename
        self._cover = cover
        self._thumbnail = thumbnail
        self._date_add = date_add
        self._date_upd = date_upd

    @property
    def id(self):
        """
        Gets the id of this VideoCategory.

        :return: The id of this VideoCategory.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VideoCategory.

        :param id: The id of this VideoCategory.
        :type: int
        """

        self._id = id

    @property
    def id_category(self):
        """
        Gets the id_category of this VideoCategory.

        :return: The id_category of this VideoCategory.
        :rtype: int
        """
        return self._id_category

    @id_category.setter
    def id_category(self, id_category):
        """
        Sets the id_category of this VideoCategory.

        :param id_category: The id_category of this VideoCategory.
        :type: int
        """

        self._id_category = id_category

    @property
    def id_media_source(self):
        """
        Gets the id_media_source of this VideoCategory.

        :return: The id_media_source of this VideoCategory.
        :rtype: int
        """
        return self._id_media_source

    @id_media_source.setter
    def id_media_source(self, id_media_source):
        """
        Sets the id_media_source of this VideoCategory.

        :param id_media_source: The id_media_source of this VideoCategory.
        :type: int
        """

        self._id_media_source = id_media_source

    @property
    def filename(self):
        """
        Gets the filename of this VideoCategory.

        :return: The filename of this VideoCategory.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this VideoCategory.

        :param filename: The filename of this VideoCategory.
        :type: str
        """

        self._filename = filename

    @property
    def cover(self):
        """
        Gets the cover of this VideoCategory.

        :return: The cover of this VideoCategory.
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """
        Sets the cover of this VideoCategory.

        :param cover: The cover of this VideoCategory.
        :type: str
        """

        self._cover = cover

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this VideoCategory.

        :return: The thumbnail of this VideoCategory.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this VideoCategory.

        :param thumbnail: The thumbnail of this VideoCategory.
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def date_add(self):
        """
        Gets the date_add of this VideoCategory.

        :return: The date_add of this VideoCategory.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this VideoCategory.

        :param date_add: The date_add of this VideoCategory.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this VideoCategory.

        :return: The date_upd of this VideoCategory.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this VideoCategory.

        :param date_upd: The date_upd of this VideoCategory.
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
