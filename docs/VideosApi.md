# VideosApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_video_to_product**](#attach_video_to_product) | **POST** /products/{product_id}/videos | 
[**create_video**](#create_video) | **POST** /videos | 
[**delete_video**](#delete_video) | **DELETE** /videos/{video_id} | 
[**get_customer_has_access_to_video**](#get_customer_has_access_to_video) | **GET** /customers/{customer_id}/videos/{video_id}/has-access | 
[**get_disabled_subscriptions**](#get_disabled_subscriptions) | **GET** /videos/{video_id}/disabled-subscriptions | 
[**get_download_url**](#get_download_url) | **GET** /customers/{customer_id}/videos/{video_id}/download | 
[**get_marlin_token**](#get_marlin_token) | **GET** /customers/{customer_id}/videos/{video_id}/marlin | 
[**get_player_url**](#get_player_url) | **GET** /customers/{customer_id}/videos/{video_id}/player | 
[**get_video**](#get_video) | **GET** /videos/{video_id} | 
[**get_video_access**](#get_video_access) | **GET** /videos/{video_id}/customers/{customer_id}/access | 
[**get_video_geolocation**](#get_video_geolocation) | **GET** /videos/{video_id}/geolocation | 
[**get_video_geolocation_0**](#get_video_geolocation_0) | **POST** /videos/{video_id}/geolocations/{ip_address} | 
[**get_video_player_url**](#get_video_player_url) | **GET** /videos/{video_id}/player | 
[**get_videos**](#get_videos) | **GET** /videos | 
[**get_videos_from_product**](#get_videos_from_product) | **GET** /products/{product_id}/videos | 
[**update_video**](#update_video) | **PUT** /videos/{video_id} | 


## **attach_video_to_product**
> attach_video_to_product(product_id, video_id)



Attach video to product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
product_id = 789 # int | ID of the product to fetch
video_id = 789 # int | ID of the video to attach

try: 
    api_instance.attach_video_to_product(product_id, video_id)
except ApiException as e:
    print("Exception when calling VideosApi->attach_video_to_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **video_id** | **int**| ID of the video to attach | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_video**
> Video create_video(body)



Create new video

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
body = kaemo_client.Video() # Video | 

try: 
    api_response = api_instance.create_video(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->create_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Video**](#Video)|  | 

### Return type

[**Video**](#Video)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_video**
> delete_video(video_id)



Delete video

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
video_id = 789 # int | ID of the video to delete

try: 
    api_instance.delete_video(video_id)
except ApiException as e:
    print("Exception when calling VideosApi->delete_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to delete | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_has_access_to_video**
> get_customer_has_access_to_video(customer_id, video_id)



Get customer access to video

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
customer_id = 789 # int | ID of the customer to fetch
video_id = 789 # int | ID of the video to fetch

try: 
    api_instance.get_customer_has_access_to_video(customer_id, video_id)
except ApiException as e:
    print("Exception when calling VideosApi->get_customer_has_access_to_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 
 **video_id** | **int**| ID of the video to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_disabled_subscriptions**
> Subscriptions get_disabled_subscriptions(video_id, page=page, per_page=per_page)



Get disabled subscriptions list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
video_id = 789 # int | ID of the video to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_disabled_subscriptions(video_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_disabled_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Subscriptions**](#Subscriptions)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_download_url**
> DownloadUrl get_download_url(customer_id, video_id)



Get video download url

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
customer_id = 789 # int | Id of the customer to fetch
video_id = 789 # int | Id of the video to fetch

try: 
    api_response = api_instance.get_download_url(customer_id, video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_download_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to fetch | 
 **video_id** | **int**| Id of the video to fetch | 

### Return type

[**DownloadUrl**](#DownloadUrl)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_marlin_token**
> MarlinToken get_marlin_token(customer_id, video_id)



Get Marlin access token for a video

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
customer_id = 789 # int | Id of the customer to fetch
video_id = 789 # int | Id of the video to fetch

try: 
    api_response = api_instance.get_marlin_token(customer_id, video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_marlin_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to fetch | 
 **video_id** | **int**| Id of the video to fetch | 

### Return type

[**MarlinToken**](#MarlinToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_player_url**
> VideoUrl get_player_url(customer_id, video_id)



Get video player url

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
customer_id = 789 # int | Id of the customer to fetch
video_id = 789 # int | Id of the video to fetch

try: 
    api_response = api_instance.get_player_url(customer_id, video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_player_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Id of the customer to fetch | 
 **video_id** | **int**| Id of the video to fetch | 

### Return type

[**VideoUrl**](#VideoUrl)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video**
> Video get_video(video_id)



Get video

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
video_id = 789 # int | ID of the video to fetch

try: 
    api_response = api_instance.get_video(video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to fetch | 

### Return type

[**Video**](#Video)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_access**
> get_video_access(video_id, customer_id)



Get video access

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
video_id = 789 # int | ID of the video to fetch
customer_id = 789 # int | ID of the customer to fetch

try: 
    api_instance.get_video_access(video_id, customer_id)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to fetch | 
 **customer_id** | **int**| ID of the customer to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_geolocation**
> Geolocs get_video_geolocation(video_id, page=page, per_page=per_page)



Get geoloc list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
video_id = 789 # int | ID of the video to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_video_geolocation(video_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_geolocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Geolocs**](#Geolocs)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_geolocation_0**
> get_video_geolocation_0(video_id, ip_address, page=page, per_page=per_page)



Check access to a product by geolocation

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
video_id = 789 # int | ID of the video to fetch
ip_address = 'ip_address_example' # str | address ip
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_instance.get_video_geolocation_0(video_id, ip_address, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_geolocation_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to fetch | 
 **ip_address** | **str**| address ip | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_player_url**
> PlayerConfiguration get_video_player_url(video_id)



Get video player url

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
video_id = 789 # int | Id of the video to fetch

try: 
    api_response = api_instance.get_video_player_url(video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_player_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| Id of the video to fetch | 

### Return type

[**PlayerConfiguration**](#PlayerConfiguration)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_videos**
> Videos get_videos(page=page, per_page=per_page, filters=filters)



Get customer list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |      ```     filters[name][value]=string&filters[name][operator]=strict&filters[duration][value]=string&filters[duration][operator]=gt     _______________      {     \"name\": {     \"value\": \"string\",     \"operator\": \"strict\"     },     \"duration\": {     \"value\": \"string\",     \"operator\": \"gt\"     }     } ```     Operator can be strict, contains, gt or lt. (optional)

try: 
    api_response = api_instance.get_videos(page=page, per_page=per_page, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|      &#x60;&#x60;&#x60;     filters[name][value]&#x3D;string&amp;filters[name][operator]&#x3D;strict&amp;filters[duration][value]&#x3D;string&amp;filters[duration][operator]&#x3D;gt     _______________      {     \&quot;name\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;duration\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;gt\&quot;     }     } &#x60;&#x60;&#x60;     Operator can be strict, contains, gt or lt. | [optional] 

### Return type

[**Videos**](#Videos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_videos_from_product**
> Videos get_videos_from_product(product_id, page=page, filters=filters, per_page=per_page)



Get videos attached to product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
filters = 'filters_example' # str |      ```     filters[name][value]=string&filters[name][operator]=strict&filters[duration][value]=string&filters[duration][operator]=gt     _______________      {     \"name\": {     \"value\": \"string\",     \"operator\": \"strict\"     },     \"duration\": {     \"value\": \"string\",     \"operator\": \"gt\"     }     } ```     Operator can be strict, contains, gt or lt. (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_videos_from_product(product_id, page=page, filters=filters, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_videos_from_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **page** | **int**|  | [optional] 
 **filters** | **str**|      &#x60;&#x60;&#x60;     filters[name][value]&#x3D;string&amp;filters[name][operator]&#x3D;strict&amp;filters[duration][value]&#x3D;string&amp;filters[duration][operator]&#x3D;gt     _______________      {     \&quot;name\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;duration\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;gt\&quot;     }     } &#x60;&#x60;&#x60;     Operator can be strict, contains, gt or lt. | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Videos**](#Videos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_video**
> Video update_video(video_id, body)



Update video

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
video_id = 789 # int | ID of the video to update
body = kaemo_client.Video() # Video | 

try: 
    api_response = api_instance.update_video(video_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->update_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to update | 
 **body** | [**Video**](#Video)|  | 

### Return type

[**Video**](#Video)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

