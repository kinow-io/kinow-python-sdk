# CartRulesApi

All URIs are relative to *https://api.kinow.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_cart_rule_to_cart**](#attach_cart_rule_to_cart) | **POST** /carts/{cart_id}/cart-rules | 
[**create_cart_rule**](#create_cart_rule) | **POST** /cart-rules | 
[**delete_cart_rule**](#delete_cart_rule) | **DELETE** /cart-rules/{cart_rule_id} | 
[**detach_cart_rule_from_cart**](#detach_cart_rule_from_cart) | **DELETE** /carts/{cart_id}/cart-rules/{cart_rule_id} | 
[**get_cart_rule**](#get_cart_rule) | **GET** /cart-rules/{cart_rule_id} | 
[**get_cart_rules**](#get_cart_rules) | **GET** /cart-rules | 
[**update_cart_rule**](#update_cart_rule) | **PUT** /cart-rules/{cart_rule_id} | 


## **attach_cart_rule_to_cart**
> attach_cart_rule_to_cart(cart_id, code, ip=ip)



Attach cart rule to cart

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
api_instance = kinow_client.CartRulesApi()
cart_id = 789 # int | Cart ID to fetch
code = 'code_example' # str | Code of the cart rule to attach
ip = 'ip_example' # str | Filter by user IP (optional)

try: 
    api_instance.attach_cart_rule_to_cart(cart_id, code, ip=ip)
except ApiException as e:
    print("Exception when calling CartRulesApi->attach_cart_rule_to_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **code** | **str**| Code of the cart rule to attach | 
 **ip** | **str**| Filter by user IP | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **create_cart_rule**
> create_cart_rule(body)



Create new cart rule

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
api_instance = kinow_client.CartRulesApi()
body = kinow_client.CreateCartRuleRequest() # CreateCartRuleRequest | 

try: 
    api_instance.create_cart_rule(body)
except ApiException as e:
    print("Exception when calling CartRulesApi->create_cart_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateCartRuleRequest**](#CreateCartRuleRequest)|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **delete_cart_rule**
> delete_cart_rule(cart_rule_id)



Delete cart rule

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
api_instance = kinow_client.CartRulesApi()
cart_rule_id = 56 # int | 

try: 
    api_instance.delete_cart_rule(cart_rule_id)
except ApiException as e:
    print("Exception when calling CartRulesApi->delete_cart_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_rule_id** | **int**|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **detach_cart_rule_from_cart**
> detach_cart_rule_from_cart(cart_id, cart_rule_id)



Detach Cart rule from Cart

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
api_instance = kinow_client.CartRulesApi()
cart_id = 789 # int | Cart ID to fetch
cart_rule_id = 789 # int | Cart rule ID to detach

try: 
    api_instance.detach_cart_rule_from_cart(cart_id, cart_rule_id)
except ApiException as e:
    print("Exception when calling CartRulesApi->detach_cart_rule_from_cart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_id** | **int**| Cart ID to fetch | 
 **cart_rule_id** | **int**| Cart rule ID to detach | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_cart_rule**
> CartRuleResponse get_cart_rule(cart_rule_id)



Get cart rule by id

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
api_instance = kinow_client.CartRulesApi()
cart_rule_id = 789 # int | Cart rule ID to fetch

try: 
    api_response = api_instance.get_cart_rule(cart_rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartRulesApi->get_cart_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_rule_id** | **int**| Cart rule ID to fetch | 

### Return type

[**CartRuleResponse**](#CartRuleResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **get_cart_rules**
> CartRuleListResponse get_cart_rules(page=page, per_page=per_page, filters=filters)



Get cart rules list

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
api_instance = kinow_client.CartRulesApi()
page = 789 # int |  (optional)
per_page = 789 # int |  (optional)
filters = 'filters_example' # str |  ``` name[value]=string&name[operator]=contains&date_add[value]=string&date_add[operator]=lt _______________  { \"name\": { \"value\": \"string\", \"operator\": \"contains\" }, \"date_add\": { \"value\": \"string\", \"operator\": \"lt\" } } ``` Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). (optional)

try: 
    api_response = api_instance.get_cart_rules(page=page, per_page=per_page, filters=filters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CartRulesApi->get_cart_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **per_page** | **int**|  | [optional] 
 **filters** | **str**|  &#x60;&#x60;&#x60; name[value]&#x3D;string&amp;name[operator]&#x3D;contains&amp;date_add[value]&#x3D;string&amp;date_add[operator]&#x3D;lt _______________  { \&quot;name\&quot;: { \&quot;value\&quot;: \&quot;string\&quot;, \&quot;operator\&quot;: \&quot;contains\&quot; }, \&quot;date_add\&quot;: { \&quot;value\&quot;: \&quot;string\&quot;, \&quot;operator\&quot;: \&quot;lt\&quot; } } &#x60;&#x60;&#x60; Operator can be: strict, contains, between, in, gt (greater than), lt (lower than). | [optional] 

### Return type

[**CartRuleListResponse**](#CartRuleListResponse)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

## **update_cart_rule**
> update_cart_rule(cart_rule_id, body)



Update cart rule

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
api_instance = kinow_client.CartRulesApi()
cart_rule_id = 56 # int | 
body = kinow_client.UpdateCartRuleRequest() # UpdateCartRuleRequest | 

try: 
    api_instance.update_cart_rule(cart_rule_id, body)
except ApiException as e:
    print("Exception when calling CartRulesApi->update_cart_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cart_rule_id** | **int**|  | 
 **body** | [**UpdateCartRuleRequest**](#UpdateCartRuleRequest)|  | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](#documentation-for-api-endpoints) [[Back to Model list]](#documentation-for-models)

