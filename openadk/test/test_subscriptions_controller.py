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

import time
from openadk.models.subscription_motions_status import SubscriptionMotionsStatus
from openadk.models.subscription_sensors_gyro_value import SubscriptionSensorsGyroValue
from openadk.models.subscription_sensors_gyro_info import SubscriptionSensorsGyroInfo
from openadk.models.subscription_sensors_environment_value import SubscriptionSensorsEnvironmentValue
from openadk.models.subscription_sensors_environment_info import SubscriptionSensorsEnvironmentInfo
from openadk.models.subscription_sensors_infrared_value import SubscriptionSensorsInfraredValue
from openadk.models.subscription_sensors_infrared_info import SubscriptionSensorsInfraredInfo
from openadk.models.subscription_sensors_ultrasonic_value import SubscriptionSensorsUltrasonicValue
from openadk.models.subscription_sensors_ultrasonic_info import SubscriptionSensorsUltrasonicInfo
from openadk.models.subscription_sensors_pressure_value import SubscriptionSensorsPressureValue
from openadk.models.subscription_sensors_pressure_info import SubscriptionSensorsPressureInfo
from openadk.models.subscription_sensors_touch_value import SubscriptionSensorsTouchValue
from openadk.models.subscription_sensors_touch_info import SubscriptionSensorsTouchInfo
from openadk.models.subscription_visions_results import SubscriptionVisionsResults
from openadk.models.subscription_visions_results import SubscriptionVisionsAnalysis
from openadk.models.subscription_visions_results import SubscriptionName
from openadk.models.subscription_visions_age import SubscriptionVisionsAge
from openadk.models.subscription_visions_gender import SubscriptionVisionsGender


