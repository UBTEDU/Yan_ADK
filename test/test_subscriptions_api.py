# coding: utf-8

"""
    Yanshee RESTful API

    Yanshee RESTful APIs是一套专门为编程爱好者提供二次开发的接口．它通过http/https的方式向外界提供机器人控制，传感器读取，机器人视觉等功能．用户还可以通过编程的方式训练自己的模型，学习一些机器学习的内容．  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import openadk
from openadk.api.subscriptions_api import SubscriptionsApi  # noqa: E501
from openadk.rest import ApiException


class TestSubscriptionsApi(unittest.TestCase):
    """SubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = openadk.api.subscriptions_api.SubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_motions_subscription(self):
        """Test case for delete_motions_subscription

        取消订阅运动状态消息  # noqa: E501
        """
        pass

    def test_delete_sensors_subscription(self):
        """Test case for delete_sensors_subscription

        取消订阅传感器消息  # noqa: E501
        """
        pass

    def test_delete_vision_subscription(self):
        """Test case for delete_vision_subscription

        取消订阅指定视觉任务消息  # noqa: E501
        """
        pass

    def test_delete_voice_asr_subscription(self):
        """Test case for delete_voice_asr_subscription

        取消订阅语义消息  # noqa: E501
        """
        pass

    def test_delete_voice_iat_subscription(self):
        """Test case for delete_voice_iat_subscription

        取消订阅语音识别JSON消息  # noqa: E501
        """
        pass

    def test_delete_voice_tts_subscription(self):
        """Test case for delete_voice_tts_subscription

        取消订阅语义消息  # noqa: E501
        """
        pass

    def test_monitor(self):
        """Test case for monitor

        取消订阅摄像头的视频流  # noqa: E501
        """
        pass

    def test_post_motions_subscription(self):
        """Test case for post_motions_subscription

        订阅运动状态消息  # noqa: E501
        """
        pass

    def test_post_sensors_subscription(self):
        """Test case for post_sensors_subscription

        订阅传感器消息  # noqa: E501
        """
        pass

    def test_post_stream(self):
        """Test case for post_stream

        订阅摄像头的视频流  # noqa: E501
        """
        pass

    def test_post_tts_subscriptions(self):
        """Test case for post_tts_subscriptions

        订阅TTS状态消息  # noqa: E501
        """
        pass

    def test_post_vision_subscription(self):
        """Test case for post_vision_subscription

        订阅指定视觉任务消息  # noqa: E501
        """
        pass

    def test_post_voice_asr_subscriptions(self):
        """Test case for post_voice_asr_subscriptions

        订阅语义理解消息  # noqa: E501
        """
        pass

    def test_post_voice_iat_subscription(self):
        """Test case for post_voice_iat_subscription

        订阅语音识别原始JSON信息  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
