# openadk.MotionsApi

All URIs are relative to *http://127.0.0.1:9090/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_motions_music**](MotionsApi.md#delete_motions_music) | **DELETE** /motions | Delete motion files
[**get_motions**](MotionsApi.md#get_motions) | **GET** /motions | Get the current motions&#39; status
[**get_motions_list**](MotionsApi.md#get_motions_list) | **GET** /motions/list | Get all the motions&#39; name
[**post_motions**](MotionsApi.md#post_motions) | **POST** /motions | Upload motion files
[**put_motions**](MotionsApi.md#put_motions) | **PUT** /motions | Update the motions


# **delete_motions_music**
> CommonResponse delete_motions_music(body)

Delete motion files

 Please note, the user only can delete the user uploaded files. 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MotionsApi()
body = openadk.Name() # Name | Motion file name

try:
    # Delete motion files
    api_response = api_instance.delete_motions_music(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionsApi->delete_motions_music: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Name**](Name.md)| Motion file name | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_motions**
> MotionsStatusResponse get_motions()

Get the current motions' status



### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MotionsApi()

try:
    # Get the current motions' status
    api_response = api_instance.get_motions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionsApi->get_motions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MotionsStatusResponse**](MotionsStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_motions_list**
> MotionsListResponse get_motions_list()

Get all the motions' name

Get all the default and the user uploaded motions' name

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MotionsApi()

try:
    # Get all the motions' name
    api_response = api_instance.get_motions_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionsApi->get_motions_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MotionsListResponse**](MotionsListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_motions**
> CommonResponse post_motions(file)

Upload motion files

 Supported file format: - hts - zip 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MotionsApi()
file = '/path/to/file.txt' # file | Uploaded file.

try:
    # Upload motion files
    api_response = api_instance.post_motions(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionsApi->post_motions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Uploaded file. | 

### Return type

[**CommonResponse**](CommonResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_motions**
> RuntimeResponse put_motions(body)

Update the motions

 Supported parameters: - start - pause - resume - stop 

### Example
```python
from __future__ import print_function
import time
import openadk
from openadk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openadk.MotionsApi()
body = openadk.MotionsOperation() # MotionsOperation | Motion control parameters

try:
    # Update the motions
    api_response = api_instance.put_motions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MotionsApi->put_motions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MotionsOperation**](MotionsOperation.md)| Motion control parameters | 

### Return type

[**RuntimeResponse**](RuntimeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

