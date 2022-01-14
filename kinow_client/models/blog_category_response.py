# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BlogCategoryResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, position=None, active=None, date_add=None, date_upd=None, name=None, meta_title=None, meta_description=None, link_rewrite=None, id=None, meta_keywords=None):
        """
        BlogCategoryResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'position': 'int',
            'active': 'int',
            'date_add': 'str',
            'date_upd': 'str',
            'name': 'list[I18nField]',
            'meta_title': 'list[I18nField]',
            'meta_description': 'list[I18nField]',
            'link_rewrite': 'list[I18nField]',
            'id': 'int',
            'meta_keywords': 'list[I18nField]'
        }

        self.attribute_map = {
            'position': 'position',
            'active': 'active',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'name': 'name',
            'meta_title': 'meta_title',
            'meta_description': 'meta_description',
            'link_rewrite': 'link_rewrite',
            'id': 'id',
            'meta_keywords': 'meta_keywords'
        }

        self._position = position
        self._active = active
        self._date_add = date_add
        self._date_upd = date_upd
        self._name = name
        self._meta_title = meta_title
        self._meta_description = meta_description
        self._link_rewrite = link_rewrite
        self._id = id
        self._meta_keywords = meta_keywords

    @property
    def position(self):
        """
        Gets the position of this BlogCategoryResponse.

        :return: The position of this BlogCategoryResponse.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this BlogCategoryResponse.

        :param position: The position of this BlogCategoryResponse.
        :type: int
        """

        self._position = position

    @property
    def active(self):
        """
        Gets the active of this BlogCategoryResponse.

        :return: The active of this BlogCategoryResponse.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this BlogCategoryResponse.

        :param active: The active of this BlogCategoryResponse.
        :type: int
        """

        self._active = active

    @property
    def date_add(self):
        """
        Gets the date_add of this BlogCategoryResponse.

        :return: The date_add of this BlogCategoryResponse.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this BlogCategoryResponse.

        :param date_add: The date_add of this BlogCategoryResponse.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this BlogCategoryResponse.

        :return: The date_upd of this BlogCategoryResponse.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this BlogCategoryResponse.

        :param date_upd: The date_upd of this BlogCategoryResponse.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def name(self):
        """
        Gets the name of this BlogCategoryResponse.

        :return: The name of this BlogCategoryResponse.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BlogCategoryResponse.

        :param name: The name of this BlogCategoryResponse.
        :type: list[I18nField]
        """

        self._name = name

    @property
    def meta_title(self):
        """
        Gets the meta_title of this BlogCategoryResponse.

        :return: The meta_title of this BlogCategoryResponse.
        :rtype: list[I18nField]
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """
        Sets the meta_title of this BlogCategoryResponse.

        :param meta_title: The meta_title of this BlogCategoryResponse.
        :type: list[I18nField]
        """

        self._meta_title = meta_title

    @property
    def meta_description(self):
        """
        Gets the meta_description of this BlogCategoryResponse.

        :return: The meta_description of this BlogCategoryResponse.
        :rtype: list[I18nField]
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """
        Sets the meta_description of this BlogCategoryResponse.

        :param meta_description: The meta_description of this BlogCategoryResponse.
        :type: list[I18nField]
        """

        self._meta_description = meta_description

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this BlogCategoryResponse.

        :return: The link_rewrite of this BlogCategoryResponse.
        :rtype: list[I18nField]
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this BlogCategoryResponse.

        :param link_rewrite: The link_rewrite of this BlogCategoryResponse.
        :type: list[I18nField]
        """

        self._link_rewrite = link_rewrite

    @property
    def id(self):
        """
        Gets the id of this BlogCategoryResponse.

        :return: The id of this BlogCategoryResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BlogCategoryResponse.

        :param id: The id of this BlogCategoryResponse.
        :type: int
        """

        self._id = id

    @property
    def meta_keywords(self):
        """
        Gets the meta_keywords of this BlogCategoryResponse.

        :return: The meta_keywords of this BlogCategoryResponse.
        :rtype: list[I18nField]
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """
        Sets the meta_keywords of this BlogCategoryResponse.

        :param meta_keywords: The meta_keywords of this BlogCategoryResponse.
        :type: list[I18nField]
        """

        self._meta_keywords = meta_keywords

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
