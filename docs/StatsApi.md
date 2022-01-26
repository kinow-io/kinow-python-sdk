# StatsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_group_total_watched**](#get_customer_group_total_watched) | **GET** /video-stats/customer-group | 
[**get_customer_sessions**](#get_customer_sessions) | **GET** /video-stats/sessions | 
[**get_customer_sessions_multiple**](#get_customer_sessions_multiple) | **POST** /video-stats/{customer_id}/sessions | 
[**get_customer_video_stats**](#get_customer_video_stats) | **GET** /video-stats/customers | 
[**get_video_stats**](#get_video_stats) | **GET** /video-stats/videos | 


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
body = kinow_client.VideoIDList1() # VideoIDList1 | List of Video IDs separated by comma, eg. '42,21,84'

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
 **body** | [**VideoIDList1**](#VideoIDList1)| List of Video IDs separated by comma, eg. &#39;42,21,84&#39; | 

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

