# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.27
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class WidgetSliderResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, label=None, description=None, url=None, type=None, type_id=None, blank=None, over=None, button=None, opacity=None, image=None, position=None, video=None):
        """
        WidgetSliderResponse - a model defined in Swagger

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
            'position': 'int',
            'video': 'WidgetSliderVideo'
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
            'position': 'position',
            'video': 'video'
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
        self._video = video

    @property
    def id(self):
        """
        Gets the id of this WidgetSliderResponse.

        :return: The id of this WidgetSliderResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WidgetSliderResponse.

        :param id: The id of this WidgetSliderResponse.
        :type: int
        """

        self._id = id

    @property
    def label(self):
        """
        Gets the label of this WidgetSliderResponse.

        :return: The label of this WidgetSliderResponse.
        :rtype: list[I18nField]
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this WidgetSliderResponse.

        :param label: The label of this WidgetSliderResponse.
        :type: list[I18nField]
        """

        self._label = label

    @property
    def description(self):
        """
        Gets the description of this WidgetSliderResponse.

        :return: The description of this WidgetSliderResponse.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this WidgetSliderResponse.

        :param description: The description of this WidgetSliderResponse.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def url(self):
        """
        Gets the url of this WidgetSliderResponse.

        :return: The url of this WidgetSliderResponse.
        :rtype: list[I18nField]
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this WidgetSliderResponse.

        :param url: The url of this WidgetSliderResponse.
        :type: list[I18nField]
        """

        self._url = url

    @property
    def type(self):
        """
        Gets the type of this WidgetSliderResponse.

        :return: The type of this WidgetSliderResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this WidgetSliderResponse.

        :param type: The type of this WidgetSliderResponse.
        :type: str
        """

        self._type = type

    @property
    def type_id(self):
        """
        Gets the type_id of this WidgetSliderResponse.

        :return: The type_id of this WidgetSliderResponse.
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """
        Sets the type_id of this WidgetSliderResponse.

        :param type_id: The type_id of this WidgetSliderResponse.
        :type: int
        """

        self._type_id = type_id

    @property
    def blank(self):
        """
        Gets the blank of this WidgetSliderResponse.

        :return: The blank of this WidgetSliderResponse.
        :rtype: int
        """
        return self._blank

    @blank.setter
    def blank(self, blank):
        """
        Sets the blank of this WidgetSliderResponse.

        :param blank: The blank of this WidgetSliderResponse.
        :type: int
        """

        self._blank = blank

    @property
    def over(self):
        """
        Gets the over of this WidgetSliderResponse.

        :return: The over of this WidgetSliderResponse.
        :rtype: int
        """
        return self._over

    @over.setter
    def over(self, over):
        """
        Sets the over of this WidgetSliderResponse.

        :param over: The over of this WidgetSliderResponse.
        :type: int
        """

        self._over = over

    @property
    def button(self):
        """
        Gets the button of this WidgetSliderResponse.

        :return: The button of this WidgetSliderResponse.
        :rtype: int
        """
        return self._button

    @button.setter
    def button(self, button):
        """
        Sets the button of this WidgetSliderResponse.

        :param button: The button of this WidgetSliderResponse.
        :type: int
        """

        self._button = button

    @property
    def opacity(self):
        """
        Gets the opacity of this WidgetSliderResponse.

        :return: The opacity of this WidgetSliderResponse.
        :rtype: float
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """
        Sets the opacity of this WidgetSliderResponse.

        :param opacity: The opacity of this WidgetSliderResponse.
        :type: float
        """

        self._opacity = opacity

    @property
    def image(self):
        """
        Gets the image of this WidgetSliderResponse.

        :return: The image of this WidgetSliderResponse.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this WidgetSliderResponse.

        :param image: The image of this WidgetSliderResponse.
        :type: str
        """

        self._image = image

    @property
    def position(self):
        """
        Gets the position of this WidgetSliderResponse.

        :return: The position of this WidgetSliderResponse.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this WidgetSliderResponse.

        :param position: The position of this WidgetSliderResponse.
        :type: int
        """

        self._position = position

    @property
    def video(self):
        """
        Gets the video of this WidgetSliderResponse.

        :return: The video of this WidgetSliderResponse.
        :rtype: WidgetSliderVideo
        """
        return self._video

    @video.setter
    def video(self, video):
        """
        Sets the video of this WidgetSliderResponse.

        :param video: The video of this WidgetSliderResponse.
        :type: WidgetSliderVideo
        """

        self._video = video

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
