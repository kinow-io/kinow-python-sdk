# ActorsApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_actor**](#get_actor) | **GET** /actors/{actor_id} | 
[**get_actors**](#get_actors) | **GET** /actors | 
[**get_product_actors**](#get_product_actors) | **GET** /products/{product_id}/actors | 


## **get_actor**
> Actor get_actor(actor_id)



Get actor

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ActorsApi()
actor_id = 789 # int | ID of the actor to fetch

try: 
    api_response = api_instance.get_actor(actor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorsApi->get_actor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **actor_id** | **int**| ID of the actor to fetch | 

### Return type

[**Actor**](#Actor)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_actors**
> Actors get_actors(page=page, per_page=per_page)



Get actors list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ActorsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_actors(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorsApi->get_actors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Actors**](#Actors)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_actors**
> Actors get_product_actors(product_id, page=page, per_page=per_page)



Get actors attached to product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ActorsApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_actors(product_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ActorsApi->get_product_actors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Actors**](#Actors)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

