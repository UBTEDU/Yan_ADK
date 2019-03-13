# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openadk.models.common_response import CommonResponse  # noqa: E501
from openadk.models.motions_status_response import MotionsStatusResponse  # noqa: E501
from openadk.models.sensors_environment_value_response import SensorsEnvironmentValueResponse  # noqa: E501
from openadk.models.sensors_gyro_value_response import SensorsGyroValueResponse  # noqa: E501
from openadk.models.sensors_infrared_value_response import SensorsInfraredValueResponse  # noqa: E501
from openadk.models.sensors_pressure_value_response import SensorsPressureValueResponse  # noqa: E501
from openadk.models.sensors_touch_value_response import SensorsTouchValueResponse  # noqa: E501
from openadk.models.sensors_ultrasonic_value_response import SensorsUltrasonicValueResponse  # noqa: E501
from openadk.models.visions_response import VisionsResponse  # noqa: E501
from openadk.models.voice_response import VoiceResponse  # noqa: E501
from openadk.test import BaseTestCase


class TestSubscriptionsController(BaseTestCase):
    """SubscriptionsController integration test stubs"""

    def test_put_motions(self):
        """Test case for put_motions

        推送运动控制状态
        """
        body = MotionsStatusResponse()
        response = self.client.open(
            '/v1/subscriptions/motions',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription(self):
        """Test case for put_sensors_subscription

        推送传感器消息
        """
        body = SensorsGyroValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/gyro',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_environment(self):
        """Test case for put_sensors_subscription_sensors_environment

        推送传感器消息
        """
        body = SensorsEnvironmentValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/environment',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_infrared(self):
        """Test case for put_sensors_subscription_sensors_infrared

        推送传感器消息
        """
        body = SensorsInfraredValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/infrared',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_pressure(self):
        """Test case for put_sensors_subscription_sensors_pressure

        推送传感器消息
        """
        body = SensorsPressureValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/pressure',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_touch(self):
        """Test case for put_sensors_subscription_sensors_touch

        推送传感器消息
        """
        body = SensorsTouchValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/touch',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_ultrasonic(self):
        """Test case for put_sensors_subscription_sensors_ultrasonic

        推送传感器消息
        """
        body = SensorsUltrasonicValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/ultrasonic',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_tts_subscriptions_voice_tts(self):
        """Test case for put_tts_subscriptions_voice_tts

        推送TTS状态消息
        """
        body = CommonResponse()
        response = self.client.open(
            '/v1/subscriptions/voice/tts',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_vision_subscription_visions(self):
        """Test case for put_vision_subscription_visions

        推送指定视觉任务消息
        """
        body = VisionsResponse()
        response = self.client.open(
            '/v1/subscriptions/visions',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_voice_asr_subscriptions_voice_asr(self):
        """Test case for put_voice_asr_subscriptions_voice_asr

        推送语义理解消息
        """
        body = VoiceResponse()
        response = self.client.open(
            '/v1/subscriptions/voice/asr',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_voice_iat_subscription_voice_iat(self):
        """Test case for put_voice_iat_subscription_voice_iat

        推送语音识别原始JSON信息
        """
        body = VoiceResponse()
        response = self.client.open(
            '/v1/subscriptions/voice/iat',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
