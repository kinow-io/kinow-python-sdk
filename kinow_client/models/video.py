# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Video(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_product=None, id_language=None, language_filter=None, id_media_source=None, name=None, description=None, duration=None, filename=None, position=None, subscription=None, free=None, download=None, active=None, date_add=None, date_upd=None, can_watch=None, cover=None, thumbnail=None, geoloc_enabled=None, behavior_detected_countries=None, behavior_non_detected_countries=None, has_free_access=None):
        """
        Video - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_product': 'int',
            'id_language': 'int',
            'language_filter': 'int',
            'id_media_source': 'int',
            'name': 'list[I18nField]',
            'description': 'list[I18nField]',
            'duration': 'int',
            'filename': 'str',
            'position': 'int',
            'subscription': 'int',
            'free': 'int',
            'download': 'int',
            'active': 'bool',
            'date_add': 'str',
            'date_upd': 'str',
            'can_watch': 'bool',
            'cover': 'str',
            'thumbnail': 'str',
            'geoloc_enabled': 'bool',
            'behavior_detected_countries': 'str',
            'behavior_non_detected_countries': 'str',
            'has_free_access': 'VideoFreeAccess'
        }

        self.attribute_map = {
            'id': 'id',
            'id_product': 'id_product',
            'id_language': 'id_language',
            'language_filter': 'language_filter',
            'id_media_source': 'id_media_source',
            'name': 'name',
            'description': 'description',
            'duration': 'duration',
            'filename': 'filename',
            'position': 'position',
            'subscription': 'subscription',
            'free': 'free',
            'download': 'download',
            'active': 'active',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'can_watch': 'can_watch',
            'cover': 'cover',
            'thumbnail': 'thumbnail',
            'geoloc_enabled': 'geoloc_enabled',
            'behavior_detected_countries': 'behavior_detected_countries',
            'behavior_non_detected_countries': 'behavior_non_detected_countries',
            'has_free_access': 'has_free_access'
        }

        self._id = id
        self._id_product = id_product
        self._id_language = id_language
        self._language_filter = language_filter
        self._id_media_source = id_media_source
        self._name = name
        self._description = description
        self._duration = duration
        self._filename = filename
        self._position = position
        self._subscription = subscription
        self._free = free
        self._download = download
        self._active = active
        self._date_add = date_add
        self._date_upd = date_upd
        self._can_watch = can_watch
        self._cover = cover
        self._thumbnail = thumbnail
        self._geoloc_enabled = geoloc_enabled
        self._behavior_detected_countries = behavior_detected_countries
        self._behavior_non_detected_countries = behavior_non_detected_countries
        self._has_free_access = has_free_access

    @property
    def id(self):
        """
        Gets the id of this Video.
        

        :return: The id of this Video.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Video.
        

        :param id: The id of this Video.
        :type: int
        """

        self._id = id

    @property
    def id_product(self):
        """
        Gets the id_product of this Video.
        

        :return: The id_product of this Video.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this Video.
        

        :param id_product: The id_product of this Video.
        :type: int
        """

        self._id_product = id_product

    @property
    def id_language(self):
        """
        Gets the id_language of this Video.
        

        :return: The id_language of this Video.
        :rtype: int
        """
        return self._id_language

    @id_language.setter
    def id_language(self, id_language):
        """
        Sets the id_language of this Video.
        

        :param id_language: The id_language of this Video.
        :type: int
        """

        self._id_language = id_language

    @property
    def language_filter(self):
        """
        Gets the language_filter of this Video.
        

        :return: The language_filter of this Video.
        :rtype: int
        """
        return self._language_filter

    @language_filter.setter
    def language_filter(self, language_filter):
        """
        Sets the language_filter of this Video.
        

        :param language_filter: The language_filter of this Video.
        :type: int
        """

        self._language_filter = language_filter

    @property
    def id_media_source(self):
        """
        Gets the id_media_source of this Video.
        

        :return: The id_media_source of this Video.
        :rtype: int
        """
        return self._id_media_source

    @id_media_source.setter
    def id_media_source(self, id_media_source):
        """
        Sets the id_media_source of this Video.
        

        :param id_media_source: The id_media_source of this Video.
        :type: int
        """

        self._id_media_source = id_media_source

    @property
    def name(self):
        """
        Gets the name of this Video.

        :return: The name of this Video.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Video.

        :param name: The name of this Video.
        :type: list[I18nField]
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Video.

        :return: The description of this Video.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Video.

        :param description: The description of this Video.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def duration(self):
        """
        Gets the duration of this Video.
        

        :return: The duration of this Video.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this Video.
        

        :param duration: The duration of this Video.
        :type: int
        """

        self._duration = duration

    @property
    def filename(self):
        """
        Gets the filename of this Video.
        

        :return: The filename of this Video.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this Video.
        

        :param filename: The filename of this Video.
        :type: str
        """

        self._filename = filename

    @property
    def position(self):
        """
        Gets the position of this Video.
        

        :return: The position of this Video.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this Video.
        

        :param position: The position of this Video.
        :type: int
        """

        self._position = position

    @property
    def subscription(self):
        """
        Gets the subscription of this Video.
        

        :return: The subscription of this Video.
        :rtype: int
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """
        Sets the subscription of this Video.
        

        :param subscription: The subscription of this Video.
        :type: int
        """

        self._subscription = subscription

    @property
    def free(self):
        """
        Gets the free of this Video.
        

        :return: The free of this Video.
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """
        Sets the free of this Video.
        

        :param free: The free of this Video.
        :type: int
        """

        self._free = free

    @property
    def download(self):
        """
        Gets the download of this Video.
        

        :return: The download of this Video.
        :rtype: int
        """
        return self._download

    @download.setter
    def download(self, download):
        """
        Sets the download of this Video.
        

        :param download: The download of this Video.
        :type: int
        """

        self._download = download

    @property
    def active(self):
        """
        Gets the active of this Video.
        

        :return: The active of this Video.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Video.
        

        :param active: The active of this Video.
        :type: bool
        """

        self._active = active

    @property
    def date_add(self):
        """
        Gets the date_add of this Video.
        

        :return: The date_add of this Video.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this Video.
        

        :param date_add: The date_add of this Video.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this Video.
        

        :return: The date_upd of this Video.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this Video.
        

        :param date_upd: The date_upd of this Video.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def can_watch(self):
        """
        Gets the can_watch of this Video.
        

        :return: The can_watch of this Video.
        :rtype: bool
        """
        return self._can_watch

    @can_watch.setter
    def can_watch(self, can_watch):
        """
        Sets the can_watch of this Video.
        

        :param can_watch: The can_watch of this Video.
        :type: bool
        """

        self._can_watch = can_watch

    @property
    def cover(self):
        """
        Gets the cover of this Video.
        

        :return: The cover of this Video.
        :rtype: str
        """
        return self._cover

    @cover.setter
    def cover(self, cover):
        """
        Sets the cover of this Video.
        

        :param cover: The cover of this Video.
        :type: str
        """

        self._cover = cover

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this Video.
        

        :return: The thumbnail of this Video.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this Video.
        

        :param thumbnail: The thumbnail of this Video.
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def geoloc_enabled(self):
        """
        Gets the geoloc_enabled of this Video.
        

        :return: The geoloc_enabled of this Video.
        :rtype: bool
        """
        return self._geoloc_enabled

    @geoloc_enabled.setter
    def geoloc_enabled(self, geoloc_enabled):
        """
        Sets the geoloc_enabled of this Video.
        

        :param geoloc_enabled: The geoloc_enabled of this Video.
        :type: bool
        """

        self._geoloc_enabled = geoloc_enabled

    @property
    def behavior_detected_countries(self):
        """
        Gets the behavior_detected_countries of this Video.
        

        :return: The behavior_detected_countries of this Video.
        :rtype: str
        """
        return self._behavior_detected_countries

    @behavior_detected_countries.setter
    def behavior_detected_countries(self, behavior_detected_countries):
        """
        Sets the behavior_detected_countries of this Video.
        

        :param behavior_detected_countries: The behavior_detected_countries of this Video.
        :type: str
        """

        self._behavior_detected_countries = behavior_detected_countries

    @property
    def behavior_non_detected_countries(self):
        """
        Gets the behavior_non_detected_countries of this Video.
        

        :return: The behavior_non_detected_countries of this Video.
        :rtype: str
        """
        return self._behavior_non_detected_countries

    @behavior_non_detected_countries.setter
    def behavior_non_detected_countries(self, behavior_non_detected_countries):
        """
        Sets the behavior_non_detected_countries of this Video.
        

        :param behavior_non_detected_countries: The behavior_non_detected_countries of this Video.
        :type: str
        """

        self._behavior_non_detected_countries = behavior_non_detected_countries

    @property
    def has_free_access(self):
        """
        Gets the has_free_access of this Video.

        :return: The has_free_access of this Video.
        :rtype: VideoFreeAccess
        """
        return self._has_free_access

    @has_free_access.setter
    def has_free_access(self, has_free_access):
        """
        Sets the has_free_access of this Video.

        :param has_free_access: The has_free_access of this Video.
        :type: VideoFreeAccess
        """

        self._has_free_access = has_free_access

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
