# coding: utf-8

"""
    Kinow API

    Client API for Kinow back-office

    OpenAPI spec version: 1.3.72
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ProductAttributeCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, product_id=None, video_id=None, mode=None, type=None, quality=None, price=None, price_mode=None, duration=None, watching_duration=None):
        """
        ProductAttributeCreateRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'product_id': 'int',
            'video_id': 'int',
            'mode': 'str',
            'type': 'str',
            'quality': 'str',
            'price': 'float',
            'price_mode': 'float',
            'duration': 'float',
            'watching_duration': 'float'
        }

        self.attribute_map = {
            'product_id': 'product_id',
            'video_id': 'video_id',
            'mode': 'mode',
            'type': 'type',
            'quality': 'quality',
            'price': 'price',
            'price_mode': 'price_mode',
            'duration': 'duration',
            'watching_duration': 'watching_duration'
        }

        self._product_id = product_id
        self._video_id = video_id
        self._mode = mode
        self._type = type
        self._quality = quality
        self._price = price
        self._price_mode = price_mode
        self._duration = duration
        self._watching_duration = watching_duration

    @property
    def product_id(self):
        """
        Gets the product_id of this ProductAttributeCreateRequest.
        Product ID to attach this access

        :return: The product_id of this ProductAttributeCreateRequest.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """
        Sets the product_id of this ProductAttributeCreateRequest.
        Product ID to attach this access

        :param product_id: The product_id of this ProductAttributeCreateRequest.
        :type: int
        """

        self._product_id = product_id

    @property
    def video_id(self):
        """
        Gets the video_id of this ProductAttributeCreateRequest.
        Video ID to restrict this access

        :return: The video_id of this ProductAttributeCreateRequest.
        :rtype: int
        """
        return self._video_id

    @video_id.setter
    def video_id(self, video_id):
        """
        Sets the video_id of this ProductAttributeCreateRequest.
        Video ID to restrict this access

        :param video_id: The video_id of this ProductAttributeCreateRequest.
        :type: int
        """

        self._video_id = video_id

    @property
    def mode(self):
        """
        Gets the mode of this ProductAttributeCreateRequest.
        RENT, BUY or SUBSCRIPTION

        :return: The mode of this ProductAttributeCreateRequest.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """
        Sets the mode of this ProductAttributeCreateRequest.
        RENT, BUY or SUBSCRIPTION

        :param mode: The mode of this ProductAttributeCreateRequest.
        :type: str
        """

        self._mode = mode

    @property
    def type(self):
        """
        Gets the type of this ProductAttributeCreateRequest.
        BOTH (Streaming & Download), STREAMING or DOWNLOAD

        :return: The type of this ProductAttributeCreateRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ProductAttributeCreateRequest.
        BOTH (Streaming & Download), STREAMING or DOWNLOAD

        :param type: The type of this ProductAttributeCreateRequest.
        :type: str
        """

        self._type = type

    @property
    def quality(self):
        """
        Gets the quality of this ProductAttributeCreateRequest.
        ALL, HD or SD

        :return: The quality of this ProductAttributeCreateRequest.
        :rtype: str
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """
        Sets the quality of this ProductAttributeCreateRequest.
        ALL, HD or SD

        :param quality: The quality of this ProductAttributeCreateRequest.
        :type: str
        """

        self._quality = quality

    @property
    def price(self):
        """
        Gets the price of this ProductAttributeCreateRequest.
        Retail price to sell this access

        :return: The price of this ProductAttributeCreateRequest.
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this ProductAttributeCreateRequest.
        Retail price to sell this access

        :param price: The price of this ProductAttributeCreateRequest.
        :type: float
        """

        self._price = price

    @property
    def price_mode(self):
        """
        Gets the price_mode of this ProductAttributeCreateRequest.
        Pre-tax price or price with tax

        :return: The price_mode of this ProductAttributeCreateRequest.
        :rtype: float
        """
        return self._price_mode

    @price_mode.setter
    def price_mode(self, price_mode):
        """
        Sets the price_mode of this ProductAttributeCreateRequest.
        Pre-tax price or price with tax

        :param price_mode: The price_mode of this ProductAttributeCreateRequest.
        :type: float
        """

        self._price_mode = price_mode

    @property
    def duration(self):
        """
        Gets the duration of this ProductAttributeCreateRequest.
        Duration in days while user can access videos

        :return: The duration of this ProductAttributeCreateRequest.
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this ProductAttributeCreateRequest.
        Duration in days while user can access videos

        :param duration: The duration of this ProductAttributeCreateRequest.
        :type: float
        """

        self._duration = duration

    @property
    def watching_duration(self):
        """
        Gets the watching_duration of this ProductAttributeCreateRequest.
        Duration in days while user can watch video after first play

        :return: The watching_duration of this ProductAttributeCreateRequest.
        :rtype: float
        """
        return self._watching_duration

    @watching_duration.setter
    def watching_duration(self, watching_duration):
        """
        Sets the watching_duration of this ProductAttributeCreateRequest.
        Duration in days while user can watch video after first play

        :param watching_duration: The watching_duration of this ProductAttributeCreateRequest.
        :type: float
        """

        self._watching_duration = watching_duration

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
