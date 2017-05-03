# CurrenciesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_currencies**](#get_currencies) | **GET** /currencies | 


## **get_currencies**
> Currencies get_currencies(page=page, per_page=per_page)



Get currency list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CurrenciesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_currencies(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->get_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Currencies**](#Currencies)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

