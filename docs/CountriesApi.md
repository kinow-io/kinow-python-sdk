# CountriesApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_countries**](#get_countries) | **GET** /countries | 
[**get_states**](#get_states) | **GET** /countries/states | 


## **get_countries**
> CountryListResponse get_countries(page=page, per_page=per_page, bypass_pagination=bypass_pagination)



Get country list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CountriesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
bypass_pagination = true # bool | Use or skip pagination (optional)

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
 **bypass_pagination** | **bool**| Use or skip pagination | [optional] 

### Return type

[**CountryListResponse**](#CountryListResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_states**
> StateListResponse get_states(page=page, per_page=per_page, bypass_pagination=bypass_pagination)



Get states list

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

# create an instance of the API class
api_instance = kinow_client.CountriesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
bypass_pagination = true # bool | Use or skip pagination (optional)

try: 
    api_response = api_instance.get_states(page=page, per_page=per_page, bypass_pagination=bypass_pagination)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->get_states: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **bypass_pagination** | **bool**| Use or skip pagination | [optional] 

### Return type

[**StateListResponse**](#StateListResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

