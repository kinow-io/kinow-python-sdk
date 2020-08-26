# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.4.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WidgetTopMenu(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, label=None, description=None, url=None, type=None, type_id=None, blank=None, unfold=None, position=None):
        """
        WidgetTopMenu - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'label': 'list[I18nField]',
            'description': 'list[I18nField]',
            'url': 'list[I18nField]',
            'type': 'str',
            'type_id': 'int',
            'blank': 'int',
            'unfold': 'int',
            'position': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'description': 'description',
            'url': 'url',
            'type': 'type',
            'type_id': 'type_id',
            'blank': 'blank',
            'unfold': 'unfold',
            'position': 'position'
        }

        self._id = id
        self._label = label
        self._description = description
        self._url = url
        self._type = type
        self._type_id = type_id
        self._blank = blank
        self._unfold = unfold
        self._position = position

    @property
    def id(self):
        """
        Gets the id of this WidgetTopMenu.
        

        :return: The id of this WidgetTopMenu.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WidgetTopMenu.
        

        :param id: The id of this WidgetTopMenu.
        :type: int
        """

        self._id = id

    @property
    def label(self):
        """
        Gets the label of this WidgetTopMenu.

        :return: The label of this WidgetTopMenu.
        :rtype: list[I18nField]
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this WidgetTopMenu.

        :param label: The label of this WidgetTopMenu.
        :type: list[I18nField]
        """

        self._label = label

    @property
    def description(self):
        """
        Gets the description of this WidgetTopMenu.

        :return: The description of this WidgetTopMenu.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WidgetTopMenu.

        :param description: The description of this WidgetTopMenu.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def url(self):
        """
        Gets the url of this WidgetTopMenu.

        :return: The url of this WidgetTopMenu.
        :rtype: list[I18nField]
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this WidgetTopMenu.

        :param url: The url of this WidgetTopMenu.
        :type: list[I18nField]
        """

        self._url = url

    @property
    def type(self):
        """
        Gets the type of this WidgetTopMenu.
        

        :return: The type of this WidgetTopMenu.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WidgetTopMenu.
        

        :param type: The type of this WidgetTopMenu.
        :type: str
        """

        self._type = type

    @property
    def type_id(self):
        """
        Gets the type_id of this WidgetTopMenu.
        

        :return: The type_id of this WidgetTopMenu.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this WidgetTopMenu.
        

        :param type_id: The type_id of this WidgetTopMenu.
        :type: int
        """

        self._type_id = type_id

    @property
    def blank(self):
        """
        Gets the blank of this WidgetTopMenu.
        

        :return: The blank of this WidgetTopMenu.
        :rtype: int
        """
        return self._blank

    @blank.setter
    def blank(self, blank):
        """
        Sets the blank of this WidgetTopMenu.
        

        :param blank: The blank of this WidgetTopMenu.
        :type: int
        """

        self._blank = blank

    @property
    def unfold(self):
        """
        Gets the unfold of this WidgetTopMenu.
        

        :return: The unfold of this WidgetTopMenu.
        :rtype: int
        """
        return self._unfold

    @unfold.setter
    def unfold(self, unfold):
        """
        Sets the unfold of this WidgetTopMenu.
        

        :param unfold: The unfold of this WidgetTopMenu.
        :type: int
        """

        self._unfold = unfold

    @property
    def position(self):
        """
        Gets the position of this WidgetTopMenu.
        

        :return: The position of this WidgetTopMenu.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this WidgetTopMenu.
        

        :param position: The position of this WidgetTopMenu.
        :type: int
        """

        self._position = position

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
