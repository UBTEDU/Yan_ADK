# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk import util


class SubscriptionsVoice(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type=None, url=None, timeout=10):  # noqa: E501
        """SubscriptionsVoice - a model defined in Swagger

        :param type: The type of this SubscriptionsVoice.  # noqa: E501
        :type type: str
        :param url: The url of this SubscriptionsVoice.  # noqa: E501
        :type url: str
        :param timeout: The timeout of this SubscriptionsVoice.  # noqa: E501
        :type timeout: int
        """
        self.swagger_types = {
            'type': str,
            'url': str,
            'timeout': int
        }

        self.attribute_map = {
            'type': 'type',
            'url': 'url',
            'timeout': 'timeout'
        }

        self._type = type
        self._url = url
        self._timeout = timeout

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscriptionsVoice of this SubscriptionsVoice.  # noqa: E501
        :rtype: SubscriptionsVoice
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self):
        """Gets the type of this SubscriptionsVoice.

        订阅的语音服务类型  # noqa: E501

        :return: The type of this SubscriptionsVoice.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubscriptionsVoice.

        订阅的语音服务类型  # noqa: E501

        :param type: The type of this SubscriptionsVoice.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def url(self):
        """Gets the url of this SubscriptionsVoice.

        协议与地址  # noqa: E501

        :return: The url of this SubscriptionsVoice.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SubscriptionsVoice.

        协议与地址  # noqa: E501

        :param url: The url of this SubscriptionsVoice.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def timeout(self):
        """Gets the timeout of this SubscriptionsVoice.

        超时停止发送的时间  # noqa: E501

        :return: The timeout of this SubscriptionsVoice.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this SubscriptionsVoice.

        超时停止发送的时间  # noqa: E501

        :param timeout: The timeout of this SubscriptionsVoice.
        :type timeout: int
        """
        if timeout is not None and timeout > 60:  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value less than or equal to `60`")  # noqa: E501
        if timeout is not None and timeout < 1:  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must be a value greater than or equal to `1`")  # noqa: E501

        self._timeout = timeout
