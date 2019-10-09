# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.26
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Subtitle(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, src=None, srclang=None, label=None, name=None, font=None, size=None, color=None, text_shadow=None, italic_color=None):
        """
        Subtitle - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'src': 'str',
            'srclang': 'str',
            'label': 'str',
            'name': 'str',
            'font': 'str',
            'size': 'int',
            'color': 'str',
            'text_shadow': 'str',
            'italic_color': 'bool'
        }

        self.attribute_map = {
            'src': 'src',
            'srclang': 'srclang',
            'label': 'label',
            'name': 'name',
            'font': 'font',
            'size': 'size',
            'color': 'color',
            'text_shadow': 'text_shadow',
            'italic_color': 'italic_color'
        }

        self._src = src
        self._srclang = srclang
        self._label = label
        self._name = name
        self._font = font
        self._size = size
        self._color = color
        self._text_shadow = text_shadow
        self._italic_color = italic_color

    @property
    def src(self):
        """
        Gets the src of this Subtitle.
        

        :return: The src of this Subtitle.
        :rtype: str
        """
        return self._src

    @src.setter
    def src(self, src):
        """
        Sets the src of this Subtitle.
        

        :param src: The src of this Subtitle.
        :type: str
        """

        self._src = src

    @property
    def srclang(self):
        """
        Gets the srclang of this Subtitle.
        

        :return: The srclang of this Subtitle.
        :rtype: str
        """
        return self._srclang

    @srclang.setter
    def srclang(self, srclang):
        """
        Sets the srclang of this Subtitle.
        

        :param srclang: The srclang of this Subtitle.
        :type: str
        """

        self._srclang = srclang

    @property
    def label(self):
        """
        Gets the label of this Subtitle.
        

        :return: The label of this Subtitle.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this Subtitle.
        

        :param label: The label of this Subtitle.
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """
        Gets the name of this Subtitle.
        

        :return: The name of this Subtitle.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Subtitle.
        

        :param name: The name of this Subtitle.
        :type: str
        """

        self._name = name

    @property
    def font(self):
        """
        Gets the font of this Subtitle.
        

        :return: The font of this Subtitle.
        :rtype: str
        """
        return self._font

    @font.setter
    def font(self, font):
        """
        Sets the font of this Subtitle.
        

        :param font: The font of this Subtitle.
        :type: str
        """

        self._font = font

    @property
    def size(self):
        """
        Gets the size of this Subtitle.
        

        :return: The size of this Subtitle.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this Subtitle.
        

        :param size: The size of this Subtitle.
        :type: int
        """

        self._size = size

    @property
    def color(self):
        """
        Gets the color of this Subtitle.
        

        :return: The color of this Subtitle.
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """
        Sets the color of this Subtitle.
        

        :param color: The color of this Subtitle.
        :type: str
        """

        self._color = color

    @property
    def text_shadow(self):
        """
        Gets the text_shadow of this Subtitle.
        

        :return: The text_shadow of this Subtitle.
        :rtype: str
        """
        return self._text_shadow

    @text_shadow.setter
    def text_shadow(self, text_shadow):
        """
        Sets the text_shadow of this Subtitle.
        

        :param text_shadow: The text_shadow of this Subtitle.
        :type: str
        """

        self._text_shadow = text_shadow

    @property
    def italic_color(self):
        """
        Gets the italic_color of this Subtitle.
        

        :return: The italic_color of this Subtitle.
        :rtype: bool
        """
        return self._italic_color

    @italic_color.setter
    def italic_color(self, italic_color):
        """
        Sets the italic_color of this Subtitle.
        

        :param italic_color: The italic_color of this Subtitle.
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
