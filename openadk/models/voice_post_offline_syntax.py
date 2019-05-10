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

from openadk.models.voice_offline_slot import VoiceOfflineSlot  # noqa: F401,E501
from openadk.models.voice_offline_syntax_rule import VoiceOfflineSyntaxRule  # noqa: F401,E501


class VoicePostOfflineSyntax(object):
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
        'grammar': 'str',
        'slot': 'list[VoiceOfflineSlot]',
        'start': 'str',
        'startinfo': 'str',
        'rule': 'list[VoiceOfflineSyntaxRule]'
    }

    attribute_map = {
        'grammar': 'grammar',
        'slot': 'slot',
        'start': 'start',
        'startinfo': 'startinfo',
        'rule': 'rule'
    }

    def __init__(self, grammar=None, slot=None, start=None, startinfo=None, rule=None):  # noqa: E501
        """VoicePostOfflineSyntax - a model defined in Swagger"""  # noqa: E501

        self._grammar = None
        self._slot = None
        self._start = None
        self._startinfo = None
        self._rule = None
        self.discriminator = None

        self.grammar = grammar
        self.slot = slot
        self.start = start
        self.startinfo = startinfo
        self.rule = rule

    @property
    def grammar(self):
        """Gets the grammar of this VoicePostOfflineSyntax.  # noqa: E501

        定义语法名称, 请输入纯字母  # noqa: E501

        :return: The grammar of this VoicePostOfflineSyntax.  # noqa: E501
        :rtype: str
        """
        return self._grammar

    @grammar.setter
    def grammar(self, grammar):
        """Sets the grammar of this VoicePostOfflineSyntax.

        定义语法名称, 请输入纯字母  # noqa: E501

        :param grammar: The grammar of this VoicePostOfflineSyntax.  # noqa: E501
        :type: str
        """
        if grammar is None:
            raise ValueError("Invalid value for `grammar`, must not be `None`")  # noqa: E501

        self._grammar = grammar

    @property
    def slot(self):
        """Gets the slot of this VoicePostOfflineSyntax.  # noqa: E501

        声明槽, 内容为字母不数字。所有的操作符及关键词均为半角字符，而丌支持全角字符。  # noqa: E501

        :return: The slot of this VoicePostOfflineSyntax.  # noqa: E501
        :rtype: list[VoiceOfflineSlot]
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this VoicePostOfflineSyntax.

        声明槽, 内容为字母不数字。所有的操作符及关键词均为半角字符，而丌支持全角字符。  # noqa: E501

        :param slot: The slot of this VoicePostOfflineSyntax.  # noqa: E501
        :type: list[VoiceOfflineSlot]
        """
        if slot is None:
            raise ValueError("Invalid value for `slot`, must not be `None`")  # noqa: E501

        self._slot = slot

    @property
    def start(self):
        """Gets the start of this VoicePostOfflineSyntax.  # noqa: E501

        定义开始规则, 内容为字母不数字。所有的操作符及关键词均为半角字符，而丌支持全角字符。  # noqa: E501

        :return: The start of this VoicePostOfflineSyntax.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this VoicePostOfflineSyntax.

        定义开始规则, 内容为字母不数字。所有的操作符及关键词均为半角字符，而丌支持全角字符。  # noqa: E501

        :param start: The start of this VoicePostOfflineSyntax.  # noqa: E501
        :type: str
        """
        if start is None:
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def startinfo(self):
        """Gets the startinfo of this VoicePostOfflineSyntax.  # noqa: E501

        定义开始规则详细内容  # noqa: E501

        :return: The startinfo of this VoicePostOfflineSyntax.  # noqa: E501
        :rtype: str
        """
        return self._startinfo

    @startinfo.setter
    def startinfo(self, startinfo):
        """Sets the startinfo of this VoicePostOfflineSyntax.

        定义开始规则详细内容  # noqa: E501

        :param startinfo: The startinfo of this VoicePostOfflineSyntax.  # noqa: E501
        :type: str
        """
        if startinfo is None:
            raise ValueError("Invalid value for `startinfo`, must not be `None`")  # noqa: E501

        self._startinfo = startinfo

    @property
    def rule(self):
        """Gets the rule of this VoicePostOfflineSyntax.  # noqa: E501

        所有的离线语法规则  # noqa: E501

        :return: The rule of this VoicePostOfflineSyntax.  # noqa: E501
        :rtype: list[VoiceOfflineSyntaxRule]
        """
        return self._rule

    @rule.setter
    def rule(self, rule):
        """Sets the rule of this VoicePostOfflineSyntax.

        所有的离线语法规则  # noqa: E501

        :param rule: The rule of this VoicePostOfflineSyntax.  # noqa: E501
        :type: list[VoiceOfflineSyntaxRule]
        """
        if rule is None:
            raise ValueError("Invalid value for `rule`, must not be `None`")  # noqa: E501

        self._rule = rule

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
        if issubclass(VoicePostOfflineSyntax, dict):
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
        if not isinstance(other, VoicePostOfflineSyntax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
