# DirectorsApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_director**](#get_director) | **GET** /directors/{director_id} | 
[**get_directors**](#get_directors) | **GET** /directors | 
[**get_product_directors**](#get_product_directors) | **GET** /products/{product_id}/directors | 


## **get_director**
> Director get_director(director_id)



Get director

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.DirectorsApi()
director_id = 789 # int | ID of the director to fetch

try: 
    api_response = api_instance.get_director(director_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectorsApi->get_director: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **director_id** | **int**| ID of the director to fetch | 

### Return type

[**Director**](#Director)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_directors**
> Director1 get_directors(page=page, per_page=per_page)



Get directors list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.DirectorsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_directors(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectorsApi->get_directors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Director1**](#Director1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_product_directors**
> Director1 get_product_directors(product_id, page=page, per_page=per_page)



Get directors of a product

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.DirectorsApi()
product_id = 789 # int | ID of the product to fetch
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_product_directors(product_id, page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectorsApi->get_product_directors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**| ID of the product to fetch | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Director1**](#Director1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

