# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openadk.models.base_model_ import Model
from openadk.models.sensors_info import SensorsInfo  # noqa: F401,E501
from openadk import util


class SensorsList(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, sensors=None):  # noqa: E501
        """SensorsList - a model defined in Swagger

        :param sensors: The sensors of this SensorsList.  # noqa: E501
        :type sensors: List[SensorsInfo]
        """
        self.swagger_types = {
            'sensors': List[SensorsInfo]
        }

        self.attribute_map = {
            'sensors': 'sensors'
        }

        self._sensors = sensors

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SensorsList of this SensorsList.  # noqa: E501
        :rtype: SensorsList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sensors(self):
        """Gets the sensors of this SensorsList.


        :return: The sensors of this SensorsList.
        :rtype: List[SensorsInfo]
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this SensorsList.


        :param sensors: The sensors of this SensorsList.
        :type sensors: List[SensorsInfo]
        """
        if sensors is None:
            raise ValueError("Invalid value for `sensors`, must not be `None`")  # noqa: E501

        self._sensors = sensors
