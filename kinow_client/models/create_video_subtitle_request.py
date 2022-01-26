# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateVideoSubtitleRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, filename=None, name=None, id_lang=None, background=None, font=None, size=None, color=None, text_shadow=None):
        """
        CreateVideoSubtitleRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'filename': 'str',
            'name': 'str',
            'id_lang': 'int',
            'background': 'int',
            'font': 'int',
            'size': 'int',
            'color': 'str',
            'text_shadow': 'str'
        }

        self.attribute_map = {
            'filename': 'filename',
            'name': 'name',
            'id_lang': 'id_lang',
            'background': 'background',
            'font': 'font',
            'size': 'size',
            'color': 'color',
            'text_shadow': 'text_shadow'
        }

        self._filename = filename
        self._name = name
        self._id_lang = id_lang
        self._background = background
        self._font = font
        self._size = size
        self._color = color
        self._text_shadow = text_shadow

    @property
    def filename(self):
        """
        Gets the filename of this CreateVideoSubtitleRequest.
        Filename

        :return: The filename of this CreateVideoSubtitleRequest.
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """
        Sets the filename of this CreateVideoSubtitleRequest.
        Filename

        :param filename: The filename of this CreateVideoSubtitleRequest.
        :type: str
        """
        if filename is None:
            raise ValueError("Invalid value for `filename`, must not be `None`")

        self._filename = filename

    @property
    def name(self):
        """
        Gets the name of this CreateVideoSubtitleRequest.
        Name

        :return: The name of this CreateVideoSubtitleRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateVideoSubtitleRequest.
        Name

        :param name: The name of this CreateVideoSubtitleRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def id_lang(self):
        """
        Gets the id_lang of this CreateVideoSubtitleRequest.
        Language ID

        :return: The id_lang of this CreateVideoSubtitleRequest.
        :rtype: int
        """
        return self._id_lang

    @id_lang.setter
    def id_lang(self, id_lang):
        """
        Sets the id_lang of this CreateVideoSubtitleRequest.
        Language ID

        :param id_lang: The id_lang of this CreateVideoSubtitleRequest.
        :type: int
        """
        if id_lang is None:
            raise ValueError("Invalid value for `id_lang`, must not be `None`")

        self._id_lang = id_lang

    @property
    def background(self):
        """
        Gets the background of this CreateVideoSubtitleRequest.
        Background color

        :return: The background of this CreateVideoSubtitleRequest.
        :rtype: int
        """
        return self._background

    @background.setter
    def background(self, background):
        """
        Sets the background of this CreateVideoSubtitleRequest.
        Background color

        :param background: The background of this CreateVideoSubtitleRequest.
        :type: int
        """

        self._background = background

    @property
    def font(self):
        """
        Gets the font of this CreateVideoSubtitleRequest.
        Font name

        :return: The font of this CreateVideoSubtitleRequest.
        :rtype: int
        """
        return self._font

    @font.setter
    def font(self, font):
        """
        Sets the font of this CreateVideoSubtitleRequest.
        Font name

        :param font: The font of this CreateVideoSubtitleRequest.
        :type: int
        """

        self._font = font

    @property
    def size(self):
        """
        Gets the size of this CreateVideoSubtitleRequest.
        Font size

        :return: The size of this CreateVideoSubtitleRequest.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this CreateVideoSubtitleRequest.
        Font size

        :param size: The size of this CreateVideoSubtitleRequest.
        :type: int
        """

        self._size = size

    @property
    def color(self):
        """
        Gets the color of this CreateVideoSubtitleRequest.
        Font color

        :return: The color of this CreateVideoSubtitleRequest.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this CreateVideoSubtitleRequest.
        Font color

        :param color: The color of this CreateVideoSubtitleRequest.
        :type: str
        """

        self._color = color

    @property
    def text_shadow(self):
        """
        Gets the text_shadow of this CreateVideoSubtitleRequest.
        Text shadow

        :return: The text_shadow of this CreateVideoSubtitleRequest.
        :rtype: str
        """
        return self._text_shadow

    @text_shadow.setter
    def text_shadow(self, text_shadow):
        """
        Sets the text_shadow of this CreateVideoSubtitleRequest.
        Text shadow

        :param text_shadow: The text_shadow of this CreateVideoSubtitleRequest.
        :type: str
        """

        self._text_shadow = text_shadow

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
