# openadk.SubscriptionsApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_motions_subscription**](SubscriptionsApi.md#delete_motions_subscription) | **DELETE** /subscriptions/motions | 取消订阅运动状态消息
[**delete_sensors_subscription**](SubscriptionsApi.md#delete_sensors_subscription) | **DELETE** /subscriptions/sensors | 取消订阅传感器消息
[**delete_visions_subscription**](SubscriptionsApi.md#delete_visions_subscription) | **DELETE** /subscriptions/visions | 取消订阅指定视觉任务消息
[**delete_voice_asr_subscription**](SubscriptionsApi.md#delete_voice_asr_subscription) | **DELETE** /subscriptions/voice/asr | 取消订阅语义理解消息
[**delete_voice_iat_subscription**](SubscriptionsApi.md#delete_voice_iat_subscription) | **DELETE** /subscriptions/voice/iat | 取消订阅语音听写推送消息
[**delete_voice_tts_subscription**](SubscriptionsApi.md#delete_voice_tts_subscription) | **DELETE** /subscriptions/voice/tts | 取消订阅语音合成状态消息
[**post_motions_subscription**](SubscriptionsApi.md#post_motions_subscription) | **POST** /subscriptions/motions | 订阅运动状态消息
[**post_sensors_subscription**](SubscriptionsApi.md#post_sensors_subscription) | **POST** /subscriptions/sensors | 订阅传感器消息
[**post_visions_subscription**](SubscriptionsApi.md#post_visions_subscription) | **POST** /subscriptions/visions | 订阅指定视觉任务消息
[**post_voice_asr_subscriptions**](SubscriptionsApi.md#post_voice_asr_subscriptions) | **POST** /subscriptions/voice/asr | 订阅语义理解消息
[**post_voice_iat_subscription**](SubscriptionsApi.md#post_voice_iat_subscription) | **POST** /subscriptions/voice/iat | 订阅语音听写推送消息
[**post_voice_tts_subscriptions**](SubscriptionsApi.md#post_voice_tts_subscriptions) | **POST** /subscriptions/voice/tts | 订阅语音合成状态消息


# **delete_motions_subscription**
> CommonResponse delete_motions_subscription(body)

取消订阅运动状态消息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsMotions() # SubscriptionsMotions | 

try:
    # 取消订阅运动状态消息
    api_response = api_instance.delete_motions_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_motions_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsMotions**](SubscriptionsMotions.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sensors_subscription**
> CommonResponse delete_sensors_subscription(body)

取消订阅传感器消息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsSensors() # SubscriptionsSensors | 

try:
    # 取消订阅传感器消息
    api_response = api_instance.delete_sensors_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_sensors_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsSensors**](SubscriptionsSensors.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_visions_subscription**
> CommonResponse delete_visions_subscription(body)

取消订阅指定视觉任务消息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsVisions() # SubscriptionsVisions | 

try:
    # 取消订阅指定视觉任务消息
    api_response = api_instance.delete_visions_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_visions_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsVisions**](SubscriptionsVisions.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_voice_asr_subscription**
> CommonResponse delete_voice_asr_subscription(body)

取消订阅语义理解消息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsAsrVoice() # SubscriptionsAsrVoice | 

try:
    # 取消订阅语义理解消息
    api_response = api_instance.delete_voice_asr_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_voice_asr_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsAsrVoice**](SubscriptionsAsrVoice.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_voice_iat_subscription**
> CommonResponse delete_voice_iat_subscription(body)

取消订阅语音听写推送消息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsIatVoice() # SubscriptionsIatVoice | 

try:
    # 取消订阅语音听写推送消息
    api_response = api_instance.delete_voice_iat_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_voice_iat_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsIatVoice**](SubscriptionsIatVoice.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_voice_tts_subscription**
> CommonResponse delete_voice_tts_subscription(body)

取消订阅语音合成状态消息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsTtsVoice() # SubscriptionsTtsVoice | 

try:
    # 取消订阅语音合成状态消息
    api_response = api_instance.delete_voice_tts_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_voice_tts_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsTtsVoice**](SubscriptionsTtsVoice.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_motions_subscription**
> CommonResponse post_motions_subscription(body)

订阅运动状态消息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsMotions() # SubscriptionsMotions | 

try:
    # 订阅运动状态消息
    api_response = api_instance.post_motions_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->post_motions_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsMotions**](SubscriptionsMotions.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sensors_subscription**
> CommonResponse post_sensors_subscription(body)

订阅传感器消息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsSensors() # SubscriptionsSensors | 

try:
    # 订阅传感器消息
    api_response = api_instance.post_sensors_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->post_sensors_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsSensors**](SubscriptionsSensors.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_visions_subscription**
> CommonResponse post_visions_subscription(body)

订阅指定视觉任务消息

URL example: http://10.10.1.30:80/subscriptions/visions

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsVisions() # SubscriptionsVisions | 

try:
    # 订阅指定视觉任务消息
    api_response = api_instance.post_visions_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->post_visions_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsVisions**](SubscriptionsVisions.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_voice_asr_subscriptions**
> CommonResponse post_voice_asr_subscriptions(body)

订阅语义理解消息

URL example: http://10.10.1.30:80/subscriptions/voice/asr

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsAsrVoice() # SubscriptionsAsrVoice | 

try:
    # 订阅语义理解消息
    api_response = api_instance.post_voice_asr_subscriptions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->post_voice_asr_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsAsrVoice**](SubscriptionsAsrVoice.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_voice_iat_subscription**
> CommonResponse post_voice_iat_subscription(body)

订阅语音听写推送消息

URL example: http://10.10.1.30:80/subscriptions/voice/iat

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsIatVoice() # SubscriptionsIatVoice | 

try:
    # 订阅语音听写推送消息
    api_response = api_instance.post_voice_iat_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->post_voice_iat_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsIatVoice**](SubscriptionsIatVoice.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_voice_tts_subscriptions**
> CommonResponse post_voice_tts_subscriptions(body)

订阅语音合成状态消息



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsTtsVoice() # SubscriptionsTtsVoice | 

try:
    # 订阅语音合成状态消息
    api_response = api_instance.post_voice_tts_subscriptions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->post_voice_tts_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsTtsVoice**](SubscriptionsTtsVoice.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

