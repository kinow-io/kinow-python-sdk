# RecommendationsApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_recommendations**](#get_customer_recommendations) | **GET** /customers/{customer_id}/recommendations | 


## **get_customer_recommendations**
> BlogPageProductsResponse get_customer_recommendations(customer_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction, ip=ip, iso_code=iso_code)



Get customer recommendations

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
api_instance = kinow_client.RecommendationsApi()
customer_id = 789 # int | 
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
sort_by = 'sort_by_example' # str | Sort by this attribute (id by default) (optional)
sort_direction = 'sort_direction_example' # str | Sorting direction (asc by default) (optional)
ip = 'ip_example' # str | Filter by user IP (optional)
iso_code = 'iso_code_example' # str | Filter by ISO Code (optional)

try: 
    api_response = api_instance.get_customer_recommendations(customer_id, page=page, per_page=per_page, sort_by=sort_by, sort_direction=sort_direction, ip=ip, iso_code=iso_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecommendationsApi->get_customer_recommendations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**|  | 
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **sort_by** | **str**| Sort by this attribute (id by default) | [optional] 
 **sort_direction** | **str**| Sorting direction (asc by default) | [optional] 
 **ip** | **str**| Filter by user IP | [optional] 
 **iso_code** | **str**| Filter by ISO Code | [optional] 

### Return type

[**BlogPageProductsResponse**](#BlogPageProductsResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

