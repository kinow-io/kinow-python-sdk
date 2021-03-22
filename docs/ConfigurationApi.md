# ConfigurationApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_configuration**](#get_configuration) | **GET** /configuration | 
[**get_configuration_analytics**](#get_configuration_analytics) | **GET** /configuration/analytics | 
[**get_configuration_by_name**](#get_configuration_by_name) | **GET** /configuration/{configuration_name} | 
[**get_configuration_logo**](#get_configuration_logo) | **GET** /configuration/logo | 
[**get_configuration_social**](#get_configuration_social) | **GET** /configuration/social | 


## **get_configuration**
> ConfigurationList get_configuration(page=page, per_page=per_page)



       Get configuration by name.       Available :          - PLATFORM_NAME          - LANG_DEFAULT          - CURRENCY_DEFAULT          - COUNTRY_DEFAULT          - TIMEZONE          - COPYRIGHT          - COOKIE_WARNING          - RECAPTCHA_KEY          - CUSTOMER_REGISTRATION          - CATALOG_RESTRICTED          - CATALOG_SUBSCRIPTION          - PRODUCTS_ORDER_BY          - PRODUCTS_ORDER_WAY          - PRODUCTS_RAIL_NB          - PRODUCTS_NEW_DAYS          - FORCE_TAX_ID          - CMS_CONDITIONS_ID          - GEOLOCATION_WHITELIST       

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

## **get_configuration_analytics**
> Analytics get_configuration_analytics(page=page, per_page=per_page)



Get analytics configuration

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
api_instance = kinow_client.ConfigurationApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)

try: 
    api_response = api_instance.get_configuration_analytics(page=page, per_page=per_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configuration_analytics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 

### Return type

[**Analytics**](#Analytics)

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

# Configure API key authorization: ApiClientId
kinow_client.configuration.api_key['X-Client-Id'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Id'] = 'Bearer'
# Configure API key authorization: ApiClientSecret
kinow_client.configuration.api_key['X-Client-Secret'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# kinow_client.configuration.api_key_prefix['X-Client-Secret'] = 'Bearer'

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

## **get_configuration_logo**
> LogoSettings get_configuration_logo()



Get logo settings

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
api_instance = kinow_client.ConfigurationApi()

try: 
    api_response = api_instance.get_configuration_logo()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configuration_logo: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LogoSettings**](#LogoSettings)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_configuration_social**
> SocialSettings get_configuration_social()



Get social networks settings

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
api_instance = kinow_client.ConfigurationApi()

try: 
    api_response = api_instance.get_configuration_social()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->get_configuration_social: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SocialSettings**](#SocialSettings)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

