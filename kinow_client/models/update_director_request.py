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


class UpdateDirectorRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description_short=None, description=None, meta_title=None, meta_description=None, meta_keywords=None, link_rewrite=None, active=None):
        """
        UpdateDirectorRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'description_short': 'list[I18nFieldInput]',
            'description': 'list[I18nFieldInput]',
            'meta_title': 'list[I18nFieldInput]',
            'meta_description': 'list[I18nFieldInput]',
            'meta_keywords': 'list[I18nFieldInput]',
            'link_rewrite': 'list[I18nFieldInput]',
            'active': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'description_short': 'description_short',
            'description': 'description',
            'meta_title': 'meta_title',
            'meta_description': 'meta_description',
            'meta_keywords': 'meta_keywords',
            'link_rewrite': 'link_rewrite',
            'active': 'active'
        }

        self._name = name
        self._description_short = description_short
        self._description = description
        self._meta_title = meta_title
        self._meta_description = meta_description
        self._meta_keywords = meta_keywords
        self._link_rewrite = link_rewrite
        self._active = active

    @property
    def name(self):
        """
        Gets the name of this UpdateDirectorRequest.

        :return: The name of this UpdateDirectorRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateDirectorRequest.

        :param name: The name of this UpdateDirectorRequest.
        :type: str
        """

        self._name = name

    @property
    def description_short(self):
        """
        Gets the description_short of this UpdateDirectorRequest.

        :return: The description_short of this UpdateDirectorRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._description_short

    @description_short.setter
    def description_short(self, description_short):
        """
        Sets the description_short of this UpdateDirectorRequest.

        :param description_short: The description_short of this UpdateDirectorRequest.
        :type: list[I18nFieldInput]
        """

        self._description_short = description_short

    @property
    def description(self):
        """
        Gets the description of this UpdateDirectorRequest.

        :return: The description of this UpdateDirectorRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateDirectorRequest.

        :param description: The description of this UpdateDirectorRequest.
        :type: list[I18nFieldInput]
        """

        self._description = description

    @property
    def meta_title(self):
        """
        Gets the meta_title of this UpdateDirectorRequest.

        :return: The meta_title of this UpdateDirectorRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """
        Sets the meta_title of this UpdateDirectorRequest.

        :param meta_title: The meta_title of this UpdateDirectorRequest.
        :type: list[I18nFieldInput]
        """

        self._meta_title = meta_title

    @property
    def meta_description(self):
        """
        Gets the meta_description of this UpdateDirectorRequest.

        :return: The meta_description of this UpdateDirectorRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """
        Sets the meta_description of this UpdateDirectorRequest.

        :param meta_description: The meta_description of this UpdateDirectorRequest.
        :type: list[I18nFieldInput]
        """

        self._meta_description = meta_description

    @property
    def meta_keywords(self):
        """
        Gets the meta_keywords of this UpdateDirectorRequest.

        :return: The meta_keywords of this UpdateDirectorRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """
        Sets the meta_keywords of this UpdateDirectorRequest.

        :param meta_keywords: The meta_keywords of this UpdateDirectorRequest.
        :type: list[I18nFieldInput]
        """

        self._meta_keywords = meta_keywords

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this UpdateDirectorRequest.

        :return: The link_rewrite of this UpdateDirectorRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this UpdateDirectorRequest.

        :param link_rewrite: The link_rewrite of this UpdateDirectorRequest.
        :type: list[I18nFieldInput]
        """

        self._link_rewrite = link_rewrite

    @property
    def active(self):
        """
        Gets the active of this UpdateDirectorRequest.

        :return: The active of this UpdateDirectorRequest.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this UpdateDirectorRequest.

        :param active: The active of this UpdateDirectorRequest.
        :type: bool
        """

        self._active = active

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
