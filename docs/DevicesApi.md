# openadk.DevicesApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_devices_battery**](DevicesApi.md#get_devices_battery) | **GET** /devices/battery | 获得机器人电量信息
[**get_devices_fall_management**](DevicesApi.md#get_devices_fall_management) | **GET** /devices/fall_managment | 获得机器人摔倒管理状态
[**get_devices_languages**](DevicesApi.md#get_devices_languages) | **GET** /devices/languages | 获得机器人语言信息
[**get_devices_led**](DevicesApi.md#get_devices_led) | **GET** /devices/led | 获取机器人灯效
[**get_devices_versions**](DevicesApi.md#get_devices_versions) | **GET** /devices/versions | 获得机器人版本信息
[**get_devices_volume**](DevicesApi.md#get_devices_volume) | **GET** /devices/volume | 获得机器人音量
[**put_devices_fall_management**](DevicesApi.md#put_devices_fall_management) | **PUT** /devices/fall_managment | 设置机器人摔倒管理状态
[**put_devices_languages**](DevicesApi.md#put_devices_languages) | **PUT** /devices/languages | 设置机器人语言
[**put_devices_led**](DevicesApi.md#put_devices_led) | **PUT** /devices/led | 设置机器人灯效
[**put_devices_volume**](DevicesApi.md#put_devices_volume) | **PUT** /devices/volume | 设置机器人音量


# **get_devices_battery**
> DevicesBatteryResponse get_devices_battery()

获得机器人电量信息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()

try:
    # 获得机器人电量信息
    api_response = api_instance.get_devices_battery()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_battery: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DevicesBatteryResponse**](DevicesBatteryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_fall_management**
> DevicesFallManagementResponse get_devices_fall_management()

获得机器人摔倒管理状态



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()

try:
    # 获得机器人摔倒管理状态
    api_response = api_instance.get_devices_fall_management()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_fall_management: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DevicesFallManagementResponse**](DevicesFallManagementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_languages**
> DevicesLanguageResponse get_devices_languages()

获得机器人语言信息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()

try:
    # 获得机器人语言信息
    api_response = api_instance.get_devices_languages()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_languages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DevicesLanguageResponse**](DevicesLanguageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_led**
> DevicesLEDResponse get_devices_led()

获取机器人灯效



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()

try:
    # 获取机器人灯效
    api_response = api_instance.get_devices_led()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_led: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DevicesLEDResponse**](DevicesLEDResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_versions**
> DevicesVersionsResponse get_devices_versions(type)

获得机器人版本信息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()
type = ['type_example'] # list[str] | 版本信息的类型

try:
    # 获得机器人版本信息
    api_response = api_instance.get_devices_versions(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**list[str]**](str.md)| 版本信息的类型 | 

### Return type

[**DevicesVersionsResponse**](DevicesVersionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_volume**
> DevicesVolumeResponse get_devices_volume()

获得机器人音量



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()

try:
    # 获得机器人音量
    api_response = api_instance.get_devices_volume()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_volume: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DevicesVolumeResponse**](DevicesVolumeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_devices_fall_management**
> CommonResponse put_devices_fall_management(body)

设置机器人摔倒管理状态



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()
body = openadk.DevicesFallManagement() # DevicesFallManagement | 

try:
    # 设置机器人摔倒管理状态
    api_response = api_instance.put_devices_fall_management(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->put_devices_fall_management: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesFallManagement**](DevicesFallManagement.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_devices_languages**
> CommonResponse put_devices_languages(body)

设置机器人语言



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()
body = openadk.DevicesLanguage() # DevicesLanguage | 语言信息

try:
    # 设置机器人语言
    api_response = api_instance.put_devices_languages(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->put_devices_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesLanguage**](DevicesLanguage.md)| 语言信息 | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_devices_led**
> CommonResponse put_devices_led(body)

设置机器人灯效



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()
body = openadk.DevicesLED() # DevicesLED | 

try:
    # 设置机器人灯效
    api_response = api_instance.put_devices_led(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->put_devices_led: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesLED**](DevicesLED.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_devices_volume**
> CommonResponse put_devices_volume(body)

设置机器人音量



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()
body = openadk.DevicesVolume() # DevicesVolume | 

try:
    # 设置机器人音量
    api_response = api_instance.put_devices_volume(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->put_devices_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesVolume**](DevicesVolume.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

