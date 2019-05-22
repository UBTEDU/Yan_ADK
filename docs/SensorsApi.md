# openadk.SensorsApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sensors_environment**](SensorsApi.md#get_sensors_environment) | **GET** /sensors/environment | Get enviornment sensor&#39;s value
[**get_sensors_gyro**](SensorsApi.md#get_sensors_gyro) | **GET** /sensors/gyro | Get gyroscope sensor&#39;s value
[**get_sensors_infrared**](SensorsApi.md#get_sensors_infrared) | **GET** /sensors/infrared | Get infrared sensor&#39;s value
[**get_sensors_list**](SensorsApi.md#get_sensors_list) | **GET** /sensors/list | Get all sensors&#39; list
[**get_sensors_pressure**](SensorsApi.md#get_sensors_pressure) | **GET** /sensors/pressure | Get pressure sensor&#39;s value
[**get_sensors_touch**](SensorsApi.md#get_sensors_touch) | **GET** /sensors/touch | Get touch sensor&#39;s value
[**get_sensors_ultrasonic**](SensorsApi.md#get_sensors_ultrasonic) | **GET** /sensors/ultrasonic | Get ultrasonic sensor&#39;s value
[**put_sensors**](SensorsApi.md#put_sensors) | **PUT** /sensors | Calibrate sensor or change sensor&#39;s I2C address


# **get_sensors_environment**
> SensorsEnvironmentValueResponse get_sensors_environment(slot=slot)

Get enviornment sensor's value

 Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()
slot = [56] # list[int] | Sensors' slot number (optional) (optional)

try:
    # Get enviornment sensor's value
    api_response = api_instance.get_sensors_environment(slot=slot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_environment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slot** | [**list[int]**](int.md)| Sensors&#39; slot number (optional) | [optional] 

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

Get gyroscope sensor's value



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
    # Get gyroscope sensor's value
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
> SensorsInfraredValueResponse get_sensors_infrared(id=id, slot=slot)

Get infrared sensor's value

 Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()
id = [56] # list[int] | Sensors' I2C address (optional) (optional)
slot = [56] # list[int] | Sensors' slot number (optional) (optional)

try:
    # Get infrared sensor's value
    api_response = api_instance.get_sensors_infrared(id=id, slot=slot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_infrared: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| Sensors&#39; I2C address (optional) | [optional] 
 **slot** | [**list[int]**](int.md)| Sensors&#39; slot number (optional) | [optional] 

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

Get all sensors' list

 The usage scenario of this API is as follows: - A new sensor is installed - Sensor is not detected - Get all the sensor list 

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
    # Get all sensors' list
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
> SensorsPressureValueResponse get_sensors_pressure(id=id, slot=slot)

Get pressure sensor's value

 Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()
id = [56] # list[int] | Sensors' I2C address (optional) (optional)
slot = [56] # list[int] | Sensors' slot number (optional) (optional)

try:
    # Get pressure sensor's value
    api_response = api_instance.get_sensors_pressure(id=id, slot=slot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_pressure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| Sensors&#39; I2C address (optional) | [optional] 
 **slot** | [**list[int]**](int.md)| Sensors&#39; slot number (optional) | [optional] 

### Return type

[**SensorsPressureValueResponse**](SensorsPressureValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_touch**
> SensorsTouchValueResponse get_sensors_touch(id=id, slot=slot)

Get touch sensor's value

 Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()
id = [56] # list[int] | Sensors' I2C address (optional) (optional)
slot = [56] # list[int] | Sensors' slot number (optional) (optional)

try:
    # Get touch sensor's value
    api_response = api_instance.get_sensors_touch(id=id, slot=slot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_touch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| Sensors&#39; I2C address (optional) | [optional] 
 **slot** | [**list[int]**](int.md)| Sensors&#39; slot number (optional) | [optional] 

### Return type

[**SensorsTouchValueResponse**](SensorsTouchValueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sensors_ultrasonic**
> SensorsUltrasonicValueResponse get_sensors_ultrasonic(id=id, slot=slot)

Get ultrasonic sensor's value

 Before calling this API, please make sure the sensor is detected. If the sensor is not detected, please call GET /sensors/list. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SensorsApi()
id = [56] # list[int] | Sensors' I2C address (optional) (optional)
slot = [56] # list[int] | Sensors' slot number (optional) (optional)

try:
    # Get ultrasonic sensor's value
    api_response = api_instance.get_sensors_ultrasonic(id=id, slot=slot)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SensorsApi->get_sensors_ultrasonic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**list[int]**](int.md)| Sensors&#39; I2C address (optional) | [optional] 
 **slot** | [**list[int]**](int.md)| Sensors&#39; slot number (optional) | [optional] 

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

Calibrate sensor or change sensor's I2C address

 The calibration only support gyroscope sensor. If your device has slot number, the sensor I2C address cannot be changed. 

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
    # Calibrate sensor or change sensor's I2C address
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

