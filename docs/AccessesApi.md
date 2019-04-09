# AccessesApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_has_access_to_product**](#get_customer_has_access_to_product) | **GET** /customers/{customer_id}/products/{product_id}/has-access | 
[**get_customer_has_access_to_video**](#get_customer_has_access_to_video) | **GET** /customers/{customer_id}/videos/{video_id}/has-access | 
[**get_product_availability**](#get_product_availability) | **GET** /products/{product_id}/access | 


## **get_customer_has_access_to_product**
> get_customer_has_access_to_product(customer_id, product_id)



Get customer access to video

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.AccessesApi()
customer_id = 789 # int | ID of the customer to fetch
product_id = 789 # int | ID of the product to fetch

try: 
    api_instance.get_customer_has_access_to_product(customer_id, product_id)
except ApiException as e:
    print("Exception when calling AccessesApi->get_customer_has_access_to_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 
 **product_id** | **int**| ID of the product to fetch | 

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
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.AccessesApi()
customer_id = 789 # int | ID of the customer to fetch
video_id = 789 # int | ID of the video to fetch

try: 
    api_instance.get_customer_has_access_to_video(customer_id, video_id)
except ApiException as e:
    print("Exception when calling AccessesApi->get_customer_has_access_to_video: %s\n" % e)
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

## **get_product_availability**
> get_product_availability(product_id)



Get availability of a product

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.AccessesApi()
product_id = 789 # int | ID of the product to fetch

try: 
    api_instance.get_product_availability(product_id)
except ApiException as e:
    print("Exception when calling AccessesApi->get_product_availability: %s\n" % e)
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

