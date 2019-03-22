# openadk.ServosApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_servos_angles**](ServosApi.md#get_servos_angles) | **GET** /servos/angles | 查询舵机角度值
[**get_servos_mode**](ServosApi.md#get_servos_mode) | **GET** /servos/mode | 查询舵机工作模式
[**put_servos_angles**](ServosApi.md#put_servos_angles) | **PUT** /servos/angles | 设置舵机角度值
[**put_servos_mode**](ServosApi.md#put_servos_mode) | **PUT** /servos/mode | 设置舵机工作模式


# **get_servos_angles**
> ServosAnglesResponse get_servos_angles(names)

查询舵机角度值

一次可以查询一个或者多个舵机角度值

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.ServosApi()
names = ['names_example'] # list[str] | 机器人舵机名称

try:
    # 查询舵机角度值
    api_response = api_instance.get_servos_angles(names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServosApi->get_servos_angles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| 机器人舵机名称 | 

### Return type

[**ServosAnglesResponse**](ServosAnglesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_servos_mode**
> ServosModeResponse get_servos_mode(names)

查询舵机工作模式

一次可以查询一个或者多个舵机的模式

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.ServosApi()
names = ['names_example'] # list[str] | 舵机名称列表

try:
    # 查询舵机工作模式
    api_response = api_instance.get_servos_mode(names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServosApi->get_servos_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| 舵机名称列表 | 

### Return type

[**ServosModeResponse**](ServosModeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_servos_angles**
> ServosResultResponse put_servos_angles(body)

设置舵机角度值

一次可以设置一个或者多个舵机角度值

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.ServosApi()
body = openadk.ServosAnglesRequest() # ServosAnglesRequest | 舵机角度信息

try:
    # 设置舵机角度值
    api_response = api_instance.put_servos_angles(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServosApi->put_servos_angles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServosAnglesRequest**](ServosAnglesRequest.md)| 舵机角度信息 | 

### Return type

[**ServosResultResponse**](ServosResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_servos_mode**
> ServosResultResponse put_servos_mode(body)

设置舵机工作模式

一次可以设置单个或者舵机的模式

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.ServosApi()
body = openadk.ServosModeRequest() # ServosModeRequest | 舵机模式信息

try:
    # 设置舵机工作模式
    api_response = api_instance.put_servos_mode(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServosApi->put_servos_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServosModeRequest**](ServosModeRequest.md)| 舵机模式信息 | 

### Return type

[**ServosResultResponse**](ServosResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

