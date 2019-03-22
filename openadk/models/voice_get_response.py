# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk import util


class VoiceGetResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code=None, status=None, timestamp=None, data=None, msg=None):  # noqa: E501
        """VoiceGetResponse - a model defined in Swagger

        :param code: The code of this VoiceGetResponse.  # noqa: E501
        :type code: int
        :param status: The status of this VoiceGetResponse.  # noqa: E501
        :type status: str
        :param timestamp: The timestamp of this VoiceGetResponse.  # noqa: E501
        :type timestamp: int
        :param data: The data of this VoiceGetResponse.  # noqa: E501
        :type data: object
        :param msg: The msg of this VoiceGetResponse.  # noqa: E501
        :type msg: str
        """
        self.swagger_types = {
            'code': int,
            'status': str,
            'timestamp': int,
            'data': object,
            'msg': str
        }

        self.attribute_map = {
            'code': 'code',
            'status': 'status',
            'timestamp': 'timestamp',
            'data': 'data',
            'msg': 'msg'
        }

        self._code = code
        self._status = status
        self._timestamp = timestamp
        self._data = data
        self._msg = msg

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VoiceGetResponse of this VoiceGetResponse.  # noqa: E501
        :rtype: VoiceGetResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this VoiceGetResponse.

        返回码，0表示正常  # noqa: E501

        :return: The code of this VoiceGetResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this VoiceGetResponse.

        返回码，0表示正常  # noqa: E501

        :param code: The code of this VoiceGetResponse.
        :type code: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def status(self):
        """Gets the status of this VoiceGetResponse.


        :return: The status of this VoiceGetResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VoiceGetResponse.


        :param status: The status of this VoiceGetResponse.
        :type status: str
        """
        allowed_values = ["idle", "running", "pause"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def timestamp(self):
        """Gets the timestamp of this VoiceGetResponse.

        时间戳, Unix标准时间  # noqa: E501

        :return: The timestamp of this VoiceGetResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this VoiceGetResponse.

        时间戳, Unix标准时间  # noqa: E501

        :param timestamp: The timestamp of this VoiceGetResponse.
        :type timestamp: int
        """

        self._timestamp = timestamp

    @property
    def data(self):
        """Gets the data of this VoiceGetResponse.

        语音返回数据  # noqa: E501

        :return: The data of this VoiceGetResponse.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this VoiceGetResponse.

        语音返回数据  # noqa: E501

        :param data: The data of this VoiceGetResponse.
        :type data: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def msg(self):
        """Gets the msg of this VoiceGetResponse.

        返回附件信息  # noqa: E501

        :return: The msg of this VoiceGetResponse.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this VoiceGetResponse.

        返回附件信息  # noqa: E501

        :param msg: The msg of this VoiceGetResponse.
        :type msg: str
        """
        if msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg
