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


class CustomerResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, lastname=None, firstname=None, email=None, id_gender=None, birthday=None, newsletter=None, optin=None, notification=None, active=None, id_lang=None, date_add=None, date_upd=None, max_viewing=None, custom=None, password=None, last_passwd_gen=None):
        """
        CustomerResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'lastname': 'str',
            'firstname': 'str',
            'email': 'str',
            'id_gender': 'int',
            'birthday': 'str',
            'newsletter': 'bool',
            'optin': 'bool',
            'notification': 'bool',
            'active': 'bool',
            'id_lang': 'int',
            'date_add': 'str',
            'date_upd': 'str',
            'max_viewing': 'int',
            'custom': 'str',
            'password': 'str',
            'last_passwd_gen': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'lastname': 'lastname',
            'firstname': 'firstname',
            'email': 'email',
            'id_gender': 'id_gender',
            'birthday': 'birthday',
            'newsletter': 'newsletter',
            'optin': 'optin',
            'notification': 'notification',
            'active': 'active',
            'id_lang': 'id_lang',
            'date_add': 'date_add',
            'date_upd': 'date_upd',
            'max_viewing': 'max_viewing',
            'custom': 'custom',
            'password': 'password',
            'last_passwd_gen': 'last_passwd_gen'
        }

        self._id = id
        self._lastname = lastname
        self._firstname = firstname
        self._email = email
        self._id_gender = id_gender
        self._birthday = birthday
        self._newsletter = newsletter
        self._optin = optin
        self._notification = notification
        self._active = active
        self._id_lang = id_lang
        self._date_add = date_add
        self._date_upd = date_upd
        self._max_viewing = max_viewing
        self._custom = custom
        self._password = password
        self._last_passwd_gen = last_passwd_gen

    @property
    def id(self):
        """
        Gets the id of this CustomerResponse.

        :return: The id of this CustomerResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CustomerResponse.

        :param id: The id of this CustomerResponse.
        :type: int
        """

        self._id = id

    @property
    def lastname(self):
        """
        Gets the lastname of this CustomerResponse.

        :return: The lastname of this CustomerResponse.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this CustomerResponse.

        :param lastname: The lastname of this CustomerResponse.
        :type: str
        """

        self._lastname = lastname

    @property
    def firstname(self):
        """
        Gets the firstname of this CustomerResponse.

        :return: The firstname of this CustomerResponse.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this CustomerResponse.

        :param firstname: The firstname of this CustomerResponse.
        :type: str
        """

        self._firstname = firstname

    @property
    def email(self):
        """
        Gets the email of this CustomerResponse.

        :return: The email of this CustomerResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CustomerResponse.

        :param email: The email of this CustomerResponse.
        :type: str
        """

        self._email = email

    @property
    def id_gender(self):
        """
        Gets the id_gender of this CustomerResponse.

        :return: The id_gender of this CustomerResponse.
        :rtype: int
        """
        return self._id_gender

    @id_gender.setter
    def id_gender(self, id_gender):
        """
        Sets the id_gender of this CustomerResponse.

        :param id_gender: The id_gender of this CustomerResponse.
        :type: int
        """

        self._id_gender = id_gender

    @property
    def birthday(self):
        """
        Gets the birthday of this CustomerResponse.

        :return: The birthday of this CustomerResponse.
        :rtype: str
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """
        Sets the birthday of this CustomerResponse.

        :param birthday: The birthday of this CustomerResponse.
        :type: str
        """

        self._birthday = birthday

    @property
    def newsletter(self):
        """
        Gets the newsletter of this CustomerResponse.

        :return: The newsletter of this CustomerResponse.
        :rtype: bool
        """
        return self._newsletter

    @newsletter.setter
    def newsletter(self, newsletter):
        """
        Sets the newsletter of this CustomerResponse.

        :param newsletter: The newsletter of this CustomerResponse.
        :type: bool
        """

        self._newsletter = newsletter

    @property
    def optin(self):
        """
        Gets the optin of this CustomerResponse.

        :return: The optin of this CustomerResponse.
        :rtype: bool
        """
        return self._optin

    @optin.setter
    def optin(self, optin):
        """
        Sets the optin of this CustomerResponse.

        :param optin: The optin of this CustomerResponse.
        :type: bool
        """

        self._optin = optin

    @property
    def notification(self):
        """
        Gets the notification of this CustomerResponse.

        :return: The notification of this CustomerResponse.
        :rtype: bool
        """
        return self._notification

    @notification.setter
    def notification(self, notification):
        """
        Sets the notification of this CustomerResponse.

        :param notification: The notification of this CustomerResponse.
        :type: bool
        """

        self._notification = notification

    @property
    def active(self):
        """
        Gets the active of this CustomerResponse.

        :return: The active of this CustomerResponse.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this CustomerResponse.

        :param active: The active of this CustomerResponse.
        :type: bool
        """

        self._active = active

    @property
    def id_lang(self):
        """
        Gets the id_lang of this CustomerResponse.

        :return: The id_lang of this CustomerResponse.
        :rtype: int
        """
        return self._id_lang

    @id_lang.setter
    def id_lang(self, id_lang):
        """
        Sets the id_lang of this CustomerResponse.

        :param id_lang: The id_lang of this CustomerResponse.
        :type: int
        """

        self._id_lang = id_lang

    @property
    def date_add(self):
        """
        Gets the date_add of this CustomerResponse.

        :return: The date_add of this CustomerResponse.
        :rtype: str
        """
        return self._date_add

    @date_add.setter
    def date_add(self, date_add):
        """
        Sets the date_add of this CustomerResponse.

        :param date_add: The date_add of this CustomerResponse.
        :type: str
        """

        self._date_add = date_add

    @property
    def date_upd(self):
        """
        Gets the date_upd of this CustomerResponse.

        :return: The date_upd of this CustomerResponse.
        :rtype: str
        """
        return self._date_upd

    @date_upd.setter
    def date_upd(self, date_upd):
        """
        Sets the date_upd of this CustomerResponse.

        :param date_upd: The date_upd of this CustomerResponse.
        :type: str
        """

        self._date_upd = date_upd

    @property
    def max_viewing(self):
        """
        Gets the max_viewing of this CustomerResponse.

        :return: The max_viewing of this CustomerResponse.
        :rtype: int
        """
        return self._max_viewing

    @max_viewing.setter
    def max_viewing(self, max_viewing):
        """
        Sets the max_viewing of this CustomerResponse.

        :param max_viewing: The max_viewing of this CustomerResponse.
        :type: int
        """

        self._max_viewing = max_viewing

    @property
    def custom(self):
        """
        Gets the custom of this CustomerResponse.

        :return: The custom of this CustomerResponse.
        :rtype: str
        """
        return self._custom

    @custom.setter
    def custom(self, custom):
        """
        Sets the custom of this CustomerResponse.

        :param custom: The custom of this CustomerResponse.
        :type: str
        """

        self._custom = custom

    @property
    def password(self):
        """
        Gets the password of this CustomerResponse.
        Only available in body

        :return: The password of this CustomerResponse.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CustomerResponse.
        Only available in body

        :param password: The password of this CustomerResponse.
        :type: str
        """

        self._password = password

    @property
    def last_passwd_gen(self):
        """
        Gets the last_passwd_gen of this CustomerResponse.

        :return: The last_passwd_gen of this CustomerResponse.
        :rtype: str
        """
        return self._last_passwd_gen

    @last_passwd_gen.setter
    def last_passwd_gen(self, last_passwd_gen):
        """
        Sets the last_passwd_gen of this CustomerResponse.

        :param last_passwd_gen: The last_passwd_gen of this CustomerResponse.
        :type: str
        """

        self._last_passwd_gen = last_passwd_gen

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
