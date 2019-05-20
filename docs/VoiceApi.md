# openadk.VoiceApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_voice_asr**](VoiceApi.md#delete_voice_asr) | **DELETE** /voice/asr | 停止语义理解
[**delete_voice_iat**](VoiceApi.md#delete_voice_iat) | **DELETE** /voice/iat | 停止语音听写
`[**delete_voice_offline_syntax**](VoiceApi.md#delete_voice_offline_syntax) | **DELETE** /voice/asr/offlinesyntax | 删除离线语法配置
[**delete_voice_tts**](VoiceApi.md#delete_voice_tts) | **DELETE** /voice/tts | 停止所有发送的语音合成
[**get_voice_asr**](VoiceApi.md#get_voice_asr) | **GET** /voice/asr | 获取语义理解工作状态
[**get_voice_iat**](VoiceApi.md#get_voice_iat) | **GET** /voice/iat | 获取语音听写结果
[**get_voice_offline_syntax**](VoiceApi.md#get_voice_offline_syntax) | **GET** /voice/asr/offlinesyntax | 获取离线语法配置
[**get_voice_offline_syntax_grammars**](VoiceApi.md#get_voice_offline_syntax_grammars) | **GET** /voice/asr/offlinesyntax/grammars | 获取离线语法名称
[**get_voice_tts**](VoiceApi.md#get_voice_tts) | **GET** /voice/tts | 获取指定或者当前工作状态
[**post_voice_offline_syntax**](VoiceApi.md#post_voice_offline_syntax) | **POST** /voice/asr/offlinesyntax | 添加离线语法配置
[**put_voice_asr**](VoiceApi.md#put_voice_asr) | **PUT** /voice/asr | 开始语义理解
[**put_voice_iat**](VoiceApi.md#put_voice_iat) | **PUT** /voice/iat | 开始语音听写
[**put_voice_offline_syntax**](VoiceApi.md#put_voice_offline_syntax) | **PUT** /voice/asr/offlinesyntax | 更新离线语法配置
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

# **delete_voice_offline_syntax**
> CommonResponse delete_voice_offline_syntax(body)

删除离线语法配置

获取系统所有的离线语法名称，请注意系统默认的离线语法名称为defaut, 它不可以通过API来添加，删除以及修改。

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()
body = openadk.VoiceDeleteOfflineSyntax() # VoiceDeleteOfflineSyntax | 

try:
    # 删除离线语法配置
    api_response = api_instance.delete_voice_offline_syntax(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->delete_voice_offline_syntax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoiceDeleteOfflineSyntax**](VoiceDeleteOfflineSyntax.md)|  | 

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

停止所有发送的语音合成



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
    # 停止所有发送的语音合成
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

获取语音听写结果



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
    # 获取语音听写结果
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

# **get_voice_offline_syntax**
> VoiceGetOfflineSyntaxResponse get_voice_offline_syntax(body)

获取离线语法配置

获取系统所有的离线语法名称，请注意系统默认的离线语法名称为defaut, 它不可以通过API来添加，删除以及修改。

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()
body = 'body_example' # str | 获得离线合成语法名称

try:
    # 获取离线语法配置
    api_response = api_instance.get_voice_offline_syntax(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->get_voice_offline_syntax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| 获得离线合成语法名称 | 

### Return type

[**VoiceGetOfflineSyntaxResponse**](VoiceGetOfflineSyntaxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voice_offline_syntax_grammars**
> VoiceGetOfflineSyntaxGrammarsResponse get_voice_offline_syntax_grammars()

获取离线语法名称

获取系统所有的离线语法名称，请注意系统默认的离线语法名称为defaut, 它不可以通过API来添加，删除以及修改。

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
    # 获取离线语法名称
    api_response = api_instance.get_voice_offline_syntax_grammars()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->get_voice_offline_syntax_grammars: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VoiceGetOfflineSyntaxGrammarsResponse**](VoiceGetOfflineSyntaxGrammarsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voice_tts**
> VoiceGetResponse get_voice_tts(timestamp=timestamp)

获取指定或者当前工作状态

带时间戳为指定任务工作状态，如果无时间戳则当前任务

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()
timestamp = 789 # int | 时间戳 (optional)

try:
    # 获取指定或者当前工作状态
    api_response = api_instance.get_voice_tts(timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->get_voice_tts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| 时间戳 | [optional] 

### Return type

[**VoiceGetResponse**](VoiceGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_voice_offline_syntax**
> CommonResponse post_voice_offline_syntax(body)

添加离线语法配置

获取系统所有的离线语法名称，请注意系统默认的离线语法名称为defaut, 它不可以通过API来添加，删除以及修改。   离线语法的配置有以下约束条件，当条件不満满足时语音识别可能结果不正确。   约束条件：   1. 所有的grammar字段不能重复;    2. 所有的slot字段不能重复;    3. 所有的rule字段不能为空，每个规则都必须保证其定义的唯一性，也就是规则名在同一个语义中不能够被定义两次。 在定义规则时，要注意规则名称不能是 VOID、 NULL 和 GARBAGE，这三个规则名称被作为保留关键词为后续功能扩展使用。;    4. 可以通过关键词!id 定义了记号所对应的语义。 语义只能支持数字，其它数字将会导致编译错诨。语义支持的数字范围为 32 位有符号整形，也就是-2^(32-1) ~ 2^(32-1) -1（其中^表示幂操作）， 当定义的数字操作此范围时，会导致编译错误或者被截断   详细信息请参看： https://doc.xfyun.cn/msc_windows/%E8%AF%AD%E6%B3%95%EF%BC%88%E5%91%BD%E4%BB%A4%E8%AF%8D%EF%BC%89%E8%AF%86%E5%88%AB.html 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()
body = openadk.VoicePostOfflineSyntax() # VoicePostOfflineSyntax | 

try:
    # 添加离线语法配置
    api_response = api_instance.post_voice_offline_syntax(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->post_voice_offline_syntax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoicePostOfflineSyntax**](VoicePostOfflineSyntax.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_voice_asr**
> CommonResponse put_voice_asr(body)

开始语义理解

当语义理解(单次/多次)或者语音听写处于工作状态时，需要先停止当前的语义理解或者语音听写。

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

当语义理解(单次/多次)或者语音听写处于工作状态时，需要先停止当前的语义理解或者语音听写。

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

# **put_voice_offline_syntax**
> CommonResponse put_voice_offline_syntax(body)

更新离线语法配置

获取系统所有的离线语法名称，请注意系统默认的离线语法名称为defaut, 它不可以通过API来添加，删除以及修改。   离线语法的配置有以下约束条件，当条件不満满足时语音识别可能结果不正确。   约束条件：   1. 所有的grammar字段不能重复;    2. 所有的slot字段不能重复;    3. 所有的rule字段不能为空，每个规则都必须保证其定义的唯一性，也就是规则名在同一个语义中不能够被定义两次。 在定义规则时，要注意规则名称不能是 VOID、 NULL 和 GARBAGE，这三个规则名称被作为保留关键词为后续功能扩展使用。;    4. 可以通过关键词!id 定义了记号所对应的语义。 语义只能支持数字，其它数字将会导致编译错诨。语义支持的数字范围为 32 位有符号整形，也就是-2^(32-1) ~ 2^(32-1) -1（其中^表示幂操作）， 当定义的数字操作此范围时，会导致编译错误或者被截断   详细信息请参看： https://doc.xfyun.cn/msc_windows/%E8%AF%AD%E6%B3%95%EF%BC%88%E5%91%BD%E4%BB%A4%E8%AF%8D%EF%BC%89%E8%AF%86%E5%88%AB.html

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()
body = openadk.VoicePutOfflineSyntax() # VoicePutOfflineSyntax | 

try:
    # 更新离线语法配置
    api_response = api_instance.put_voice_offline_syntax(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->put_voice_offline_syntax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoicePutOfflineSyntax**](VoicePutOfflineSyntax.md)|  | 

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

