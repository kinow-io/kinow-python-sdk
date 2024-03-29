# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.28
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class UpdateCustomerRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, firstname=None, lastname=None, email=None, password=None, id_gender=None, birthday=None, newsletter=None, optin=None, active=None, id_lang=None, notification=None, max_viewing=None, custom=None):
        """
        UpdateCustomerRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'firstname': 'str',
            'lastname': 'str',
            'email': 'str',
            'password': 'str',
            'id_gender': 'int',
            'birthday': 'str',
            'newsletter': 'bool',
            'optin': 'bool',
            'active': 'bool',
            'id_lang': 'int',
            'notification': 'bool',
            'max_viewing': 'int',
            'custom': 'str'
        }

        self.attribute_map = {
            'firstname': 'firstname',
            'lastname': 'lastname',
            'email': 'email',
            'password': 'password',
            'id_gender': 'id_gender',
            'birthday': 'birthday',
            'newsletter': 'newsletter',
            'optin': 'optin',
            'active': 'active',
            'id_lang': 'id_lang',
            'notification': 'notification',
            'max_viewing': 'max_viewing',
            'custom': 'custom'
        }

        self._firstname = firstname
        self._lastname = lastname
        self._email = email
        self._password = password
        self._id_gender = id_gender
        self._birthday = birthday
        self._newsletter = newsletter
        self._optin = optin
        self._active = active
        self._id_lang = id_lang
        self._notification = notification
        self._max_viewing = max_viewing
        self._custom = custom

    @property
    def firstname(self):
        """
        Gets the firstname of this UpdateCustomerRequest.

        :return: The firstname of this UpdateCustomerRequest.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this UpdateCustomerRequest.

        :param firstname: The firstname of this UpdateCustomerRequest.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this UpdateCustomerRequest.

        :return: The lastname of this UpdateCustomerRequest.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this UpdateCustomerRequest.

        :param lastname: The lastname of this UpdateCustomerRequest.
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """
        Gets the email of this UpdateCustomerRequest.

        :return: The email of this UpdateCustomerRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this UpdateCustomerRequest.

        :param email: The email of this UpdateCustomerRequest.
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """
        Gets the password of this UpdateCustomerRequest.

        :return: The password of this UpdateCustomerRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this UpdateCustomerRequest.

        :param password: The password of this UpdateCustomerRequest.
        :type: str
        """

        self._password = password

    @property
    def id_gender(self):
        """
        Gets the id_gender of this UpdateCustomerRequest.

        :return: The id_gender of this UpdateCustomerRequest.
        :rtype: int
        """
        return self._id_gender

    @id_gender.setter
    def id_gender(self, id_gender):
        """
        Sets the id_gender of this UpdateCustomerRequest.

        :param id_gender: The id_gender of this UpdateCustomerRequest.
        :type: int
        """

        self._id_gender = id_gender

    @property
    def birthday(self):
        """
        Gets the birthday of this UpdateCustomerRequest.

        :return: The birthday of this UpdateCustomerRequest.
        :rtype: str
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """
        Sets the birthday of this UpdateCustomerRequest.

        :param birthday: The birthday of this UpdateCustomerRequest.
        :type: str
        """

        self._birthday = birthday

    @property
    def newsletter(self):
        """
        Gets the newsletter of this UpdateCustomerRequest.

        :return: The newsletter of this UpdateCustomerRequest.
        :rtype: bool
        """
        return self._newsletter

    @newsletter.setter
    def newsletter(self, newsletter):
        """
        Sets the newsletter of this UpdateCustomerRequest.

        :param newsletter: The newsletter of this UpdateCustomerRequest.
        :type: bool
        """

        self._newsletter = newsletter

    @property
    def optin(self):
        """
        Gets the optin of this UpdateCustomerRequest.

        :return: The optin of this UpdateCustomerRequest.
        :rtype: bool
        """
        return self._optin

    @optin.setter
    def optin(self, optin):
        """
        Sets the optin of this UpdateCustomerRequest.

        :param optin: The optin of this UpdateCustomerRequest.
        :type: bool
        """

        self._optin = optin

    @property
    def active(self):
        """
        Gets the active of this UpdateCustomerRequest.

        :return: The active of this UpdateCustomerRequest.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this UpdateCustomerRequest.

        :param active: The active of this UpdateCustomerRequest.
        :type: bool
        """

        self._active = active

    @property
    def id_lang(self):
        """
        Gets the id_lang of this UpdateCustomerRequest.

        :return: The id_lang of this UpdateCustomerRequest.
        :rtype: int
        """
        return self._id_lang

    @id_lang.setter
    def id_lang(self, id_lang):
        """
        Sets the id_lang of this UpdateCustomerRequest.

        :param id_lang: The id_lang of this UpdateCustomerRequest.
        :type: int
        """

        self._id_lang = id_lang

    @property
    def notification(self):
        """
        Gets the notification of this UpdateCustomerRequest.

        :return: The notification of this UpdateCustomerRequest.
        :rtype: bool
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """
        Sets the notification of this UpdateCustomerRequest.

        :param notification: The notification of this UpdateCustomerRequest.
        :type: bool
        """

        self._notification = notification

    @property
    def max_viewing(self):
        """
        Gets the max_viewing of this UpdateCustomerRequest.

        :return: The max_viewing of this UpdateCustomerRequest.
        :rtype: int
        """
        return self._max_viewing

    @max_viewing.setter
    def max_viewing(self, max_viewing):
        """
        Sets the max_viewing of this UpdateCustomerRequest.

        :param max_viewing: The max_viewing of this UpdateCustomerRequest.
        :type: int
        """

        self._max_viewing = max_viewing

    @property
    def custom(self):
        """
        Gets the custom of this UpdateCustomerRequest.

        :return: The custom of this UpdateCustomerRequest.
        :rtype: str
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """
        Sets the custom of this UpdateCustomerRequest.

        :param custom: The custom of this UpdateCustomerRequest.
        :type: str
        """

        self._custom = custom

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
