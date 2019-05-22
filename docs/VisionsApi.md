# openadk.VisionsApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vision_photo**](VisionsApi.md#delete_vision_photo) | **DELETE** /visions/photos | Delete a photo based the name
[**delete_vision_photo_samples**](VisionsApi.md#delete_vision_photo_samples) | **DELETE** /visions/photosamples | Delete the uploaded sample
[**delete_visions_streams**](VisionsApi.md#delete_visions_streams) | **DELETE** /visions/streams | Turn off the web stream for the camera
[**delete_visions_tags**](VisionsApi.md#delete_visions_tags) | **DELETE** /visions/tags | Delete a sample&#39;s tag based the tag name
[**get_photo_samples**](VisionsApi.md#get_photo_samples) | **GET** /visions/photosamples | Get all the uploaded photo samples
[**get_vision**](VisionsApi.md#get_vision) | **GET** /visions | Get compute vision result
[**get_visions_photos**](VisionsApi.md#get_visions_photos) | **GET** /visions/photos | Get a specific photo based the name
[**get_visions_photos_lists**](VisionsApi.md#get_visions_photos_lists) | **GET** /visions/photos/list | Get the photo&#39;s list
[**get_visions_tags**](VisionsApi.md#get_visions_tags) | **GET** /visions/tags | Get all the tag list
[**post_vision_photo**](VisionsApi.md#post_vision_photo) | **POST** /visions/photos | Take a photo
[**post_visions_photo_samples**](VisionsApi.md#post_visions_photo_samples) | **POST** /visions/photosamples | Upload photo sample
[**post_visions_streams**](VisionsApi.md#post_visions_streams) | **POST** /visions/streams | Turn on the web stream for the camera
[**put_visions**](VisionsApi.md#put_visions) | **PUT** /visions | Start or stop a compute vision task
[**put_visions_tags**](VisionsApi.md#put_visions_tags) | **PUT** /visions/tags | Set the sample&#39;s tag


# **delete_vision_photo**
> CommonResponse delete_vision_photo(body)

Delete a photo based the name



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
    # Delete a photo based the name
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

Delete the uploaded sample



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = openadk.Name() # Name | Sample name (optional)

try:
    # Delete the uploaded sample
    api_response = api_instance.delete_vision_photo_samples(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->delete_vision_photo_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Name**](Name.md)| Sample name | [optional] 

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

Turn off the web stream for the camera



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
    # Turn off the web stream for the camera
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

Delete a sample's tag based the tag name



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = openadk.VisionsDeleteTags() # VisionsDeleteTags | Sample's name (optional)

try:
    # Delete a sample's tag based the tag name
    api_response = api_instance.delete_visions_tags(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->delete_visions_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VisionsDeleteTags**](VisionsDeleteTags.md)| Sample&#39;s name | [optional] 

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

Get all the uploaded photo samples



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
    # Get all the uploaded photo samples
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

Get compute vision result

 Combination constraint  face - age - gender - age_group - quantity - expression - recognition  object - recognition  color - color_detect 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
option = 'option_example' # str | Module name (optional)
type = 'type_example' # str | Compute vision task name (optional)

try:
    # Get compute vision result
    api_response = api_instance.get_vision(option=option, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->get_vision: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **option** | **str**| Module name | [optional] 
 **type** | **str**| Compute vision task name | [optional] 

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

Get a specific photo based the name



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = 'body_example' # str | Photo name

try:
    # Get a specific photo based the name
    api_instance.get_visions_photos(body)
except ApiException as e:
    print("Exception when calling VisionsApi->get_visions_photos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Photo name | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_visions_photos_lists**
> VisionsPhotoListResponse get_visions_photos_lists()

Get the photo's list



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
    # Get the photo's list
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

Get all the tag list



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
    # Get all the tag list
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

Take a photo



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = openadk.VisionsPhoto() # VisionsPhoto | Photo resolution (optional)

try:
    # Take a photo
    api_response = api_instance.post_vision_photo(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->post_vision_photo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VisionsPhoto**](VisionsPhoto.md)| Photo resolution | [optional] 

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

Upload photo sample

 Please upload the sample before set the sample tag. Supported format: - jpg - png 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
file = '/path/to/file.txt' # file | The file to be uploaded

try:
    # Upload photo sample
    api_response = api_instance.post_visions_photo_samples(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->post_visions_photo_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The file to be uploaded | 

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

Turn on the web stream for the camera

 Turn on the web stream for the camera. The user can get the web stream via web browser. For example: http://192.168.1.100:8000 Please note, when the steam is turned on, new resolution cannot be applied. The API will return {'code':20001, 'data':{}, 'msg':''Resource is not availble.｝ 

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
    # Turn on the web stream for the camera
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

Start or stop a compute vision task

 Please note that the system is designed to run a specific compute vision task one by one. If a task is already started, please stop it before start a new vision task. If the vision tasks are using different module, the vision task can be supported running at the same time. 

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
    # Start or stop a compute vision task
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

Set the sample's tag

 Please upload the sample before set the sample tag. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.VisionsApi()
body = openadk.VisionsPutTags() # VisionsPutTags | Sample's tag name (optional)

try:
    # Set the sample's tag
    api_response = api_instance.put_visions_tags(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VisionsApi->put_visions_tags: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VisionsPutTags**](VisionsPutTags.md)| Sample&#39;s tag name | [optional] 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

