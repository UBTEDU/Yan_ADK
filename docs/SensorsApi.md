# openadk.SensorsApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sensors_environment**](SensorsApi.md#get_sensors_environment) | **GET** /sensors/environment | 获取环境传感器值
[**get_sensors_gyro**](SensorsApi.md#get_sensors_gyro) | **GET** /sensors/gyro | 获取运动传感器值
[**get_sensors_infrared**](SensorsApi.md#get_sensors_infrared) | **GET** /sensors/infrared | 获取红外传感器值
[**get_sensors_list**](SensorsApi.md#get_sensors_list) | **GET** /sensors/list | 获取所有传感器的列表
[**get_sensors_pressure**](SensorsApi.md#get_sensors_pressure) | **GET** /sensors/pressure | 获取压力传感器值
[**get_sensors_touch**](SensorsApi.md#get_sensors_touch) | **GET** /sensors/touch | 获取触摸传感器值
[**get_sensors_ultrasonic**](SensorsApi.md#get_sensors_ultrasonic) | **GET** /sensors/ultrasonic | 获取超声传感器值
[**put_sensors**](SensorsApi.md#put_sensors) | **PUT** /sensors | 传感器设置（校准或修改ID）


# **get_sensors_environment**
> SensorsEnvironmentValueResponse get_sensors_environment()

获取环境传感器值



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()

try:
    # 获取环境传感器值
    api_response = api_instance.get_sensors_environment()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_environment: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SensorsEnvironmentValueResponse**](SensorsEnvironmentValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_gyro**
> SensorsGyroValueResponse get_sensors_gyro()

获取运动传感器值



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()

try:
    # 获取运动传感器值
    api_response = api_instance.get_sensors_gyro()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_gyro: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SensorsGyroValueResponse**](SensorsGyroValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_infrared**
> SensorsInfraredValueResponse get_sensors_infrared(id=id)

获取红外传感器值



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()
id = [56] # list[int] | 传感器ID，可不填 (optional)

try:
    # 获取红外传感器值
    api_response = api_instance.get_sensors_infrared(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_infrared: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| 传感器ID，可不填 | [optional] 

### Return type

[**SensorsInfraredValueResponse**](SensorsInfraredValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_list**
> SensorsListResponse get_sensors_list()

获取所有传感器的列表



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()

try:
    # 获取所有传感器的列表
    api_response = api_instance.get_sensors_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SensorsListResponse**](SensorsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_pressure**
> SensorsPressureValueResponse get_sensors_pressure(id=id)

获取压力传感器值



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()
id = [56] # list[int] | 传感器ID，可不填 (optional)

try:
    # 获取压力传感器值
    api_response = api_instance.get_sensors_pressure(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_pressure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| 传感器ID，可不填 | [optional] 

### Return type

[**SensorsPressureValueResponse**](SensorsPressureValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_touch**
> SensorsTouchValueResponse get_sensors_touch(id=id)

获取触摸传感器值



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()
id = [56] # list[int] | 传感器ID，可不填 (optional)

try:
    # 获取触摸传感器值
    api_response = api_instance.get_sensors_touch(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_touch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| 传感器ID，可不填 | [optional] 

### Return type

[**SensorsTouchValueResponse**](SensorsTouchValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_ultrasonic**
> SensorsUltrasonicValueResponse get_sensors_ultrasonic(id=id)

获取超声传感器值



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()
id = [56] # list[int] | 传感器ID，可不填 (optional)

try:
    # 获取超声传感器值
    api_response = api_instance.get_sensors_ultrasonic(id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_ultrasonic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| 传感器ID，可不填 | [optional] 

### Return type

[**SensorsUltrasonicValueResponse**](SensorsUltrasonicValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sensors**
> CommonResponse put_sensors(body)

传感器设置（校准或修改ID）

目前只支持运动传感器（gyro）校准，以及部分传感器修改ID

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()
body = openadk.SensorsOperationRequest() # SensorsOperationRequest | 

try:
    # 传感器设置（校准或修改ID）
    api_response = api_instance.put_sensors(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->put_sensors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SensorsOperationRequest**](SensorsOperationRequest.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

