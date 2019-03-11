# coding: utf-8

"""
    Kinow API

    Public api for Kinow back office

    OpenAPI spec version: 1.0.75
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Director(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, date_add=None, date_upd=None, active=None, link_rewrite=None, description=None, image=None, description_short=None):
        """
        Director - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'date_add': 'str',
            'date_upd': 'str',
            'active': 'bool',
            'link_rewrite': 'list[I18nField]',
            'description': 'list[I18nField]',
            'image': 'str',
            'description_short': 'list[I18nField]'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'active': 'active',
            'link_rewrite': 'link_rewrite',
            'description': 'description',
            'image': 'image',
            'description_short': 'description_short'
        }

        self._id = id
        self._name = name
        self._date_add = date_add
        self._date_upd = date_upd
        self._active = active
        self._link_rewrite = link_rewrite
        self._description = description
        self._image = image
        self._description_short = description_short

    @property
    def id(self):
        """
        Gets the id of this Director.

        :return: The id of this Director.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Director.

        :param id: The id of this Director.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Director.

        :return: The name of this Director.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Director.

        :param name: The name of this Director.
        :type: str
        """

        self._name = name

    @property
    def date_add(self):
        """
        Gets the date_add of this Director.

        :return: The date_add of this Director.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this Director.

        :param date_add: The date_add of this Director.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this Director.

        :return: The date_upd of this Director.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this Director.

        :param date_upd: The date_upd of this Director.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def active(self):
        """
        Gets the active of this Director.

        :return: The active of this Director.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this Director.

        :param active: The active of this Director.
        :type: bool
        """

        self._active = active

    @property
    def link_rewrite(self):
        """
        Gets the link_rewrite of this Director.

        :return: The link_rewrite of this Director.
        :rtype: list[I18nField]
        """
        return self._link_rewrite

    @link_rewrite.setter
    def link_rewrite(self, link_rewrite):
        """
        Sets the link_rewrite of this Director.

        :param link_rewrite: The link_rewrite of this Director.
        :type: list[I18nField]
        """

        self._link_rewrite = link_rewrite

    @property
    def description(self):
        """
        Gets the description of this Director.

        :return: The description of this Director.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Director.

        :param description: The description of this Director.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def image(self):
        """
        Gets the image of this Director.

        :return: The image of this Director.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this Director.

        :param image: The image of this Director.
        :type: str
        """

        self._image = image

    @property
    def description_short(self):
        """
        Gets the description_short of this Director.

        :return: The description_short of this Director.
        :rtype: list[I18nField]
        """
        return self._description_short

    @description_short.setter
    def description_short(self, description_short):
        """
        Sets the description_short of this Director.

        :param description_short: The description_short of this Director.
        :type: list[I18nField]
        """

        self._description_short = description_short

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
