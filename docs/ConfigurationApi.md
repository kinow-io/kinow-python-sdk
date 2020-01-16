# ConfigurationApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration**](#get_configuration) | **GET** /configuration | 
[**get_configuration_by_name**](#get_configuration_by_name) | **GET** /configuration/{configuration_name} | 


## **get_configuration**
> ConfigurationList get_configuration(page=page, per_page=per_page)



       Get configuration by name.       Available :          - LANG_DEFAULT          - CURRENCY_DEFAULT          - COUNTRY_DEFAULT          - TIMEZONE       

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ConfigurationApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_configuration(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**ConfigurationList**](#ConfigurationList)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_configuration_by_name**
> Configuration get_configuration_by_name(configuration_name)



      Get configuration by name.      Available :      - LANG_DEFAULT      - CURRENCY_DEFAULT      - COUNTRY_DEFAULT      - TIMEZONE      

### Example 
```python
from __future__ import print_statement
import time
import kinow_client
from kinow_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = kinow_client.ConfigurationApi()
configuration_name = 'configuration_name_example' # str | 

try: 
    api_response = api_instance.get_configuration_by_name(configuration_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configuration_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_name** | **str**|  | 

### Return type

[**Configuration**](#Configuration)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)
