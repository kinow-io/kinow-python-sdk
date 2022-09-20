# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.17
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DirectorProductRole(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, roles=None, id=None, reference=None, date_from=None, date_to=None, visible_before_publication=None, visible_after_publication=None, price=None, price_mode=None, position=None, active=None, available_for_order=None, date_add=None, date_upd=None, id_category_default=None, images=None, attributes=None, meta_description=None, meta_keywords=None, meta_title=None, link_rewrite=None, name=None, description=None, description_short=None, tags=None, can_buy=None, available_in_subscriptions=None, duration=None, type=None, group_restriction_behavior=None, geoloc_enabled=None, behavior_detected_countries=None, behavior_non_detected_countries=None, id_product_attribute=None, categories=None):
        """
        DirectorProductRole - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'roles': 'list[I18nField]',
            'id': 'int',
            'reference': 'str',
            'date_from': 'str',
            'date_to': 'str',
            'visible_before_publication': 'bool',
            'visible_after_publication': 'bool',
            'price': 'int',
            'price_mode': 'int',
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
            'tags': 'list[Tag]',
            'can_buy': 'bool',
            'available_in_subscriptions': 'bool',
            'duration': 'int',
            'type': 'str',
            'group_restriction_behavior': 'int',
            'geoloc_enabled': 'bool',
            'behavior_detected_countries': 'str',
            'behavior_non_detected_countries': 'str',
            'id_product_attribute': 'int',
            'categories': 'list[ProductCategories]'
        }

        self.attribute_map = {
            'roles': 'roles',
            'id': 'id',
            'reference': 'reference',
            'date_from': 'date_from',
            'date_to': 'date_to',
            'visible_before_publication': 'visible_before_publication',
            'visible_after_publication': 'visible_after_publication',
            'price': 'price',
            'price_mode': 'price_mode',
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
            'tags': 'tags',
            'can_buy': 'can_buy',
            'available_in_subscriptions': 'available_in_subscriptions',
            'duration': 'duration',
            'type': 'type',
            'group_restriction_behavior': 'group_restriction_behavior',
            'geoloc_enabled': 'geoloc_enabled',
            'behavior_detected_countries': 'behavior_detected_countries',
            'behavior_non_detected_countries': 'behavior_non_detected_countries',
            'id_product_attribute': 'id_product_attribute',
            'categories': 'categories'
        }

        self._roles = roles
        self._id = id
        self._reference = reference
        self._date_from = date_from
        self._date_to = date_to
        self._visible_before_publication = visible_before_publication
        self._visible_after_publication = visible_after_publication
        self._price = price
        self._price_mode = price_mode
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
        self._can_buy = can_buy
        self._available_in_subscriptions = available_in_subscriptions
        self._duration = duration
        self._type = type
        self._group_restriction_behavior = group_restriction_behavior
        self._geoloc_enabled = geoloc_enabled
        self._behavior_detected_countries = behavior_detected_countries
        self._behavior_non_detected_countries = behavior_non_detected_countries
        self._id_product_attribute = id_product_attribute
        self._categories = categories

    @property
    def roles(self):
        """
        Gets the roles of this DirectorProductRole.

        :return: The roles of this DirectorProductRole.
        :rtype: list[I18nField]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this DirectorProductRole.

        :param roles: The roles of this DirectorProductRole.
        :type: list[I18nField]
        """

        self._roles = roles

    @property
    def id(self):
        """
        Gets the id of this DirectorProductRole.

        :return: The id of this DirectorProductRole.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DirectorProductRole.

        :param id: The id of this DirectorProductRole.
        :type: int
        """

        self._id = id

    @property
    def reference(self):
        """
        Gets the reference of this DirectorProductRole.

        :return: The reference of this DirectorProductRole.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this DirectorProductRole.

        :param reference: The reference of this DirectorProductRole.
        :type: str
        """

        self._reference = reference

    @property
    def date_from(self):
        """
        Gets the date_from of this DirectorProductRole.

        :return: The date_from of this DirectorProductRole.
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """
        Sets the date_from of this DirectorProductRole.

        :param date_from: The date_from of this DirectorProductRole.
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """
        Gets the date_to of this DirectorProductRole.

        :return: The date_to of this DirectorProductRole.
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """
        Sets the date_to of this DirectorProductRole.

        :param date_to: The date_to of this DirectorProductRole.
        :type: str
        """

        self._date_to = date_to

    @property
    def visible_before_publication(self):
        """
        Gets the visible_before_publication of this DirectorProductRole.

        :return: The visible_before_publication of this DirectorProductRole.
        :rtype: bool
        """
        return self._visible_before_publication

    @visible_before_publication.setter
    def visible_before_publication(self, visible_before_publication):
        """
        Sets the visible_before_publication of this DirectorProductRole.

        :param visible_before_publication: The visible_before_publication of this DirectorProductRole.
        :type: bool
        """

        self._visible_before_publication = visible_before_publication

    @property
    def visible_after_publication(self):
        """
        Gets the visible_after_publication of this DirectorProductRole.

        :return: The visible_after_publication of this DirectorProductRole.
        :rtype: bool
        """
        return self._visible_after_publication

    @visible_after_publication.setter
    def visible_after_publication(self, visible_after_publication):
        """
        Sets the visible_after_publication of this DirectorProductRole.

        :param visible_after_publication: The visible_after_publication of this DirectorProductRole.
        :type: bool
        """

        self._visible_after_publication = visible_after_publication

    @property
    def price(self):
        """
        Gets the price of this DirectorProductRole.

        :return: The price of this DirectorProductRole.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this DirectorProductRole.

        :param price: The price of this DirectorProductRole.
        :type: int
        """

        self._price = price

    @property
    def price_mode(self):
        """
        Gets the price_mode of this DirectorProductRole.

        :return: The price_mode of this DirectorProductRole.
        :rtype: int
        """
        return self._price_mode

    @price_mode.setter
    def price_mode(self, price_mode):
        """
        Sets the price_mode of this DirectorProductRole.

        :param price_mode: The price_mode of this DirectorProductRole.
        :type: int
        """

        self._price_mode = price_mode

    @property
    def position(self):
        """
        Gets the position of this DirectorProductRole.

        :return: The position of this DirectorProductRole.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this DirectorProductRole.

        :param position: The position of this DirectorProductRole.
        :type: int
        """

        self._position = position

    @property
    def active(self):
        """
        Gets the active of this DirectorProductRole.

        :return: The active of this DirectorProductRole.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this DirectorProductRole.

        :param active: The active of this DirectorProductRole.
        :type: bool
        """

        self._active = active

    @property
    def available_for_order(self):
        """
        Gets the available_for_order of this DirectorProductRole.

        :return: The available_for_order of this DirectorProductRole.
        :rtype: bool
        """
        return self._available_for_order

    @available_for_order.setter
    def available_for_order(self, available_for_order):
        """
        Sets the available_for_order of this DirectorProductRole.

        :param available_for_order: The available_for_order of this DirectorProductRole.
        :type: bool
        """

        self._available_for_order = available_for_order

    @property
    def date_add(self):
        """
        Gets the date_add of this DirectorProductRole.

        :return: The date_add of this DirectorProductRole.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this DirectorProductRole.

        :param date_add: The date_add of this DirectorProductRole.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this DirectorProductRole.

        :return: The date_upd of this DirectorProductRole.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this DirectorProductRole.

        :param date_upd: The date_upd of this DirectorProductRole.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def id_category_default(self):
        """
        Gets the id_category_default of this DirectorProductRole.

        :return: The id_category_default of this DirectorProductRole.
        :rtype: int
        """
        return self._id_category_default

    @id_category_default.setter
    def id_category_default(self, id_category_default):
        """
        Sets the id_category_default of this DirectorProductRole.

        :param id_category_default: The id_category_default of this DirectorProductRole.
        :type: int
        """

        self._id_category_default = id_category_default

    @property
    def images(self):
        """
        Gets the images of this DirectorProductRole.

        :return: The images of this DirectorProductRole.
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this DirectorProductRole.

        :param images: The images of this DirectorProductRole.
        :type: list[Image]
        """

        self._images = images

    @property
    def attributes(self):
        """
        Gets the attributes of this DirectorProductRole.

        :return: The attributes of this DirectorProductRole.
        :rtype: list[ProductAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this DirectorProductRole.

        :param attributes: The attributes of this DirectorProductRole.
        :type: list[ProductAttribute]
        """

        self._attributes = attributes

    @property
    def meta_description(self):
        """
        Gets the meta_description of this DirectorProductRole.

        :return: The meta_description of this DirectorProductRole.
        :rtype: list[I18nField]
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """
        Sets the meta_description of this DirectorProductRole.

        :param meta_description: The meta_description of this DirectorProductRole.
        :type: list[I18nField]
        """

        self._meta_description = meta_description

    @property
    def meta_keywords(self):
        """
        Gets the meta_keywords of this DirectorProductRole.

        :return: The meta_keywords of this DirectorProductRole.
        :rtype: list[I18nField]
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """
        Sets the meta_keywords of this DirectorProductRole.

        :param meta_keywords: The meta_keywords of this DirectorProductRole.
        :type: list[I18nField]
        """

        self._meta_keywords = meta_keywords

    @property
    def meta_title(self):
        """
        Gets the meta_title of this DirectorProductRole.

        :return: The meta_title of this DirectorProductRole.
        :rtype: list[I18nField]
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """
        Sets the meta_title of this DirectorProductRole.

        :param meta_title: The meta_title of this DirectorProductRole.
        :type: list[I18nField]
        """

        self._meta_title = meta_title

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this DirectorProductRole.

        :return: The link_rewrite of this DirectorProductRole.
        :rtype: list[I18nField]
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this DirectorProductRole.

        :param link_rewrite: The link_rewrite of this DirectorProductRole.
        :type: list[I18nField]
        """

        self._link_rewrite = link_rewrite

    @property
    def name(self):
        """
        Gets the name of this DirectorProductRole.

        :return: The name of this DirectorProductRole.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DirectorProductRole.

        :param name: The name of this DirectorProductRole.
        :type: list[I18nField]
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DirectorProductRole.

        :return: The description of this DirectorProductRole.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DirectorProductRole.

        :param description: The description of this DirectorProductRole.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def description_short(self):
        """
        Gets the description_short of this DirectorProductRole.

        :return: The description_short of this DirectorProductRole.
        :rtype: list[I18nField]
        """
        return self._description_short

    @description_short.setter
    def description_short(self, description_short):
        """
        Sets the description_short of this DirectorProductRole.

        :param description_short: The description_short of this DirectorProductRole.
        :type: list[I18nField]
        """

        self._description_short = description_short

    @property
    def tags(self):
        """
        Gets the tags of this DirectorProductRole.

        :return: The tags of this DirectorProductRole.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this DirectorProductRole.

        :param tags: The tags of this DirectorProductRole.
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def can_buy(self):
        """
        Gets the can_buy of this DirectorProductRole.

        :return: The can_buy of this DirectorProductRole.
        :rtype: bool
        """
        return self._can_buy

    @can_buy.setter
    def can_buy(self, can_buy):
        """
        Sets the can_buy of this DirectorProductRole.

        :param can_buy: The can_buy of this DirectorProductRole.
        :type: bool
        """

        self._can_buy = can_buy

    @property
    def available_in_subscriptions(self):
        """
        Gets the available_in_subscriptions of this DirectorProductRole.

        :return: The available_in_subscriptions of this DirectorProductRole.
        :rtype: bool
        """
        return self._available_in_subscriptions

    @available_in_subscriptions.setter
    def available_in_subscriptions(self, available_in_subscriptions):
        """
        Sets the available_in_subscriptions of this DirectorProductRole.

        :param available_in_subscriptions: The available_in_subscriptions of this DirectorProductRole.
        :type: bool
        """

        self._available_in_subscriptions = available_in_subscriptions

    @property
    def duration(self):
        """
        Gets the duration of this DirectorProductRole.

        :return: The duration of this DirectorProductRole.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this DirectorProductRole.

        :param duration: The duration of this DirectorProductRole.
        :type: int
        """

        self._duration = duration

    @property
    def type(self):
        """
        Gets the type of this DirectorProductRole.

        :return: The type of this DirectorProductRole.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DirectorProductRole.

        :param type: The type of this DirectorProductRole.
        :type: str
        """

        self._type = type

    @property
    def group_restriction_behavior(self):
        """
        Gets the group_restriction_behavior of this DirectorProductRole.

        :return: The group_restriction_behavior of this DirectorProductRole.
        :rtype: int
        """
        return self._group_restriction_behavior

    @group_restriction_behavior.setter
    def group_restriction_behavior(self, group_restriction_behavior):
        """
        Sets the group_restriction_behavior of this DirectorProductRole.

        :param group_restriction_behavior: The group_restriction_behavior of this DirectorProductRole.
        :type: int
        """

        self._group_restriction_behavior = group_restriction_behavior

    @property
    def geoloc_enabled(self):
        """
        Gets the geoloc_enabled of this DirectorProductRole.

        :return: The geoloc_enabled of this DirectorProductRole.
        :rtype: bool
        """
        return self._geoloc_enabled

    @geoloc_enabled.setter
    def geoloc_enabled(self, geoloc_enabled):
        """
        Sets the geoloc_enabled of this DirectorProductRole.

        :param geoloc_enabled: The geoloc_enabled of this DirectorProductRole.
        :type: bool
        """

        self._geoloc_enabled = geoloc_enabled

    @property
    def behavior_detected_countries(self):
        """
        Gets the behavior_detected_countries of this DirectorProductRole.

        :return: The behavior_detected_countries of this DirectorProductRole.
        :rtype: str
        """
        return self._behavior_detected_countries

    @behavior_detected_countries.setter
    def behavior_detected_countries(self, behavior_detected_countries):
        """
        Sets the behavior_detected_countries of this DirectorProductRole.

        :param behavior_detected_countries: The behavior_detected_countries of this DirectorProductRole.
        :type: str
        """

        self._behavior_detected_countries = behavior_detected_countries

    @property
    def behavior_non_detected_countries(self):
        """
        Gets the behavior_non_detected_countries of this DirectorProductRole.

        :return: The behavior_non_detected_countries of this DirectorProductRole.
        :rtype: str
        """
        return self._behavior_non_detected_countries

    @behavior_non_detected_countries.setter
    def behavior_non_detected_countries(self, behavior_non_detected_countries):
        """
        Sets the behavior_non_detected_countries of this DirectorProductRole.

        :param behavior_non_detected_countries: The behavior_non_detected_countries of this DirectorProductRole.
        :type: str
        """

        self._behavior_non_detected_countries = behavior_non_detected_countries

    @property
    def id_product_attribute(self):
        """
        Gets the id_product_attribute of this DirectorProductRole.

        :return: The id_product_attribute of this DirectorProductRole.
        :rtype: int
        """
        return self._id_product_attribute

    @id_product_attribute.setter
    def id_product_attribute(self, id_product_attribute):
        """
        Sets the id_product_attribute of this DirectorProductRole.

        :param id_product_attribute: The id_product_attribute of this DirectorProductRole.
        :type: int
        """

        self._id_product_attribute = id_product_attribute

    @property
    def categories(self):
        """
        Gets the categories of this DirectorProductRole.

        :return: The categories of this DirectorProductRole.
        :rtype: list[ProductCategories]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this DirectorProductRole.

        :param categories: The categories of this DirectorProductRole.
        :type: list[ProductCategories]
        """

        self._categories = categories

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
