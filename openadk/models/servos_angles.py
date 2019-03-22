# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk import util


class ServosAngles(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, right_shoulder_roll=None, right_shoulder_flex=None, right_elbow_flex=None, left_shoulder_roll=None, left_shoulder_flex=None, left_elbow_flex=None, right_hip_lr=None, right_hip_fb=None, right_knee_flex=None, right_ankle_fb=None, right_ankle_ud=None, left_hip_lr=None, left_hip_fb=None, left_knee_flex=None, left_ankle_fb=None, left_ankle_ud=None, neck_lr=None):  # noqa: E501
        """ServosAngles - a model defined in Swagger

        :param right_shoulder_roll: The right_shoulder_roll of this ServosAngles.  # noqa: E501
        :type right_shoulder_roll: int
        :param right_shoulder_flex: The right_shoulder_flex of this ServosAngles.  # noqa: E501
        :type right_shoulder_flex: int
        :param right_elbow_flex: The right_elbow_flex of this ServosAngles.  # noqa: E501
        :type right_elbow_flex: int
        :param left_shoulder_roll: The left_shoulder_roll of this ServosAngles.  # noqa: E501
        :type left_shoulder_roll: int
        :param left_shoulder_flex: The left_shoulder_flex of this ServosAngles.  # noqa: E501
        :type left_shoulder_flex: int
        :param left_elbow_flex: The left_elbow_flex of this ServosAngles.  # noqa: E501
        :type left_elbow_flex: int
        :param right_hip_lr: The right_hip_lr of this ServosAngles.  # noqa: E501
        :type right_hip_lr: int
        :param right_hip_fb: The right_hip_fb of this ServosAngles.  # noqa: E501
        :type right_hip_fb: int
        :param right_knee_flex: The right_knee_flex of this ServosAngles.  # noqa: E501
        :type right_knee_flex: int
        :param right_ankle_fb: The right_ankle_fb of this ServosAngles.  # noqa: E501
        :type right_ankle_fb: int
        :param right_ankle_ud: The right_ankle_ud of this ServosAngles.  # noqa: E501
        :type right_ankle_ud: int
        :param left_hip_lr: The left_hip_lr of this ServosAngles.  # noqa: E501
        :type left_hip_lr: int
        :param left_hip_fb: The left_hip_fb of this ServosAngles.  # noqa: E501
        :type left_hip_fb: int
        :param left_knee_flex: The left_knee_flex of this ServosAngles.  # noqa: E501
        :type left_knee_flex: int
        :param left_ankle_fb: The left_ankle_fb of this ServosAngles.  # noqa: E501
        :type left_ankle_fb: int
        :param left_ankle_ud: The left_ankle_ud of this ServosAngles.  # noqa: E501
        :type left_ankle_ud: int
        :param neck_lr: The neck_lr of this ServosAngles.  # noqa: E501
        :type neck_lr: int
        """
        self.swagger_types = {
            'right_shoulder_roll': int,
            'right_shoulder_flex': int,
            'right_elbow_flex': int,
            'left_shoulder_roll': int,
            'left_shoulder_flex': int,
            'left_elbow_flex': int,
            'right_hip_lr': int,
            'right_hip_fb': int,
            'right_knee_flex': int,
            'right_ankle_fb': int,
            'right_ankle_ud': int,
            'left_hip_lr': int,
            'left_hip_fb': int,
            'left_knee_flex': int,
            'left_ankle_fb': int,
            'left_ankle_ud': int,
            'neck_lr': int
        }

        self.attribute_map = {
            'right_shoulder_roll': 'RightShoulderRoll',
            'right_shoulder_flex': 'RightShoulderFlex',
            'right_elbow_flex': 'RightElbowFlex',
            'left_shoulder_roll': 'LeftShoulderRoll',
            'left_shoulder_flex': 'LeftShoulderFlex',
            'left_elbow_flex': 'LeftElbowFlex',
            'right_hip_lr': 'RightHipLR',
            'right_hip_fb': 'RightHipFB',
            'right_knee_flex': 'RightKneeFlex',
            'right_ankle_fb': 'RightAnkleFB',
            'right_ankle_ud': 'RightAnkleUD',
            'left_hip_lr': 'LeftHipLR',
            'left_hip_fb': 'LeftHipFB',
            'left_knee_flex': 'LeftKneeFlex',
            'left_ankle_fb': 'LeftAnkleFB',
            'left_ankle_ud': 'LeftAnkleUD',
            'neck_lr': 'NeckLR'
        }

        self._right_shoulder_roll = right_shoulder_roll
        self._right_shoulder_flex = right_shoulder_flex
        self._right_elbow_flex = right_elbow_flex
        self._left_shoulder_roll = left_shoulder_roll
        self._left_shoulder_flex = left_shoulder_flex
        self._left_elbow_flex = left_elbow_flex
        self._right_hip_lr = right_hip_lr
        self._right_hip_fb = right_hip_fb
        self._right_knee_flex = right_knee_flex
        self._right_ankle_fb = right_ankle_fb
        self._right_ankle_ud = right_ankle_ud
        self._left_hip_lr = left_hip_lr
        self._left_hip_fb = left_hip_fb
        self._left_knee_flex = left_knee_flex
        self._left_ankle_fb = left_ankle_fb
        self._left_ankle_ud = left_ankle_ud
        self._neck_lr = neck_lr

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServosAngles of this ServosAngles.  # noqa: E501
        :rtype: ServosAngles
        """
        return util.deserialize_model(dikt, cls)

    @property
    def right_shoulder_roll(self):
        """Gets the right_shoulder_roll of this ServosAngles.

        1号舵机  # noqa: E501

        :return: The right_shoulder_roll of this ServosAngles.
        :rtype: int
        """
        return self._right_shoulder_roll

    @right_shoulder_roll.setter
    def right_shoulder_roll(self, right_shoulder_roll):
        """Sets the right_shoulder_roll of this ServosAngles.

        1号舵机  # noqa: E501

        :param right_shoulder_roll: The right_shoulder_roll of this ServosAngles.
        :type right_shoulder_roll: int
        """
        if right_shoulder_roll is not None and right_shoulder_roll > 180:  # noqa: E501
            raise ValueError("Invalid value for `right_shoulder_roll`, must be a value less than or equal to `180`")  # noqa: E501
        if right_shoulder_roll is not None and right_shoulder_roll < 0:  # noqa: E501
            raise ValueError("Invalid value for `right_shoulder_roll`, must be a value greater than or equal to `0`")  # noqa: E501

        self._right_shoulder_roll = right_shoulder_roll

    @property
    def right_shoulder_flex(self):
        """Gets the right_shoulder_flex of this ServosAngles.

        2号舵机  # noqa: E501

        :return: The right_shoulder_flex of this ServosAngles.
        :rtype: int
        """
        return self._right_shoulder_flex

    @right_shoulder_flex.setter
    def right_shoulder_flex(self, right_shoulder_flex):
        """Sets the right_shoulder_flex of this ServosAngles.

        2号舵机  # noqa: E501

        :param right_shoulder_flex: The right_shoulder_flex of this ServosAngles.
        :type right_shoulder_flex: int
        """
        if right_shoulder_flex is not None and right_shoulder_flex > 180:  # noqa: E501
            raise ValueError("Invalid value for `right_shoulder_flex`, must be a value less than or equal to `180`")  # noqa: E501
        if right_shoulder_flex is not None and right_shoulder_flex < 0:  # noqa: E501
            raise ValueError("Invalid value for `right_shoulder_flex`, must be a value greater than or equal to `0`")  # noqa: E501

        self._right_shoulder_flex = right_shoulder_flex

    @property
    def right_elbow_flex(self):
        """Gets the right_elbow_flex of this ServosAngles.

        3号舵机  # noqa: E501

        :return: The right_elbow_flex of this ServosAngles.
        :rtype: int
        """
        return self._right_elbow_flex

    @right_elbow_flex.setter
    def right_elbow_flex(self, right_elbow_flex):
        """Sets the right_elbow_flex of this ServosAngles.

        3号舵机  # noqa: E501

        :param right_elbow_flex: The right_elbow_flex of this ServosAngles.
        :type right_elbow_flex: int
        """
        if right_elbow_flex is not None and right_elbow_flex > 180:  # noqa: E501
            raise ValueError("Invalid value for `right_elbow_flex`, must be a value less than or equal to `180`")  # noqa: E501
        if right_elbow_flex is not None and right_elbow_flex < 0:  # noqa: E501
            raise ValueError("Invalid value for `right_elbow_flex`, must be a value greater than or equal to `0`")  # noqa: E501

        self._right_elbow_flex = right_elbow_flex

    @property
    def left_shoulder_roll(self):
        """Gets the left_shoulder_roll of this ServosAngles.

        4号舵机  # noqa: E501

        :return: The left_shoulder_roll of this ServosAngles.
        :rtype: int
        """
        return self._left_shoulder_roll

    @left_shoulder_roll.setter
    def left_shoulder_roll(self, left_shoulder_roll):
        """Sets the left_shoulder_roll of this ServosAngles.

        4号舵机  # noqa: E501

        :param left_shoulder_roll: The left_shoulder_roll of this ServosAngles.
        :type left_shoulder_roll: int
        """
        if left_shoulder_roll is not None and left_shoulder_roll > 180:  # noqa: E501
            raise ValueError("Invalid value for `left_shoulder_roll`, must be a value less than or equal to `180`")  # noqa: E501
        if left_shoulder_roll is not None and left_shoulder_roll < 0:  # noqa: E501
            raise ValueError("Invalid value for `left_shoulder_roll`, must be a value greater than or equal to `0`")  # noqa: E501

        self._left_shoulder_roll = left_shoulder_roll

    @property
    def left_shoulder_flex(self):
        """Gets the left_shoulder_flex of this ServosAngles.

        5号舵机  # noqa: E501

        :return: The left_shoulder_flex of this ServosAngles.
        :rtype: int
        """
        return self._left_shoulder_flex

    @left_shoulder_flex.setter
    def left_shoulder_flex(self, left_shoulder_flex):
        """Sets the left_shoulder_flex of this ServosAngles.

        5号舵机  # noqa: E501

        :param left_shoulder_flex: The left_shoulder_flex of this ServosAngles.
        :type left_shoulder_flex: int
        """
        if left_shoulder_flex is not None and left_shoulder_flex > 180:  # noqa: E501
            raise ValueError("Invalid value for `left_shoulder_flex`, must be a value less than or equal to `180`")  # noqa: E501
        if left_shoulder_flex is not None and left_shoulder_flex < 0:  # noqa: E501
            raise ValueError("Invalid value for `left_shoulder_flex`, must be a value greater than or equal to `0`")  # noqa: E501

        self._left_shoulder_flex = left_shoulder_flex

    @property
    def left_elbow_flex(self):
        """Gets the left_elbow_flex of this ServosAngles.

        6号舵机  # noqa: E501

        :return: The left_elbow_flex of this ServosAngles.
        :rtype: int
        """
        return self._left_elbow_flex

    @left_elbow_flex.setter
    def left_elbow_flex(self, left_elbow_flex):
        """Sets the left_elbow_flex of this ServosAngles.

        6号舵机  # noqa: E501

        :param left_elbow_flex: The left_elbow_flex of this ServosAngles.
        :type left_elbow_flex: int
        """
        if left_elbow_flex is not None and left_elbow_flex > 180:  # noqa: E501
            raise ValueError("Invalid value for `left_elbow_flex`, must be a value less than or equal to `180`")  # noqa: E501
        if left_elbow_flex is not None and left_elbow_flex < 0:  # noqa: E501
            raise ValueError("Invalid value for `left_elbow_flex`, must be a value greater than or equal to `0`")  # noqa: E501

        self._left_elbow_flex = left_elbow_flex

    @property
    def right_hip_lr(self):
        """Gets the right_hip_lr of this ServosAngles.

        7号舵机  # noqa: E501

        :return: The right_hip_lr of this ServosAngles.
        :rtype: int
        """
        return self._right_hip_lr

    @right_hip_lr.setter
    def right_hip_lr(self, right_hip_lr):
        """Sets the right_hip_lr of this ServosAngles.

        7号舵机  # noqa: E501

        :param right_hip_lr: The right_hip_lr of this ServosAngles.
        :type right_hip_lr: int
        """
        if right_hip_lr is not None and right_hip_lr > 180:  # noqa: E501
            raise ValueError("Invalid value for `right_hip_lr`, must be a value less than or equal to `180`")  # noqa: E501
        if right_hip_lr is not None and right_hip_lr < 0:  # noqa: E501
            raise ValueError("Invalid value for `right_hip_lr`, must be a value greater than or equal to `0`")  # noqa: E501

        self._right_hip_lr = right_hip_lr

    @property
    def right_hip_fb(self):
        """Gets the right_hip_fb of this ServosAngles.

        8号舵机  # noqa: E501

        :return: The right_hip_fb of this ServosAngles.
        :rtype: int
        """
        return self._right_hip_fb

    @right_hip_fb.setter
    def right_hip_fb(self, right_hip_fb):
        """Sets the right_hip_fb of this ServosAngles.

        8号舵机  # noqa: E501

        :param right_hip_fb: The right_hip_fb of this ServosAngles.
        :type right_hip_fb: int
        """
        if right_hip_fb is not None and right_hip_fb > 180:  # noqa: E501
            raise ValueError("Invalid value for `right_hip_fb`, must be a value less than or equal to `180`")  # noqa: E501
        if right_hip_fb is not None and right_hip_fb < 0:  # noqa: E501
            raise ValueError("Invalid value for `right_hip_fb`, must be a value greater than or equal to `0`")  # noqa: E501

        self._right_hip_fb = right_hip_fb

    @property
    def right_knee_flex(self):
        """Gets the right_knee_flex of this ServosAngles.

        9号舵机  # noqa: E501

        :return: The right_knee_flex of this ServosAngles.
        :rtype: int
        """
        return self._right_knee_flex

    @right_knee_flex.setter
    def right_knee_flex(self, right_knee_flex):
        """Sets the right_knee_flex of this ServosAngles.

        9号舵机  # noqa: E501

        :param right_knee_flex: The right_knee_flex of this ServosAngles.
        :type right_knee_flex: int
        """
        if right_knee_flex is not None and right_knee_flex > 180:  # noqa: E501
            raise ValueError("Invalid value for `right_knee_flex`, must be a value less than or equal to `180`")  # noqa: E501
        if right_knee_flex is not None and right_knee_flex < 0:  # noqa: E501
            raise ValueError("Invalid value for `right_knee_flex`, must be a value greater than or equal to `0`")  # noqa: E501

        self._right_knee_flex = right_knee_flex

    @property
    def right_ankle_fb(self):
        """Gets the right_ankle_fb of this ServosAngles.

        10号舵机  # noqa: E501

        :return: The right_ankle_fb of this ServosAngles.
        :rtype: int
        """
        return self._right_ankle_fb

    @right_ankle_fb.setter
    def right_ankle_fb(self, right_ankle_fb):
        """Sets the right_ankle_fb of this ServosAngles.

        10号舵机  # noqa: E501

        :param right_ankle_fb: The right_ankle_fb of this ServosAngles.
        :type right_ankle_fb: int
        """
        if right_ankle_fb is not None and right_ankle_fb > 180:  # noqa: E501
            raise ValueError("Invalid value for `right_ankle_fb`, must be a value less than or equal to `180`")  # noqa: E501
        if right_ankle_fb is not None and right_ankle_fb < 0:  # noqa: E501
            raise ValueError("Invalid value for `right_ankle_fb`, must be a value greater than or equal to `0`")  # noqa: E501

        self._right_ankle_fb = right_ankle_fb

    @property
    def right_ankle_ud(self):
        """Gets the right_ankle_ud of this ServosAngles.

        11号舵机  # noqa: E501

        :return: The right_ankle_ud of this ServosAngles.
        :rtype: int
        """
        return self._right_ankle_ud

    @right_ankle_ud.setter
    def right_ankle_ud(self, right_ankle_ud):
        """Sets the right_ankle_ud of this ServosAngles.

        11号舵机  # noqa: E501

        :param right_ankle_ud: The right_ankle_ud of this ServosAngles.
        :type right_ankle_ud: int
        """
        if right_ankle_ud is not None and right_ankle_ud > 180:  # noqa: E501
            raise ValueError("Invalid value for `right_ankle_ud`, must be a value less than or equal to `180`")  # noqa: E501
        if right_ankle_ud is not None and right_ankle_ud < 0:  # noqa: E501
            raise ValueError("Invalid value for `right_ankle_ud`, must be a value greater than or equal to `0`")  # noqa: E501

        self._right_ankle_ud = right_ankle_ud

    @property
    def left_hip_lr(self):
        """Gets the left_hip_lr of this ServosAngles.

        12号舵机  # noqa: E501

        :return: The left_hip_lr of this ServosAngles.
        :rtype: int
        """
        return self._left_hip_lr

    @left_hip_lr.setter
    def left_hip_lr(self, left_hip_lr):
        """Sets the left_hip_lr of this ServosAngles.

        12号舵机  # noqa: E501

        :param left_hip_lr: The left_hip_lr of this ServosAngles.
        :type left_hip_lr: int
        """
        if left_hip_lr is not None and left_hip_lr > 180:  # noqa: E501
            raise ValueError("Invalid value for `left_hip_lr`, must be a value less than or equal to `180`")  # noqa: E501
        if left_hip_lr is not None and left_hip_lr < 0:  # noqa: E501
            raise ValueError("Invalid value for `left_hip_lr`, must be a value greater than or equal to `0`")  # noqa: E501

        self._left_hip_lr = left_hip_lr

    @property
    def left_hip_fb(self):
        """Gets the left_hip_fb of this ServosAngles.

        13号舵机  # noqa: E501

        :return: The left_hip_fb of this ServosAngles.
        :rtype: int
        """
        return self._left_hip_fb

    @left_hip_fb.setter
    def left_hip_fb(self, left_hip_fb):
        """Sets the left_hip_fb of this ServosAngles.

        13号舵机  # noqa: E501

        :param left_hip_fb: The left_hip_fb of this ServosAngles.
        :type left_hip_fb: int
        """
        if left_hip_fb is not None and left_hip_fb > 180:  # noqa: E501
            raise ValueError("Invalid value for `left_hip_fb`, must be a value less than or equal to `180`")  # noqa: E501
        if left_hip_fb is not None and left_hip_fb < 0:  # noqa: E501
            raise ValueError("Invalid value for `left_hip_fb`, must be a value greater than or equal to `0`")  # noqa: E501

        self._left_hip_fb = left_hip_fb

    @property
    def left_knee_flex(self):
        """Gets the left_knee_flex of this ServosAngles.

        14号舵机  # noqa: E501

        :return: The left_knee_flex of this ServosAngles.
        :rtype: int
        """
        return self._left_knee_flex

    @left_knee_flex.setter
    def left_knee_flex(self, left_knee_flex):
        """Sets the left_knee_flex of this ServosAngles.

        14号舵机  # noqa: E501

        :param left_knee_flex: The left_knee_flex of this ServosAngles.
        :type left_knee_flex: int
        """
        if left_knee_flex is not None and left_knee_flex > 180:  # noqa: E501
            raise ValueError("Invalid value for `left_knee_flex`, must be a value less than or equal to `180`")  # noqa: E501
        if left_knee_flex is not None and left_knee_flex < 0:  # noqa: E501
            raise ValueError("Invalid value for `left_knee_flex`, must be a value greater than or equal to `0`")  # noqa: E501

        self._left_knee_flex = left_knee_flex

    @property
    def left_ankle_fb(self):
        """Gets the left_ankle_fb of this ServosAngles.

        15号舵机  # noqa: E501

        :return: The left_ankle_fb of this ServosAngles.
        :rtype: int
        """
        return self._left_ankle_fb

    @left_ankle_fb.setter
    def left_ankle_fb(self, left_ankle_fb):
        """Sets the left_ankle_fb of this ServosAngles.

        15号舵机  # noqa: E501

        :param left_ankle_fb: The left_ankle_fb of this ServosAngles.
        :type left_ankle_fb: int
        """
        if left_ankle_fb is not None and left_ankle_fb > 180:  # noqa: E501
            raise ValueError("Invalid value for `left_ankle_fb`, must be a value less than or equal to `180`")  # noqa: E501
        if left_ankle_fb is not None and left_ankle_fb < 0:  # noqa: E501
            raise ValueError("Invalid value for `left_ankle_fb`, must be a value greater than or equal to `0`")  # noqa: E501

        self._left_ankle_fb = left_ankle_fb

    @property
    def left_ankle_ud(self):
        """Gets the left_ankle_ud of this ServosAngles.

        16号舵机  # noqa: E501

        :return: The left_ankle_ud of this ServosAngles.
        :rtype: int
        """
        return self._left_ankle_ud

    @left_ankle_ud.setter
    def left_ankle_ud(self, left_ankle_ud):
        """Sets the left_ankle_ud of this ServosAngles.

        16号舵机  # noqa: E501

        :param left_ankle_ud: The left_ankle_ud of this ServosAngles.
        :type left_ankle_ud: int
        """
        if left_ankle_ud is not None and left_ankle_ud > 180:  # noqa: E501
            raise ValueError("Invalid value for `left_ankle_ud`, must be a value less than or equal to `180`")  # noqa: E501
        if left_ankle_ud is not None and left_ankle_ud < 0:  # noqa: E501
            raise ValueError("Invalid value for `left_ankle_ud`, must be a value greater than or equal to `0`")  # noqa: E501

        self._left_ankle_ud = left_ankle_ud

    @property
    def neck_lr(self):
        """Gets the neck_lr of this ServosAngles.

        17号舵机  # noqa: E501

        :return: The neck_lr of this ServosAngles.
        :rtype: int
        """
        return self._neck_lr

    @neck_lr.setter
    def neck_lr(self, neck_lr):
        """Sets the neck_lr of this ServosAngles.

        17号舵机  # noqa: E501

        :param neck_lr: The neck_lr of this ServosAngles.
        :type neck_lr: int
        """
        if neck_lr is not None and neck_lr > 135:  # noqa: E501
            raise ValueError("Invalid value for `neck_lr`, must be a value less than or equal to `135`")  # noqa: E501
        if neck_lr is not None and neck_lr < 45:  # noqa: E501
            raise ValueError("Invalid value for `neck_lr`, must be a value greater than or equal to `45`")  # noqa: E501

        self._neck_lr = neck_lr
