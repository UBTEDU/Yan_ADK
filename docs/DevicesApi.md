# openadk.DevicesApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_devices_battery**](DevicesApi.md#get_devices_battery) | **GET** /devices/battery | Get the battery information
[**get_devices_fall_management**](DevicesApi.md#get_devices_fall_management) | **GET** /devices/fall_management | Get fall management configuration
[**get_devices_languages**](DevicesApi.md#get_devices_languages) | **GET** /devices/languages | Get language settings
[**get_devices_led**](DevicesApi.md#get_devices_led) | **GET** /devices/led | Get the light effects
[**get_devices_versions**](DevicesApi.md#get_devices_versions) | **GET** /devices/versions | Get the system versions
[**get_devices_volume**](DevicesApi.md#get_devices_volume) | **GET** /devices/volume | Get the volume
[**put_devices_fall_management**](DevicesApi.md#put_devices_fall_management) | **PUT** /devices/fall_management | Set fall management configuration
[**put_devices_languages**](DevicesApi.md#put_devices_languages) | **PUT** /devices/languages | Set language settings
[**put_devices_led**](DevicesApi.md#put_devices_led) | **PUT** /devices/led | Set the light effects
[**put_devices_volume**](DevicesApi.md#put_devices_volume) | **PUT** /devices/volume | Set the volume


# **get_devices_battery**
> DevicesBatteryResponse get_devices_battery()

Get the battery information



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
    # Get the battery information
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

Get fall management configuration



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
    # Get fall management configuration
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

Get language settings



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
    # Get language settings
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

Get the light effects



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
    # Get the light effects
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

Get the system versions



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()
type = ['type_example'] # list[str] | Version type

try:
    # Get the system versions
    api_response = api_instance.get_devices_versions(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->get_devices_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**list[str]**](str.md)| Version type | 

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

Get the volume



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
    # Get the volume
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

Set fall management configuration



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
    # Set fall management configuration
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

Set language settings



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.DevicesApi()
body = openadk.DevicesLanguage() # DevicesLanguage | Language information

try:
    # Set language settings
    api_response = api_instance.put_devices_languages(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesApi->put_devices_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DevicesLanguage**](DevicesLanguage.md)| Language information | 

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

Set the light effects



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
    # Set the light effects
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

Set the volume



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
    # Set the volume
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

