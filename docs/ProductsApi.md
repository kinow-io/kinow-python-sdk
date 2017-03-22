# kaemo_client.ProductsApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_video_to_product**](#attach_video_to_product) | **POST** /products/{product_id}/videos | 
[**create_product**](#create_product) | **POST** /products | 
[**delete_product**](#delete_product) | **DELETE** /products/{product_id} | 
[**get_product**](#get_product) | **GET** /products/{product_id} | 
[**get_product_attributes**](#get_product_attributes) | **GET** /products/{product_id}/attributes | 
[**get_product_features**](#get_product_features) | **GET** /products/{product_id}/features | 
[**get_product_geolocations**](#get_product_geolocations) | **GET** /products/{product_id}/geolocations | 
[**get_product_geolocations_by_ip**](#get_product_geolocations_by_ip) | **POST** /products/{product_id}/geolocations/{ip_address} | 
[**get_products**](#get_products) | **GET** /products | 
[**get_videos_from_product**](#get_videos_from_product) | **GET** /products/{product_id}/videos | 
[**update_product**](#update_product) | **PUT** /products/{product_id} | 


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
api_instance = kaemo_client.ProductsApi()
product_id = 789 # int | ID of the product to fetch
video_id = 789 # int | ID of the video to attach

try: 
    api_instance.attach_video_to_product(product_id, video_id)
except ApiException as e:
    print("Exception when calling ProductsApi->attach_video_to_product: %s\n" % e)
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

## **create_product**
> Product create_product(body)



Create new product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductsApi()
body = kaemo_client.Product() # Product | 

try: 
    api_response = api_instance.create_product(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->create_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Product**](#Product)|  | 

### Return type

[**Product**](#Product)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_product**
> delete_product(product_id)



Delete product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductsApi()
product_id = 789 # int | ID of the product to fetch

try: 
    api_instance.delete_product(product_id)
except ApiException as e:
    print("Exception when calling ProductsApi->delete_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product**
> Product get_product(product_id)



Get product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductsApi()
product_id = 789 # int | ID of the product to fetch

try: 
    api_response = api_instance.get_product(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 

### Return type

[**Product**](#Product)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_attributes**
> ProductAttributesResponse get_product_attributes(product_id, page=page, per_page=per_page)



Get videos attached to product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductsApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_attributes(product_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**ProductAttributesResponse**](#ProductAttributesResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_features**
> Features get_product_features(product_id, page=page, per_page=per_page)



Get videos attached to product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductsApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_features(product_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Features**](#Features)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_geolocations**
> Geolocs get_product_geolocations(product_id, page=page, per_page=per_page)



Get videos attached to product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductsApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_geolocations(product_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_geolocations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
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



check access to a product by geolocation

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductsApi()
product_id = 789 # int | ID of the product to fetch
ip_address = 'ip_address_example' # str | address ip
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_instance.get_product_geolocations_by_ip(product_id, ip_address, page=page, per_page=per_page)
except ApiException as e:
    print("Exception when calling ProductsApi->get_product_geolocations_by_ip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **ip_address** | **str**| address ip | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_products**
> Products get_products(page=page, per_page=per_page)



Get products list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_products(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Products**](#Products)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_videos_from_product**
> Videos get_videos_from_product(product_id, page=page, per_page=per_page)



Get videos attached to product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductsApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_videos_from_product(product_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->get_videos_from_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Videos**](#Videos)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_product**
> Product update_product(product_id, body)



Update product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductsApi()
product_id = 789 # int | ID of the product to fetch
body = kaemo_client.Product() # Product | 

try: 
    api_response = api_instance.update_product(product_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->update_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **body** | [**Product**](#Product)|  | 

### Return type

[**Product**](#Product)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

