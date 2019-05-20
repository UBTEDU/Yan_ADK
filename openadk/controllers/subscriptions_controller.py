import connexion
import six

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
from openadk import util


def put_motions(body):  # noqa: E501
    """Get the motion&#39;s status, which is pushed from the remote device.

     Get motions&#39; status. The possible values: - idle - run - pause  # noqa: E501

    :param body:  The motion&#39;s status. 
    :type body: dict | bytes

    :rtype: SubscriptionCommonResponse
    """
    if connexion.request.is_json:
        body = SubscriptionMotionsStatusResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_sensors_subscription(body):  # noqa: E501
    """Get the gyroscope sensor&#39;s data, which is pushed from the remote device.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SubscriptionCommonResponse
    """
    if connexion.request.is_json:
        body = SubscriptionSensorsGyroValueResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_sensors_subscription_sensors_environment(body):  # noqa: E501
    """Get environment sensor&#39;s data, which is pushed from the remote device.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SubscriptionCommonResponse
    """
    if connexion.request.is_json:
        body = SubscriptionSensorsEnvironmentValueResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_sensors_subscription_sensors_infrared(body):  # noqa: E501
    """Get infrared sensor&#39;s data, which is pushed from the remote device.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SubscriptionCommonResponse
    """
    if connexion.request.is_json:
        body = SubscriptionSensorsInfraredValueResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_sensors_subscription_sensors_pressure(body):  # noqa: E501
    """Get pressure sensor&#39;s data, which is pushed from the remote device.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SubscriptionCommonResponse
    """
    if connexion.request.is_json:
        body = SubscriptionSensorsPressureValueResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_sensors_subscription_sensors_touch(body):  # noqa: E501
    """Get touch sensor&#39;s data, which is pushed from the remote device.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SubscriptionCommonResponse
    """
    if connexion.request.is_json:
        body = SubscriptionSensorsTouchValueResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_sensors_subscription_sensors_ultrasonic(body):  # noqa: E501
    """Get ultrasonic sensor&#39;s data, which is pushed from the remote device.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SubscriptionCommonResponse
    """
    if connexion.request.is_json:
        body = SubscriptionSensorsUltrasonicValueResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_tts_subscriptions_voice_tts(body):  # noqa: E501
    """Get text to speech&#39;s result, which is pushed from the remote device.

    Example URL : http://10.10.1.30:80/tts # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SubscriptionCommonResponse
    """
    if connexion.request.is_json:
        body = SubscriptionVoiceResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_vision_subscription_visions(body):  # noqa: E501
    """Get compute vision&#39;s result, which is pushed from the remote device.

    URL example: http://10.10.1.30:80/subscriptions/visions # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SubscriptionCommonResponse
    """
    if connexion.request.is_json:
        body = SubscriptionVisionsGetResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_voice_asr_subscriptions_voice_asr(body):  # noqa: E501
    """Get automatic speech recognition&#39;s result, which is pushed from the remote device.

    URL example: http://10.10.1.30:80/subscriptions/voice/asr # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SubscriptionCommonResponse
    """
    if connexion.request.is_json:
        body = SubscriptionVoiceResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def put_voice_iat_subscription_voice_iat(body):  # noqa: E501
    """Get auto transform&#39;s result, which is pushed from the remote device.

    URL example: http://10.10.1.30:80/subscriptions/voice/iat # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: SubscriptionCommonResponse
    """
    if connexion.request.is_json:
        body = SubscriptionVoiceResponse.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
