# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk import util


class MotionsInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name=None, music=None):  # noqa: E501
        """MotionsInfo - a model defined in Swagger

        :param name: The name of this MotionsInfo.  # noqa: E501
        :type name: str
        :param music: The music of this MotionsInfo.  # noqa: E501
        :type music: bool
        """
        self.swagger_types = {
            'name': str,
            'music': bool
        }

        self.attribute_map = {
            'name': 'name',
            'music': 'music'
        }

        self._name = name
        self._music = music

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MotionsInfo of this MotionsInfo.  # noqa: E501
        :rtype: MotionsInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this MotionsInfo.

        动作名称  # noqa: E501

        :return: The name of this MotionsInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MotionsInfo.

        动作名称  # noqa: E501

        :param name: The name of this MotionsInfo.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def music(self):
        """Gets the music of this MotionsInfo.

        是否带有音乐  # noqa: E501

        :return: The music of this MotionsInfo.
        :rtype: bool
        """
        return self._music

    @music.setter
    def music(self, music):
        """Sets the music of this MotionsInfo.

        是否带有音乐  # noqa: E501

        :param music: The music of this MotionsInfo.
        :type music: bool
        """
        if music is None:
            raise ValueError("Invalid value for `music`, must not be `None`")  # noqa: E501

        self._music = music
