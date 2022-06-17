# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.12
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CreateAttributeRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product_id=None, video_group_id=None, video_id=None, type=None, mode=None, quality=None, price=None, price_mode=None, duration=None, watching_duration=None, maximum_views=None):
        """
        CreateAttributeRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'product_id': 'int',
            'video_group_id': 'int',
            'video_id': 'int',
            'type': 'str',
            'mode': 'str',
            'quality': 'str',
            'price': 'float',
            'price_mode': 'int',
            'duration': 'int',
            'watching_duration': 'int',
            'maximum_views': 'int'
        }

        self.attribute_map = {
            'product_id': 'product_id',
            'video_group_id': 'video_group_id',
            'video_id': 'video_id',
            'type': 'type',
            'mode': 'mode',
            'quality': 'quality',
            'price': 'price',
            'price_mode': 'price_mode',
            'duration': 'duration',
            'watching_duration': 'watching_duration',
            'maximum_views': 'maximum_views'
        }

        self._product_id = product_id
        self._video_group_id = video_group_id
        self._video_id = video_id
        self._type = type
        self._mode = mode
        self._quality = quality
        self._price = price
        self._price_mode = price_mode
        self._duration = duration
        self._watching_duration = watching_duration
        self._maximum_views = maximum_views

    @property
    def product_id(self):
        """
        Gets the product_id of this CreateAttributeRequest.
        Product ID to attach this access

        :return: The product_id of this CreateAttributeRequest.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this CreateAttributeRequest.
        Product ID to attach this access

        :param product_id: The product_id of this CreateAttributeRequest.
        :type: int
        """

        self._product_id = product_id

    @property
    def video_group_id(self):
        """
        Gets the video_group_id of this CreateAttributeRequest.
        Video Group ID to restrict this access

        :return: The video_group_id of this CreateAttributeRequest.
        :rtype: int
        """
        return self._video_group_id

    @video_group_id.setter
    def video_group_id(self, video_group_id):
        """
        Sets the video_group_id of this CreateAttributeRequest.
        Video Group ID to restrict this access

        :param video_group_id: The video_group_id of this CreateAttributeRequest.
        :type: int
        """

        self._video_group_id = video_group_id

    @property
    def video_id(self):
        """
        Gets the video_id of this CreateAttributeRequest.
        Video ID to restrict this access

        :return: The video_id of this CreateAttributeRequest.
        :rtype: int
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """
        Sets the video_id of this CreateAttributeRequest.
        Video ID to restrict this access

        :param video_id: The video_id of this CreateAttributeRequest.
        :type: int
        """

        self._video_id = video_id

    @property
    def type(self):
        """
        Gets the type of this CreateAttributeRequest.
        RENT, BUY or SUBSCRIPTION

        :return: The type of this CreateAttributeRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this CreateAttributeRequest.
        RENT, BUY or SUBSCRIPTION

        :param type: The type of this CreateAttributeRequest.
        :type: str
        """

        self._type = type

    @property
    def mode(self):
        """
        Gets the mode of this CreateAttributeRequest.
        BOTH (Streaming & Download), STREAMING or DOWNLOAD

        :return: The mode of this CreateAttributeRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this CreateAttributeRequest.
        BOTH (Streaming & Download), STREAMING or DOWNLOAD

        :param mode: The mode of this CreateAttributeRequest.
        :type: str
        """

        self._mode = mode

    @property
    def quality(self):
        """
        Gets the quality of this CreateAttributeRequest.
        ALL, HD or SD

        :return: The quality of this CreateAttributeRequest.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """
        Sets the quality of this CreateAttributeRequest.
        ALL, HD or SD

        :param quality: The quality of this CreateAttributeRequest.
        :type: str
        """

        self._quality = quality

    @property
    def price(self):
        """
        Gets the price of this CreateAttributeRequest.
        Retail price to sell this access

        :return: The price of this CreateAttributeRequest.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this CreateAttributeRequest.
        Retail price to sell this access

        :param price: The price of this CreateAttributeRequest.
        :type: float
        """

        self._price = price

    @property
    def price_mode(self):
        """
        Gets the price_mode of this CreateAttributeRequest.
        Pre-tax price (0) or price with tax (1)

        :return: The price_mode of this CreateAttributeRequest.
        :rtype: int
        """
        return self._price_mode

    @price_mode.setter
    def price_mode(self, price_mode):
        """
        Sets the price_mode of this CreateAttributeRequest.
        Pre-tax price (0) or price with tax (1)

        :param price_mode: The price_mode of this CreateAttributeRequest.
        :type: int
        """

        self._price_mode = price_mode

    @property
    def duration(self):
        """
        Gets the duration of this CreateAttributeRequest.
        Duration in days while user can access videos

        :return: The duration of this CreateAttributeRequest.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this CreateAttributeRequest.
        Duration in days while user can access videos

        :param duration: The duration of this CreateAttributeRequest.
        :type: int
        """

        self._duration = duration

    @property
    def watching_duration(self):
        """
        Gets the watching_duration of this CreateAttributeRequest.
        Duration in days while user can watch video after first play

        :return: The watching_duration of this CreateAttributeRequest.
        :rtype: int
        """
        return self._watching_duration

    @watching_duration.setter
    def watching_duration(self, watching_duration):
        """
        Sets the watching_duration of this CreateAttributeRequest.
        Duration in days while user can watch video after first play

        :param watching_duration: The watching_duration of this CreateAttributeRequest.
        :type: int
        """

        self._watching_duration = watching_duration

    @property
    def maximum_views(self):
        """
        Gets the maximum_views of this CreateAttributeRequest.
        Maximum views a user can watch video

        :return: The maximum_views of this CreateAttributeRequest.
        :rtype: int
        """
        return self._maximum_views

    @maximum_views.setter
    def maximum_views(self, maximum_views):
        """
        Sets the maximum_views of this CreateAttributeRequest.
        Maximum views a user can watch video

        :param maximum_views: The maximum_views of this CreateAttributeRequest.
        :type: int
        """

        self._maximum_views = maximum_views

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