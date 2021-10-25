# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 1.4.58
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class CustomerCreateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, firstname=None, lastname=None, email=None, password=None, id_gender=None, birthday=None, newsletter=None, optin=None, active=None, id_lang=None, id_country=None, city=None, postcode=None, address1=None, company=None, send_mail=None):
        """
        CustomerCreateRequest - a model defined in Swagger

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
            'id_country': 'int',
            'city': 'str',
            'postcode': 'str',
            'address1': 'str',
            'company': 'str',
            'send_mail': 'bool'
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
            'id_country': 'id_country',
            'city': 'city',
            'postcode': 'postcode',
            'address1': 'address1',
            'company': 'company',
            'send_mail': 'send_mail'
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
        self._id_country = id_country
        self._city = city
        self._postcode = postcode
        self._address1 = address1
        self._company = company
        self._send_mail = send_mail

    @property
    def firstname(self):
        """
        Gets the firstname of this CustomerCreateRequest.

        :return: The firstname of this CustomerCreateRequest.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this CustomerCreateRequest.

        :param firstname: The firstname of this CustomerCreateRequest.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this CustomerCreateRequest.

        :return: The lastname of this CustomerCreateRequest.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this CustomerCreateRequest.

        :param lastname: The lastname of this CustomerCreateRequest.
        :type: str
        """

        self._lastname = lastname

    @property
    def email(self):
        """
        Gets the email of this CustomerCreateRequest.

        :return: The email of this CustomerCreateRequest.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this CustomerCreateRequest.

        :param email: The email of this CustomerCreateRequest.
        :type: str
        """

        self._email = email

    @property
    def password(self):
        """
        Gets the password of this CustomerCreateRequest.

        :return: The password of this CustomerCreateRequest.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CustomerCreateRequest.

        :param password: The password of this CustomerCreateRequest.
        :type: str
        """

        self._password = password

    @property
    def id_gender(self):
        """
        Gets the id_gender of this CustomerCreateRequest.

        :return: The id_gender of this CustomerCreateRequest.
        :rtype: int
        """
        return self._id_gender

    @id_gender.setter
    def id_gender(self, id_gender):
        """
        Sets the id_gender of this CustomerCreateRequest.

        :param id_gender: The id_gender of this CustomerCreateRequest.
        :type: int
        """

        self._id_gender = id_gender

    @property
    def birthday(self):
        """
        Gets the birthday of this CustomerCreateRequest.

        :return: The birthday of this CustomerCreateRequest.
        :rtype: str
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """
        Sets the birthday of this CustomerCreateRequest.

        :param birthday: The birthday of this CustomerCreateRequest.
        :type: str
        """

        self._birthday = birthday

    @property
    def newsletter(self):
        """
        Gets the newsletter of this CustomerCreateRequest.

        :return: The newsletter of this CustomerCreateRequest.
        :rtype: bool
        """
        return self._newsletter

    @newsletter.setter
    def newsletter(self, newsletter):
        """
        Sets the newsletter of this CustomerCreateRequest.

        :param newsletter: The newsletter of this CustomerCreateRequest.
        :type: bool
        """

        self._newsletter = newsletter

    @property
    def optin(self):
        """
        Gets the optin of this CustomerCreateRequest.

        :return: The optin of this CustomerCreateRequest.
        :rtype: bool
        """
        return self._optin

    @optin.setter
    def optin(self, optin):
        """
        Sets the optin of this CustomerCreateRequest.

        :param optin: The optin of this CustomerCreateRequest.
        :type: bool
        """

        self._optin = optin

    @property
    def active(self):
        """
        Gets the active of this CustomerCreateRequest.

        :return: The active of this CustomerCreateRequest.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this CustomerCreateRequest.

        :param active: The active of this CustomerCreateRequest.
        :type: bool
        """

        self._active = active

    @property
    def id_lang(self):
        """
        Gets the id_lang of this CustomerCreateRequest.

        :return: The id_lang of this CustomerCreateRequest.
        :rtype: int
        """
        return self._id_lang

    @id_lang.setter
    def id_lang(self, id_lang):
        """
        Sets the id_lang of this CustomerCreateRequest.

        :param id_lang: The id_lang of this CustomerCreateRequest.
        :type: int
        """

        self._id_lang = id_lang

    @property
    def id_country(self):
        """
        Gets the id_country of this CustomerCreateRequest.

        :return: The id_country of this CustomerCreateRequest.
        :rtype: int
        """
        return self._id_country

    @id_country.setter
    def id_country(self, id_country):
        """
        Sets the id_country of this CustomerCreateRequest.

        :param id_country: The id_country of this CustomerCreateRequest.
        :type: int
        """

        self._id_country = id_country

    @property
    def city(self):
        """
        Gets the city of this CustomerCreateRequest.

        :return: The city of this CustomerCreateRequest.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this CustomerCreateRequest.

        :param city: The city of this CustomerCreateRequest.
        :type: str
        """

        self._city = city

    @property
    def postcode(self):
        """
        Gets the postcode of this CustomerCreateRequest.

        :return: The postcode of this CustomerCreateRequest.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """
        Sets the postcode of this CustomerCreateRequest.

        :param postcode: The postcode of this CustomerCreateRequest.
        :type: str
        """

        self._postcode = postcode

    @property
    def address1(self):
        """
        Gets the address1 of this CustomerCreateRequest.

        :return: The address1 of this CustomerCreateRequest.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this CustomerCreateRequest.

        :param address1: The address1 of this CustomerCreateRequest.
        :type: str
        """

        self._address1 = address1

    @property
    def company(self):
        """
        Gets the company of this CustomerCreateRequest.

        :return: The company of this CustomerCreateRequest.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this CustomerCreateRequest.

        :param company: The company of this CustomerCreateRequest.
        :type: str
        """

        self._company = company

    @property
    def send_mail(self):
        """
        Gets the send_mail of this CustomerCreateRequest.

        :return: The send_mail of this CustomerCreateRequest.
        :rtype: bool
        """
        return self._send_mail

    @send_mail.setter
    def send_mail(self, send_mail):
        """
        Sets the send_mail of this CustomerCreateRequest.

        :param send_mail: The send_mail of this CustomerCreateRequest.
        :type: bool
        """

        self._send_mail = send_mail

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
