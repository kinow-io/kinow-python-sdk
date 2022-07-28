# coding: utf-8

"""
    Server API

    Reference for Server API (REST/Json)

    OpenAPI spec version: 2.0.13
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SubscriptionResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, id_product=None, duration=None, download=None, trial_duration=None, trial_percent=None, trial_sub=None, limit=None, limit_duration=None, alert_type=None, alert_qty=None, active=None, recurring_payment=None):
        """
        SubscriptionResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'id_product': 'int',
            'duration': 'int',
            'download': 'bool',
            'trial_duration': 'int',
            'trial_percent': 'int',
            'trial_sub': 'int',
            'limit': 'bool',
            'limit_duration': 'int',
            'alert_type': 'str',
            'alert_qty': 'int',
            'active': 'bool',
            'recurring_payment': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'id_product': 'id_product',
            'duration': 'duration',
            'download': 'download',
            'trial_duration': 'trial_duration',
            'trial_percent': 'trial_percent',
            'trial_sub': 'trial_sub',
            'limit': 'limit',
            'limit_duration': 'limit_duration',
            'alert_type': 'alert_type',
            'alert_qty': 'alert_qty',
            'active': 'active',
            'recurring_payment': 'recurring_payment'
        }

        self._id = id
        self._id_product = id_product
        self._duration = duration
        self._download = download
        self._trial_duration = trial_duration
        self._trial_percent = trial_percent
        self._trial_sub = trial_sub
        self._limit = limit
        self._limit_duration = limit_duration
        self._alert_type = alert_type
        self._alert_qty = alert_qty
        self._active = active
        self._recurring_payment = recurring_payment

    @property
    def id(self):
        """
        Gets the id of this SubscriptionResponse.

        :return: The id of this SubscriptionResponse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SubscriptionResponse.

        :param id: The id of this SubscriptionResponse.
        :type: int
        """

        self._id = id

    @property
    def id_product(self):
        """
        Gets the id_product of this SubscriptionResponse.

        :return: The id_product of this SubscriptionResponse.
        :rtype: int
        """
        return self._id_product

    @id_product.setter
    def id_product(self, id_product):
        """
        Sets the id_product of this SubscriptionResponse.

        :param id_product: The id_product of this SubscriptionResponse.
        :type: int
        """

        self._id_product = id_product

    @property
    def duration(self):
        """
        Gets the duration of this SubscriptionResponse.

        :return: The duration of this SubscriptionResponse.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this SubscriptionResponse.

        :param duration: The duration of this SubscriptionResponse.
        :type: int
        """

        self._duration = duration

    @property
    def download(self):
        """
        Gets the download of this SubscriptionResponse.

        :return: The download of this SubscriptionResponse.
        :rtype: bool
        """
        return self._download

    @download.setter
    def download(self, download):
        """
        Sets the download of this SubscriptionResponse.

        :param download: The download of this SubscriptionResponse.
        :type: bool
        """

        self._download = download

    @property
    def trial_duration(self):
        """
        Gets the trial_duration of this SubscriptionResponse.

        :return: The trial_duration of this SubscriptionResponse.
        :rtype: int
        """
        return self._trial_duration

    @trial_duration.setter
    def trial_duration(self, trial_duration):
        """
        Sets the trial_duration of this SubscriptionResponse.

        :param trial_duration: The trial_duration of this SubscriptionResponse.
        :type: int
        """

        self._trial_duration = trial_duration

    @property
    def trial_percent(self):
        """
        Gets the trial_percent of this SubscriptionResponse.

        :return: The trial_percent of this SubscriptionResponse.
        :rtype: int
        """
        return self._trial_percent

    @trial_percent.setter
    def trial_percent(self, trial_percent):
        """
        Sets the trial_percent of this SubscriptionResponse.

        :param trial_percent: The trial_percent of this SubscriptionResponse.
        :type: int
        """

        self._trial_percent = trial_percent

    @property
    def trial_sub(self):
        """
        Gets the trial_sub of this SubscriptionResponse.

        :return: The trial_sub of this SubscriptionResponse.
        :rtype: int
        """
        return self._trial_sub

    @trial_sub.setter
    def trial_sub(self, trial_sub):
        """
        Sets the trial_sub of this SubscriptionResponse.

        :param trial_sub: The trial_sub of this SubscriptionResponse.
        :type: int
        """

        self._trial_sub = trial_sub

    @property
    def limit(self):
        """
        Gets the limit of this SubscriptionResponse.

        :return: The limit of this SubscriptionResponse.
        :rtype: bool
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this SubscriptionResponse.

        :param limit: The limit of this SubscriptionResponse.
        :type: bool
        """

        self._limit = limit

    @property
    def limit_duration(self):
        """
        Gets the limit_duration of this SubscriptionResponse.

        :return: The limit_duration of this SubscriptionResponse.
        :rtype: int
        """
        return self._limit_duration

    @limit_duration.setter
    def limit_duration(self, limit_duration):
        """
        Sets the limit_duration of this SubscriptionResponse.

        :param limit_duration: The limit_duration of this SubscriptionResponse.
        :type: int
        """

        self._limit_duration = limit_duration

    @property
    def alert_type(self):
        """
        Gets the alert_type of this SubscriptionResponse.

        :return: The alert_type of this SubscriptionResponse.
        :rtype: str
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """
        Sets the alert_type of this SubscriptionResponse.

        :param alert_type: The alert_type of this SubscriptionResponse.
        :type: str
        """

        self._alert_type = alert_type

    @property
    def alert_qty(self):
        """
        Gets the alert_qty of this SubscriptionResponse.

        :return: The alert_qty of this SubscriptionResponse.
        :rtype: int
        """
        return self._alert_qty

    @alert_qty.setter
    def alert_qty(self, alert_qty):
        """
        Sets the alert_qty of this SubscriptionResponse.

        :param alert_qty: The alert_qty of this SubscriptionResponse.
        :type: int
        """

        self._alert_qty = alert_qty

    @property
    def active(self):
        """
        Gets the active of this SubscriptionResponse.

        :return: The active of this SubscriptionResponse.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this SubscriptionResponse.

        :param active: The active of this SubscriptionResponse.
        :type: bool
        """

        self._active = active

    @property
    def recurring_payment(self):
        """
        Gets the recurring_payment of this SubscriptionResponse.

        :return: The recurring_payment of this SubscriptionResponse.
        :rtype: int
        """
        return self._recurring_payment

    @recurring_payment.setter
    def recurring_payment(self, recurring_payment):
        """
        Sets the recurring_payment of this SubscriptionResponse.

        :param recurring_payment: The recurring_payment of this SubscriptionResponse.
        :type: int
        """

        self._recurring_payment = recurring_payment

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
