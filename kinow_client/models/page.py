# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.41
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Page(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, page=None, enabled=None, title=None, description=None, keywords=None, url_rewrite=None):
        """
        Page - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'page': 'str',
            'enabled': 'bool',
            'title': 'list[I18nField]',
            'description': 'list[I18nField]',
            'keywords': 'list[I18nField]',
            'url_rewrite': 'list[I18nField]'
        }

        self.attribute_map = {
            'id': 'id',
            'page': 'page',
            'enabled': 'enabled',
            'title': 'title',
            'description': 'description',
            'keywords': 'keywords',
            'url_rewrite': 'url_rewrite'
        }

        self._id = id
        self._page = page
        self._enabled = enabled
        self._title = title
        self._description = description
        self._keywords = keywords
        self._url_rewrite = url_rewrite

    @property
    def id(self):
        """
        Gets the id of this Page.

        :return: The id of this Page.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Page.

        :param id: The id of this Page.
        :type: int
        """

        self._id = id

    @property
    def page(self):
        """
        Gets the page of this Page.

        :return: The page of this Page.
        :rtype: str
        """
        return self._page

    @page.setter
    def page(self, page):
        """
        Sets the page of this Page.

        :param page: The page of this Page.
        :type: str
        """

        self._page = page

    @property
    def enabled(self):
        """
        Gets the enabled of this Page.

        :return: The enabled of this Page.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this Page.

        :param enabled: The enabled of this Page.
        :type: bool
        """

        self._enabled = enabled

    @property
    def title(self):
        """
        Gets the title of this Page.

        :return: The title of this Page.
        :rtype: list[I18nField]
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this Page.

        :param title: The title of this Page.
        :type: list[I18nField]
        """

        self._title = title

    @property
    def description(self):
        """
        Gets the description of this Page.

        :return: The description of this Page.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Page.

        :param description: The description of this Page.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def keywords(self):
        """
        Gets the keywords of this Page.

        :return: The keywords of this Page.
        :rtype: list[I18nField]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """
        Sets the keywords of this Page.

        :param keywords: The keywords of this Page.
        :type: list[I18nField]
        """

        self._keywords = keywords

    @property
    def url_rewrite(self):
        """
        Gets the url_rewrite of this Page.

        :return: The url_rewrite of this Page.
        :rtype: list[I18nField]
        """
        return self._url_rewrite

    @url_rewrite.setter
    def url_rewrite(self, url_rewrite):
        """
        Sets the url_rewrite of this Page.

        :param url_rewrite: The url_rewrite of this Page.
        :type: list[I18nField]
        """

        self._url_rewrite = url_rewrite

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
