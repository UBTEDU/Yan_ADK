import json

import connexion
import six

from openadk.models import SensorsEnvironmentInfo, SensorsEnvironmentValue
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
from openadk import util
from openadk.ubtrc.ubtrc import UBTReturnValue


def put_motions(body):  # noqa: E501
    """推送运动控制状态

    可以控制执行指定动作、暂停、继续、停止和复位 # noqa: E501

    :param body: 运动控制的参数
    :type body: dict | bytes

    :rtype: CommonResponse
    """
    if connexion.request.is_json:
        body = MotionsStatusResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_sensors_subscription(body):  # noqa: E501
    """推送传感器消息

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CommonResponse
    """
    if connexion.request.is_json:
        body = SensorsGyroValueResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_sensors_subscription_sensors_environment(body):  # noqa: E501
    """推送传感器消息

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CommonResponse
    """
    if connexion.request.is_json:
        body = SensorsEnvironmentValueResponse.from_dict(connexion.request.get_json())  # noqa: E501

    push_data_dict = body.to_dict()
    print (push_data_dict)
    print (push_data_dict['code'])
    print (push_data_dict['msg'])
    print (push_data_dict['data'])
    environment_array = push_data_dict['data']['environment']
    print ("Length of enviorment {environment_array}, type (type)".format(environment_array=len(environment_array), type=type(environment_array)))

    for iter_item in environment_array:
        print ("Environment data {data}".format(data=iter_item))

    response_code = UBTReturnValue.SUCCESS.value['code']
    response_msg = UBTReturnValue.SUCCESS.value['msg']
    response_body = CommonResponse(code=response_code, data="""{}""", msg=response_msg)

    return response_body


def put_sensors_subscription_sensors_infrared(body):  # noqa: E501
    """推送传感器消息

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CommonResponse
    """
    if connexion.request.is_json:
        body = SensorsInfraredValueResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_sensors_subscription_sensors_pressure(body):  # noqa: E501
    """推送传感器消息

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CommonResponse
    """
    if connexion.request.is_json:
        body = SensorsPressureValueResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_sensors_subscription_sensors_touch(body):  # noqa: E501
    """推送传感器消息

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CommonResponse
    """
    if connexion.request.is_json:
        body = SensorsTouchValueResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_sensors_subscription_sensors_ultrasonic(body):  # noqa: E501
    """推送传感器消息

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CommonResponse
    """
    if connexion.request.is_json:
        body = SensorsUltrasonicValueResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_tts_subscriptions_voice_tts(body):  # noqa: E501
    """推送TTS状态消息

    URL example: http://10.10.1.30:80/tts # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CommonResponse
    """
    if connexion.request.is_json:
        body = CommonResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_vision_subscription_visions(body):  # noqa: E501
    """推送指定视觉任务消息

    URL example: http://10.10.1.30:80/subscriptions/visions # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CommonResponse
    """
    if connexion.request.is_json:
        body = VisionsResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_voice_asr_subscriptions_voice_asr(body):  # noqa: E501
    """推送语义理解消息

    URL example: http://10.10.1.30:80/subscriptions/voice/asr # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CommonResponse
    """
    if connexion.request.is_json:
        body = VoiceResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_voice_iat_subscription_voice_iat(body):  # noqa: E501
    """推送语音识别原始JSON信息

    URL example: http://10.10.1.30:80/subscriptions/voice/iat # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: CommonResponse
    """
    if connexion.request.is_json:
        body = VoiceResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
