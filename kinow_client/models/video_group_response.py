# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.15
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VideoGroupResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_product=None, name=None, description=None, position=None, date_add=None, date_upd=None):
        """
        VideoGroupResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_product': 'int',
            'name': 'list[I18nField]',
            'description': 'list[I18nField]',
            'position': 'int',
            'date_add': 'str',
            'date_upd': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'id_product': 'id_product',
            'name': 'name',
            'description': 'description',
            'position': 'position',
            'date_add': 'date_add',
            'date_upd': 'date_upd'
        }

        self._id = id
        self._id_product = id_product
        self._name = name
        self._description = description
        self._position = position
        self._date_add = date_add
        self._date_upd = date_upd

    @property
    def id(self):
        """
        Gets the id of this VideoGroupResponse.

        :return: The id of this VideoGroupResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VideoGroupResponse.

        :param id: The id of this VideoGroupResponse.
        :type: int
        """

        self._id = id

    @property
    def id_product(self):
        """
        Gets the id_product of this VideoGroupResponse.

        :return: The id_product of this VideoGroupResponse.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this VideoGroupResponse.

        :param id_product: The id_product of this VideoGroupResponse.
        :type: int
        """

        self._id_product = id_product

    @property
    def name(self):
        """
        Gets the name of this VideoGroupResponse.

        :return: The name of this VideoGroupResponse.
        :rtype: list[I18nField]
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VideoGroupResponse.

        :param name: The name of this VideoGroupResponse.
        :type: list[I18nField]
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this VideoGroupResponse.

        :return: The description of this VideoGroupResponse.
        :rtype: list[I18nField]
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VideoGroupResponse.

        :param description: The description of this VideoGroupResponse.
        :type: list[I18nField]
        """

        self._description = description

    @property
    def position(self):
        """
        Gets the position of this VideoGroupResponse.

        :return: The position of this VideoGroupResponse.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this VideoGroupResponse.

        :param position: The position of this VideoGroupResponse.
        :type: int
        """

        self._position = position

    @property
    def date_add(self):
        """
        Gets the date_add of this VideoGroupResponse.

        :return: The date_add of this VideoGroupResponse.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this VideoGroupResponse.

        :param date_add: The date_add of this VideoGroupResponse.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this VideoGroupResponse.

        :return: The date_upd of this VideoGroupResponse.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this VideoGroupResponse.

        :param date_upd: The date_upd of this VideoGroupResponse.
        :type: str
        """

        self._date_upd = date_upd

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