class TestSubscriptionsController(BaseTestCase):
    """SubscriptionsController integration test stubs"""

    def test_put_motions(self):
        """Test case for put_motions

        Get the motion's status, which is pushed from the remote device.
        """
        timestamp = int(time.time())
        data = SubscriptionMotionsStatus(status='run', name='raise', timestamp=timestamp)
        body = SubscriptionMotionsStatusResponse(code=0, data=data, msg='Motions status msg')

        response = self.client.open(
            '/v1/subscriptions/motions',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))['data']
        response_data = SubscriptionMotionsStatus.from_dict(response_data)
        self.assertEqual(response_data, data, response.data.decode('utf-8'))

    def test_put_sensors_subscription(self):
        """Test case for put_sensors_subscription

        Get the gyroscope sensor's data, which is pushed from the remote device.
        """
        gyro_data = {
                        "accel-x": 0.147949,
                        "accel-y": 0.116699,
                        "accel-z": 0.813477,
                        "compass-x": 0.1021,
                        "compass-y": 0.602,
                        "compass-z": 0.01232,
                        "euler-x": 8.073578,
                        "euler-y": -10.11795,
                        "euler-z": 0.72052,
                        "gyro-x": 0.1021,
                        "gyro-y": 0.602,
                        "gyro-z": 0.0213,
                        "id": 52
                     }
        gyro = [SubscriptionSensorsGyroInfo.from_dict(gyro_data)]
        data = SubscriptionSensorsGyroValue(gyro=gyro)
        body = SubscriptionSensorsGyroValueResponse(code=0, data=data, msg='Gyro sensor msg')

        response = self.client.open(
            '/v1/subscriptions/sensors/gyro',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))['data']
        response_data = SubscriptionSensorsGyroValue.from_dict(response_data)
        self.assertEqual(response_data, data, response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_environment(self):
        """Test case for put_sensors_subscription_sensors_environment

        Get environment sensor's data, which is pushed from the remote device.
        """
        environment_data = {
                                "humidity": 75,
                                "id": 54,
                                "pressure": 1003,
                                "slot": 1,
                                "temperature": 25
                            }
        environment = [SubscriptionSensorsEnvironmentInfo.from_dict(environment_data)]
        data = SubscriptionSensorsEnvironmentValue(environment=environment)
        body = SubscriptionSensorsEnvironmentValueResponse(code=0, data=data, msg='Environment sensor msg')

        response = self.client.open(
            '/v1/subscriptions/sensors/environment',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))['data']
        response_data = SubscriptionSensorsEnvironmentValue.from_dict(response_data)
        self.assertEqual(response_data, data, response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_infrared(self):
        """Test case for put_sensors_subscription_sensors_infrared

        Get infrared sensor's data, which is pushed from the remote device.
        """
        infrared_data = {
                            "id": 23,
                            "slot": 1,
                            "value": 25
                         }
        infrared = [SubscriptionSensorsInfraredInfo.from_dict(infrared_data)]
        data = SubscriptionSensorsInfraredValue(infrared=infrared)
        body = SubscriptionSensorsInfraredValueResponse(code=0, data=data, msg='Infrared sensor msg')

        response = self.client.open(
            '/v1/subscriptions/sensors/infrared',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))['data']
        response_data = SubscriptionSensorsInfraredValue.from_dict(response_data)
        self.assertEqual(response_data, data, response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_pressure(self):
        """Test case for put_sensors_subscription_sensors_pressure

        Get pressure sensor's data, which is pushed from the remote device.
        """
        pressure_data = {
                            "id": 35,
                            "slot": 1,
                            "value": 25
                        }
        pressure = [SubscriptionSensorsPressureInfo.from_dict(pressure_data)]
        data = SubscriptionSensorsPressureValue(pressure=pressure)
        body = SubscriptionSensorsPressureValueResponse(code=0, data=data, msg='Pressure sensor msg')

        response = self.client.open(
            '/v1/subscriptions/sensors/pressure',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))['data']
        response_data = SubscriptionSensorsPressureValue.from_dict(response_data)
        self.assertEqual(response_data, data, response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_touch(self):
        """Test case for put_sensors_subscription_sensors_touch

        Get touch sensor's data, which is pushed from the remote device.
        """
        touch_data = {
                        "id": 29,
                        "slot": 1,
                        "value": 25
                     }
        touch = [SubscriptionSensorsTouchInfo.from_dict(touch_data)]
        data = SubscriptionSensorsTouchValue(touch=touch)
        body = SubscriptionSensorsTouchValueResponse(code=0, data=data, msg='Touch sensor msg')

        response = self.client.open(
            '/v1/subscriptions/sensors/touch',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))['data']
        response_data = SubscriptionSensorsTouchValue.from_dict(response_data)
        self.assertEqual(response_data, data, response.data.decode('utf-8'))

    def test_put_sensors_subscription_sensors_ultrasonic(self):
        """Test case for put_sensors_subscription_sensors_ultrasonic

        Get ultrasonic sensor's data, which is pushed from the remote device.
        """
        ultrasonic_data = {
                                "id": 17,
                                "slot": 1,
                                "value": 25
                           }
        ultrasonic = [SubscriptionSensorsUltrasonicInfo.from_dict(ultrasonic_data)]
        data = SubscriptionSensorsUltrasonicValue(ultrasonic=ultrasonic)
        body = SubscriptionSensorsUltrasonicValueResponse(code=0, data=data, msg='Ultrasonic sensor msg')

        response = self.client.open(
            '/v1/subscriptions/sensors/ultrasonic',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))['data']
        response_data = SubscriptionSensorsUltrasonicValue.from_dict(response_data)
        self.assertEqual(response_data, data, response.data.decode('utf-8'))

    def test_put_tts_subscriptions_voice_tts(self):
        """Test case for put_tts_subscriptions_voice_tts

        Get text to speech's result, which is pushed from the remote device.
        """
        tts_data = {
                      "code": 0,
                      "type": "tts",
                      "data": {'status': 'build'},
                      "timestamp": int(time.time()),
                      "msg": "Success"
                    }
        # 此处疑似生成的tts推送消息数据结构用错了，应该是SubscriptionVoiceResponse
        body = SubscriptionVoiceResponse.from_dict(tts_data)

        response = self.client.open(
            '/v1/subscriptions/voice/tts',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))
        response_data = SubscriptionVoiceResponse.from_dict(response_data)
        self.assertEqual(response_data, body, response.data.decode('utf-8'))

    def test_put_vision_subscription_visions(self):
        """Test case for put_vision_subscription_visions

        Get compute vision's result, which is pushed from the remote device.
        """
        age = SubscriptionVisionsAge(age=15, group='youth')
        gender = SubscriptionVisionsGender(gender='male')
        result_data = {
                            'analysis': SubscriptionVisionsAnalysis(age=age, gender=gender).to_dict(),
                            'recognition': SubscriptionName(name='someone').to_dict(),
                            'quantity': 3,
                            'color': [SubscriptionName(name='blue').to_dict()]
                       }
        vision_data = {
                          "code": 0,
                          "data": SubscriptionVisionsResults.from_dict(result_data).to_dict(),
                          "msg": "Success",
                          "status": "idle",
                          "timestamp": 1551838515,
                          "type": "recognition"
                       }
        body = SubscriptionVisionsGetResponse.from_dict(vision_data)

        response = self.client.open(
            '/v1/subscriptions/visions',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))
        response_data = SubscriptionVisionsGetResponse.from_dict(response_data)
        self.assertEqual(response_data, body, response.data.decode('utf-8'))

    def test_put_voice_asr_subscriptions_voice_asr(self):
        """Test case for put_voice_asr_subscriptions_voice_asr

        Get automatic speech recognition's result, which is pushed from the remote device.
        """
        asr_data = {
                        'code': 0,
                        'type': 'asr',
                        'data': {'text': '好啊好啊，很高兴遇到你。', 'question': '你好'},
                        'timestamp': int(time.time()),
                        'msg': 'Success'
                    }
        body = SubscriptionVoiceResponse.from_dict(asr_data)

        response = self.client.open(
            '/v1/subscriptions/voice/asr',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))
        response_data = SubscriptionVoiceResponse.from_dict(response_data)
        self.assertEqual(response_data, body, response.data.decode('utf-8'))

    def test_put_voice_iat_subscription_voice_iat(self):
        """Test case for put_voice_iat_subscription_voice_iat

        Get auto transform's result, which is pushed from the remote device.
        """
        iat_data = {
            'code': 0,
            'type': 'iat',
            'data': {'text': '江山如此多娇'},
            'timestamp': int(time.time()),
            'msg': 'Success'
        }
        body = SubscriptionVoiceResponse.from_dict(iat_data)

        response = self.client.open(
            '/v1/subscriptions/voice/iat',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        response_data = json.loads(response.data.decode('utf-8'))
        response_data = SubscriptionVoiceResponse.from_dict(response_data)
        self.assertEqual(response_data, body, response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
