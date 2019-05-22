# openadk.MediaApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_media_music**](MediaApi.md#delete_media_music) | **DELETE** /media/music | Delete uploaded music
[**get_media_music**](MediaApi.md#get_media_music) | **GET** /media/music | Get the music playing status
[**get_media_music_list**](MediaApi.md#get_media_music_list) | **GET** /media/music/list | Get the music list
[**post_media_music**](MediaApi.md#post_media_music) | **POST** /media/music | Upload music
[**put_media_music**](MediaApi.md#put_media_music) | **PUT** /media/music | Start or stop music


# **delete_media_music**
> CommonResponse delete_media_music(body)

Delete uploaded music

Please note, only the user uploaded music can be removed.

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MediaApi()
body = openadk.Name() # Name | Music file name

try:
    # Delete uploaded music
    api_response = api_instance.delete_media_music(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->delete_media_music: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Name**](Name.md)| Music file name | 

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

Get the music playing status



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
    # Get the music playing status
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

Get the music list

Get all the default and user uploaded music

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
    # Get the music list
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

Upload music

The music format only support wav and mp3

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MediaApi()
file = '/path/to/file.txt' # file | Upload music file

try:
    # Upload music
    api_response = api_instance.post_media_music(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->post_media_music: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Upload music file | 

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

Start or stop music

The music format only support wav and mp3

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MediaApi()
body = openadk.MediaMusicOperation() # MediaMusicOperation | Music playing settings

try:
    # Start or stop music
    api_response = api_instance.put_media_music(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaApi->put_media_music: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MediaMusicOperation**](MediaMusicOperation.md)| Music playing settings | 

### Return type

[**RuntimeResponse**](RuntimeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

