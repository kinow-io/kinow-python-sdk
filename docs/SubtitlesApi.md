# SubtitlesApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_extract_subtitle**](#create_extract_subtitle) | **POST** /extracts/{extract_id}/subtitle | 
[**create_video_subtitle**](#create_video_subtitle) | **POST** /videos/{video_id}/subtitle | 
[**get_category_video_subtitles**](#get_category_video_subtitles) | **GET** /categories/videos/{video_id}/subtitles | 
[**get_extract_subtitles**](#get_extract_subtitles) | **GET** /extracts/{extract_id}/subtitles | 
[**get_subtitles**](#get_subtitles) | **GET** /subtitles | 
[**get_video_subtitles**](#get_video_subtitles) | **GET** /videos/{video_id}/subtitles | 


## **create_extract_subtitle**
> Subtitle create_extract_subtitle(extract_id, body)



Create new Extract Subtitle

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.SubtitlesApi()
extract_id = 789 # int | Extract ID to attach the created Subtitle
body = kinow_client.CreateExtractSubtitleRequest() # CreateExtractSubtitleRequest | Subtitle settings

try: 
    api_response = api_instance.create_extract_subtitle(extract_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubtitlesApi->create_extract_subtitle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| Extract ID to attach the created Subtitle | 
 **body** | [**CreateExtractSubtitleRequest**](#CreateExtractSubtitleRequest)| Subtitle settings | 

### Return type

[**Subtitle**](#Subtitle)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_video_subtitle**
> Subtitle create_video_subtitle(video_id, body)



Create new Video Subtitle

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.SubtitlesApi()
video_id = 789 # int | Video ID to attach the created Subtitle
body = kinow_client.CreateVideoSubtitleRequest() # CreateVideoSubtitleRequest | Subtitle settings

try: 
    api_response = api_instance.create_video_subtitle(video_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubtitlesApi->create_video_subtitle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| Video ID to attach the created Subtitle | 
 **body** | [**CreateVideoSubtitleRequest**](#CreateVideoSubtitleRequest)| Subtitle settings | 

### Return type

[**Subtitle**](#Subtitle)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_category_video_subtitles**
> VideoSubtitlesResponse get_category_video_subtitles(video_id, page=page, per_page=per_page)



Get subtitles of a video

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.SubtitlesApi()
video_id = 789 # int | Video ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_category_video_subtitles(video_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubtitlesApi->get_category_video_subtitles: %s\n" % e)
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

## **get_extract_subtitles**
> VideoSubtitlesResponse get_extract_subtitles(extract_id, page=page, per_page=per_page)



Get subtitles of an extract

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.SubtitlesApi()
extract_id = 789 # int | Extract ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_extract_subtitles(extract_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubtitlesApi->get_extract_subtitles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extract_id** | **int**| Extract ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**VideoSubtitlesResponse**](#VideoSubtitlesResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_subtitles**
> SubtitleFiles get_subtitles(page=page, per_page=per_page)



Get Subtitles list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.SubtitlesApi()
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

[**SubtitleFiles**](#SubtitleFiles)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

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

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

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

