# coding: utf-8

"""
    Kaemo API

    Public api for Kaemo back office

    OpenAPI spec version: 1.0.19
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Product(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, reference=None, date_from=None, date_to=None, price=None, position=None, active=None, available_for_order=None, date_add=None, date_upd=None, id_category_default=None, images=None, attributes=None, meta_description=None, meta_keywords=None, meta_title=None, link_rewrite=None, name=None, description=None, description_short=None, tags=None):
        """
        Product - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'reference': 'str',
            'date_from': 'str',
            'date_to': 'str',
            'price': 'float',
            'position': 'int',
            'active': 'bool',
            'available_for_order': 'bool',
            'date_add': 'str',
            'date_upd': 'str',
            'id_category_default': 'int',
            'images': 'list[Image]',
            'attributes': 'list[ProductAttribute]',
            'meta_description': 'list[I18nField]',
            'meta_keywords': 'list[I18nField]',
            'meta_title': 'list[I18nField]',
            'link_rewrite': 'list[I18nField]',
            'name': 'list[I18nField]',
            'description': 'list[I18nField]',
            'description_short': 'list[I18nField]',
            'tags': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'reference': 'reference',
            'date_from': 'date_from',
            'date_to': 'date_to',
            'price': 'price',
            'position': 'position',
            'active': 'active',
            'available_for_order': 'available_for_order',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'id_category_default': 'id_category_default',
            'images': 'images',
            'attributes': 'attributes',
            'meta_description': 'meta_description',
            'meta_keywords': 'meta_keywords',
            'meta_title': 'meta_title',
            'link_rewrite': 'link_rewrite',
            'name': 'name',
            'description': 'description',
            'description_short': 'description_short',
            'tags': 'tags'
        }

        self._id = id
        self._reference = reference
        self._date_from = date_from
        self._date_to = date_to
        self._price = price
        self._position = position
        self._active = active
        self._available_for_order = available_for_order
        self._date_add = date_add
        self._date_upd = date_upd
        self._id_category_default = id_category_default
        self._images = images
        self._attributes = attributes
        self._meta_description = meta_description
        self._meta_keywords = meta_keywords
        self._meta_title = meta_title
        self._link_rewrite = link_rewrite
        self._name = name
        self._description = description
        self._description_short = description_short
        self._tags = tags

    @property
    def id(self):
        """
        Gets the id of this Product.

        :return: The id of this Product.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Product.

        :param id: The id of this Product.
        :type: int
        """

        self._id = id

    @property
    def reference(self):
        """
        Gets the reference of this Product.

        :return: The reference of this Product.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this Product.

        :param reference: The reference of this Product.
        :type: str
        """

        self._reference = reference

    @property
    def date_from(self):
        """
        Gets the date_from of this Product.

        :return: The date_from of this Product.
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """
        Sets the date_from of this Product.

        :param date_from: The date_from of this Product.
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """
        Gets the date_to of this Product.

        :return: The date_to of this Product.
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """
        Sets the date_to of this Product.

        :param date_to: The date_to of this Product.
        :type: str
        """

        self._date_to = date_to

    @property
    def price(self):
        """
        Gets the price of this Product.

        :return: The price of this Product.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this Product.

        :param price: The price of this Product.
        :type: float
        """

        self._price = price

    @property
    def position(self):
        """
        Gets the position of this Product.

        :return: The position of this Product.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this Product.

        :param position: The position of this Product.
        :type: int
        """

        self._position = position

    @property
    def active(self):
        """
        Gets the active of this Product.

        :return: The active of this Product.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Product.

        :param active: The active of this Product.
        :type: bool
        """

        self._active = active

    @property
    def available_for_order(self):
        """
        Gets the available_for_order of this Product.

        :return: The available_for_order of this Product.
        :rtype: bool
        """
        return self._available_for_order

    @available_for_order.setter
    def available_for_order(self, available_for_order):
        """
        Sets the available_for_order of this Product.

        :param available_for_order: The available_for_order of this Product.
        :type: bool
        """

        self._available_for_order = available_for_order

    @property
    def date_add(self):
        """
        Gets the date_add of this Product.

        :return: The date_add of this Product.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this Product.

        :param date_add: The date_add of this Product.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this Product.

        :return: The date_upd of this Product.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this Product.

        :param date_upd: The date_upd of this Product.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def id_category_default(self):
        """
        Gets the id_category_default of this Product.

        :return: The id_category_default of this Product.
        :rtype: int
        """
        return self._id_category_default

    @id_category_default.setter
    def id_category_default(self, id_category_default):
        """
        Sets the id_category_default of this Product.

        :param id_category_default: The id_category_default of this Product.
        :type: int
        """

        self._id_category_default = id_category_default

    @property
    def images(self):
        """
        Gets the images of this Product.

        :return: The images of this Product.
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this Product.

        :param images: The images of this Product.
        :type: list[Image]
        """

        self._images = images

    @property
    def attributes(self):
        """
        Gets the attributes of this Product.

        :return: The attributes of this Product.
        :rtype: list[ProductAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this Product.

        :param attributes: The attributes of this Product.
        :type: list[ProductAttribute]
        """

        self._attributes = attributes

    @property
    def meta_description(self):
        """
        Gets the meta_description of this Product.

        :return: The meta_description of this Product.
        :rtype: list[I18nField]
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """
        Sets the meta_description of this Product.

        :param meta_description: The meta_description of this Product.
        :type: list[I18nField]
        """

        self._meta_description = meta_description

    @property
    def meta_keywords(self):
        """
        Gets the meta_keywords of this Product.

        :return: The meta_keywords of this Product.
        :rtype: list[I18nField]
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """
        Sets the meta_keywords of this Product.

        :param meta_keywords: The meta_keywords of this Product.
        :type: list[I18nField]
        """

        self._meta_keywords = meta_keywords

    @property
    def meta_title(self):
        """
        Gets the meta_title of this Product.

        :return: The meta_title of this Product.
        :rtype: list[I18nField]
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """
        Sets the meta_title of this Product.

        :param meta_title: The meta_title of this Product.
        :type: list[I18nField]
        """

        self._meta_title = meta_title

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this Product.

        :return: The link_rewrite of this Product.
        :rtype: list[I18nField]
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this Product.

        :param link_rewrite: The link_rewrite of this Product.
        :type: list[I18nField]
        """

        self._link_rewrite = link_rewrite

    @property
    def name(self):
        """
        Gets the name of this Product.

        :return: The name of this Product.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Product.

        :param name: The name of this Product.
        :type: list[I18nField]
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Product.

        :return: The description of this Product.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Product.

        :param description: The description of this Product.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def description_short(self):
        """
        Gets the description_short of this Product.

        :return: The description_short of this Product.
        :rtype: list[I18nField]
        """
        return self._description_short

    @description_short.setter
    def description_short(self, description_short):
        """
        Sets the description_short of this Product.

        :param description_short: The description_short of this Product.
        :type: list[I18nField]
        """

        self._description_short = description_short

    @property
    def tags(self):
        """
        Gets the tags of this Product.

        :return: The tags of this Product.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Product.

        :param tags: The tags of this Product.
        :type: str
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
