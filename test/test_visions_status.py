# coding: utf-8

"""
    Yanshee RESTful API

    什么是apollo? 它是一个组合的称呼, Yanshee用它以API的形式向软件开发者们提供它内部所支持的功能.这包含基于TCP/UDP的Json字符串交互方式(port:20001), 软件开发套件(open SDK) 和RESTful框架, 但不包括自然用户界面,如语音和视觉等. 准备的说, 它专门设计用于那些希望以编程的方式对Yanshee进行控制的场景, 比如使用python脚本, 苹果应用, 安卓应用和 浏览器以及其他支持HTTP传输协议的工具等.我们建议您优先选择RESTful方式来对Yanshee进行编程控制. 更详细的内容, 可在浏览器输入以下地址获取: http:///apollo.      For this sample, you can use the api key `special-key` to test the authorization     filters.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import openadk
from openadk.models.visions_status import VisionsStatus  # noqa: E501
from openadk.rest import ApiException


class TestVisionsStatus(unittest.TestCase):
    """VisionsStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVisionsStatus(self):
        """Test VisionsStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = openadk.models.visions_status.VisionsStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
