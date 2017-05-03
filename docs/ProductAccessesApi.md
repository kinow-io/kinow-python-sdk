# ProductAccessesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_accesses_subscriptions**](#get_customer_accesses_subscriptions) | **GET** /customers/{customer_id}/accesses/subscriptions | 
[**get_customer_accesses_videos**](#get_customer_accesses_videos) | **GET** /customers/{customer_id}/accesses/videos | 
[**get_product_accesses**](#get_product_accesses) | **GET** /product-accesses | 
[**update_product_access**](#update_product_access) | **PUT** /product-accesses/{product_access_id} | 


## **get_customer_accesses_subscriptions**
> SubscriptionAccesses get_customer_accesses_subscriptions(customer_id, page=page, per_page=per_page)



Get customer accesses for subscription

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductAccessesApi()
customer_id = 789 # int | ID of the customer to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_accesses_subscriptions(customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->get_customer_accesses_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**SubscriptionAccesses**](#SubscriptionAccesses)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_accesses_videos**
> SubscriptionAccesses get_customer_accesses_videos(customer_id, page=page, per_page=per_page)



Get customer access for videos

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductAccessesApi()
customer_id = 789 # int | ID of the customer to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_customer_accesses_videos(customer_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->get_customer_accesses_videos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**SubscriptionAccesses**](#SubscriptionAccesses)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_accesses**
> SubscriptionAccesses get_product_accesses(page=page, per_page=per_page, type=type, date_add=date_add, date_add_direction=date_add_direction, date_exp=date_exp, date_exp_direction=date_exp_direction)



Get product accesses list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductAccessesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
type = 'type_example' # str | Filter by access type, available values are: video, sub (optional)
date_add = 'date_add_example' # str | Filter by creation date (optional)
date_add_direction = 'date_add_direction_example' # str | Choose the direction for date_add parameter, default value is after ,available values are: before, equal, after (optional)
date_exp = 'date_exp_example' # str | Filter by expiration date (optional)
date_exp_direction = 'date_exp_direction_example' # str | Choose the direction for date_exp parameter, default value is after ,available values are: before, equal, after (optional)

try: 
    api_response = api_instance.get_product_accesses(page=page, per_page=per_page, type=type, date_add=date_add, date_add_direction=date_add_direction, date_exp=date_exp, date_exp_direction=date_exp_direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->get_product_accesses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **type** | **str**| Filter by access type, available values are: video, sub | [optional] 
 **date_add** | **str**| Filter by creation date | [optional] 
 **date_add_direction** | **str**| Choose the direction for date_add parameter, default value is after ,available values are: before, equal, after | [optional] 
 **date_exp** | **str**| Filter by expiration date | [optional] 
 **date_exp_direction** | **str**| Choose the direction for date_exp parameter, default value is after ,available values are: before, equal, after | [optional] 

### Return type

[**SubscriptionAccesses**](#SubscriptionAccesses)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_product_access**
> ProductAccess update_product_access(product_access_id, body)



Update product access

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ProductAccessesApi()
product_access_id = 789 # int | ID of the product access to update
body = kaemo_client.ProductAccess() # ProductAccess | 

try: 
    api_response = api_instance.update_product_access(product_access_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductAccessesApi->update_product_access: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_access_id** | **int**| ID of the product access to update | 
 **body** | [**ProductAccess**](#ProductAccess)|  | 

### Return type

[**ProductAccess**](#ProductAccess)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

