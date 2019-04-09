# SubtitlesApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_video_subtitles**](#get_video_subtitles) | **GET** /videos/{video_id}/subtitles | 


## **get_video_subtitles**
> VideoSubtitlesResponse get_video_subtitles(video_id, page=page, per_page=per_page)



Get subtitles of a video

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.SubtitlesApi()
video_id = 789 # int | Video ID to fetch
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
 **video_id** | **int**| Video ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**VideoSubtitlesResponse**](#VideoSubtitlesResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

