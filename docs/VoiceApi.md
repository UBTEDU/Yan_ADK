# openadk.VoiceApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_voice_asr**](VoiceApi.md#delete_voice_asr) | **DELETE** /voice/asr | 停止语义理解
[**delete_voice_iat**](VoiceApi.md#delete_voice_iat) | **DELETE** /voice/iat | 停止语音听写
[**delete_voice_tts**](VoiceApi.md#delete_voice_tts) | **DELETE** /voice/tts | 停止当前的语音合成
[**get_voice_asr**](VoiceApi.md#get_voice_asr) | **GET** /voice/asr | 获取语义理解工作状态
[**get_voice_iat**](VoiceApi.md#get_voice_iat) | **GET** /voice/iat | 获取语音听写工作状态
[**get_voice_tts**](VoiceApi.md#get_voice_tts) | **GET** /voice/tts | 获取当前语音合成工作状态
[**put_voice_asr**](VoiceApi.md#put_voice_asr) | **PUT** /voice/asr | 开始语义理解
[**put_voice_iat**](VoiceApi.md#put_voice_iat) | **PUT** /voice/iat | 开始语音听写
[**put_voice_tts**](VoiceApi.md#put_voice_tts) | **PUT** /voice/tts | 开始语音合成任务


# **delete_voice_asr**
> CommonResponse delete_voice_asr()

停止语义理解

停止开启的语义理解。

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()

try:
    # 停止语义理解
    api_response = api_instance.delete_voice_asr()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->delete_voice_asr: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_voice_iat**
> CommonResponse delete_voice_iat()

停止语音听写

停止开启的语音听写.

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()

try:
    # 停止语音听写
    api_response = api_instance.delete_voice_iat()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->delete_voice_iat: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_voice_tts**
> CommonResponse delete_voice_tts()

停止当前的语音合成



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()

try:
    # 停止当前的语音合成
    api_response = api_instance.delete_voice_tts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->delete_voice_tts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voice_asr**
> VoiceGetResponse get_voice_asr()

获取语义理解工作状态



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()

try:
    # 获取语义理解工作状态
    api_response = api_instance.get_voice_asr()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->get_voice_asr: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VoiceGetResponse**](VoiceGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voice_iat**
> VoiceGetResponse get_voice_iat()

获取语音听写工作状态



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()

try:
    # 获取语音听写工作状态
    api_response = api_instance.get_voice_iat()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->get_voice_iat: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VoiceGetResponse**](VoiceGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voice_tts**
> VoiceGetResponse get_voice_tts()

获取当前语音合成工作状态



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()

try:
    # 获取当前语音合成工作状态
    api_response = api_instance.get_voice_tts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->get_voice_tts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VoiceGetResponse**](VoiceGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_voice_asr**
> CommonResponse put_voice_asr(body)

开始语义理解

当语义理解(单次/多次)或者语音识别处于工作状态时，需要先停止当前的语义理解或者语音识别。

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()
body = openadk.VoiceAsrOption() # VoiceAsrOption | 

try:
    # 开始语义理解
    api_response = api_instance.put_voice_asr(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->put_voice_asr: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoiceAsrOption**](VoiceAsrOption.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_voice_iat**
> CommonResponse put_voice_iat(body=body)

开始语音听写

当语义理解(单次/多次)或者语音识别处于工作状态时，需要先停止当前的语义理解或者语音识别。

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()
body = openadk.VoiceIatRequest() # VoiceIatRequest |  (optional)

try:
    # 开始语音听写
    api_response = api_instance.put_voice_iat(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->put_voice_iat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoiceIatRequest**](VoiceIatRequest.md)|  | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_voice_tts**
> CommonResponse put_voice_tts(body)

开始语音合成任务

合成指定的语句并播放。当语音合成处于工作状态时可以接受新的语音合成任务。

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()
body = openadk.VoiceTTSStr() # VoiceTTSStr | 

try:
    # 开始语音合成任务
    api_response = api_instance.put_voice_tts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->put_voice_tts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoiceTTSStr**](VoiceTTSStr.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

