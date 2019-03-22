# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk.models.devices_led import DevicesLED  # noqa: F401,E501
from openadk import util


class DevicesLEDResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code=None, data=None, msg=None):  # noqa: E501
        """DevicesLEDResponse - a model defined in Swagger

        :param code: The code of this DevicesLEDResponse.  # noqa: E501
        :type code: int
        :param data: The data of this DevicesLEDResponse.  # noqa: E501
        :type data: List[DevicesLED]
        :param msg: The msg of this DevicesLEDResponse.  # noqa: E501
        :type msg: str
        """
        self.swagger_types = {
            'code': int,
            'data': List[DevicesLED],
            'msg': str
        }

        self.attribute_map = {
            'code': 'code',
            'data': 'data',
            'msg': 'msg'
        }

        self._code = code
        self._data = data
        self._msg = msg

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DevicesLEDResponse of this DevicesLEDResponse.  # noqa: E501
        :rtype: DevicesLEDResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this DevicesLEDResponse.

        错误码  # noqa: E501

        :return: The code of this DevicesLEDResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DevicesLEDResponse.

        错误码  # noqa: E501

        :param code: The code of this DevicesLEDResponse.
        :type code: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def data(self):
        """Gets the data of this DevicesLEDResponse.


        :return: The data of this DevicesLEDResponse.
        :rtype: List[DevicesLED]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this DevicesLEDResponse.


        :param data: The data of this DevicesLEDResponse.
        :type data: List[DevicesLED]
        """

        self._data = data

    @property
    def msg(self):
        """Gets the msg of this DevicesLEDResponse.

        错误码消息  # noqa: E501

        :return: The msg of this DevicesLEDResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this DevicesLEDResponse.

        错误码消息  # noqa: E501

        :param msg: The msg of this DevicesLEDResponse.
        :type msg: str
        """
        if msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg
