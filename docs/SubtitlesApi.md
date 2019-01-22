# SubtitlesApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_subtitle**](#get_subtitle) | **GET** /subtitles/{subtitle_id} | 
[**get_subtitles**](#get_subtitles) | **GET** /subtitles | 
[**get_video_subtitles**](#get_video_subtitles) | **GET** /videos/{video_id}/subtitles | 


## **get_subtitle**
> Subtitle get_subtitle(subtitle_id)



Get Subtitle

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.SubtitlesApi()
subtitle_id = 789 # int | ID of the product to fetch

try: 
    api_response = api_instance.get_subtitle(subtitle_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubtitlesApi->get_subtitle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subtitle_id** | **int**| ID of the product to fetch | 

### Return type

[**Subtitle**](#Subtitle)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_subtitles**
> Subtitles get_subtitles(page=page, per_page=per_page)



Get Subtitles list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.SubtitlesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_subtitles(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubtitlesApi->get_subtitles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Subtitles**](#Subtitles)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_subtitles**
> Subtitles get_video_subtitles(video_id, page=page, per_page=per_page)



Get video subtitles

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.SubtitlesApi()
video_id = 789 # int | ID of the video to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_video_subtitles(video_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubtitlesApi->get_video_subtitles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Subtitles**](#Subtitles)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

