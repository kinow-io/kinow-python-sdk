# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.21
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Actor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, description_short=None, description=None, image=None, images=None, meta_title=None, meta_description=None, meta_keywords=None, link_rewrite=None, roles=None, active=None, date_add=None, date_upd=None):
        """
        Actor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'description_short': 'list[I18nField]',
            'description': 'list[I18nField]',
            'image': 'str',
            'images': 'list[Image]',
            'meta_title': 'list[I18nField]',
            'meta_description': 'list[I18nField]',
            'meta_keywords': 'list[I18nField]',
            'link_rewrite': 'list[I18nField]',
            'roles': 'list[I18nField]',
            'active': 'bool',
            'date_add': 'str',
            'date_upd': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description_short': 'description_short',
            'description': 'description',
            'image': 'image',
            'images': 'images',
            'meta_title': 'meta_title',
            'meta_description': 'meta_description',
            'meta_keywords': 'meta_keywords',
            'link_rewrite': 'link_rewrite',
            'roles': 'roles',
            'active': 'active',
            'date_add': 'date_add',
            'date_upd': 'date_upd'
        }

        self._id = id
        self._name = name
        self._description_short = description_short
        self._description = description
        self._image = image
        self._images = images
        self._meta_title = meta_title
        self._meta_description = meta_description
        self._meta_keywords = meta_keywords
        self._link_rewrite = link_rewrite
        self._roles = roles
        self._active = active
        self._date_add = date_add
        self._date_upd = date_upd

    @property
    def id(self):
        """
        Gets the id of this Actor.

        :return: The id of this Actor.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Actor.

        :param id: The id of this Actor.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Actor.

        :return: The name of this Actor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Actor.

        :param name: The name of this Actor.
        :type: str
        """

        self._name = name

    @property
    def description_short(self):
        """
        Gets the description_short of this Actor.

        :return: The description_short of this Actor.
        :rtype: list[I18nField]
        """
        return self._description_short

    @description_short.setter
    def description_short(self, description_short):
        """
        Sets the description_short of this Actor.

        :param description_short: The description_short of this Actor.
        :type: list[I18nField]
        """

        self._description_short = description_short

    @property
    def description(self):
        """
        Gets the description of this Actor.

        :return: The description of this Actor.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Actor.

        :param description: The description of this Actor.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def image(self):
        """
        Gets the image of this Actor.

        :return: The image of this Actor.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this Actor.

        :param image: The image of this Actor.
        :type: str
        """

        self._image = image

    @property
    def images(self):
        """
        Gets the images of this Actor.

        :return: The images of this Actor.
        :rtype: list[Image]
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this Actor.

        :param images: The images of this Actor.
        :type: list[Image]
        """

        self._images = images

    @property
    def meta_title(self):
        """
        Gets the meta_title of this Actor.

        :return: The meta_title of this Actor.
        :rtype: list[I18nField]
        """
        return self._meta_title

    @meta_title.setter
    def meta_title(self, meta_title):
        """
        Sets the meta_title of this Actor.

        :param meta_title: The meta_title of this Actor.
        :type: list[I18nField]
        """

        self._meta_title = meta_title

    @property
    def meta_description(self):
        """
        Gets the meta_description of this Actor.

        :return: The meta_description of this Actor.
        :rtype: list[I18nField]
        """
        return self._meta_description

    @meta_description.setter
    def meta_description(self, meta_description):
        """
        Sets the meta_description of this Actor.

        :param meta_description: The meta_description of this Actor.
        :type: list[I18nField]
        """

        self._meta_description = meta_description

    @property
    def meta_keywords(self):
        """
        Gets the meta_keywords of this Actor.

        :return: The meta_keywords of this Actor.
        :rtype: list[I18nField]
        """
        return self._meta_keywords

    @meta_keywords.setter
    def meta_keywords(self, meta_keywords):
        """
        Sets the meta_keywords of this Actor.

        :param meta_keywords: The meta_keywords of this Actor.
        :type: list[I18nField]
        """

        self._meta_keywords = meta_keywords

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this Actor.

        :return: The link_rewrite of this Actor.
        :rtype: list[I18nField]
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this Actor.

        :param link_rewrite: The link_rewrite of this Actor.
        :type: list[I18nField]
        """

        self._link_rewrite = link_rewrite

    @property
    def roles(self):
        """
        Gets the roles of this Actor.

        :return: The roles of this Actor.
        :rtype: list[I18nField]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """
        Sets the roles of this Actor.

        :param roles: The roles of this Actor.
        :type: list[I18nField]
        """

        self._roles = roles

    @property
    def active(self):
        """
        Gets the active of this Actor.

        :return: The active of this Actor.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Actor.

        :param active: The active of this Actor.
        :type: bool
        """

        self._active = active

    @property
    def date_add(self):
        """
        Gets the date_add of this Actor.

        :return: The date_add of this Actor.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this Actor.

        :param date_add: The date_add of this Actor.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this Actor.

        :return: The date_upd of this Actor.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this Actor.

        :param date_upd: The date_upd of this Actor.
        :type: str
        """

        self._date_upd = date_upd

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
