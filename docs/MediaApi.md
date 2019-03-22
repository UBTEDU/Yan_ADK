# openadk.MediaApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_media_music**](MediaApi.md#delete_media_music) | **DELETE** /media/music | 删除音乐文件（只能删除用户上传的文件）
[**get_media_music**](MediaApi.md#get_media_music) | **GET** /media/music | 获取音乐播放状态
[**get_media_music_list**](MediaApi.md#get_media_music_list) | **GET** /media/music/list | 获取音乐列表
[**post_media_music**](MediaApi.md#post_media_music) | **POST** /media/music | 上传音乐文件
[**put_media_music**](MediaApi.md#put_media_music) | **PUT** /media/music | 播放/停止音乐


# **delete_media_music**
> CommonResponse delete_media_music(body)

删除音乐文件（只能删除用户上传的文件）



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MediaApi()
body = openadk.Name() # Name | 音乐文件名

try:
    # 删除音乐文件（只能删除用户上传的文件）
    api_response = api_instance.delete_media_music(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->delete_media_music: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Name**](Name.md)| 音乐文件名 | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_music**
> MediaMusicStatusResponse get_media_music()

获取音乐播放状态



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MediaApi()

try:
    # 获取音乐播放状态
    api_response = api_instance.get_media_music()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_media_music: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MediaMusicStatusResponse**](MediaMusicStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_music_list**
> MediaMusicListResponse get_media_music_list()

获取音乐列表

可以获得所有内置和用户上传的音乐列表

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MediaApi()

try:
    # 获取音乐列表
    api_response = api_instance.get_media_music_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->get_media_music_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MediaMusicListResponse**](MediaMusicListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_media_music**
> CommonResponse post_media_music(file)

上传音乐文件

文件格式目前仅支持wav或者mp3

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MediaApi()
file = '/path/to/file.txt' # file | 上传文件

try:
    # 上传音乐文件
    api_response = api_instance.post_media_music(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->post_media_music: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| 上传文件 | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_media_music**
> RuntimeResponse put_media_music(body)

播放/停止音乐

目前支持的音乐格式：wav和mp3

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MediaApi()
body = openadk.MediaMusicOperation() # MediaMusicOperation | 音乐播放控制

try:
    # 播放/停止音乐
    api_response = api_instance.put_media_music(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->put_media_music: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MediaMusicOperation**](MediaMusicOperation.md)| 音乐播放控制 | 

### Return type

[**RuntimeResponse**](RuntimeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

