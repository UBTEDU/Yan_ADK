# openadk.VisionsApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vision_photo**](VisionsApi.md#delete_vision_photo) | **DELETE** /visions/photos | 删除指定照片
[**delete_vision_photo_samples**](VisionsApi.md#delete_vision_photo_samples) | **DELETE** /visions/photosamples | 删除上传的样本
[**delete_visions_streams**](VisionsApi.md#delete_visions_streams) | **DELETE** /visions/streams | 关闭摄像头的视频流
[**delete_visions_tags**](VisionsApi.md#delete_visions_tags) | **DELETE** /visions/tags | 删除指定样本标签
[**get_photo_samples**](VisionsApi.md#get_photo_samples) | **GET** /visions/photosamples | 获取上传样本列表
[**get_vision**](VisionsApi.md#get_vision) | **GET** /visions | 获取任务結果
[**get_visions_photos**](VisionsApi.md#get_visions_photos) | **GET** /visions/photos | 获取指定照片
[**get_visions_photos_lists**](VisionsApi.md#get_visions_photos_lists) | **GET** /visions/photos/list | 获取拍照列表
[**get_visions_tags**](VisionsApi.md#get_visions_tags) | **GET** /visions/tags | 获取已设置标签列表
[**post_vision_photo**](VisionsApi.md#post_vision_photo) | **POST** /visions/photos | 拍一张照片
[**post_visions_photo_samples**](VisionsApi.md#post_visions_photo_samples) | **POST** /visions/photosamples | 上传样本
[**post_visions_streams**](VisionsApi.md#post_visions_streams) | **POST** /visions/streams | 打开摄像头的视频流
[**put_visions**](VisionsApi.md#put_visions) | **PUT** /visions | 指定视觉任务停止或开始
[**put_visions_tags**](VisionsApi.md#put_visions_tags) | **PUT** /visions/tags | 设置样本标签


# **delete_vision_photo**
> CommonResponse delete_vision_photo(body)

删除指定照片



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = openadk.Name() # Name | 

try:
    # 删除指定照片
    api_response = api_instance.delete_vision_photo(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->delete_vision_photo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Name**](Name.md)|  | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vision_photo_samples**
> CommonResponse delete_vision_photo_samples(body=body)

删除上传的样本



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = openadk.Name() # Name | 样本名称 (optional)

try:
    # 删除上传的样本
    api_response = api_instance.delete_vision_photo_samples(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->delete_vision_photo_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Name**](Name.md)| 样本名称 | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_visions_streams**
> CommonResponse delete_visions_streams()

关闭摄像头的视频流



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()

try:
    # 关闭摄像头的视频流
    api_response = api_instance.delete_visions_streams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->delete_visions_streams: %s\n" % e)
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

# **delete_visions_tags**
> CommonResponse delete_visions_tags(body=body)

删除指定样本标签



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = openadk.VisionsDeleteTags() # VisionsDeleteTags | 样本名称 (optional)

try:
    # 删除指定样本标签
    api_response = api_instance.delete_visions_tags(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->delete_visions_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VisionsDeleteTags**](VisionsDeleteTags.md)| 样本名称 | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_photo_samples**
> VisionsPhotoListResponse get_photo_samples()

获取上传样本列表



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()

try:
    # 获取上传样本列表
    api_response = api_instance.get_photo_samples()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->get_photo_samples: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VisionsPhotoListResponse**](VisionsPhotoListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vision**
> VisionsGetResponse get_vision(option=option, type=type)

获取任务結果



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
option = 'option_example' # str | 模型名 (optional)
type = 'type_example' # str | 任务名称 (optional)

try:
    # 获取任务結果
    api_response = api_instance.get_vision(option=option, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->get_vision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **option** | **str**| 模型名 | [optional] 
 **type** | **str**| 任务名称 | [optional] 

### Return type

[**VisionsGetResponse**](VisionsGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visions_photos**
> get_visions_photos(body)

获取指定照片



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = 'body_example' # str | 照片名

try:
    # 获取指定照片
    api_instance.get_visions_photos(body)
except ApiException as e:
    print("Exception when calling VisionsApi->get_visions_photos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| 照片名 | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visions_photos_lists**
> VisionsPhotoListResponse get_visions_photos_lists()

获取拍照列表



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()

try:
    # 获取拍照列表
    api_response = api_instance.get_visions_photos_lists()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->get_visions_photos_lists: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VisionsPhotoListResponse**](VisionsPhotoListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visions_tags**
> VisionsTagsResponse get_visions_tags()

获取已设置标签列表



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()

try:
    # 获取已设置标签列表
    api_response = api_instance.get_visions_tags()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->get_visions_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VisionsTagsResponse**](VisionsTagsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_vision_photo**
> VisionsPhotoResponse post_vision_photo(body=body)

拍一张照片



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = openadk.VisionsPhoto() # VisionsPhoto | 照片分辨率 (optional)

try:
    # 拍一张照片
    api_response = api_instance.post_vision_photo(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->post_vision_photo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VisionsPhoto**](VisionsPhoto.md)| 照片分辨率 | [optional] 

### Return type

[**VisionsPhotoResponse**](VisionsPhotoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_visions_photo_samples**
> CommonResponse post_visions_photo_samples(file)

上传样本

请先上传样本数据再设置样本标签, 只支持样本格式为jpg与png

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
file = '/path/to/file.txt' # file | 上传文件

try:
    # 上传样本
    api_response = api_instance.post_visions_photo_samples(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->post_visions_photo_samples: %s\n" % e)
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

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_visions_streams**
> CommonResponse post_visions_streams(body=body)

打开摄像头的视频流

打开摄像头视频流．用户可以通信浏览器直接接收视频．视频将以mjpg格式通过http的形式发布．url: http://机器人ip地址:8000 当视频流已经打开时，不会响应新的分辨率请求．返回｛'code':20001, 'data':{}, 'msg':''Resource is not availble.｝

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = openadk.VisionsStream() # VisionsStream |  (optional)

try:
    # 打开摄像头的视频流
    api_response = api_instance.post_visions_streams(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->post_visions_streams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VisionsStream**](VisionsStream.md)|  | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_visions**
> VisionsPutResponse put_visions(body)

指定视觉任务停止或开始

机器人每次只能执行一种占用的视觉任务，如需执行不同的占用的视觉任务，必须先停止当前执行的占用视觉任务

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = openadk.VisionsTask() # VisionsTask | 

try:
    # 指定视觉任务停止或开始
    api_response = api_instance.put_visions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->put_visions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VisionsTask**](VisionsTask.md)|  | 

### Return type

[**VisionsPutResponse**](VisionsPutResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_visions_tags**
> CommonResponse put_visions_tags(body=body)

设置样本标签

请先上传样本数据再设置样本标签

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = openadk.VisionsPutTags() # VisionsPutTags | 样本名 (optional)

try:
    # 设置样本标签
    api_response = api_instance.put_visions_tags(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->put_visions_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VisionsPutTags**](VisionsPutTags.md)| 样本名 | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

