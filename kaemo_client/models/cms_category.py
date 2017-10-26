# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.25
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CMSCategory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_parent=None, position=None, level_depth=None, active=None, date_add=None, date_upd=None, name=None, description=None, link_rewrite=None, meta_title=None, meta_keywords=None, meta_description=None):
        """
        CMSCategory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_parent': 'int',
            'position': 'int',
            'level_depth': 'int',
            'active': 'bool',
            'date_add': 'str',
            'date_upd': 'str',
            'name': 'list[I18nField]',
            'description': 'list[I18nField]',
            'link_rewrite': 'list[I18nField]',
            'meta_title': 'list[I18nField]',
            'meta_keywords': 'list[I18nField]',
            'meta_description': 'list[I18nField]'
        }

        self.attribute_map = {
            'id_parent': 'id_parent',
            'position': 'position',
            'level_depth': 'level_depth',
            'active': 'active',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'name': 'name',
            'description': 'description',
            'link_rewrite': 'link_rewrite',
            'meta_title': 'meta_title',
            'meta_keywords': 'meta_keywords',
            'meta_description': 'meta_description'
        }

        self._id_parent = id_parent
        self._position = position
        self._level_depth = level_depth
        self._active = active
        self._date_add = date_add
        self._date_upd = date_upd
        self._name = name
        self._description = description
        self._link_rewrite = link_rewrite
        self._meta_title = meta_title
        self._meta_keywords = meta_keywords
        self._meta_description = meta_description

    @property
    def id_parent(self):
        """
        Gets the id_parent of this CMSCategory.
        $id_parent

        :return: The id_parent of this CMSCategory.
        :rtype: int
        """
        return self._id_parent

    @id_parent.setter
    def id_parent(self, id_parent):
        """
        Sets the id_parent of this CMSCategory.
        $id_parent

        :param id_parent: The id_parent of this CMSCategory.
        :type: int
        """

        self._id_parent = id_parent

    @property
    def position(self):
        """
        Gets the position of this CMSCategory.
        $position

        :return: The position of this CMSCategory.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this CMSCategory.
        $position

        :param position: The position of this CMSCategory.
        :type: int
        """

        self._position = position

    @property
    def level_depth(self):
        """
        Gets the level_depth of this CMSCategory.
        $level_depth

        :return: The level_depth of this CMSCategory.
        :rtype: int
        """
        return self._level_depth

    @level_depth.setter
    def level_depth(self, level_depth):
        """
        Sets the level_depth of this CMSCategory.
        $level_depth

        :param level_depth: The level_depth of this CMSCategory.
        :type: int
        """

        self._level_depth = level_depth

    @property
    def active(self):
        """
        Gets the active of this CMSCategory.
        $active

        :return: The active of this CMSCategory.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this CMSCategory.
        $active

        :param active: The active of this CMSCategory.
        :type: bool
        """

        self._active = active

    @property
    def date_add(self):
        """
        Gets the date_add of this CMSCategory.
        $date_add

        :return: The date_add of this CMSCategory.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this CMSCategory.
        $date_add

        :param date_add: The date_add of this CMSCategory.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this CMSCategory.
        $date_upd

        :return: The date_upd of this CMSCategory.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this CMSCategory.
        $date_upd

        :param date_upd: The date_upd of this CMSCategory.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def name(self):
        """
        Gets the name of this CMSCategory.

        :return: The name of this CMSCategory.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CMSCategory.

        :param name: The name of this CMSCategory.
        :type: list[I18nField]
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CMSCategory.

        :return: The description of this CMSCategory.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CMSCategory.

        :param description: The description of this CMSCategory.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this CMSCategory.

        :return: The link_rewrite of this CMSCategory.
        :rtype: list[I18nField]
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this CMSCategory.

        :param link_rewrite: The link_rewrite of this CMSCategory.
        :type: list[I18nField]
        """

        self._link_rewrite = link_rewrite

    @property
    def meta_title(self):
        """
        Gets the meta_title of this CMSCategory.

        :return: The meta_title of this CMSCategory.
        :rtype: list[I18nField]
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """
        Sets the meta_title of this CMSCategory.

        :param meta_title: The meta_title of this CMSCategory.
        :type: list[I18nField]
        """

        self._meta_title = meta_title

    @property
    def meta_keywords(self):
        """
        Gets the meta_keywords of this CMSCategory.

        :return: The meta_keywords of this CMSCategory.
        :rtype: list[I18nField]
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """
        Sets the meta_keywords of this CMSCategory.

        :param meta_keywords: The meta_keywords of this CMSCategory.
        :type: list[I18nField]
        """

        self._meta_keywords = meta_keywords

    @property
    def meta_description(self):
        """
        Gets the meta_description of this CMSCategory.

        :return: The meta_description of this CMSCategory.
        :rtype: list[I18nField]
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """
        Sets the meta_description of this CMSCategory.

        :param meta_description: The meta_description of this CMSCategory.
        :type: list[I18nField]
        """

        self._meta_description = meta_description

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
