# StatsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_video_stat_session**](#create_video_stat_session) | **POST** /video-stats/sessions | 
[**get_customer_group_total_watched**](#get_customer_group_total_watched) | **GET** /video-stats/customer-group | 
[**get_customer_sessions**](#get_customer_sessions) | **GET** /video-stats/sessions | 
[**get_customer_sessions_multiple**](#get_customer_sessions_multiple) | **POST** /video-stats/{customer_id}/sessions | 
[**get_customer_video_stats**](#get_customer_video_stats) | **GET** /video-stats/customers | 
[**get_customer_videos_view_informations**](#get_customer_videos_view_informations) | **POST** /video-stats/views/{customer_id} | 
[**get_products_watched**](#get_products_watched) | **GET** /video-stats/products-watched | 
[**get_video_stats**](#get_video_stats) | **GET** /video-stats/videos | 
[**get_videos_watching**](#get_videos_watching) | **GET** /video-stats/videos-watching | 
[**set_customer_video_view_informations**](#set_customer_video_view_informations) | **PUT** /video-stats/views/{customer_id}/{video_id} | 


## **create_video_stat_session**
> CreateVideoStatSessionResponse create_video_stat_session(body)



Create a video stat session for a customer

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
api_instance = kinow_client.StatsApi()
body = kinow_client.CreateVideoStatSessionRequest() # CreateVideoStatSessionRequest | Video stat session parameters

try: 
    api_response = api_instance.create_video_stat_session(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->create_video_stat_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateVideoStatSessionRequest**](#CreateVideoStatSessionRequest)| Video stat session parameters | 

### Return type

[**CreateVideoStatSessionResponse**](#CreateVideoStatSessionResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_group_total_watched**
> CustomerGroupVideoStatsListResponse get_customer_group_total_watched(group_id, date_from=date_from, date_to=date_to, page=page, per_page=per_page)



Get video statistics for a given customer group

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
api_instance = kinow_client.StatsApi()
group_id = 789 # int | Customer group ID to fecth
date_from = 'date_from_example' # str | Search entries from this date (optional)
date_to = 'date_to_example' # str | Search entries to this date (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_group_total_watched(group_id, date_from=date_from, date_to=date_to, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_customer_group_total_watched: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **int**| Customer group ID to fecth | 
 **date_from** | **str**| Search entries from this date | [optional] 
 **date_to** | **str**| Search entries to this date | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**CustomerGroupVideoStatsListResponse**](#CustomerGroupVideoStatsListResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_sessions**
> SessionVideoStatListResponse get_customer_sessions(customer_id=customer_id, group_id=group_id, video_id=video_id, date_from=date_from, date_to=date_to, page=page, per_page=per_page)



Get Customer video sessions statistics

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
api_instance = kinow_client.StatsApi()
customer_id = 789 # int | Customer ID to fetch (optional)
group_id = 789 # int | Group ID to fetch (optional)
video_id = 789 # int | Video ID to fetch (optional)
date_from = 'date_from_example' # str | Search entries from this date (optional)
date_to = 'date_to_example' # str | Search entries to this date (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_sessions(customer_id=customer_id, group_id=group_id, video_id=video_id, date_from=date_from, date_to=date_to, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_customer_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | [optional] 
 **group_id** | **int**| Group ID to fetch | [optional] 
 **video_id** | **int**| Video ID to fetch | [optional] 
 **date_from** | **str**| Search entries from this date | [optional] 
 **date_to** | **str**| Search entries to this date | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**SessionVideoStatListResponse**](#SessionVideoStatListResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_sessions_multiple**
> list[SessionVideoStat] get_customer_sessions_multiple(customer_id, body)



Get Customer sessions statistics for multiple videos

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
api_instance = kinow_client.StatsApi()
customer_id = 789 # int | Customer ID to fetch
body = kinow_client.VideoIDList2() # VideoIDList2 | List of Video IDs separated by comma, eg. '42,21,84'

try: 
    api_response = api_instance.get_customer_sessions_multiple(customer_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_customer_sessions_multiple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **body** | [**VideoIDList2**](#VideoIDList2)| List of Video IDs separated by comma, eg. &#39;42,21,84&#39; | 

### Return type

[**list[SessionVideoStat]**](#SessionVideoStat)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_video_stats**
> CustomerVideoStatsListResponse get_customer_video_stats(customer_id, date_from=date_from, date_to=date_to, page=page, per_page=per_page)



Get customer video statistics

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
api_instance = kinow_client.StatsApi()
customer_id = 789 # int | Customer ID to fetch
date_from = 'date_from_example' # str | Search entries from this date (optional)
date_to = 'date_to_example' # str | Search entries to this date (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_video_stats(customer_id, date_from=date_from, date_to=date_to, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_customer_video_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **date_from** | **str**| Search entries from this date | [optional] 
 **date_to** | **str**| Search entries to this date | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**CustomerVideoStatsListResponse**](#CustomerVideoStatsListResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_videos_view_informations**
> list[VideoViewInformations] get_customer_videos_view_informations(customer_id, body)



Get a list of videos view informations for a customer

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
api_instance = kinow_client.StatsApi()
customer_id = 789 # int | Customer ID to fetch
body = kinow_client.VideoIDList1() # VideoIDList1 | List of Video IDs separated by comma, eg. '42,21,84'

try: 
    api_response = api_instance.get_customer_videos_view_informations(customer_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_customer_videos_view_informations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **body** | [**VideoIDList1**](#VideoIDList1)| List of Video IDs separated by comma, eg. &#39;42,21,84&#39; | 

### Return type

[**list[VideoViewInformations]**](#VideoViewInformations)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_products_watched**
> BlogPageProductsResponse get_products_watched(customer_id, page=page, per_page=per_page, ip=ip, iso_code=iso_code)



Get products watched

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
api_instance = kinow_client.StatsApi()
customer_id = 789 # int | Customer ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
ip = 'ip_example' # str | Filter by user IP (optional)
iso_code = 'iso_code_example' # str | Filter by ISO Code (optional)

try: 
    api_response = api_instance.get_products_watched(customer_id, page=page, per_page=per_page, ip=ip, iso_code=iso_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_products_watched: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **ip** | **str**| Filter by user IP | [optional] 
 **iso_code** | **str**| Filter by ISO Code | [optional] 

### Return type

[**BlogPageProductsResponse**](#BlogPageProductsResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_stats**
> VideoStatListResponse get_video_stats(video_id=video_id, date_from=date_from, date_to=date_to, page=page)



Get video statistics

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
api_instance = kinow_client.StatsApi()
video_id = 789 # int | Video ID to fetch (optional)
date_from = 'date_from_example' # str | Search entries from this date (optional)
date_to = 'date_to_example' # str | Search entries to this date (optional)
page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_video_stats(video_id=video_id, date_from=date_from, date_to=date_to, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_video_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| Video ID to fetch | [optional] 
 **date_from** | **str**| Search entries from this date | [optional] 
 **date_to** | **str**| Search entries to this date | [optional] 
 **page** | **int**|  | [optional] 

### Return type

[**VideoStatListResponse**](#VideoStatListResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_videos_watching**
> VideoStatsVideosWatchingResponse get_videos_watching(customer_id, page=page, per_page=per_page, ip=ip, iso_code=iso_code)



Get videos watching

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
api_instance = kinow_client.StatsApi()
customer_id = 789 # int | Customer ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
ip = 'ip_example' # str | Filter by user IP (optional)
iso_code = 'iso_code_example' # str | Filter by ISO Code (optional)

try: 
    api_response = api_instance.get_videos_watching(customer_id, page=page, per_page=per_page, ip=ip, iso_code=iso_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatsApi->get_videos_watching: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **ip** | **str**| Filter by user IP | [optional] 
 **iso_code** | **str**| Filter by ISO Code | [optional] 

### Return type

[**VideoStatsVideosWatchingResponse**](#VideoStatsVideosWatchingResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **set_customer_video_view_informations**
> set_customer_video_view_informations(customer_id, video_id, body)



Set a video view informations for a customer

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
api_instance = kinow_client.StatsApi()
customer_id = 789 # int | Customer ID to fetch
video_id = 789 # int | Video ID to fetch
body = kinow_client.View() # View | Boolean view

try: 
    api_instance.set_customer_video_view_informations(customer_id, video_id, body)
except ApiException as e:
    print("Exception when calling StatsApi->set_customer_video_view_informations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID to fetch | 
 **video_id** | **int**| Video ID to fetch | 
 **body** | [**View**](#View)| Boolean view | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

