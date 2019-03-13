# coding: utf-8

"""
    Copyright (c) 2019—2029 UBTECH All rights reserved.
"""

from enum import Enum, unique

@unique
class UBTReturnValue(Enum):
    """
    This module include all the error code for Yanshee-RESTful project
    """
    SUCCESS =       {'code': 0,         'msg': 'Success'}
    FAILURE =       {'code': 1,         'msg': 'Failure'}


    NETWORK_CONNECTION_TIMEOUT = {'code': 10001,    'msg': 'Connection timeout, please check your network.'}

    SYSTEM_RESOURCE_NOT_AVAILABLE   = {'code': 20001,    'msg': 'Resource is not availble.'}
    SYSTEM_RESOURCE_NOT_FOUND       = {'code': 20002,    'msg': 'Resource not exist.'}