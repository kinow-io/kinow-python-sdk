# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.18
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VideoViewInformations(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id_product_video=None, view=None):
        """
        VideoViewInformations - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id_product_video': 'float',
            'view': 'bool'
        }

        self.attribute_map = {
            'id_product_video': 'id_product_video',
            'view': 'view'
        }

        self._id_product_video = id_product_video
        self._view = view

    @property
    def id_product_video(self):
        """
        Gets the id_product_video of this VideoViewInformations.

        :return: The id_product_video of this VideoViewInformations.
        :rtype: float
        """
        return self._id_product_video

    @id_product_video.setter
    def id_product_video(self, id_product_video):
        """
        Sets the id_product_video of this VideoViewInformations.

        :param id_product_video: The id_product_video of this VideoViewInformations.
        :type: float
        """

        self._id_product_video = id_product_video

    @property
    def view(self):
        """
        Gets the view of this VideoViewInformations.

        :return: The view of this VideoViewInformations.
        :rtype: bool
        """
        return self._view

    @view.setter
    def view(self, view):
        """
        Sets the view of this VideoViewInformations.

        :param view: The view of this VideoViewInformations.
        :type: bool
        """

        self._view = view

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
