# kaemo_client.AddressApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_address**](#get_customer_address) | **GET** /customers/{customer_id}/address | 


## **get_customer_address**
> Address get_customer_address(customer_id)



Get customer address

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.AddressApi()
customer_id = 789 # int | ID of the customer to fetch

try: 
    api_response = api_instance.get_customer_address(customer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AddressApi->get_customer_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| ID of the customer to fetch | 

### Return type

[**Address**](#Address)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

