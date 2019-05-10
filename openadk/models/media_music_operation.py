# coding: utf-8

"""
    Yanshee RESTful API

    Yanshee RESTful APIs是一套专门为编程爱好者提供二次开发的接口．它通过http/https的方式向外界提供机器人控制，传感器读取，机器人视觉等功能．用户还可以通过编程的方式训练自己的模型，学习一些机器学习的内容．  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class MediaMusicOperation(object):
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
        'operation': 'str',
        'name': 'str'
    }

    attribute_map = {
        'operation': 'operation',
        'name': 'name'
    }

    def __init__(self, operation='start', name='SorrySorry.mp3'):  # noqa: E501
        """MediaMusicOperation - a model defined in Swagger"""  # noqa: E501

        self._operation = None
        self._name = None
        self.discriminator = None

        self.operation = operation
        if name is not None:
            self.name = name

    @property
    def operation(self):
        """Gets the operation of this MediaMusicOperation.  # noqa: E501

        播放控制  # noqa: E501

        :return: The operation of this MediaMusicOperation.  # noqa: E501
        :rtype: str
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        """Sets the operation of this MediaMusicOperation.

        播放控制  # noqa: E501

        :param operation: The operation of this MediaMusicOperation.  # noqa: E501
        :type: str
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501
        allowed_values = ["start", "stop"]  # noqa: E501
        if operation not in allowed_values:
            raise ValueError(
                "Invalid value for `operation` ({0}), must be one of {1}"  # noqa: E501
                .format(operation, allowed_values)
            )

        self._operation = operation

    @property
    def name(self):
        """Gets the name of this MediaMusicOperation.  # noqa: E501

        音乐名称  # noqa: E501

        :return: The name of this MediaMusicOperation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MediaMusicOperation.

        音乐名称  # noqa: E501

        :param name: The name of this MediaMusicOperation.  # noqa: E501
        :type: str
        """

        self._name = name

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
        if issubclass(MediaMusicOperation, dict):
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
        if not isinstance(other, MediaMusicOperation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
