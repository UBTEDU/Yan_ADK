# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openadk.models.subscription_common_response import SubscriptionCommonResponse  # noqa: E501
from openadk.models.subscription_motions_status_response import SubscriptionMotionsStatusResponse  # noqa: E501
from openadk.models.subscription_sensors_environment_value_response import SubscriptionSensorsEnvironmentValueResponse  # noqa: E501
from openadk.models.subscription_sensors_gyro_value_response import SubscriptionSensorsGyroValueResponse  # noqa: E501
from openadk.models.subscription_sensors_infrared_value_response import SubscriptionSensorsInfraredValueResponse  # noqa: E501
from openadk.models.subscription_sensors_pressure_value_response import SubscriptionSensorsPressureValueResponse  # noqa: E501
from openadk.models.subscription_sensors_touch_value_response import SubscriptionSensorsTouchValueResponse  # noqa: E501
from openadk.models.subscription_sensors_ultrasonic_value_response import SubscriptionSensorsUltrasonicValueResponse  # noqa: E501
from openadk.models.subscription_visions_get_response import SubscriptionVisionsGetResponse  # noqa: E501
from openadk.models.subscription_voice_response import SubscriptionVoiceResponse  # noqa: E501
from openadk.test import BaseTestCase


class TestSubscriptionsController(BaseTestCase):
    """SubscriptionsController integration test stubs"""

    def test_put_motions(self):
        """Test case for put_motions

        Get the motion's status, which is pushed from the remote device.
        """
        body = SubscriptionMotionsStatusResponse()
        response = self.client.open(
            '/v1/subscriptions/motions',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription(self):
        """Test case for put_sensors_subscription

        Get the gyroscope sensor's data, which is pushed from the remote device.
        """
        body = SubscriptionSensorsGyroValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/gyro',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_environment(self):
        """Test case for put_sensors_subscription_sensors_environment

        Get environment sensor's data, which is pushed from the remote device.
        """
        body = SubscriptionSensorsEnvironmentValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/environment',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_infrared(self):
        """Test case for put_sensors_subscription_sensors_infrared

        Get infrared sensor's data, which is pushed from the remote device.
        """
        body = SubscriptionSensorsInfraredValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/infrared',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_pressure(self):
        """Test case for put_sensors_subscription_sensors_pressure

        Get pressure sensor's data, which is pushed from the remote device.
        """
        body = SubscriptionSensorsPressureValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/pressure',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_touch(self):
        """Test case for put_sensors_subscription_sensors_touch

        Get touch sensor's data, which is pushed from the remote device.
        """
        body = SubscriptionSensorsTouchValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/touch',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_ultrasonic(self):
        """Test case for put_sensors_subscription_sensors_ultrasonic

        Get ultrasonic sensor's data, which is pushed from the remote device.
        """
        body = SubscriptionSensorsUltrasonicValueResponse()
        response = self.client.open(
            '/v1/subscriptions/sensors/ultrasonic',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_tts_subscriptions_voice_tts(self):
        """Test case for put_tts_subscriptions_voice_tts

        Get text to speech's result, which is pushed from the remote device.
        """
        body = SubscriptionVoiceResponse()
        response = self.client.open(
            '/v1/subscriptions/voice/tts',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_vision_subscription_visions(self):
        """Test case for put_vision_subscription_visions

        Get compute vision's result, which is pushed from the remote device.
        """
        body = SubscriptionVisionsGetResponse()
        response = self.client.open(
            '/v1/subscriptions/visions',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_voice_asr_subscriptions_voice_asr(self):
        """Test case for put_voice_asr_subscriptions_voice_asr

        Get automatic speech recognition's result, which is pushed from the remote device.
        """
        body = SubscriptionVoiceResponse()
        response = self.client.open(
            '/v1/subscriptions/voice/asr',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_put_voice_iat_subscription_voice_iat(self):
        """Test case for put_voice_iat_subscription_voice_iat

        Get auto transform's result, which is pushed from the remote device.
        """
        body = SubscriptionVoiceResponse()
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
