# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateCategoryRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_parent=None, date_add=None, date_upd=None, active=None, level_depth=None, position=None, images=None, meta_description=None, meta_keywords=None, meta_title=None, link_rewrite=None, name=None, description=None, description_short=None):
        """
        UpdateCategoryRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_parent': 'int',
            'date_add': 'str',
            'date_upd': 'str',
            'active': 'bool',
            'level_depth': 'int',
            'position': 'int',
            'images': 'list[Image]',
            'meta_description': 'list[I18nField]',
            'meta_keywords': 'list[I18nField]',
            'meta_title': 'list[I18nField]',
            'link_rewrite': 'list[I18nField]',
            'name': 'list[I18nField]',
            'description': 'list[I18nField]',
            'description_short': 'list[I18nField]'
        }

        self.attribute_map = {
            'id_parent': 'id_parent',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'active': 'active',
            'level_depth': 'level_depth',
            'position': 'position',
            'images': 'images',
            'meta_description': 'meta_description',
            'meta_keywords': 'meta_keywords',
            'meta_title': 'meta_title',
            'link_rewrite': 'link_rewrite',
            'name': 'name',
            'description': 'description',
            'description_short': 'description_short'
        }

        self._id_parent = id_parent
        self._date_add = date_add
        self._date_upd = date_upd
        self._active = active
        self._level_depth = level_depth
        self._position = position
        self._images = images
        self._meta_description = meta_description
        self._meta_keywords = meta_keywords
        self._meta_title = meta_title
        self._link_rewrite = link_rewrite
        self._name = name
        self._description = description
        self._description_short = description_short

    @property
    def id_parent(self):
        """
        Gets the id_parent of this UpdateCategoryRequest.

        :return: The id_parent of this UpdateCategoryRequest.
        :rtype: int
        """
        return self._id_parent

    @id_parent.setter
    def id_parent(self, id_parent):
        """
        Sets the id_parent of this UpdateCategoryRequest.

        :param id_parent: The id_parent of this UpdateCategoryRequest.
        :type: int
        """

        self._id_parent = id_parent

    @property
    def date_add(self):
        """
        Gets the date_add of this UpdateCategoryRequest.

        :return: The date_add of this UpdateCategoryRequest.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this UpdateCategoryRequest.

        :param date_add: The date_add of this UpdateCategoryRequest.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this UpdateCategoryRequest.

        :return: The date_upd of this UpdateCategoryRequest.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this UpdateCategoryRequest.

        :param date_upd: The date_upd of this UpdateCategoryRequest.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def active(self):
        """
        Gets the active of this UpdateCategoryRequest.

        :return: The active of this UpdateCategoryRequest.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this UpdateCategoryRequest.

        :param active: The active of this UpdateCategoryRequest.
        :type: bool
        """

        self._active = active

    @property
    def level_depth(self):
        """
        Gets the level_depth of this UpdateCategoryRequest.

        :return: The level_depth of this UpdateCategoryRequest.
        :rtype: int
        """
        return self._level_depth

    @level_depth.setter
    def level_depth(self, level_depth):
        """
        Sets the level_depth of this UpdateCategoryRequest.

        :param level_depth: The level_depth of this UpdateCategoryRequest.
        :type: int
        """

        self._level_depth = level_depth

    @property
    def position(self):
        """
        Gets the position of this UpdateCategoryRequest.

        :return: The position of this UpdateCategoryRequest.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this UpdateCategoryRequest.

        :param position: The position of this UpdateCategoryRequest.
        :type: int
        """

        self._position = position

    @property
    def images(self):
        """
        Gets the images of this UpdateCategoryRequest.

        :return: The images of this UpdateCategoryRequest.
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this UpdateCategoryRequest.

        :param images: The images of this UpdateCategoryRequest.
        :type: list[Image]
        """

        self._images = images

    @property
    def meta_description(self):
        """
        Gets the meta_description of this UpdateCategoryRequest.

        :return: The meta_description of this UpdateCategoryRequest.
        :rtype: list[I18nField]
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """
        Sets the meta_description of this UpdateCategoryRequest.

        :param meta_description: The meta_description of this UpdateCategoryRequest.
        :type: list[I18nField]
        """

        self._meta_description = meta_description

    @property
    def meta_keywords(self):
        """
        Gets the meta_keywords of this UpdateCategoryRequest.

        :return: The meta_keywords of this UpdateCategoryRequest.
        :rtype: list[I18nField]
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """
        Sets the meta_keywords of this UpdateCategoryRequest.

        :param meta_keywords: The meta_keywords of this UpdateCategoryRequest.
        :type: list[I18nField]
        """

        self._meta_keywords = meta_keywords

    @property
    def meta_title(self):
        """
        Gets the meta_title of this UpdateCategoryRequest.

        :return: The meta_title of this UpdateCategoryRequest.
        :rtype: list[I18nField]
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """
        Sets the meta_title of this UpdateCategoryRequest.

        :param meta_title: The meta_title of this UpdateCategoryRequest.
        :type: list[I18nField]
        """

        self._meta_title = meta_title

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this UpdateCategoryRequest.

        :return: The link_rewrite of this UpdateCategoryRequest.
        :rtype: list[I18nField]
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this UpdateCategoryRequest.

        :param link_rewrite: The link_rewrite of this UpdateCategoryRequest.
        :type: list[I18nField]
        """

        self._link_rewrite = link_rewrite

    @property
    def name(self):
        """
        Gets the name of this UpdateCategoryRequest.

        :return: The name of this UpdateCategoryRequest.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateCategoryRequest.

        :param name: The name of this UpdateCategoryRequest.
        :type: list[I18nField]
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this UpdateCategoryRequest.

        :return: The description of this UpdateCategoryRequest.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateCategoryRequest.

        :param description: The description of this UpdateCategoryRequest.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def description_short(self):
        """
        Gets the description_short of this UpdateCategoryRequest.

        :return: The description_short of this UpdateCategoryRequest.
        :rtype: list[I18nField]
        """
        return self._description_short

    @description_short.setter
    def description_short(self, description_short):
        """
        Sets the description_short of this UpdateCategoryRequest.

        :param description_short: The description_short of this UpdateCategoryRequest.
        :type: list[I18nField]
        """

        self._description_short = description_short

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
