# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.50
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WidgetSlider(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, label=None, description=None, url=None, type=None, type_id=None, blank=None, over=None, button=None, opacity=None, image=None, position=None):
        """
        WidgetSlider - a model defined in Swagger

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
            'over': 'int',
            'button': 'int',
            'opacity': 'float',
            'image': 'str',
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
            'over': 'over',
            'button': 'button',
            'opacity': 'opacity',
            'image': 'image',
            'position': 'position'
        }

        self._id = id
        self._label = label
        self._description = description
        self._url = url
        self._type = type
        self._type_id = type_id
        self._blank = blank
        self._over = over
        self._button = button
        self._opacity = opacity
        self._image = image
        self._position = position

    @property
    def id(self):
        """
        Gets the id of this WidgetSlider.
        

        :return: The id of this WidgetSlider.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WidgetSlider.
        

        :param id: The id of this WidgetSlider.
        :type: int
        """

        self._id = id

    @property
    def label(self):
        """
        Gets the label of this WidgetSlider.

        :return: The label of this WidgetSlider.
        :rtype: list[I18nField]
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this WidgetSlider.

        :param label: The label of this WidgetSlider.
        :type: list[I18nField]
        """

        self._label = label

    @property
    def description(self):
        """
        Gets the description of this WidgetSlider.

        :return: The description of this WidgetSlider.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WidgetSlider.

        :param description: The description of this WidgetSlider.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def url(self):
        """
        Gets the url of this WidgetSlider.

        :return: The url of this WidgetSlider.
        :rtype: list[I18nField]
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this WidgetSlider.

        :param url: The url of this WidgetSlider.
        :type: list[I18nField]
        """

        self._url = url

    @property
    def type(self):
        """
        Gets the type of this WidgetSlider.
        

        :return: The type of this WidgetSlider.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WidgetSlider.
        

        :param type: The type of this WidgetSlider.
        :type: str
        """

        self._type = type

    @property
    def type_id(self):
        """
        Gets the type_id of this WidgetSlider.
        

        :return: The type_id of this WidgetSlider.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this WidgetSlider.
        

        :param type_id: The type_id of this WidgetSlider.
        :type: int
        """

        self._type_id = type_id

    @property
    def blank(self):
        """
        Gets the blank of this WidgetSlider.
        

        :return: The blank of this WidgetSlider.
        :rtype: int
        """
        return self._blank

    @blank.setter
    def blank(self, blank):
        """
        Sets the blank of this WidgetSlider.
        

        :param blank: The blank of this WidgetSlider.
        :type: int
        """

        self._blank = blank

    @property
    def over(self):
        """
        Gets the over of this WidgetSlider.
        

        :return: The over of this WidgetSlider.
        :rtype: int
        """
        return self._over

    @over.setter
    def over(self, over):
        """
        Sets the over of this WidgetSlider.
        

        :param over: The over of this WidgetSlider.
        :type: int
        """

        self._over = over

    @property
    def button(self):
        """
        Gets the button of this WidgetSlider.
        

        :return: The button of this WidgetSlider.
        :rtype: int
        """
        return self._button

    @button.setter
    def button(self, button):
        """
        Sets the button of this WidgetSlider.
        

        :param button: The button of this WidgetSlider.
        :type: int
        """

        self._button = button

    @property
    def opacity(self):
        """
        Gets the opacity of this WidgetSlider.
        

        :return: The opacity of this WidgetSlider.
        :rtype: float
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """
        Sets the opacity of this WidgetSlider.
        

        :param opacity: The opacity of this WidgetSlider.
        :type: float
        """

        self._opacity = opacity

    @property
    def image(self):
        """
        Gets the image of this WidgetSlider.
        

        :return: The image of this WidgetSlider.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this WidgetSlider.
        

        :param image: The image of this WidgetSlider.
        :type: str
        """

        self._image = image

    @property
    def position(self):
        """
        Gets the position of this WidgetSlider.
        

        :return: The position of this WidgetSlider.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this WidgetSlider.
        

        :param position: The position of this WidgetSlider.
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
