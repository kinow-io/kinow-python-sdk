# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.5.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductAttribute(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, video_group_id=None, video_id=None, name=None, price=None, price_mode=None, price_without_reduction=None, mode=None, type=None, quality=None, duration=None, watching_duration=None, maximum_views=None, active=None):
        """
        ProductAttribute - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'video_group_id': 'int',
            'video_id': 'int',
            'name': 'str',
            'price': 'float',
            'price_mode': 'float',
            'price_without_reduction': 'float',
            'mode': 'str',
            'type': 'str',
            'quality': 'str',
            'duration': 'int',
            'watching_duration': 'int',
            'maximum_views': 'int',
            'active': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'video_group_id': 'video_group_id',
            'video_id': 'video_id',
            'name': 'name',
            'price': 'price',
            'price_mode': 'price_mode',
            'price_without_reduction': 'price_without_reduction',
            'mode': 'mode',
            'type': 'type',
            'quality': 'quality',
            'duration': 'duration',
            'watching_duration': 'watching_duration',
            'maximum_views': 'maximum_views',
            'active': 'active'
        }

        self._id = id
        self._video_group_id = video_group_id
        self._video_id = video_id
        self._name = name
        self._price = price
        self._price_mode = price_mode
        self._price_without_reduction = price_without_reduction
        self._mode = mode
        self._type = type
        self._quality = quality
        self._duration = duration
        self._watching_duration = watching_duration
        self._maximum_views = maximum_views
        self._active = active

    @property
    def id(self):
        """
        Gets the id of this ProductAttribute.

        :return: The id of this ProductAttribute.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProductAttribute.

        :param id: The id of this ProductAttribute.
        :type: int
        """

        self._id = id

    @property
    def video_group_id(self):
        """
        Gets the video_group_id of this ProductAttribute.

        :return: The video_group_id of this ProductAttribute.
        :rtype: int
        """
        return self._video_group_id

    @video_group_id.setter
    def video_group_id(self, video_group_id):
        """
        Sets the video_group_id of this ProductAttribute.

        :param video_group_id: The video_group_id of this ProductAttribute.
        :type: int
        """

        self._video_group_id = video_group_id

    @property
    def video_id(self):
        """
        Gets the video_id of this ProductAttribute.

        :return: The video_id of this ProductAttribute.
        :rtype: int
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """
        Sets the video_id of this ProductAttribute.

        :param video_id: The video_id of this ProductAttribute.
        :type: int
        """

        self._video_id = video_id

    @property
    def name(self):
        """
        Gets the name of this ProductAttribute.

        :return: The name of this ProductAttribute.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProductAttribute.

        :param name: The name of this ProductAttribute.
        :type: str
        """

        self._name = name

    @property
    def price(self):
        """
        Gets the price of this ProductAttribute.

        :return: The price of this ProductAttribute.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ProductAttribute.

        :param price: The price of this ProductAttribute.
        :type: float
        """

        self._price = price

    @property
    def price_mode(self):
        """
        Gets the price_mode of this ProductAttribute.

        :return: The price_mode of this ProductAttribute.
        :rtype: float
        """
        return self._price_mode

    @price_mode.setter
    def price_mode(self, price_mode):
        """
        Sets the price_mode of this ProductAttribute.

        :param price_mode: The price_mode of this ProductAttribute.
        :type: float
        """

        self._price_mode = price_mode

    @property
    def price_without_reduction(self):
        """
        Gets the price_without_reduction of this ProductAttribute.

        :return: The price_without_reduction of this ProductAttribute.
        :rtype: float
        """
        return self._price_without_reduction

    @price_without_reduction.setter
    def price_without_reduction(self, price_without_reduction):
        """
        Sets the price_without_reduction of this ProductAttribute.

        :param price_without_reduction: The price_without_reduction of this ProductAttribute.
        :type: float
        """

        self._price_without_reduction = price_without_reduction

    @property
    def mode(self):
        """
        Gets the mode of this ProductAttribute.

        :return: The mode of this ProductAttribute.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this ProductAttribute.

        :param mode: The mode of this ProductAttribute.
        :type: str
        """

        self._mode = mode

    @property
    def type(self):
        """
        Gets the type of this ProductAttribute.

        :return: The type of this ProductAttribute.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProductAttribute.

        :param type: The type of this ProductAttribute.
        :type: str
        """

        self._type = type

    @property
    def quality(self):
        """
        Gets the quality of this ProductAttribute.

        :return: The quality of this ProductAttribute.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """
        Sets the quality of this ProductAttribute.

        :param quality: The quality of this ProductAttribute.
        :type: str
        """

        self._quality = quality

    @property
    def duration(self):
        """
        Gets the duration of this ProductAttribute.

        :return: The duration of this ProductAttribute.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this ProductAttribute.

        :param duration: The duration of this ProductAttribute.
        :type: int
        """

        self._duration = duration

    @property
    def watching_duration(self):
        """
        Gets the watching_duration of this ProductAttribute.

        :return: The watching_duration of this ProductAttribute.
        :rtype: int
        """
        return self._watching_duration

    @watching_duration.setter
    def watching_duration(self, watching_duration):
        """
        Sets the watching_duration of this ProductAttribute.

        :param watching_duration: The watching_duration of this ProductAttribute.
        :type: int
        """

        self._watching_duration = watching_duration

    @property
    def maximum_views(self):
        """
        Gets the maximum_views of this ProductAttribute.

        :return: The maximum_views of this ProductAttribute.
        :rtype: int
        """
        return self._maximum_views

    @maximum_views.setter
    def maximum_views(self, maximum_views):
        """
        Sets the maximum_views of this ProductAttribute.

        :param maximum_views: The maximum_views of this ProductAttribute.
        :type: int
        """

        self._maximum_views = maximum_views

    @property
    def active(self):
        """
        Gets the active of this ProductAttribute.

        :return: The active of this ProductAttribute.
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this ProductAttribute.

        :param active: The active of this ProductAttribute.
        :type: int
        """

        self._active = active

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
