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
from openadk.api.visions_api import VisionsApi  # noqa: E501
from openadk.rest import ApiException


class TestVisionsApi(unittest.TestCase):
    """VisionsApi unit test stubs"""

    def setUp(self):
        self.api = openadk.api.visions_api.VisionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_tags(self):
        """Test case for delete_tags

        删除指定样本标签  # noqa: E501
        """
        pass

    def test_delete_vision_photo(self):
        """Test case for delete_vision_photo

        删除指定照片  # noqa: E501
        """
        pass

    def test_delete_vision_photo_samples(self):
        """Test case for delete_vision_photo_samples

        删除上传的照片  # noqa: E501
        """
        pass

    def test_get_photo_samples(self):
        """Test case for get_photo_samples

        获取上传照片列表  # noqa: E501
        """
        pass

    def test_get_tags(self):
        """Test case for get_tags

        获取已设置标签列表  # noqa: E501
        """
        pass

    def test_get_vision(self):
        """Test case for get_vision

        获取任务結果  # noqa: E501
        """
        pass

    def test_get_visions_photos(self):
        """Test case for get_visions_photos

        获取指定照片  # noqa: E501
        """
        pass

    def test_get_visions_photos_lists(self):
        """Test case for get_visions_photos_lists

        获取机器人拍照列表  # noqa: E501
        """
        pass

    def test_post_vision_photo(self):
        """Test case for post_vision_photo

        拍一张照片  # noqa: E501
        """
        pass

    def test_put_tags(self):
        """Test case for put_tags

        设置样本标签  # noqa: E501
        """
        pass

    def test_put_vision(self):
        """Test case for put_vision

        指定视觉任务停止或开始  # noqa: E501
        """
        pass

    def test_put_visions_photo_samples(self):
        """Test case for put_visions_photo_samples

        上传样本照片  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
