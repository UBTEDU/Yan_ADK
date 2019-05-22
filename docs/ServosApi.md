# openadk.ServosApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_servos_angles**](ServosApi.md#get_servos_angles) | **GET** /servos/angles | Get servos&#39; angle
[**get_servos_mode**](ServosApi.md#get_servos_mode) | **GET** /servos/mode | Get servos working mode
[**put_servos_angles**](ServosApi.md#put_servos_angles) | **PUT** /servos/angles | Set servos&#39; angle
[**put_servos_mode**](ServosApi.md#put_servos_mode) | **PUT** /servos/mode | Set the servos working mode


# **get_servos_angles**
> ServosAnglesResponse get_servos_angles(names)

Get servos' angle

 Please note, one API calling can get multiple servos' angle value. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.ServosApi()
names = ['names_example'] # list[str] | Servos' name

try:
    # Get servos' angle
    api_response = api_instance.get_servos_angles(names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServosApi->get_servos_angles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| Servos&#39; name | 

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

Get servos working mode

 Please note, one API calling can get multiple servos' working mode. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.ServosApi()
names = ['names_example'] # list[str] | All servo's name.

try:
    # Get servos working mode
    api_response = api_instance.get_servos_mode(names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServosApi->get_servos_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| All servo&#39;s name. | 

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

Set servos' angle

 Please note, one API calling can set multiple servos' angle value. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.ServosApi()
body = openadk.ServosAnglesRequest() # ServosAnglesRequest | Servo' angle

try:
    # Set servos' angle
    api_response = api_instance.put_servos_angles(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServosApi->put_servos_angles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServosAnglesRequest**](ServosAnglesRequest.md)| Servo&#39; angle | 

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

Set the servos working mode

 Please note, one API calling can set multiple servos' working mode. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.ServosApi()
body = openadk.ServosModeRequest() # ServosModeRequest | Servos' working mode

try:
    # Set the servos working mode
    api_response = api_instance.put_servos_mode(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServosApi->put_servos_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServosModeRequest**](ServosModeRequest.md)| Servos&#39; working mode | 

### Return type

[**ServosResultResponse**](ServosResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

