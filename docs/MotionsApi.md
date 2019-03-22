# openadk.MotionsApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_motions_music**](MotionsApi.md#delete_motions_music) | **DELETE** /motions | 删除动作文件（只能删除用户上传的文件）
[**get_motions**](MotionsApi.md#get_motions) | **GET** /motions | 获取当前的运动状态
[**get_motions_list**](MotionsApi.md#get_motions_list) | **GET** /motions/list | 获取动作列表
[**post_motions**](MotionsApi.md#post_motions) | **POST** /motions | 上传动作文件
[**put_motions**](MotionsApi.md#put_motions) | **PUT** /motions | 运动控制


# **delete_motions_music**
> CommonResponse delete_motions_music(body)

删除动作文件（只能删除用户上传的文件）



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MotionsApi()
body = openadk.Name() # Name | 动作文件名

try:
    # 删除动作文件（只能删除用户上传的文件）
    api_response = api_instance.delete_motions_music(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionsApi->delete_motions_music: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Name**](Name.md)| 动作文件名 | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_motions**
> MotionsStatusResponse get_motions()

获取当前的运动状态



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MotionsApi()

try:
    # 获取当前的运动状态
    api_response = api_instance.get_motions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionsApi->get_motions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MotionsStatusResponse**](MotionsStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_motions_list**
> MotionsListResponse get_motions_list()

获取动作列表

可以获得所有内置和用户上传的动作列表

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MotionsApi()

try:
    # 获取动作列表
    api_response = api_instance.get_motions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionsApi->get_motions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MotionsListResponse**](MotionsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_motions**
> CommonResponse post_motions(file)

上传动作文件

文件格式目前仅支持hts或者zip

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MotionsApi()
file = '/path/to/file.txt' # file | 上传文件

try:
    # 上传动作文件
    api_response = api_instance.post_motions(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionsApi->post_motions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| 上传文件 | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_motions**
> RuntimeResponse put_motions(body)

运动控制

可以控制执行指定动作、暂停、继续、停止和复位

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MotionsApi()
body = openadk.MotionsOperation() # MotionsOperation | 运动控制的参数

try:
    # 运动控制
    api_response = api_instance.put_motions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionsApi->put_motions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MotionsOperation**](MotionsOperation.md)| 运动控制的参数 | 

### Return type

[**RuntimeResponse**](RuntimeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

