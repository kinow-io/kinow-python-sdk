# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CMSPage(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_cms_category=None, active=None, position=None, link_rewrite=None, meta_title=None, meta_description=None, meta_keywords=None, content=None):
        """
        CMSPage - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_cms_category': 'int',
            'active': 'bool',
            'position': 'int',
            'link_rewrite': 'list[I18nField]',
            'meta_title': 'list[I18nField]',
            'meta_description': 'list[I18nField]',
            'meta_keywords': 'list[I18nField]',
            'content': 'list[I18nField]'
        }

        self.attribute_map = {
            'id': 'id',
            'id_cms_category': 'id_cms_category',
            'active': 'active',
            'position': 'position',
            'link_rewrite': 'link_rewrite',
            'meta_title': 'meta_title',
            'meta_description': 'meta_description',
            'meta_keywords': 'meta_keywords',
            'content': 'content'
        }

        self._id = id
        self._id_cms_category = id_cms_category
        self._active = active
        self._position = position
        self._link_rewrite = link_rewrite
        self._meta_title = meta_title
        self._meta_description = meta_description
        self._meta_keywords = meta_keywords
        self._content = content

    @property
    def id(self):
        """
        Gets the id of this CMSPage.

        :return: The id of this CMSPage.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CMSPage.

        :param id: The id of this CMSPage.
        :type: int
        """

        self._id = id

    @property
    def id_cms_category(self):
        """
        Gets the id_cms_category of this CMSPage.

        :return: The id_cms_category of this CMSPage.
        :rtype: int
        """
        return self._id_cms_category

    @id_cms_category.setter
    def id_cms_category(self, id_cms_category):
        """
        Sets the id_cms_category of this CMSPage.

        :param id_cms_category: The id_cms_category of this CMSPage.
        :type: int
        """

        self._id_cms_category = id_cms_category

    @property
    def active(self):
        """
        Gets the active of this CMSPage.
        $active

        :return: The active of this CMSPage.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this CMSPage.
        $active

        :param active: The active of this CMSPage.
        :type: bool
        """

        self._active = active

    @property
    def position(self):
        """
        Gets the position of this CMSPage.

        :return: The position of this CMSPage.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this CMSPage.

        :param position: The position of this CMSPage.
        :type: int
        """

        self._position = position

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this CMSPage.

        :return: The link_rewrite of this CMSPage.
        :rtype: list[I18nField]
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this CMSPage.

        :param link_rewrite: The link_rewrite of this CMSPage.
        :type: list[I18nField]
        """

        self._link_rewrite = link_rewrite

    @property
    def meta_title(self):
        """
        Gets the meta_title of this CMSPage.

        :return: The meta_title of this CMSPage.
        :rtype: list[I18nField]
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """
        Sets the meta_title of this CMSPage.

        :param meta_title: The meta_title of this CMSPage.
        :type: list[I18nField]
        """

        self._meta_title = meta_title

    @property
    def meta_description(self):
        """
        Gets the meta_description of this CMSPage.

        :return: The meta_description of this CMSPage.
        :rtype: list[I18nField]
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """
        Sets the meta_description of this CMSPage.

        :param meta_description: The meta_description of this CMSPage.
        :type: list[I18nField]
        """

        self._meta_description = meta_description

    @property
    def meta_keywords(self):
        """
        Gets the meta_keywords of this CMSPage.

        :return: The meta_keywords of this CMSPage.
        :rtype: list[I18nField]
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """
        Sets the meta_keywords of this CMSPage.

        :param meta_keywords: The meta_keywords of this CMSPage.
        :type: list[I18nField]
        """

        self._meta_keywords = meta_keywords

    @property
    def content(self):
        """
        Gets the content of this CMSPage.

        :return: The content of this CMSPage.
        :rtype: list[I18nField]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this CMSPage.

        :param content: The content of this CMSPage.
        :type: list[I18nField]
        """

        self._content = content

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
