# MediaSourcesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_media_source**](#get_media_source) | **GET** /media-sources/{source_id} | 
[**get_media_source_files**](#get_media_source_files) | **GET** /media-sources/{source_id}/files | 
[**get_media_sources**](#get_media_sources) | **GET** /media-sources | 
[**post_media_source_files**](#post_media_source_files) | **POST** /media-sources/{source_id}/files | 


## **get_media_source**
> MediaSource get_media_source(source_id)



Get media source

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.MediaSourcesApi()
source_id = 789 # int | ID of the media source to fetch

try: 
    api_response = api_instance.get_media_source(source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaSourcesApi->get_media_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**| ID of the media source to fetch | 

### Return type

[**MediaSource**](#MediaSource)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_media_source_files**
> MediaFiles get_media_source_files(source_id, page=page, per_page=per_page, filters=filters)



Get media source files

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.MediaSourcesApi()
source_id = 789 # int | ID of the media source to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |      ```     filters[name][value]=string&filters[name][operator]=contains&filters[date_add][value]=string&filters[date_add][operator]=lt     _______________      {     \"name\": {     \"value\": \"string\",     \"operator\": \"contains\"     },     \"date_add\": {     \"value\": \"string\",     \"operator\": \"lt\"     }     } ```Operator can be strict, contains, gt or lt. (optional)

try: 
    api_response = api_instance.get_media_source_files(source_id, page=page, per_page=per_page, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaSourcesApi->get_media_source_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**| ID of the media source to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|      &#x60;&#x60;&#x60;     filters[name][value]&#x3D;string&amp;filters[name][operator]&#x3D;contains&amp;filters[date_add][value]&#x3D;string&amp;filters[date_add][operator]&#x3D;lt     _______________      {     \&quot;name\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;contains\&quot;     },     \&quot;date_add\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;lt\&quot;     }     } &#x60;&#x60;&#x60;Operator can be strict, contains, gt or lt. | [optional] 

### Return type

[**MediaFiles**](#MediaFiles)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_media_sources**
> MediaSources get_media_sources(page=page, per_page=per_page)



Get media source list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.MediaSourcesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_media_sources(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaSourcesApi->get_media_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**MediaSources**](#MediaSources)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **post_media_source_files**
> MediaFile post_media_source_files(source_id, body)



Post media file

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.MediaSourcesApi()
source_id = 789 # int | ID of the media source to fetch
body = kaemo_client.MediaFile() # MediaFile | Create MediaFile object

try: 
    api_response = api_instance.post_media_source_files(source_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MediaSourcesApi->post_media_source_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_id** | **int**| ID of the media source to fetch | 
 **body** | [**MediaFile**](#MediaFile)| Create MediaFile object | 

### Return type

[**MediaFile**](#MediaFile)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

