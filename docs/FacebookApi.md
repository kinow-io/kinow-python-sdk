# FacebookApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_facebook_id**](#create_facebook_id) | **POST** /facebook/customers | 
[**get_facebook_customer**](#get_facebook_customer) | **GET** /facebook/customers/{facebook_id} | 


## **create_facebook_id**
> create_facebook_id(customer_id, facebook_id)



Create new Facebook ID for user

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.FacebookApi()
customer_id = 789 # int | Customer ID
facebook_id = 'facebook_id_example' # str | Facebook ID

try: 
    api_instance.create_facebook_id(customer_id, facebook_id)
except ApiException as e:
    print("Exception when calling FacebookApi->create_facebook_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| Customer ID | 
 **facebook_id** | **str**| Facebook ID | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_facebook_customer**
> CustomerId get_facebook_customer(facebook_id)



Get customer ID by Facebook ID

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.FacebookApi()
facebook_id = 789 # int | Facebook ID to fetch

try: 
    api_response = api_instance.get_facebook_customer(facebook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FacebookApi->get_facebook_customer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **facebook_id** | **int**| Facebook ID to fetch | 

### Return type

[**CustomerId**](#CustomerId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

