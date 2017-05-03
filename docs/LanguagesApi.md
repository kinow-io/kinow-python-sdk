# LanguagesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_languages**](#get_languages) | **GET** /languages | 


## **get_languages**
> Languages get_languages(page=page, per_page=per_page)



Get language list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.LanguagesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_languages(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LanguagesApi->get_languages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Languages**](#Languages)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

