# coding: utf-8

"""
    Yanshee RESTful API

    Yanshee RESTful APIs是一套专门为编程爱好者提供二次开发的接口．它通过http/https的方式向外界提供机器人控制，传感器读取，机器人视觉等功能．用户还可以通过编程的方式训练自己的模型，学习一些机器学习的内容．  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: swenggroup@ubtrobot.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openadk.api_client import ApiClient


class ServosApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_servos_angles(self, names, **kwargs):  # noqa: E501
        """查询舵机角度值  # noqa: E501

        一次可以查询一个或者多个舵机角度值  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_servos_angles(names, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] names: 机器人舵机名称 (required)
        :return: ServosAnglesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_servos_angles_with_http_info(names, **kwargs)  # noqa: E501
        else:
            (data) = self.get_servos_angles_with_http_info(names, **kwargs)  # noqa: E501
            return data

    def get_servos_angles_with_http_info(self, names, **kwargs):  # noqa: E501
        """查询舵机角度值  # noqa: E501

        一次可以查询一个或者多个舵机角度值  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_servos_angles_with_http_info(names, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] names: 机器人舵机名称 (required)
        :return: ServosAnglesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['names']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_servos_angles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'names' is set
        if ('names' not in params or
                params['names'] is None):
            raise ValueError("Missing the required parameter `names` when calling `get_servos_angles`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'names' in params:
            query_params.append(('names', params['names']))  # noqa: E501
            collection_formats['names'] = 'multi'  # noqa: E501

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
            '/servos/angles', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServosAnglesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_servos_mode(self, names, **kwargs):  # noqa: E501
        """查询舵机工作模式  # noqa: E501

        一次可以查询一个或者多个舵机的模式  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_servos_mode(names, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] names: 舵机名称列表 (required)
        :return: ServosModeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_servos_mode_with_http_info(names, **kwargs)  # noqa: E501
        else:
            (data) = self.get_servos_mode_with_http_info(names, **kwargs)  # noqa: E501
            return data

    def get_servos_mode_with_http_info(self, names, **kwargs):  # noqa: E501
        """查询舵机工作模式  # noqa: E501

        一次可以查询一个或者多个舵机的模式  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_servos_mode_with_http_info(names, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] names: 舵机名称列表 (required)
        :return: ServosModeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['names']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_servos_mode" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'names' is set
        if ('names' not in params or
                params['names'] is None):
            raise ValueError("Missing the required parameter `names` when calling `get_servos_mode`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'names' in params:
            query_params.append(('names', params['names']))  # noqa: E501
            collection_formats['names'] = 'multi'  # noqa: E501

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
            '/servos/mode', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServosModeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_servos_angles(self, body, **kwargs):  # noqa: E501
        """设置舵机角度值  # noqa: E501

        一次可以设置一个或者多个舵机角度值  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_servos_angles(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServosAnglesRequest body: 舵机角度信息 (required)
        :return: ServosResultResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_servos_angles_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.put_servos_angles_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def put_servos_angles_with_http_info(self, body, **kwargs):  # noqa: E501
        """设置舵机角度值  # noqa: E501

        一次可以设置一个或者多个舵机角度值  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_servos_angles_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServosAnglesRequest body: 舵机角度信息 (required)
        :return: ServosResultResponse
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
                    " to method put_servos_angles" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_servos_angles`")  # noqa: E501

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
            '/servos/angles', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServosResultResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_servos_mode(self, body, **kwargs):  # noqa: E501
        """设置舵机工作模式  # noqa: E501

        一次可以设置单个或者舵机的模式  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_servos_mode(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServosModeRequest body: 舵机模式信息 (required)
        :return: ServosResultResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_servos_mode_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.put_servos_mode_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def put_servos_mode_with_http_info(self, body, **kwargs):  # noqa: E501
        """设置舵机工作模式  # noqa: E501

        一次可以设置单个或者舵机的模式  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_servos_mode_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ServosModeRequest body: 舵机模式信息 (required)
        :return: ServosResultResponse
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
                    " to method put_servos_mode" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `put_servos_mode`")  # noqa: E501

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
            '/servos/mode', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ServosResultResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
