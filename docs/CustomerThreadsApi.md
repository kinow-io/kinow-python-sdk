# CustomerThreadsApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_thread**](#get_customer_thread) | **GET** /customer-threads/{customer_thread_id} | 
[**get_customer_threads**](#get_customer_threads) | **GET** /customer-threads | 


## **get_customer_thread**
> CustomerThread get_customer_thread(customer_thread_id)



Get customer thread

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomerThreadsApi()
customer_thread_id = 789 # int | ID of the customer thread to fetch

try: 
    api_response = api_instance.get_customer_thread(customer_thread_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerThreadsApi->get_customer_thread: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_thread_id** | **int**| ID of the customer thread to fetch | 

### Return type

[**CustomerThread**](#CustomerThread)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_customer_threads**
> CustomerThread1 get_customer_threads(page=page, per_page=per_page, date_add=date_add, date_add_operator=date_add_operator)



Get customer threads list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CustomerThreadsApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
date_add = 'date_add_example' # str |  (optional)
date_add_operator = 'date_add_operator_example' # str |  (optional)

try: 
    api_response = api_instance.get_customer_threads(page=page, per_page=per_page, date_add=date_add, date_add_operator=date_add_operator)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomerThreadsApi->get_customer_threads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **date_add** | **str**|  | [optional] 
 **date_add_operator** | **str**|  | [optional] 

### Return type

[**CustomerThread1**](#CustomerThread1)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

