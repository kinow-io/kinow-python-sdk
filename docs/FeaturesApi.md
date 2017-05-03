# FeaturesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_features**](#get_features) | **GET** /features | 
[**get_product_features**](#get_product_features) | **GET** /products/{product_id}/features | 


## **get_features**
> Products1 get_features(page=page, per_page=per_page)



Get feature list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.FeaturesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_features(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Products1**](#Products1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_features**
> Products1 get_product_features(product_id, page=page, per_page=per_page)



Get videos attached to product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.FeaturesApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_features(product_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_product_features: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Products1**](#Products1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

