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


class SubtitleResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, src=None, srclang=None, name=None, font=None, size=None, color=None, text_shadow=None, background=None, opacity=None, italic_color=None):
        """
        SubtitleResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'src': 'str',
            'srclang': 'str',
            'name': 'str',
            'font': 'str',
            'size': 'float',
            'color': 'str',
            'text_shadow': 'str',
            'background': 'str',
            'opacity': 'int',
            'italic_color': 'bool'
        }

        self.attribute_map = {
            'id': 'id',
            'src': 'src',
            'srclang': 'srclang',
            'name': 'name',
            'font': 'font',
            'size': 'size',
            'color': 'color',
            'text_shadow': 'text_shadow',
            'background': 'background',
            'opacity': 'opacity',
            'italic_color': 'italic_color'
        }

        self._id = id
        self._src = src
        self._srclang = srclang
        self._name = name
        self._font = font
        self._size = size
        self._color = color
        self._text_shadow = text_shadow
        self._background = background
        self._opacity = opacity
        self._italic_color = italic_color

    @property
    def id(self):
        """
        Gets the id of this SubtitleResponse.

        :return: The id of this SubtitleResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SubtitleResponse.

        :param id: The id of this SubtitleResponse.
        :type: int
        """

        self._id = id

    @property
    def src(self):
        """
        Gets the src of this SubtitleResponse.

        :return: The src of this SubtitleResponse.
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """
        Sets the src of this SubtitleResponse.

        :param src: The src of this SubtitleResponse.
        :type: str
        """

        self._src = src

    @property
    def srclang(self):
        """
        Gets the srclang of this SubtitleResponse.

        :return: The srclang of this SubtitleResponse.
        :rtype: str
        """
        return self._srclang

    @srclang.setter
    def srclang(self, srclang):
        """
        Sets the srclang of this SubtitleResponse.

        :param srclang: The srclang of this SubtitleResponse.
        :type: str
        """

        self._srclang = srclang

    @property
    def name(self):
        """
        Gets the name of this SubtitleResponse.

        :return: The name of this SubtitleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SubtitleResponse.

        :param name: The name of this SubtitleResponse.
        :type: str
        """

        self._name = name

    @property
    def font(self):
        """
        Gets the font of this SubtitleResponse.

        :return: The font of this SubtitleResponse.
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        """
        Sets the font of this SubtitleResponse.

        :param font: The font of this SubtitleResponse.
        :type: str
        """

        self._font = font

    @property
    def size(self):
        """
        Gets the size of this SubtitleResponse.

        :return: The size of this SubtitleResponse.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this SubtitleResponse.

        :param size: The size of this SubtitleResponse.
        :type: float
        """

        self._size = size

    @property
    def color(self):
        """
        Gets the color of this SubtitleResponse.

        :return: The color of this SubtitleResponse.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this SubtitleResponse.

        :param color: The color of this SubtitleResponse.
        :type: str
        """

        self._color = color

    @property
    def text_shadow(self):
        """
        Gets the text_shadow of this SubtitleResponse.

        :return: The text_shadow of this SubtitleResponse.
        :rtype: str
        """
        return self._text_shadow

    @text_shadow.setter
    def text_shadow(self, text_shadow):
        """
        Sets the text_shadow of this SubtitleResponse.

        :param text_shadow: The text_shadow of this SubtitleResponse.
        :type: str
        """

        self._text_shadow = text_shadow

    @property
    def background(self):
        """
        Gets the background of this SubtitleResponse.

        :return: The background of this SubtitleResponse.
        :rtype: str
        """
        return self._background

    @background.setter
    def background(self, background):
        """
        Sets the background of this SubtitleResponse.

        :param background: The background of this SubtitleResponse.
        :type: str
        """

        self._background = background

    @property
    def opacity(self):
        """
        Gets the opacity of this SubtitleResponse.

        :return: The opacity of this SubtitleResponse.
        :rtype: int
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """
        Sets the opacity of this SubtitleResponse.

        :param opacity: The opacity of this SubtitleResponse.
        :type: int
        """

        self._opacity = opacity

    @property
    def italic_color(self):
        """
        Gets the italic_color of this SubtitleResponse.

        :return: The italic_color of this SubtitleResponse.
        :rtype: bool
        """
        return self._italic_color

    @italic_color.setter
    def italic_color(self, italic_color):
        """
        Sets the italic_color of this SubtitleResponse.

        :param italic_color: The italic_color of this SubtitleResponse.
        :type: bool
        """

        self._italic_color = italic_color

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
