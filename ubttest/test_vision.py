# coding: utf-8

"""
    Copyright (c) 2019 UBTECH All rights reserved.
"""

from __future__ import print_function
import time
import openadk
from openadk import VisionsTask
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
configuration = openadk.Configuration()
configuration.host = 'http://10.10.64.182:9090/v1'

api_instance = openadk.DevicesApi(openadk.ApiClient(configuration))

try:
    # 获得机器人电量信息
    api_response = api_instance.get_devices_battery()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_battery: %s\n" % e)

api_instance = openadk.VoiceApi(openadk.ApiClient(configuration))

try:
    # 获得机器人电量信息
    api_response = api_instance.get_voice_tts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_battery: %s\n" % e)

api_instance = openadk.VisionsApi(openadk.ApiClient(configuration))

try:
    # 获得机器人电量信息
    body = VisionsTask(type='tracking', operation='start', option='face')
    api_response = api_instance.get_vision()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_battery: %s\n" % e)