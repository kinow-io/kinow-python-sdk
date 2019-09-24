# GeolocationsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geolocations**](#geolocations) | **POST** /geolocations | 
[**get_ip_location**](#get_ip_location) | **GET** /geolocations/ip | 
[**get_product_geolocations**](#get_product_geolocations) | **GET** /products/{product_id}/geolocations | 
[**get_product_geolocations_by_ip**](#get_product_geolocations_by_ip) | **POST** /products/{product_id}/geolocations | 
[**get_video_geolocation_by_ip**](#get_video_geolocation_by_ip) | **POST** /videos/{video_id}/geolocations/{ip_address} | 
[**set_product_geolocation**](#set_product_geolocation) | **PUT** /products/{product_id}/geolocations | 
[**set_video_geolocation**](#set_video_geolocation) | **PUT** /videos/{video_id}/geolocations | 


## **geolocations**
> geolocations(ip_address)



Check access to platform by ip

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.GeolocationsApi()
ip_address = 'ip_address_example' # str | address ip

try: 
    api_instance.geolocations(ip_address)
except ApiException as e:
    print("Exception when calling GeolocationsApi->geolocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| address ip | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_ip_location**
> IPLocation get_ip_location(ip_address)



Get IP location

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.GeolocationsApi()
ip_address = 'ip_address_example' # str | address ip

try: 
    api_response = api_instance.get_ip_location(ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeolocationsApi->get_ip_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| address ip | 

### Return type

[**IPLocation**](#IPLocation)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_geolocations**
> Geolocs get_product_geolocations(product_id, page=page, per_page=per_page)



Get product geolocation restrictions

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.GeolocationsApi()
product_id = 789 # int | Product ID to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_geolocations(product_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeolocationsApi->get_product_geolocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| Product ID to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Geolocs**](#Geolocs)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_geolocations_by_ip**
> get_product_geolocations_by_ip(product_id, ip_address, page=page, per_page=per_page)



Check product access using geolocation

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.GeolocationsApi()
product_id = 789 # int | Product ID to fetch
ip_address = 'ip_address_example' # str | address ip
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_instance.get_product_geolocations_by_ip(product_id, ip_address, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling GeolocationsApi->get_product_geolocations_by_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| Product ID to fetch | 
 **ip_address** | **str**| address ip | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_video_geolocation_by_ip**
> get_video_geolocation_by_ip(video_id, ip_address, page=page, per_page=per_page)



Check access to a product by geolocation

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.GeolocationsApi()
video_id = 789 # int | Video ID to fetch
ip_address = 'ip_address_example' # str | IP address
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_instance.get_video_geolocation_by_ip(video_id, ip_address, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling GeolocationsApi->get_video_geolocation_by_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| Video ID to fetch | 
 **ip_address** | **str**| IP address | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **set_product_geolocation**
> set_product_geolocation(product_id, enabled, behavior_detected_countries, behavior_non_detected_countries, countries=countries, page=page, per_page=per_page)



Handle geolocation for products by countries

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.GeolocationsApi()
product_id = 789 # int | Product ID to fetch
enabled = 56 # int | Enabled
behavior_detected_countries = 'behavior_detected_countries_example' # str | Behavior for detected countries
behavior_non_detected_countries = 'behavior_non_detected_countries_example' # str | Behavior for non-detected countries
countries = 'countries_example' # str | IDs of the non-detected countries separated by comma (optional)
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_instance.set_product_geolocation(product_id, enabled, behavior_detected_countries, behavior_non_detected_countries, countries=countries, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling GeolocationsApi->set_product_geolocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| Product ID to fetch | 
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

## **set_video_geolocation**
> set_video_geolocation(video_id, enabled, behavior_detected_countries, behavior_non_detected_countries, countries=countries)



Handle geolocation for videos by countries

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.GeolocationsApi()
video_id = 789 # int | Video ID to fetch
enabled = 56 # int | Enabled
behavior_detected_countries = 'behavior_detected_countries_example' # str | Behavior for detected countries
behavior_non_detected_countries = 'behavior_non_detected_countries_example' # str | Behavior for non-detected countries
countries = 'countries_example' # str | IDs of the non-detected countries separated by comma (optional)

try: 
    api_instance.set_video_geolocation(video_id, enabled, behavior_detected_countries, behavior_non_detected_countries, countries=countries)
except ApiException as e:
    print("Exception when calling GeolocationsApi->set_video_geolocation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**| Video ID to fetch | 
 **enabled** | **int**| Enabled | 
 **behavior_detected_countries** | **str**| Behavior for detected countries | 
 **behavior_non_detected_countries** | **str**| Behavior for non-detected countries | 
 **countries** | **str**| IDs of the non-detected countries separated by comma | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

