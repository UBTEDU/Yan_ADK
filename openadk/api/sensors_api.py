# coding: utf-8

"""
    Yanshee RESTful API

     ## Overview Yanshee RESTful APIs are generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the [OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server. The API service uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.  To provide the API service, Yanshee RESTful APIs are integrated into apollo package, it is a part of Yanshee-ROS framework. Yanshee RESTful APIs provided two language versions: - [English version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_en/1.0.0) - [Chinese version](https://app.swaggerhub.com/apis-docs/UBTEDU/apollo_cn/1.0.0)  ## Requirements. Python 2.7 or 3.4+  ## Getting Started Please follow the [installation procedure](#installation--usage) and then run the following:  ``` from __future__ import print_function import time import openadk from openadk.rest import ApiException from pprint import pprint  # create an instance of the API class configuration = openadk.Configuration() configuration.host = 'http://192.168.1.100:9090/v1' api_instance = openadk.DevicesApi(openadk.ApiClient(configuration)) try:  # Get system's battery information  api_response = api_instance.get_devices_battery()  pprint(api_response) except ApiException as e:  print(\"Exception when calling DevicesApi->get_devices_battery: %s\" % e)  ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openadk.api_client import ApiClient


class SensorsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_sensors_environment(self, **kwargs):  # noqa: E501
        """Get enviornment sensor's value  # noqa: E501

         Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_environment(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] slot: Sensors' slot number (optional)
        :return: SensorsEnvironmentValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sensors_environment_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sensors_environment_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sensors_environment_with_http_info(self, **kwargs):  # noqa: E501
        """Get enviornment sensor's value  # noqa: E501

         Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_environment_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] slot: Sensors' slot number (optional)
        :return: SensorsEnvironmentValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['slot']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sensors_environment" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'slot' in params:
            query_params.append(('slot', params['slot']))  # noqa: E501
            collection_formats['slot'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sensors/environment', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SensorsEnvironmentValueResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sensors_gyro(self, **kwargs):  # noqa: E501
        """Get gyroscope sensor's value  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_gyro(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SensorsGyroValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sensors_gyro_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sensors_gyro_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sensors_gyro_with_http_info(self, **kwargs):  # noqa: E501
        """Get gyroscope sensor's value  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_gyro_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SensorsGyroValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sensors_gyro" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sensors/gyro', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SensorsGyroValueResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sensors_infrared(self, **kwargs):  # noqa: E501
        """Get infrared sensor's value  # noqa: E501

         Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_infrared(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] id: Sensors' I2C address (optional)
        :param list[int] slot: Sensors' slot number (optional)
        :return: SensorsInfraredValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sensors_infrared_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sensors_infrared_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sensors_infrared_with_http_info(self, **kwargs):  # noqa: E501
        """Get infrared sensor's value  # noqa: E501

         Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_infrared_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] id: Sensors' I2C address (optional)
        :param list[int] slot: Sensors' slot number (optional)
        :return: SensorsInfraredValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'slot']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sensors_infrared" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
            collection_formats['id'] = 'csv'  # noqa: E501
        if 'slot' in params:
            query_params.append(('slot', params['slot']))  # noqa: E501
            collection_formats['slot'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sensors/infrared', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SensorsInfraredValueResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sensors_list(self, **kwargs):  # noqa: E501
        """Get all sensors' list  # noqa: E501

         The usage scenario of this API is as follows: - A new sensor is installed - Sensor is not detected - Get all the sensor list   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SensorsListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sensors_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sensors_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sensors_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get all sensors' list  # noqa: E501

         The usage scenario of this API is as follows: - A new sensor is installed - Sensor is not detected - Get all the sensor list   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: SensorsListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sensors_list" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sensors/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SensorsListResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sensors_pressure(self, **kwargs):  # noqa: E501
        """Get pressure sensor's value  # noqa: E501

         Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_pressure(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] id: Sensors' I2C address (optional)
        :param list[int] slot: Sensors' slot number (optional)
        :return: SensorsPressureValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sensors_pressure_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sensors_pressure_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sensors_pressure_with_http_info(self, **kwargs):  # noqa: E501
        """Get pressure sensor's value  # noqa: E501

         Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_pressure_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] id: Sensors' I2C address (optional)
        :param list[int] slot: Sensors' slot number (optional)
        :return: SensorsPressureValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'slot']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sensors_pressure" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
            collection_formats['id'] = 'csv'  # noqa: E501
        if 'slot' in params:
            query_params.append(('slot', params['slot']))  # noqa: E501
            collection_formats['slot'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sensors/pressure', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SensorsPressureValueResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sensors_touch(self, **kwargs):  # noqa: E501
        """Get touch sensor's value  # noqa: E501

         Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_touch(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] id: Sensors' I2C address (optional)
        :param list[int] slot: Sensors' slot number (optional)
        :return: SensorsTouchValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sensors_touch_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sensors_touch_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sensors_touch_with_http_info(self, **kwargs):  # noqa: E501
        """Get touch sensor's value  # noqa: E501

         Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_touch_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] id: Sensors' I2C address (optional)
        :param list[int] slot: Sensors' slot number (optional)
        :return: SensorsTouchValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'slot']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sensors_touch" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
            collection_formats['id'] = 'csv'  # noqa: E501
        if 'slot' in params:
            query_params.append(('slot', params['slot']))  # noqa: E501
            collection_formats['slot'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sensors/touch', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SensorsTouchValueResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sensors_ultrasonic(self, **kwargs):  # noqa: E501
        """Get ultrasonic sensor's value  # noqa: E501

         Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_ultrasonic(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] id: Sensors' I2C address (optional)
        :param list[int] slot: Sensors' slot number (optional)
        :return: SensorsUltrasonicValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sensors_ultrasonic_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_sensors_ultrasonic_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_sensors_ultrasonic_with_http_info(self, **kwargs):  # noqa: E501
        """Get ultrasonic sensor's value  # noqa: E501

         Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sensors_ultrasonic_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] id: Sensors' I2C address (optional)
        :param list[int] slot: Sensors' slot number (optional)
        :return: SensorsUltrasonicValueResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'slot']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sensors_ultrasonic" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))  # noqa: E501
            collection_formats['id'] = 'csv'  # noqa: E501
        if 'slot' in params:
            query_params.append(('slot', params['slot']))  # noqa: E501
            collection_formats['slot'] = 'csv'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sensors/ultrasonic', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SensorsUltrasonicValueResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_sensors(self, body, **kwargs):  # noqa: E501
        """Calibrate sensor or change sensor's I2C address  # noqa: E501

         The calibration only support gyroscope sensor. If your device has slot number, the sensor I2C address cannot be changed.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_sensors(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SensorsOperationRequest body: (required)
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_sensors_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.put_sensors_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def put_sensors_with_http_info(self, body, **kwargs):  # noqa: E501
        """Calibrate sensor or change sensor's I2C address  # noqa: E501

         The calibration only support gyroscope sensor. If your device has slot number, the sensor I2C address cannot be changed.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_sensors_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SensorsOperationRequest body: (required)
        :return: CommonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_sensors" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_sensors`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/sensors', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CommonResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
