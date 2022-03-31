# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.8
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SocialSettings(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, facebook=None, twitter=None, youtube=None, pinterest=None, dailymotion=None, tumblr=None, instagram=None, tiktok=None, twitch=None, linked_in=None, soundcloud=None, flickr=None, discord=None):
        """
        SocialSettings - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'facebook': 'str',
            'twitter': 'str',
            'youtube': 'str',
            'pinterest': 'str',
            'dailymotion': 'str',
            'tumblr': 'str',
            'instagram': 'str',
            'tiktok': 'str',
            'twitch': 'str',
            'linked_in': 'str',
            'soundcloud': 'str',
            'flickr': 'str',
            'discord': 'str'
        }

        self.attribute_map = {
            'facebook': 'facebook',
            'twitter': 'twitter',
            'youtube': 'youtube',
            'pinterest': 'pinterest',
            'dailymotion': 'dailymotion',
            'tumblr': 'tumblr',
            'instagram': 'instagram',
            'tiktok': 'tiktok',
            'twitch': 'twitch',
            'linked_in': 'linkedIn',
            'soundcloud': 'soundcloud',
            'flickr': 'flickr',
            'discord': 'discord'
        }

        self._facebook = facebook
        self._twitter = twitter
        self._youtube = youtube
        self._pinterest = pinterest
        self._dailymotion = dailymotion
        self._tumblr = tumblr
        self._instagram = instagram
        self._tiktok = tiktok
        self._twitch = twitch
        self._linked_in = linked_in
        self._soundcloud = soundcloud
        self._flickr = flickr
        self._discord = discord

    @property
    def facebook(self):
        """
        Gets the facebook of this SocialSettings.

        :return: The facebook of this SocialSettings.
        :rtype: str
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """
        Sets the facebook of this SocialSettings.

        :param facebook: The facebook of this SocialSettings.
        :type: str
        """

        self._facebook = facebook

    @property
    def twitter(self):
        """
        Gets the twitter of this SocialSettings.

        :return: The twitter of this SocialSettings.
        :rtype: str
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """
        Sets the twitter of this SocialSettings.

        :param twitter: The twitter of this SocialSettings.
        :type: str
        """

        self._twitter = twitter

    @property
    def youtube(self):
        """
        Gets the youtube of this SocialSettings.

        :return: The youtube of this SocialSettings.
        :rtype: str
        """
        return self._youtube

    @youtube.setter
    def youtube(self, youtube):
        """
        Sets the youtube of this SocialSettings.

        :param youtube: The youtube of this SocialSettings.
        :type: str
        """

        self._youtube = youtube

    @property
    def pinterest(self):
        """
        Gets the pinterest of this SocialSettings.

        :return: The pinterest of this SocialSettings.
        :rtype: str
        """
        return self._pinterest

    @pinterest.setter
    def pinterest(self, pinterest):
        """
        Sets the pinterest of this SocialSettings.

        :param pinterest: The pinterest of this SocialSettings.
        :type: str
        """

        self._pinterest = pinterest

    @property
    def dailymotion(self):
        """
        Gets the dailymotion of this SocialSettings.

        :return: The dailymotion of this SocialSettings.
        :rtype: str
        """
        return self._dailymotion

    @dailymotion.setter
    def dailymotion(self, dailymotion):
        """
        Sets the dailymotion of this SocialSettings.

        :param dailymotion: The dailymotion of this SocialSettings.
        :type: str
        """

        self._dailymotion = dailymotion

    @property
    def tumblr(self):
        """
        Gets the tumblr of this SocialSettings.

        :return: The tumblr of this SocialSettings.
        :rtype: str
        """
        return self._tumblr

    @tumblr.setter
    def tumblr(self, tumblr):
        """
        Sets the tumblr of this SocialSettings.

        :param tumblr: The tumblr of this SocialSettings.
        :type: str
        """

        self._tumblr = tumblr

    @property
    def instagram(self):
        """
        Gets the instagram of this SocialSettings.

        :return: The instagram of this SocialSettings.
        :rtype: str
        """
        return self._instagram

    @instagram.setter
    def instagram(self, instagram):
        """
        Sets the instagram of this SocialSettings.

        :param instagram: The instagram of this SocialSettings.
        :type: str
        """

        self._instagram = instagram

    @property
    def tiktok(self):
        """
        Gets the tiktok of this SocialSettings.

        :return: The tiktok of this SocialSettings.
        :rtype: str
        """
        return self._tiktok

    @tiktok.setter
    def tiktok(self, tiktok):
        """
        Sets the tiktok of this SocialSettings.

        :param tiktok: The tiktok of this SocialSettings.
        :type: str
        """

        self._tiktok = tiktok

    @property
    def twitch(self):
        """
        Gets the twitch of this SocialSettings.

        :return: The twitch of this SocialSettings.
        :rtype: str
        """
        return self._twitch

    @twitch.setter
    def twitch(self, twitch):
        """
        Sets the twitch of this SocialSettings.

        :param twitch: The twitch of this SocialSettings.
        :type: str
        """

        self._twitch = twitch

    @property
    def linked_in(self):
        """
        Gets the linked_in of this SocialSettings.

        :return: The linked_in of this SocialSettings.
        :rtype: str
        """
        return self._linked_in

    @linked_in.setter
    def linked_in(self, linked_in):
        """
        Sets the linked_in of this SocialSettings.

        :param linked_in: The linked_in of this SocialSettings.
        :type: str
        """

        self._linked_in = linked_in

    @property
    def soundcloud(self):
        """
        Gets the soundcloud of this SocialSettings.

        :return: The soundcloud of this SocialSettings.
        :rtype: str
        """
        return self._soundcloud

    @soundcloud.setter
    def soundcloud(self, soundcloud):
        """
        Sets the soundcloud of this SocialSettings.

        :param soundcloud: The soundcloud of this SocialSettings.
        :type: str
        """

        self._soundcloud = soundcloud

    @property
    def flickr(self):
        """
        Gets the flickr of this SocialSettings.

        :return: The flickr of this SocialSettings.
        :rtype: str
        """
        return self._flickr

    @flickr.setter
    def flickr(self, flickr):
        """
        Sets the flickr of this SocialSettings.

        :param flickr: The flickr of this SocialSettings.
        :type: str
        """

        self._flickr = flickr

    @property
    def discord(self):
        """
        Gets the discord of this SocialSettings.

        :return: The discord of this SocialSettings.
        :rtype: str
        """
        return self._discord

    @discord.setter
    def discord(self, discord):
        """
        Sets the discord of this SocialSettings.

        :param discord: The discord of this SocialSettings.
        :type: str
        """

        self._discord = discord

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
