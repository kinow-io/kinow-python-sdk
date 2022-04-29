# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.9
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateProductRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description_short=None, description=None, meta_title=None, meta_description=None, meta_keywords=None, link_rewrite=None, active=None, reference=None, date_from=None, date_to=None, availability_before=None, availability_after=None, id_category_default=None, tags=None):
        """
        UpdateProductRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'list[I18nFieldInput]',
            'description_short': 'list[I18nFieldInput]',
            'description': 'list[I18nFieldInput]',
            'meta_title': 'list[I18nFieldInput]',
            'meta_description': 'list[I18nFieldInput]',
            'meta_keywords': 'list[I18nFieldInput]',
            'link_rewrite': 'list[I18nFieldInput]',
            'active': 'bool',
            'reference': 'str',
            'date_from': 'str',
            'date_to': 'str',
            'availability_before': 'int',
            'availability_after': 'int',
            'id_category_default': 'int',
            'tags': 'list[I18nField]'
        }

        self.attribute_map = {
            'name': 'name',
            'description_short': 'description_short',
            'description': 'description',
            'meta_title': 'meta_title',
            'meta_description': 'meta_description',
            'meta_keywords': 'meta_keywords',
            'link_rewrite': 'link_rewrite',
            'active': 'active',
            'reference': 'reference',
            'date_from': 'date_from',
            'date_to': 'date_to',
            'availability_before': 'availability_before',
            'availability_after': 'availability_after',
            'id_category_default': 'id_category_default',
            'tags': 'tags'
        }

        self._name = name
        self._description_short = description_short
        self._description = description
        self._meta_title = meta_title
        self._meta_description = meta_description
        self._meta_keywords = meta_keywords
        self._link_rewrite = link_rewrite
        self._active = active
        self._reference = reference
        self._date_from = date_from
        self._date_to = date_to
        self._availability_before = availability_before
        self._availability_after = availability_after
        self._id_category_default = id_category_default
        self._tags = tags

    @property
    def name(self):
        """
        Gets the name of this UpdateProductRequest.

        :return: The name of this UpdateProductRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UpdateProductRequest.

        :param name: The name of this UpdateProductRequest.
        :type: list[I18nFieldInput]
        """

        self._name = name

    @property
    def description_short(self):
        """
        Gets the description_short of this UpdateProductRequest.

        :return: The description_short of this UpdateProductRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._description_short

    @description_short.setter
    def description_short(self, description_short):
        """
        Sets the description_short of this UpdateProductRequest.

        :param description_short: The description_short of this UpdateProductRequest.
        :type: list[I18nFieldInput]
        """

        self._description_short = description_short

    @property
    def description(self):
        """
        Gets the description of this UpdateProductRequest.

        :return: The description of this UpdateProductRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateProductRequest.

        :param description: The description of this UpdateProductRequest.
        :type: list[I18nFieldInput]
        """

        self._description = description

    @property
    def meta_title(self):
        """
        Gets the meta_title of this UpdateProductRequest.

        :return: The meta_title of this UpdateProductRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """
        Sets the meta_title of this UpdateProductRequest.

        :param meta_title: The meta_title of this UpdateProductRequest.
        :type: list[I18nFieldInput]
        """

        self._meta_title = meta_title

    @property
    def meta_description(self):
        """
        Gets the meta_description of this UpdateProductRequest.

        :return: The meta_description of this UpdateProductRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """
        Sets the meta_description of this UpdateProductRequest.

        :param meta_description: The meta_description of this UpdateProductRequest.
        :type: list[I18nFieldInput]
        """

        self._meta_description = meta_description

    @property
    def meta_keywords(self):
        """
        Gets the meta_keywords of this UpdateProductRequest.

        :return: The meta_keywords of this UpdateProductRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """
        Sets the meta_keywords of this UpdateProductRequest.

        :param meta_keywords: The meta_keywords of this UpdateProductRequest.
        :type: list[I18nFieldInput]
        """

        self._meta_keywords = meta_keywords

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this UpdateProductRequest.

        :return: The link_rewrite of this UpdateProductRequest.
        :rtype: list[I18nFieldInput]
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this UpdateProductRequest.

        :param link_rewrite: The link_rewrite of this UpdateProductRequest.
        :type: list[I18nFieldInput]
        """

        self._link_rewrite = link_rewrite

    @property
    def active(self):
        """
        Gets the active of this UpdateProductRequest.

        :return: The active of this UpdateProductRequest.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this UpdateProductRequest.

        :param active: The active of this UpdateProductRequest.
        :type: bool
        """

        self._active = active

    @property
    def reference(self):
        """
        Gets the reference of this UpdateProductRequest.

        :return: The reference of this UpdateProductRequest.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this UpdateProductRequest.

        :param reference: The reference of this UpdateProductRequest.
        :type: str
        """

        self._reference = reference

    @property
    def date_from(self):
        """
        Gets the date_from of this UpdateProductRequest.

        :return: The date_from of this UpdateProductRequest.
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """
        Sets the date_from of this UpdateProductRequest.

        :param date_from: The date_from of this UpdateProductRequest.
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """
        Gets the date_to of this UpdateProductRequest.

        :return: The date_to of this UpdateProductRequest.
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """
        Sets the date_to of this UpdateProductRequest.

        :param date_to: The date_to of this UpdateProductRequest.
        :type: str
        """

        self._date_to = date_to

    @property
    def availability_before(self):
        """
        Gets the availability_before of this UpdateProductRequest.
        Value can be 1, 2 or 3

        :return: The availability_before of this UpdateProductRequest.
        :rtype: int
        """
        return self._availability_before

    @availability_before.setter
    def availability_before(self, availability_before):
        """
        Sets the availability_before of this UpdateProductRequest.
        Value can be 1, 2 or 3

        :param availability_before: The availability_before of this UpdateProductRequest.
        :type: int
        """

        self._availability_before = availability_before

    @property
    def availability_after(self):
        """
        Gets the availability_after of this UpdateProductRequest.
        Value can be 1, 2 or 3

        :return: The availability_after of this UpdateProductRequest.
        :rtype: int
        """
        return self._availability_after

    @availability_after.setter
    def availability_after(self, availability_after):
        """
        Sets the availability_after of this UpdateProductRequest.
        Value can be 1, 2 or 3

        :param availability_after: The availability_after of this UpdateProductRequest.
        :type: int
        """

        self._availability_after = availability_after

    @property
    def id_category_default(self):
        """
        Gets the id_category_default of this UpdateProductRequest.

        :return: The id_category_default of this UpdateProductRequest.
        :rtype: int
        """
        return self._id_category_default

    @id_category_default.setter
    def id_category_default(self, id_category_default):
        """
        Sets the id_category_default of this UpdateProductRequest.

        :param id_category_default: The id_category_default of this UpdateProductRequest.
        :type: int
        """

        self._id_category_default = id_category_default

    @property
    def tags(self):
        """
        Gets the tags of this UpdateProductRequest.

        :return: The tags of this UpdateProductRequest.
        :rtype: list[I18nField]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this UpdateProductRequest.

        :param tags: The tags of this UpdateProductRequest.
        :type: list[I18nField]
        """

        self._tags = tags

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
