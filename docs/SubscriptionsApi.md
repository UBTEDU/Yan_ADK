# openadk.SubscriptionsApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_motions_subscription**](SubscriptionsApi.md#delete_motions_subscription) | **DELETE** /subscriptions/motions | Unsubscribe the motion status
[**delete_sensors_subscription**](SubscriptionsApi.md#delete_sensors_subscription) | **DELETE** /subscriptions/sensors | Unsubscribe the sensor&#39;s value
[**delete_visions_subscription**](SubscriptionsApi.md#delete_visions_subscription) | **DELETE** /subscriptions/visions | Unsubscribe compute vision result
[**delete_voice_asr_subscription**](SubscriptionsApi.md#delete_voice_asr_subscription) | **DELETE** /subscriptions/voice/asr | Unsubscribe auto speech recognition result
[**delete_voice_iat_subscription**](SubscriptionsApi.md#delete_voice_iat_subscription) | **DELETE** /subscriptions/voice/iat | Unsubscribe auto transform result
[**delete_voice_tts_subscription**](SubscriptionsApi.md#delete_voice_tts_subscription) | **DELETE** /subscriptions/voice/tts | Unsubscribe text to speech result
[**post_motions_subscription**](SubscriptionsApi.md#post_motions_subscription) | **POST** /subscriptions/motions | Subscribe the motion status
[**post_sensors_subscription**](SubscriptionsApi.md#post_sensors_subscription) | **POST** /subscriptions/sensors | Subscribe the sensor&#39;s value
[**post_visions_subscription**](SubscriptionsApi.md#post_visions_subscription) | **POST** /subscriptions/visions | Subscribe compute vision result
[**post_voice_asr_subscriptions**](SubscriptionsApi.md#post_voice_asr_subscriptions) | **POST** /subscriptions/voice/asr | Subscribe auto speech recognition result
[**post_voice_iat_subscription**](SubscriptionsApi.md#post_voice_iat_subscription) | **POST** /subscriptions/voice/iat | Subscribe auto transform result
[**post_voice_tts_subscriptions**](SubscriptionsApi.md#post_voice_tts_subscriptions) | **POST** /subscriptions/voice/tts | Subscribe text to speech result


# **delete_motions_subscription**
> CommonResponse delete_motions_subscription(body)

Unsubscribe the motion status



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsMotionsDelete() # SubscriptionsMotionsDelete | 

try:
    # Unsubscribe the motion status
    api_response = api_instance.delete_motions_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_motions_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsMotionsDelete**](SubscriptionsMotionsDelete.md)|  | 

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

Unsubscribe the sensor's value



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsSensorsDelete() # SubscriptionsSensorsDelete | 

try:
    # Unsubscribe the sensor's value
    api_response = api_instance.delete_sensors_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_sensors_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsSensorsDelete**](SubscriptionsSensorsDelete.md)|  | 

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

Unsubscribe compute vision result



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsVisionsDelete() # SubscriptionsVisionsDelete | 

try:
    # Unsubscribe compute vision result
    api_response = api_instance.delete_visions_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_visions_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsVisionsDelete**](SubscriptionsVisionsDelete.md)|  | 

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

Unsubscribe auto speech recognition result



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsAsrVoiceDelete() # SubscriptionsAsrVoiceDelete | 

try:
    # Unsubscribe auto speech recognition result
    api_response = api_instance.delete_voice_asr_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_voice_asr_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsAsrVoiceDelete**](SubscriptionsAsrVoiceDelete.md)|  | 

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

Unsubscribe auto transform result



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsIatVoiceDelete() # SubscriptionsIatVoiceDelete | 

try:
    # Unsubscribe auto transform result
    api_response = api_instance.delete_voice_iat_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_voice_iat_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsIatVoiceDelete**](SubscriptionsIatVoiceDelete.md)|  | 

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

Unsubscribe text to speech result



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.SubscriptionsApi()
body = openadk.SubscriptionsTtsVoiceDelete() # SubscriptionsTtsVoiceDelete | 

try:
    # Unsubscribe text to speech result
    api_response = api_instance.delete_voice_tts_subscription(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_voice_tts_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubscriptionsTtsVoiceDelete**](SubscriptionsTtsVoiceDelete.md)|  | 

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

Subscribe the motion status



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
    # Subscribe the motion status
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

Subscribe the sensor's value



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
    # Subscribe the sensor's value
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

Subscribe compute vision result

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
    # Subscribe compute vision result
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

Subscribe auto speech recognition result

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
    # Subscribe auto speech recognition result
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

Subscribe auto transform result

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
    # Subscribe auto transform result
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

Subscribe text to speech result



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
    # Subscribe text to speech result
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

