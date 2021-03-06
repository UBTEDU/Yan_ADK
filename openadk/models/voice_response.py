# coding: utf-8

"""
    Yanshee RESTful API

     ## Overview Yanshee RESTful APIs are generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the [OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server. The API service uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.  To provide the API service, Yanshee RESTful APIs are integrated into apollo package, it is a part of Yanshee-ROS framework. Yanshee RESTful APIs provided two language versions: - [English version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_en/1.0.0) - [Chinese version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_cn/1.0.0)  ## Requirements. Python 2.7 or 3.4+  ## Getting Started Please follow the [installation procedure](#installation--usage) and then run the following:  ``` from __future__ import print_function import time import openadk from openadk.rest import ApiException from pprint import pprint  # create an instance of the API class configuration = openadk.Configuration() configuration.host = 'http://192.168.1.100:9090/v1' api_instance = openadk.DevicesApi(openadk.ApiClient(configuration)) try:  # Get system's battery information  api_response = api_instance.get_devices_battery()  pprint(api_response) except ApiException as e:  print(\"Exception when calling DevicesApi->get_devices_battery: %s\" % e)  ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class VoiceResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'code': 'int',
        'type': 'str',
        'status': 'str',
        'data': 'object',
        'timestamp': 'int',
        'msg': 'str'
    }

    attribute_map = {
        'code': 'code',
        'type': 'type',
        'status': 'status',
        'data': 'data',
        'timestamp': 'timestamp',
        'msg': 'msg'
    }

    def __init__(self, code=None, type=None, status=None, data=None, timestamp=None, msg=None):  # noqa: E501
        """VoiceResponse - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._type = None
        self._status = None
        self._data = None
        self._timestamp = None
        self._msg = None
        self.discriminator = None

        self.code = code
        self.type = type
        if status is not None:
            self.status = status
        if data is not None:
            self.data = data
        if timestamp is not None:
            self.timestamp = timestamp
        self.msg = msg

    @property
    def code(self):
        """Gets the code of this VoiceResponse.  # noqa: E501

        Return code, 0 means success  # noqa: E501

        :return: The code of this VoiceResponse.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this VoiceResponse.

        Return code, 0 means success  # noqa: E501

        :param code: The code of this VoiceResponse.  # noqa: E501
        :type: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def type(self):
        """Gets the type of this VoiceResponse.  # noqa: E501

         Speech recognition result type. The possible value: - asr - iat - tts   # noqa: E501

        :return: The type of this VoiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VoiceResponse.

         Speech recognition result type. The possible value: - asr - iat - tts   # noqa: E501

        :param type: The type of this VoiceResponse.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def status(self):
        """Gets the status of this VoiceResponse.  # noqa: E501

         status - build - idle - run   # noqa: E501

        :return: The status of this VoiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VoiceResponse.

         status - build - idle - run   # noqa: E501

        :param status: The status of this VoiceResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def data(self):
        """Gets the data of this VoiceResponse.  # noqa: E501

        Speech recognition result data.  # noqa: E501

        :return: The data of this VoiceResponse.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this VoiceResponse.

        Speech recognition result data.  # noqa: E501

        :param data: The data of this VoiceResponse.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def timestamp(self):
        """Gets the timestamp of this VoiceResponse.  # noqa: E501

         Speech recognition timestamp.   # noqa: E501

        :return: The timestamp of this VoiceResponse.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this VoiceResponse.

         Speech recognition timestamp.   # noqa: E501

        :param timestamp: The timestamp of this VoiceResponse.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def msg(self):
        """Gets the msg of this VoiceResponse.  # noqa: E501

        Return message  # noqa: E501

        :return: The msg of this VoiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        """Sets the msg of this VoiceResponse.

        Return message  # noqa: E501

        :param msg: The msg of this VoiceResponse.  # noqa: E501
        :type: str
        """
        if msg is None:
            raise ValueError("Invalid value for `msg`, must not be `None`")  # noqa: E501

        self._msg = msg

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(VoiceResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, VoiceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
