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


class SensorsTouchInfo(object):
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
        'id': 'int',
        'slot': 'int',
        'value': 'int'
    }

    attribute_map = {
        'id': 'id',
        'slot': 'slot',
        'value': 'value'
    }

    def __init__(self, id=None, slot=None, value=None):  # noqa: E501
        """SensorsTouchInfo - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._slot = None
        self._value = None
        self.discriminator = None

        self.id = id
        if slot is not None:
            self.slot = slot
        self.value = value

    @property
    def id(self):
        """Gets the id of this SensorsTouchInfo.  # noqa: E501

        传感器地址  # noqa: E501

        :return: The id of this SensorsTouchInfo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SensorsTouchInfo.

        传感器地址  # noqa: E501

        :param id: The id of this SensorsTouchInfo.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and id > 127:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value less than or equal to `127`")  # noqa: E501
        if id is not None and id < 1:  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def slot(self):
        """Gets the slot of this SensorsTouchInfo.  # noqa: E501

        传感器槽位号  # noqa: E501

        :return: The slot of this SensorsTouchInfo.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this SensorsTouchInfo.

        传感器槽位号  # noqa: E501

        :param slot: The slot of this SensorsTouchInfo.  # noqa: E501
        :type: int
        """
        if slot is not None and slot > 6:  # noqa: E501
            raise ValueError("Invalid value for `slot`, must be a value less than or equal to `6`")  # noqa: E501
        if slot is not None and slot < 1:  # noqa: E501
            raise ValueError("Invalid value for `slot`, must be a value greater than or equal to `1`")  # noqa: E501

        self._slot = slot

    @property
    def value(self):
        """Gets the value of this SensorsTouchInfo.  # noqa: E501

         取值说明： - 0 （未触摸） - 1 （触摸btn1） - 2 （触摸btn2） - 3 （触摸两边）   # noqa: E501

        :return: The value of this SensorsTouchInfo.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SensorsTouchInfo.

         取值说明： - 0 （未触摸） - 1 （触摸btn1） - 2 （触摸btn2） - 3 （触摸两边）   # noqa: E501

        :param value: The value of this SensorsTouchInfo.  # noqa: E501
        :type: int
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if issubclass(SensorsTouchInfo, dict):
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
        if not isinstance(other, SensorsTouchInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
