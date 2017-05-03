# ExtractsApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_product_extracts**](#get_product_extracts) | **GET** /products/{product_id}/extracts | 


## **get_product_extracts**
> ProductExtractsResponse get_product_extracts(product_id, page=page, per_page=per_page)



Get extracts of a product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.ExtractsApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_extracts(product_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractsApi->get_product_extracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**ProductExtractsResponse**](#ProductExtractsResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

