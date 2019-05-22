# openadk.VoiceApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_voice_asr**](VoiceApi.md#delete_voice_asr) | **DELETE** /voice/asr | Stop automatic speech recognition
[**delete_voice_iat**](VoiceApi.md#delete_voice_iat) | **DELETE** /voice/iat | Stop auto transform
[**delete_voice_offline_syntax**](VoiceApi.md#delete_voice_offline_syntax) | **DELETE** /voice/asr/offlinesyntax | Delete a offline grammar based offline grammar&#39;s name
[**delete_voice_tts**](VoiceApi.md#delete_voice_tts) | **DELETE** /voice/tts | Stop all text to speech
[**get_voice_asr**](VoiceApi.md#get_voice_asr) | **GET** /voice/asr | Get automatic speech recognition working status
[**get_voice_iat**](VoiceApi.md#get_voice_iat) | **GET** /voice/iat | Get auto transform(iat) result
[**get_voice_offline_syntax**](VoiceApi.md#get_voice_offline_syntax) | **GET** /voice/asr/offlinesyntax | Get offline grammar configuration
[**get_voice_offline_syntax_grammars**](VoiceApi.md#get_voice_offline_syntax_grammars) | **GET** /voice/asr/offlinesyntax/grammars | Get offline grammars&#39; name
[**get_voice_tts**](VoiceApi.md#get_voice_tts) | **GET** /voice/tts | Get specified or current working status
[**post_voice_offline_syntax**](VoiceApi.md#post_voice_offline_syntax) | **POST** /voice/asr/offlinesyntax | Add a new offline grammar
[**put_voice_asr**](VoiceApi.md#put_voice_asr) | **PUT** /voice/asr | Start automatic speech recognition
[**put_voice_iat**](VoiceApi.md#put_voice_iat) | **PUT** /voice/iat | Start auto transform
[**put_voice_offline_syntax**](VoiceApi.md#put_voice_offline_syntax) | **PUT** /voice/asr/offlinesyntax | Update offline grammar based grammar&#39;s name
[**put_voice_tts**](VoiceApi.md#put_voice_tts) | **PUT** /voice/tts | Start text to speech


# **delete_voice_asr**
> CommonResponse delete_voice_asr()

Stop automatic speech recognition



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
    # Stop automatic speech recognition
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

Stop auto transform



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
    # Stop auto transform
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

Delete a offline grammar based offline grammar's name

Default offline grammar cannot be added, deleted or modified.

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
    # Delete a offline grammar based offline grammar's name
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

Stop all text to speech



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
    # Stop all text to speech
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

Get automatic speech recognition working status



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
    # Get automatic speech recognition working status
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

Get auto transform(iat) result



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
    # Get auto transform(iat) result
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

Get offline grammar configuration

 Get all offline grammars' details. Please note, the default offline grammar's name is \"default\". Default offline grammar cannot be added, deleted or modified. The current offline speech recognition can support Chinese and English. But the English support is an experimental feature. All the field name and value should be written as <html><font color=\"red\">uppercase camel case format</font></html>. ``` {  \"grammar\": \"LocalCmd\",  \"slot\": [   {    \"name\": \"Pre\"   },   {    \"name\": \"Commands\"   }  ],  \"start\": \"LocalCmdStart\",  \"startinfo\": \"[<Pre>]<Commands>\",  \"rule\": [   {    \"name\": \"Pre\",    \"value\": \"IWantYou|Please|Start\"   },   {    \"name\": \"Commands\",    \"value\": \"Dancing\"   }  ] } ```  Please be very careful when you configure offline grammar. If the configuration is not matched the restrictions. Speech recognition may not work. The restrictions as below: - All grammar value cannot be duplicated; - All slot field cannot be duplicated; - All rule field cannot be NULL. Every rule name and value should be unique. Please pay special attention that <html><strong><font color=\"blue\">VOID</font></strong></html>, <html><strong><font color=\"blue\">NULL</font></strong></html> and <html><strong><font color=\"blue\">GARBAGE</font></strong></html> are reserved as key words. Please do not use them. - In rule field, the user can use key words !id to define the semantic. The semantic only support numbers, please do not use other character. The supported semantic number is 32 bits signed integer. The range is <html>[-2<sup>(32-1)</sup>, 2<sup>(32-1)</sup> -1]</html>.  The grammar specification and built-in keywords:  | Operator | description | example | |---|---|---| |!| the next field is a keywords | !grammar| |<>| define a rule name | &lt;name&gt;| |;| terminator | end of a line | | &Iota; | Or, define a side-by-side structure | 张三&Iota;李四 | |[]| optional, indicating that the content can be said | &lt;call&gt;: [找] &lt;name&gt;| |:| define a rule | &lt;name&gt;:张三&Iota;李四| |()| encapsulation operation, defining implicit rules |&lt;call&gt;:找(张三&Iota;李四)| |/* */| block comment |/* comment content */| |//| line comment | // comment content | More details： https://doc.xfyun.cn/msc_windows/%E8%AF%AD%E6%B3%95%EF%BC%88%E5%91%BD%E4%BB%A4%E8%AF%8D%EF%BC%89%E8%AF%86%E5%88%AB.html 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()
body = 'body_example' # str | Offline grammar's name

try:
    # Get offline grammar configuration
    api_response = api_instance.get_voice_offline_syntax(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->get_voice_offline_syntax: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Offline grammar&#39;s name | 

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

Get offline grammars' name

 Get all offline grammars' name. Please note, the default offline grammar's name is \"default\". Default offline grammar cannot be added, deleted or modified. 

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
    # Get offline grammars' name
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

Get specified or current working status

 If the input parameter has a timestamp, it means getting the specified text to speech status. If the input parameter has no timestamp, it means getting the current text to speech status. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VoiceApi()
timestamp = 789 # int | Timestamp, Unix standard time. (optional)

try:
    # Get specified or current working status
    api_response = api_instance.get_voice_tts(timestamp=timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoiceApi->get_voice_tts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **int**| Timestamp, Unix standard time. | [optional] 

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

Add a new offline grammar

 Create a new offline grammar. Please note, the default offline grammar's name is \"default\". Default offline grammar cannot be added, deleted or modified. The current offline speech recognition can support Chinese and English. But the English support is an experimental feature. All the field name and value should be written as <html><font color=\"red\">uppercase camel case format</font></html>. ``` {  \"grammar\": \"LocalCmd\",  \"slot\": [   {    \"name\": \"Pre\"   },   {    \"name\": \"Commands\"   }  ],  \"start\": \"LocalCmdStart\",  \"startinfo\": \"[<Pre>]<Commands>\",  \"rule\": [   {    \"name\": \"Pre\",    \"value\": \"IWantYou|Please|Start\"   },   {    \"name\": \"Commands\",    \"value\": \"Dancing\"   }  ] } ```  Please be very careful when you configure offline grammar. If the configuration is not matched the restrictions. Speech recognition may not work. The restrictions as below: - All grammar value cannot be duplicated; - All slot field cannot be duplicated; - All rule field cannot be NULL. Every rule name and value should be unique. Please pay special attention that <html><strong><font color=\"blue\">VOID</font></strong></html>, <html><strong><font color=\"blue\">NULL</font></strong></html> and <html><strong><font color=\"blue\">GARBAGE</font></strong></html> are reserved as key words. Please do not use them. - In rule field, the user can use key words !id to define the semantic. The semantic only support numbers, please do not use other character. The supported semantic number is 32 bits signed integer. The range is <html>[-2<sup>(32-1)</sup>, 2<sup>(32-1)</sup> -1]</html>.  The grammar specification and built-in keywords:  | Operator | description | example | |---|---|---| |!| the next field is a keywords | !grammar| |<>| define a rule name | &lt;name&gt;| |;| terminator | end of a line | | &Iota; | Or, define a side-by-side structure | 张三&Iota;李四 | |[]| optional, indicating that the content can be said | &lt;call&gt;: [找] &lt;name&gt;| |:| define a rule | &lt;name&gt;:张三&Iota;李四| |()| encapsulation operation, defining implicit rules |&lt;call&gt;:找(张三&Iota;李四)| |/* */| block comment |/* comment content */| |//| line comment | // comment content | More details： https://doc.xfyun.cn/msc_windows/%E8%AF%AD%E6%B3%95%EF%BC%88%E5%91%BD%E4%BB%A4%E8%AF%8D%EF%BC%89%E8%AF%86%E5%88%AB.html 

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
    # Add a new offline grammar
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

Start automatic speech recognition

 Please note, automatic speech recognition(asr) cannot work with auto transform(iat). When you start automatic speech, please make sure auto transform(iat) is not started. 

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
    # Start automatic speech recognition
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

Start auto transform

 Please note, automatic speech recognition(asr) cannot work with auto transform(iat). When you start automatic speech, please make sure automatic speech recognition(asr) is not started. 

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
    # Start auto transform
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

Update offline grammar based grammar's name

 Update an offline grammar based the grammar name. Please note, the default offline grammar's name is \"default\". Default offline grammar cannot be added, deleted or modified. The current offline speech recognition can support Chinese and English. But the English support is an experimental feature. All the field name and value should be written as <html><font color=\"red\">uppercase camel case format</font></html>. ``` {  \"grammar\": \"LocalCmd\",  \"slot\": [   {    \"name\": \"Pre\"   },   {    \"name\": \"Commands\"   }  ],  \"start\": \"LocalCmdStart\",  \"startinfo\": \"[<Pre>]<Commands>\",  \"rule\": [   {    \"name\": \"Pre\",    \"value\": \"IWantYou|Please|Start\"   },   {    \"name\": \"Commands\",    \"value\": \"Dancing\"   }  ] } ```  Please be very careful when you configure offline grammar. If the configuration is not matched the restrictions. Speech recognition may not work. The restrictions as below: - All grammar value cannot be duplicated; - All slot field cannot be duplicated; - All rule field cannot be NULL. Every rule name and value should be unique. Please pay special attention that <html><strong><font color=\"blue\">VOID</font></strong></html>, <html><strong><font color=\"blue\">NULL</font></strong></html> and <html><strong><font color=\"blue\">GARBAGE</font></strong></html> are reserved as key words. Please do not use them. - In rule field, the user can use key words !id to define the semantic. The semantic only support numbers, please do not use other character. The supported semantic number is 32 bits signed integer. The range is <html>[-2<sup>(32-1)</sup>, 2<sup>(32-1)</sup> -1]</html>.  The grammar specification and built-in keywords:  | Operator | description | example | |---|---|---| |!| the next field is a keywords | !grammar| |<>| define a rule name | &lt;name&gt;| |;| terminator | end of a line | | &Iota; | Or, define a side-by-side structure | 张三&Iota;李四 | |[]| optional, indicating that the content can be said | &lt;call&gt;: [找] &lt;name&gt;| |:| define a rule | &lt;name&gt;:张三&Iota;李四| |()| encapsulation operation, defining implicit rules |&lt;call&gt;:找(张三&Iota;李四)| |/* */| block comment |/* comment content */| |//| line comment | // comment content | More details： https://doc.xfyun.cn/msc_windows/%E8%AF%AD%E6%B3%95%EF%BC%88%E5%91%BD%E4%BB%A4%E8%AF%8D%EF%BC%89%E8%AF%86%E5%88%AB.html 

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
    # Update offline grammar based grammar's name
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

Start text to speech

 Start text to speech and play the result. 

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
    # Start text to speech
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

