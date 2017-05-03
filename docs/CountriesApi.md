# CountriesApi

All URIs are relative to *https://api.kaemo.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries**](#get_countries) | **GET** /countries | 


## **get_countries**
> Countries get_countries(page=page, per_page=per_page, bypass_pagination=bypass_pagination)



Get country list

### Example 
```python
from __future__ import print_statement
import time
import kaemo_client
from kaemo_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kaemo_client.CountriesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
bypass_pagination = true # bool |  (optional)

try: 
    api_response = api_instance.get_countries(page=page, per_page=per_page, bypass_pagination=bypass_pagination)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->get_countries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **bypass_pagination** | **bool**|  | [optional] 

### Return type

[**Countries**](#Countries)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

