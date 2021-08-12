# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.46
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WidgetFooterMenu(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, label=None, url=None, column=None, type=None, type_id=None, blank=None, position=None):
        """
        WidgetFooterMenu - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'label': 'list[I18nField]',
            'url': 'list[I18nField]',
            'column': 'str',
            'type': 'str',
            'type_id': 'int',
            'blank': 'int',
            'position': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'url': 'url',
            'column': 'column',
            'type': 'type',
            'type_id': 'type_id',
            'blank': 'blank',
            'position': 'position'
        }

        self._id = id
        self._label = label
        self._url = url
        self._column = column
        self._type = type
        self._type_id = type_id
        self._blank = blank
        self._position = position

    @property
    def id(self):
        """
        Gets the id of this WidgetFooterMenu.

        :return: The id of this WidgetFooterMenu.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WidgetFooterMenu.

        :param id: The id of this WidgetFooterMenu.
        :type: int
        """

        self._id = id

    @property
    def label(self):
        """
        Gets the label of this WidgetFooterMenu.

        :return: The label of this WidgetFooterMenu.
        :rtype: list[I18nField]
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this WidgetFooterMenu.

        :param label: The label of this WidgetFooterMenu.
        :type: list[I18nField]
        """

        self._label = label

    @property
    def url(self):
        """
        Gets the url of this WidgetFooterMenu.

        :return: The url of this WidgetFooterMenu.
        :rtype: list[I18nField]
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this WidgetFooterMenu.

        :param url: The url of this WidgetFooterMenu.
        :type: list[I18nField]
        """

        self._url = url

    @property
    def column(self):
        """
        Gets the column of this WidgetFooterMenu.

        :return: The column of this WidgetFooterMenu.
        :rtype: str
        """
        return self._column

    @column.setter
    def column(self, column):
        """
        Sets the column of this WidgetFooterMenu.

        :param column: The column of this WidgetFooterMenu.
        :type: str
        """

        self._column = column

    @property
    def type(self):
        """
        Gets the type of this WidgetFooterMenu.

        :return: The type of this WidgetFooterMenu.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WidgetFooterMenu.

        :param type: The type of this WidgetFooterMenu.
        :type: str
        """

        self._type = type

    @property
    def type_id(self):
        """
        Gets the type_id of this WidgetFooterMenu.

        :return: The type_id of this WidgetFooterMenu.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this WidgetFooterMenu.

        :param type_id: The type_id of this WidgetFooterMenu.
        :type: int
        """

        self._type_id = type_id

    @property
    def blank(self):
        """
        Gets the blank of this WidgetFooterMenu.

        :return: The blank of this WidgetFooterMenu.
        :rtype: int
        """
        return self._blank

    @blank.setter
    def blank(self, blank):
        """
        Sets the blank of this WidgetFooterMenu.

        :param blank: The blank of this WidgetFooterMenu.
        :type: int
        """

        self._blank = blank

    @property
    def position(self):
        """
        Gets the position of this WidgetFooterMenu.

        :return: The position of this WidgetFooterMenu.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this WidgetFooterMenu.

        :param position: The position of this WidgetFooterMenu.
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
