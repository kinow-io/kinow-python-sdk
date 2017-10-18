# VideosApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_features_to_video**](#attach_features_to_video) | **POST** /videos/{video_id}/features | 
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
[**get_video_features**](#get_video_features) | **GET** /videos/{video_id}/features | 
[**get_video_geolocation**](#get_video_geolocation) | **GET** /videos/{video_id}/geolocation | 
[**get_video_geolocation_0**](#get_video_geolocation_0) | **POST** /videos/{video_id}/geolocations/{ip_address} | 
[**get_video_player_url**](#get_video_player_url) | **GET** /videos/{video_id}/player | 
[**get_video_views**](#get_video_views) | **GET** /videos/{video_id}/views | 
[**get_videos**](#get_videos) | **GET** /videos | 
[**get_videos_from_product**](#get_videos_from_product) | **GET** /products/{product_id}/videos | 
[**set_video_geolocation**](#set_video_geolocation) | **PUT** /videos/{video_id}/geolocations | 
[**update_video**](#update_video) | **PUT** /videos/{video_id} | 


## **attach_features_to_video**
> attach_features_to_video(video_id, features)



Attach feature to video

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.VideosApi()
video_id = 789 # int | 
features = 'features_example' # str |      To attach existing FeatureValue to Product:     ```     [{     \"id_feature\":3,     \"id_feature_value\":5     }]     ```      To create a custom FeatureValue:     ```     [{     \"id_feature\":3,     \"custom_value\":[{     \"lang\": 1,     \"value\": \"string\"     }]     }]     ```

try: 
    api_instance.attach_features_to_video(video_id, features)
except ApiException as e:
    print("Exception when calling VideosApi->attach_features_to_video: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**|  | 
 **features** | **str**|      To attach existing FeatureValue to Product:     &#x60;&#x60;&#x60;     [{     \&quot;id_feature\&quot;:3,     \&quot;id_feature_value\&quot;:5     }]     &#x60;&#x60;&#x60;      To create a custom FeatureValue:     &#x60;&#x60;&#x60;     [{     \&quot;id_feature\&quot;:3,     \&quot;custom_value\&quot;:[{     \&quot;lang\&quot;: 1,     \&quot;value\&quot;: \&quot;string\&quot;     }]     }]     &#x60;&#x60;&#x60; | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

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

## **get_video_features**
> Features get_video_features(video_id, page=page, per_page=per_page)



Get video features

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
    api_response = api_instance.get_video_features(video_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Features**](#Features)

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
> PlayerConfiguration get_video_player_url(video_id, customer_id=customer_id)



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
customer_id = 789 # int |  (optional)

try: 
    api_response = api_instance.get_video_player_url(video_id, customer_id=customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_player_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| Id of the video to fetch | 
 **customer_id** | **int**|  | [optional] 

### Return type

[**PlayerConfiguration**](#PlayerConfiguration)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_views**
> VideoViews get_video_views(video_id)



Get video views

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
    api_response = api_instance.get_video_views(video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_video_views: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to fetch | 

### Return type

[**VideoViews**](#VideoViews)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_videos**
> Videos get_videos(page=page, per_page=per_page, features=features, filters=filters, ip=ip)



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
features = 'features_example' # str |      ```     features[*][value]=string&features[*][operator]=strict&features[1][value]=string&features[1][operator]=strict     _______________      {     \"*\": {     \"value\": \"string\",     \"operator\": \"strict\"     },     \"1\": {     \"value\": \"string\",     \"operator\": \"contains\"     }     } ```     Operator can be strict, contains, gt or lt.     To search on all features, you can pass * as featureId. (optional)
filters = 'filters_example' # str |      ```     filters[name][value]=string&filters[name][operator]=strict&filters[duration][value]=string&filters[duration][operator]=gt     _______________      {     \"name\": {     \"value\": \"string\",     \"operator\": \"strict\"     },     \"duration\": {     \"value\": \"string\",     \"operator\": \"gt\"     }     } ```     Operator can be strict, contains, gt or lt. (optional)
ip = 'ip_example' # str | filter by customer ip (optional)

try: 
    api_response = api_instance.get_videos(page=page, per_page=per_page, features=features, filters=filters, ip=ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->get_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **features** | **str**|      &#x60;&#x60;&#x60;     features[*][value]&#x3D;string&amp;features[*][operator]&#x3D;strict&amp;features[1][value]&#x3D;string&amp;features[1][operator]&#x3D;strict     _______________      {     \&quot;*\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;1\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;contains\&quot;     }     } &#x60;&#x60;&#x60;     Operator can be strict, contains, gt or lt.     To search on all features, you can pass * as featureId. | [optional] 
 **filters** | **str**|      &#x60;&#x60;&#x60;     filters[name][value]&#x3D;string&amp;filters[name][operator]&#x3D;strict&amp;filters[duration][value]&#x3D;string&amp;filters[duration][operator]&#x3D;gt     _______________      {     \&quot;name\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;strict\&quot;     },     \&quot;duration\&quot;: {     \&quot;value\&quot;: \&quot;string\&quot;,     \&quot;operator\&quot;: \&quot;gt\&quot;     }     } &#x60;&#x60;&#x60;     Operator can be strict, contains, gt or lt. | [optional] 
 **ip** | **str**| filter by customer ip | [optional] 

### Return type

[**Videos**](#Videos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_videos_from_product**
> Videos get_videos_from_product(product_id, page=page, filters=filters, per_page=per_page, ip=ip)



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
ip = 'ip_example' # str | filter by customer ip (optional)

try: 
    api_response = api_instance.get_videos_from_product(product_id, page=page, filters=filters, per_page=per_page, ip=ip)
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
 **ip** | **str**| filter by customer ip | [optional] 

### Return type

[**Videos**](#Videos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **set_video_geolocation**
> set_video_geolocation(video_id, enabled, behavior_detected_countries, behavior_non_detected_countries, countries=countries, page=page, per_page=per_page)



Handle geolocation for videos by countries

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
enabled = 56 # int | Enabled
behavior_detected_countries = 'behavior_detected_countries_example' # str | Behavior for detected countries
behavior_non_detected_countries = 'behavior_non_detected_countries_example' # str | Behavior for non-detected countries
countries = 'countries_example' # str | IDs of the non-detected countries separated by comma (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_instance.set_video_geolocation(video_id, enabled, behavior_detected_countries, behavior_non_detected_countries, countries=countries, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling VideosApi->set_video_geolocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| ID of the video to fetch | 
 **enabled** | **int**| Enabled | 
 **behavior_detected_countries** | **str**| Behavior for detected countries | 
 **behavior_non_detected_countries** | **str**| Behavior for non-detected countries | 
 **countries** | **str**| IDs of the non-detected countries separated by comma | [optional] 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

void (empty response body)

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

