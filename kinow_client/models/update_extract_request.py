# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.5
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateExtractRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_product=None, id_product_image=None, id_media_player=None, id_media_source=None, filename=None, position=None, active=None, date_add=None, date_upd=None, can_watch=None, name=None, description=None, cover=None, thumbnail=None, advertising_url=None):
        """
        UpdateExtractRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_product': 'int',
            'id_product_image': 'int',
            'id_media_player': 'int',
            'id_media_source': 'int',
            'filename': 'str',
            'position': 'int',
            'active': 'bool',
            'date_add': 'str',
            'date_upd': 'str',
            'can_watch': 'bool',
            'name': 'list[I18nField]',
            'description': 'list[I18nField]',
            'cover': 'str',
            'thumbnail': 'str',
            'advertising_url': 'str'
        }

        self.attribute_map = {
            'id_product': 'id_product',
            'id_product_image': 'id_product_image',
            'id_media_player': 'id_media_player',
            'id_media_source': 'id_media_source',
            'filename': 'filename',
            'position': 'position',
            'active': 'active',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'can_watch': 'can_watch',
            'name': 'name',
            'description': 'description',
            'cover': 'cover',
            'thumbnail': 'thumbnail',
            'advertising_url': 'advertising_url'
        }

        self._id_product = id_product
        self._id_product_image = id_product_image
        self._id_media_player = id_media_player
        self._id_media_source = id_media_source
        self._filename = filename
        self._position = position
        self._active = active
        self._date_add = date_add
        self._date_upd = date_upd
        self._can_watch = can_watch
        self._name = name
        self._description = description
        self._cover = cover
        self._thumbnail = thumbnail
        self._advertising_url = advertising_url

    @property
    def id_product(self):
        """
        Gets the id_product of this UpdateExtractRequest.

        :return: The id_product of this UpdateExtractRequest.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this UpdateExtractRequest.

        :param id_product: The id_product of this UpdateExtractRequest.
        :type: int
        """

        self._id_product = id_product

    @property
    def id_product_image(self):
        """
        Gets the id_product_image of this UpdateExtractRequest.

        :return: The id_product_image of this UpdateExtractRequest.
        :rtype: int
        """
        return self._id_product_image

    @id_product_image.setter
    def id_product_image(self, id_product_image):
        """
        Sets the id_product_image of this UpdateExtractRequest.

        :param id_product_image: The id_product_image of this UpdateExtractRequest.
        :type: int
        """

        self._id_product_image = id_product_image

    @property
    def id_media_player(self):
        """
        Gets the id_media_player of this UpdateExtractRequest.

        :return: The id_media_player of this UpdateExtractRequest.
        :rtype: int
        """
        return self._id_media_player

    @id_media_player.setter
    def id_media_player(self, id_media_player):
        """
        Sets the id_media_player of this UpdateExtractRequest.

        :param id_media_player: The id_media_player of this UpdateExtractRequest.
        :type: int
        """

        self._id_media_player = id_media_player

    @property
    def id_media_source(self):
        """
        Gets the id_media_source of this UpdateExtractRequest.

        :return: The id_media_source of this UpdateExtractRequest.
        :rtype: int
        """
        return self._id_media_source

    @id_media_source.setter
    def id_media_source(self, id_media_source):
        """
        Sets the id_media_source of this UpdateExtractRequest.

        :param id_media_source: The id_media_source of this UpdateExtractRequest.
        :type: int
        """

        self._id_media_source = id_media_source

    @property
    def filename(self):
        """
        Gets the filename of this UpdateExtractRequest.

        :return: The filename of this UpdateExtractRequest.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this UpdateExtractRequest.

        :param filename: The filename of this UpdateExtractRequest.
        :type: str
        """

        self._filename = filename

    @property
    def position(self):
        """
        Gets the position of this UpdateExtractRequest.

        :return: The position of this UpdateExtractRequest.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this UpdateExtractRequest.

        :param position: The position of this UpdateExtractRequest.
        :type: int
        """

        self._position = position

    @property
    def active(self):
        """
        Gets the active of this UpdateExtractRequest.

        :return: The active of this UpdateExtractRequest.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this UpdateExtractRequest.

        :param active: The active of this UpdateExtractRequest.
        :type: bool
        """

        self._active = active

    @property
    def date_add(self):
        """
        Gets the date_add of this UpdateExtractRequest.

        :return: The date_add of this UpdateExtractRequest.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this UpdateExtractRequest.

        :param date_add: The date_add of this UpdateExtractRequest.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this UpdateExtractRequest.

        :return: The date_upd of this UpdateExtractRequest.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this UpdateExtractRequest.

        :param date_upd: The date_upd of this UpdateExtractRequest.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def can_watch(self):
        """
        Gets the can_watch of this UpdateExtractRequest.

        :return: The can_watch of this UpdateExtractRequest.
        :rtype: bool
        """
        return self._can_watch

    @can_watch.setter
    def can_watch(self, can_watch):
        """
        Sets the can_watch of this UpdateExtractRequest.

        :param can_watch: The can_watch of this UpdateExtractRequest.
        :type: bool
        """

        self._can_watch = can_watch

    @property
    def name(self):
        """
        Gets the name of this UpdateExtractRequest.

        :return: The name of this UpdateExtractRequest.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateExtractRequest.

        :param name: The name of this UpdateExtractRequest.
        :type: list[I18nField]
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this UpdateExtractRequest.

        :return: The description of this UpdateExtractRequest.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateExtractRequest.

        :param description: The description of this UpdateExtractRequest.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def cover(self):
        """
        Gets the cover of this UpdateExtractRequest.

        :return: The cover of this UpdateExtractRequest.
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """
        Sets the cover of this UpdateExtractRequest.

        :param cover: The cover of this UpdateExtractRequest.
        :type: str
        """

        self._cover = cover

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this UpdateExtractRequest.

        :return: The thumbnail of this UpdateExtractRequest.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this UpdateExtractRequest.

        :param thumbnail: The thumbnail of this UpdateExtractRequest.
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def advertising_url(self):
        """
        Gets the advertising_url of this UpdateExtractRequest.

        :return: The advertising_url of this UpdateExtractRequest.
        :rtype: str
        """
        return self._advertising_url

    @advertising_url.setter
    def advertising_url(self, advertising_url):
        """
        Sets the advertising_url of this UpdateExtractRequest.

        :param advertising_url: The advertising_url of this UpdateExtractRequest.
        :type: str
        """

        self._advertising_url = advertising_url

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
