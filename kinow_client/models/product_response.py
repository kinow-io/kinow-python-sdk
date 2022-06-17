# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description_short=None, description=None, meta_title=None, meta_description=None, meta_keywords=None, link_rewrite=None, active=None, id=None, reference=None, date_from=None, date_to=None, visible_before_publication=None, visible_after_publication=None, price=None, price_mode=None, position=None, available_for_order=None, date_add=None, date_upd=None, id_category_default=None, images=None, attributes=None, tags=None, can_buy=None, available_in_subscriptions=None, duration=None, type=None, group_restriction_behavior=None, geoloc_enabled=None, behavior_detected_countries=None, behavior_non_detected_countries=None, id_product_attribute=None, roles=None, categories=None):
        """
        ProductResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'list[I18nField]',
            'description_short': 'list[I18nField]',
            'description': 'list[I18nField]',
            'meta_title': 'list[I18nField]',
            'meta_description': 'list[I18nField]',
            'meta_keywords': 'list[I18nField]',
            'link_rewrite': 'list[I18nField]',
            'active': 'bool',
            'id': 'int',
            'reference': 'str',
            'date_from': 'str',
            'date_to': 'str',
            'visible_before_publication': 'bool',
            'visible_after_publication': 'bool',
            'price': 'int',
            'price_mode': 'int',
            'position': 'int',
            'available_for_order': 'bool',
            'date_add': 'str',
            'date_upd': 'str',
            'id_category_default': 'int',
            'images': 'list[Image]',
            'attributes': 'list[ProductAttribute]',
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
            'roles': 'str',
            'categories': 'list[ProductCategories]'
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
            'id': 'id',
            'reference': 'reference',
            'date_from': 'date_from',
            'date_to': 'date_to',
            'visible_before_publication': 'visible_before_publication',
            'visible_after_publication': 'visible_after_publication',
            'price': 'price',
            'price_mode': 'price_mode',
            'position': 'position',
            'available_for_order': 'available_for_order',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'id_category_default': 'id_category_default',
            'images': 'images',
            'attributes': 'attributes',
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
            'roles': 'roles',
            'categories': 'categories'
        }

        self._name = name
        self._description_short = description_short
        self._description = description
        self._meta_title = meta_title
        self._meta_description = meta_description
        self._meta_keywords = meta_keywords
        self._link_rewrite = link_rewrite
        self._active = active
        self._id = id
        self._reference = reference
        self._date_from = date_from
        self._date_to = date_to
        self._visible_before_publication = visible_before_publication
        self._visible_after_publication = visible_after_publication
        self._price = price
        self._price_mode = price_mode
        self._position = position
        self._available_for_order = available_for_order
        self._date_add = date_add
        self._date_upd = date_upd
        self._id_category_default = id_category_default
        self._images = images
        self._attributes = attributes
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
        self._roles = roles
        self._categories = categories

    @property
    def name(self):
        """
        Gets the name of this ProductResponse.

        :return: The name of this ProductResponse.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProductResponse.

        :param name: The name of this ProductResponse.
        :type: list[I18nField]
        """

        self._name = name

    @property
    def description_short(self):
        """
        Gets the description_short of this ProductResponse.

        :return: The description_short of this ProductResponse.
        :rtype: list[I18nField]
        """
        return self._description_short

    @description_short.setter
    def description_short(self, description_short):
        """
        Sets the description_short of this ProductResponse.

        :param description_short: The description_short of this ProductResponse.
        :type: list[I18nField]
        """

        self._description_short = description_short

    @property
    def description(self):
        """
        Gets the description of this ProductResponse.

        :return: The description of this ProductResponse.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProductResponse.

        :param description: The description of this ProductResponse.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def meta_title(self):
        """
        Gets the meta_title of this ProductResponse.

        :return: The meta_title of this ProductResponse.
        :rtype: list[I18nField]
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """
        Sets the meta_title of this ProductResponse.

        :param meta_title: The meta_title of this ProductResponse.
        :type: list[I18nField]
        """

        self._meta_title = meta_title

    @property
    def meta_description(self):
        """
        Gets the meta_description of this ProductResponse.

        :return: The meta_description of this ProductResponse.
        :rtype: list[I18nField]
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """
        Sets the meta_description of this ProductResponse.

        :param meta_description: The meta_description of this ProductResponse.
        :type: list[I18nField]
        """

        self._meta_description = meta_description

    @property
    def meta_keywords(self):
        """
        Gets the meta_keywords of this ProductResponse.

        :return: The meta_keywords of this ProductResponse.
        :rtype: list[I18nField]
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """
        Sets the meta_keywords of this ProductResponse.

        :param meta_keywords: The meta_keywords of this ProductResponse.
        :type: list[I18nField]
        """

        self._meta_keywords = meta_keywords

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this ProductResponse.

        :return: The link_rewrite of this ProductResponse.
        :rtype: list[I18nField]
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this ProductResponse.

        :param link_rewrite: The link_rewrite of this ProductResponse.
        :type: list[I18nField]
        """

        self._link_rewrite = link_rewrite

    @property
    def active(self):
        """
        Gets the active of this ProductResponse.

        :return: The active of this ProductResponse.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ProductResponse.

        :param active: The active of this ProductResponse.
        :type: bool
        """

        self._active = active

    @property
    def id(self):
        """
        Gets the id of this ProductResponse.

        :return: The id of this ProductResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductResponse.

        :param id: The id of this ProductResponse.
        :type: int
        """

        self._id = id

    @property
    def reference(self):
        """
        Gets the reference of this ProductResponse.

        :return: The reference of this ProductResponse.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this ProductResponse.

        :param reference: The reference of this ProductResponse.
        :type: str
        """

        self._reference = reference

    @property
    def date_from(self):
        """
        Gets the date_from of this ProductResponse.

        :return: The date_from of this ProductResponse.
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """
        Sets the date_from of this ProductResponse.

        :param date_from: The date_from of this ProductResponse.
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """
        Gets the date_to of this ProductResponse.

        :return: The date_to of this ProductResponse.
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """
        Sets the date_to of this ProductResponse.

        :param date_to: The date_to of this ProductResponse.
        :type: str
        """

        self._date_to = date_to

    @property
    def visible_before_publication(self):
        """
        Gets the visible_before_publication of this ProductResponse.

        :return: The visible_before_publication of this ProductResponse.
        :rtype: bool
        """
        return self._visible_before_publication

    @visible_before_publication.setter
    def visible_before_publication(self, visible_before_publication):
        """
        Sets the visible_before_publication of this ProductResponse.

        :param visible_before_publication: The visible_before_publication of this ProductResponse.
        :type: bool
        """

        self._visible_before_publication = visible_before_publication

    @property
    def visible_after_publication(self):
        """
        Gets the visible_after_publication of this ProductResponse.

        :return: The visible_after_publication of this ProductResponse.
        :rtype: bool
        """
        return self._visible_after_publication

    @visible_after_publication.setter
    def visible_after_publication(self, visible_after_publication):
        """
        Sets the visible_after_publication of this ProductResponse.

        :param visible_after_publication: The visible_after_publication of this ProductResponse.
        :type: bool
        """

        self._visible_after_publication = visible_after_publication

    @property
    def price(self):
        """
        Gets the price of this ProductResponse.

        :return: The price of this ProductResponse.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ProductResponse.

        :param price: The price of this ProductResponse.
        :type: int
        """

        self._price = price

    @property
    def price_mode(self):
        """
        Gets the price_mode of this ProductResponse.

        :return: The price_mode of this ProductResponse.
        :rtype: int
        """
        return self._price_mode

    @price_mode.setter
    def price_mode(self, price_mode):
        """
        Sets the price_mode of this ProductResponse.

        :param price_mode: The price_mode of this ProductResponse.
        :type: int
        """

        self._price_mode = price_mode

    @property
    def position(self):
        """
        Gets the position of this ProductResponse.

        :return: The position of this ProductResponse.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this ProductResponse.

        :param position: The position of this ProductResponse.
        :type: int
        """

        self._position = position

    @property
    def available_for_order(self):
        """
        Gets the available_for_order of this ProductResponse.

        :return: The available_for_order of this ProductResponse.
        :rtype: bool
        """
        return self._available_for_order

    @available_for_order.setter
    def available_for_order(self, available_for_order):
        """
        Sets the available_for_order of this ProductResponse.

        :param available_for_order: The available_for_order of this ProductResponse.
        :type: bool
        """

        self._available_for_order = available_for_order

    @property
    def date_add(self):
        """
        Gets the date_add of this ProductResponse.

        :return: The date_add of this ProductResponse.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this ProductResponse.

        :param date_add: The date_add of this ProductResponse.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this ProductResponse.

        :return: The date_upd of this ProductResponse.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this ProductResponse.

        :param date_upd: The date_upd of this ProductResponse.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def id_category_default(self):
        """
        Gets the id_category_default of this ProductResponse.

        :return: The id_category_default of this ProductResponse.
        :rtype: int
        """
        return self._id_category_default

    @id_category_default.setter
    def id_category_default(self, id_category_default):
        """
        Sets the id_category_default of this ProductResponse.

        :param id_category_default: The id_category_default of this ProductResponse.
        :type: int
        """

        self._id_category_default = id_category_default

    @property
    def images(self):
        """
        Gets the images of this ProductResponse.

        :return: The images of this ProductResponse.
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this ProductResponse.

        :param images: The images of this ProductResponse.
        :type: list[Image]
        """

        self._images = images

    @property
    def attributes(self):
        """
        Gets the attributes of this ProductResponse.

        :return: The attributes of this ProductResponse.
        :rtype: list[ProductAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this ProductResponse.

        :param attributes: The attributes of this ProductResponse.
        :type: list[ProductAttribute]
        """

        self._attributes = attributes

    @property
    def tags(self):
        """
        Gets the tags of this ProductResponse.

        :return: The tags of this ProductResponse.
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ProductResponse.

        :param tags: The tags of this ProductResponse.
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def can_buy(self):
        """
        Gets the can_buy of this ProductResponse.

        :return: The can_buy of this ProductResponse.
        :rtype: bool
        """
        return self._can_buy

    @can_buy.setter
    def can_buy(self, can_buy):
        """
        Sets the can_buy of this ProductResponse.

        :param can_buy: The can_buy of this ProductResponse.
        :type: bool
        """

        self._can_buy = can_buy

    @property
    def available_in_subscriptions(self):
        """
        Gets the available_in_subscriptions of this ProductResponse.

        :return: The available_in_subscriptions of this ProductResponse.
        :rtype: bool
        """
        return self._available_in_subscriptions

    @available_in_subscriptions.setter
    def available_in_subscriptions(self, available_in_subscriptions):
        """
        Sets the available_in_subscriptions of this ProductResponse.

        :param available_in_subscriptions: The available_in_subscriptions of this ProductResponse.
        :type: bool
        """

        self._available_in_subscriptions = available_in_subscriptions

    @property
    def duration(self):
        """
        Gets the duration of this ProductResponse.

        :return: The duration of this ProductResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this ProductResponse.

        :param duration: The duration of this ProductResponse.
        :type: int
        """

        self._duration = duration

    @property
    def type(self):
        """
        Gets the type of this ProductResponse.

        :return: The type of this ProductResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProductResponse.

        :param type: The type of this ProductResponse.
        :type: str
        """

        self._type = type

    @property
    def group_restriction_behavior(self):
        """
        Gets the group_restriction_behavior of this ProductResponse.

        :return: The group_restriction_behavior of this ProductResponse.
        :rtype: int
        """
        return self._group_restriction_behavior

    @group_restriction_behavior.setter
    def group_restriction_behavior(self, group_restriction_behavior):
        """
        Sets the group_restriction_behavior of this ProductResponse.

        :param group_restriction_behavior: The group_restriction_behavior of this ProductResponse.
        :type: int
        """

        self._group_restriction_behavior = group_restriction_behavior

    @property
    def geoloc_enabled(self):
        """
        Gets the geoloc_enabled of this ProductResponse.

        :return: The geoloc_enabled of this ProductResponse.
        :rtype: bool
        """
        return self._geoloc_enabled

    @geoloc_enabled.setter
    def geoloc_enabled(self, geoloc_enabled):
        """
        Sets the geoloc_enabled of this ProductResponse.

        :param geoloc_enabled: The geoloc_enabled of this ProductResponse.
        :type: bool
        """

        self._geoloc_enabled = geoloc_enabled

    @property
    def behavior_detected_countries(self):
        """
        Gets the behavior_detected_countries of this ProductResponse.

        :return: The behavior_detected_countries of this ProductResponse.
        :rtype: str
        """
        return self._behavior_detected_countries

    @behavior_detected_countries.setter
    def behavior_detected_countries(self, behavior_detected_countries):
        """
        Sets the behavior_detected_countries of this ProductResponse.

        :param behavior_detected_countries: The behavior_detected_countries of this ProductResponse.
        :type: str
        """

        self._behavior_detected_countries = behavior_detected_countries

    @property
    def behavior_non_detected_countries(self):
        """
        Gets the behavior_non_detected_countries of this ProductResponse.

        :return: The behavior_non_detected_countries of this ProductResponse.
        :rtype: str
        """
        return self._behavior_non_detected_countries

    @behavior_non_detected_countries.setter
    def behavior_non_detected_countries(self, behavior_non_detected_countries):
        """
        Sets the behavior_non_detected_countries of this ProductResponse.

        :param behavior_non_detected_countries: The behavior_non_detected_countries of this ProductResponse.
        :type: str
        """

        self._behavior_non_detected_countries = behavior_non_detected_countries

    @property
    def id_product_attribute(self):
        """
        Gets the id_product_attribute of this ProductResponse.

        :return: The id_product_attribute of this ProductResponse.
        :rtype: int
        """
        return self._id_product_attribute

    @id_product_attribute.setter
    def id_product_attribute(self, id_product_attribute):
        """
        Sets the id_product_attribute of this ProductResponse.

        :param id_product_attribute: The id_product_attribute of this ProductResponse.
        :type: int
        """

        self._id_product_attribute = id_product_attribute

    @property
    def roles(self):
        """
        Gets the roles of this ProductResponse.

        :return: The roles of this ProductResponse.
        :rtype: str
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this ProductResponse.

        :param roles: The roles of this ProductResponse.
        :type: str
        """

        self._roles = roles

    @property
    def categories(self):
        """
        Gets the categories of this ProductResponse.

        :return: The categories of this ProductResponse.
        :rtype: list[ProductCategories]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """
        Sets the categories of this ProductResponse.

        :param categories: The categories of this ProductResponse.
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
